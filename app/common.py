from eospy import EosClient
from eospy.transaction_builder import TransactionBuilder, Action


def send_action(action_name, args):
    eos_conn = EosClient(
            api_endpoint="http://localhost:8888",
            wallet_endpoint="http://localhost:8888"
            )
    txBuilder = TransactionBuilder(eos_conn)
    
    try:
        eos_conn.wallet_unlock('PW5K79yJYFyWUdwgCQP9xa7ru4bEcFa2RuttMo5hJLinmMez69S3e')
    except:
        pass
    
    #param = {
    #          "action": "writeaction",
    #          "code": "david",
    #          "args": {
    #              "user": "david",
    #              "action_type": action_name,
    #              "objective": "",
    #              "amount": point_amount
    #          }
    #        }

    bin_param = eos_conn.chain_abi_json_to_bin(args)
    act = Action("david", action_name, "david", "active", bin_param['binargs'])
    ready_tx, chain_id =  txBuilder.build_sign_transaction_request([act])
    signed_transaction = eos_conn.wallet_sign_transaction(ready_tx, ['EOS8KYhBt3w9yZ7dhNTPqHfDG4GgYKRfVGFoiKEcZ9byHNYhLcVPS'], chain_id)
    ret = eos_conn.chain_push_transaction(signed_transaction)

    return ret
