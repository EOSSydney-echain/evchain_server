from flask import Blueprint
import app.action.controller as ctrl

action = Blueprint('action', __name__)

action.add_url_rule('/explore', view_func=ctrl.explore, methods=['GET'])
action.add_url_rule('/write', view_func=ctrl.write, methods=['POST'])
