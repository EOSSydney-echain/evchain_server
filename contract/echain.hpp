/**
 *  @file
 *  @copyright defined in eos/LICENSE.txt
 */
#include <eosiolib/eosio.hpp>
#include <eosiolib/print.hpp>
#include <eosiolib/asset.hpp>
#include <eosiolib/symbol.hpp>
#include <string>

namespace echain{
class token : public eosio::contract {                                                             
      private:
          struct etoken {
              account_name   name;
              eosio::asset   balance;

              uint64_t primary_key()const { return name; };
          };

          struct actions {
	      uint64_t       id;
	      time           executed_at;
              account_name   name;
              std::string    action_type;
              account_name   objective;
              uint64_t       amount;

              uint64_t       primary_key()const { return id; };
	      account_name   get_name() const { return name; };
	  };

          eosio::multi_index<N(etoken), etoken>  _token_index;

          eosio::multi_index<N(actions), actions
	       , eosio::indexed_by< N( byname ), eosio::const_mem_fun< actions, uint64_t, &actions::get_name> >
	      >  _action_index;

          void _add_token_balance( account_name payer, account_name to, eosio::asset q );
	  void _issue( account_name to, eosio::asset quantity );

      public:
          token( account_name self ):contract(self),_token_index(_self, _self),_action_index(_self, _self){}
	  void transfer ( account_name from, account_name to, eosio::asset quantity );
          void getbalance ( account_name user );

          void issuetoken( account_name to, eosio::asset quantity);
	  void getactions(uint64_t page=1);

	  void writeaction(
                  account_name             name,
                  std::string              action_type,
                  account_name             objective,
                  uint64_t                 amount
		);

    };
    EOSIO_ABI(token, (transfer)(issuetoken)(getbalance)(getactions)(writeaction) );
}
