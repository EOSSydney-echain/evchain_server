from flask import Blueprint
import app.status.controller as ctrl

status = Blueprint('status', __name__)

status.add_url_rule('/getBalance/<user>', view_func=ctrl.getBalance, methods=['GET'])
status.add_url_rule('/transfer', view_func=ctrl.transfer, methods=['POST'])
