import app.common as common

def explore(page=1):
    args = {
              "action": "getactions",
              "code": "david",
              "args": {
                  "page": page
              }
            }

    ret = common.send_action("getactions", args)
    return ret

def write(name, action_type, objective, amount):
    args = {
              "action": "writeaction",
              "code": "david",
              "args": {
                  "name": name,
                  "action_type": action_type,
                  "objective": objective,
                  "amount": amount
              }
            }

    ret = common.send_action("writeaction", args)
    return ret

