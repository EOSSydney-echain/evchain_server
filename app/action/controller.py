from flask import request, make_response, json
import app.action.model as model

def explore():
    page = request.args.get('page', 1)
    resp = model.explore(page)
    return make_response(json.jsonify(data=resp), 200)

def write():
    name = request.form['name']
    action_type = request.form['action_type']
    objective = request.form['objective']
    amount = request.form['amount']

    resp = model.translate(name, action_type, objective, amount)
    return make_response(json.jsonify(data="ok"), 200)

