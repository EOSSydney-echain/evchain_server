import app.common as common

def getBalance(name):
    param = {
              "action": "getbalance",
              "code": "david",
              "args": {
                  "user": name
              }
            }

    ret = common.getBalance("getbalance", param)
    return ret

def transfer(source_user, target_user, amount):
    param = {
              "action": "trans",
              "code": "david",
              "args": {
                  "from": source_user,
                  "to": target_user,
                  "quantity": amount
              }
            }

    ret = common.getBalance("trans", param)
    return ret

