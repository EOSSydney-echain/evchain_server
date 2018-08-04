#include <eosiolib/eosio.hpp>
#include <eosiolib/print.hpp>
#include <eosiolib/asset.hpp>
#include <eosiolib/symbol.hpp>
#include <string>
#include "echain.hpp"

namespace echain{

void token::_add_token_balance( account_name payer, account_name to, eosio::asset q ) {
    /**
        simple.token
    */
    auto toitr = _token_index.find( to );
    if( toitr == _token_index.end() ) {
        _token_index.emplace( payer, [&]( auto& a ) {
            a.name = to;
            a.balance = q;
        });
    } else {
        _token_index.modify( toitr, 0, [&]( auto& a ) {
            a.balance += q;
            eosio_assert( a.balance >= q, "overflow detected" );
        });  
    }
}


void token::transfer( account_name from, account_name to, eosio::asset quantity ) {
   require_auth( from );

   const auto& fromacnt = _token_index.get( from );
   eosio_assert( fromacnt.balance >= quantity, "overdrawn balance" );
   _token_index.modify( fromacnt, from, [&]( auto& a ){ a.balance -= quantity; } );

   _add_token_balance( from, to, quantity );
}


void token::_issue(account_name to, eosio::asset quantity ) {
   require_auth( _self );
   token::_add_token_balance( _self, to, quantity );
}

void token::getbalance( account_name user ){
    auto itr = _token_index.find( user );
    eosio::print(itr->balance);
}

void token::writeaction(
          account_name           name
        , std::string            action_type
        , account_name           objective
        , uint64_t               amount
     )
{
    _action_index.emplace( name, [&]( auto& a ) {
        a.id = _action_index.available_primary_key();
        a.executed_at = now();
        a.name        = name;
        a.action_type = action_type;
        a.objective   = objective;
        a.amount      = amount;
    });
    
}


void token::getactions(uint64_t page){
    auto itr = _action_index.rbegin();
    for (uint64_t i=0; i < 20*(page-1); ++i) itr++;

    eosio::print("[");
    for (uint64_t i=0; i < 20; ++i){
        auto user_name_obj = eosio::name{itr->name};
        auto objective_name_obj = eosio::name{itr->objective};
        std::string user_name = user_name_obj.to_string();
        std::string objective_name = objective_name_obj.to_string();

        eosio::print("{");
        eosio::print("    \"time\": ", itr->executed_at);
        eosio::print("  , \"user\": \"", user_name,"\"");
        eosio::print("  , \"action_type\": \"", itr->action_type, "\"");
        eosio::print("  , \"objective\": \"", objective_name, "\"");
        eosio::print("  , \"amount\": ", itr->amount);
        eosio::print("}");

        itr++;

        if (itr == _action_index.rend() ) break;
        if (i != 19) eosio::print(", ");
    }
    eosio::print("]");
}


}
