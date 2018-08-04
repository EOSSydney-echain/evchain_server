from flask import request, make_response, json
import app.status.model as model

def getBalance(user):
    resp = model.getBalance(user)
    return make_response(json.jsonify(data=resp), 200)

def transfer():
    source_user = request.form['from']
    target_user = request.form['to']
    amount = request.form['quantity']
    resp = model.transfer(source_user, target_user, amount)
    return make_response(json.jsonify(data=resp), 200)
