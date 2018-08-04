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


void token::_issue(account_name to, eosio::asset quantity ) {
   require_auth( _self );
   token::_add_token_balance( _self, to, quantity );
}





}
