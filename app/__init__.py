# -*- coding: utf-8 -*-
from flask import Flask, g, redirect, make_response, jsonify
from flask_session import Session
from flask_cors import CORS
import os
import subprocess, shlex

# Define the WSGI application object
app = Flask(__name__, static_url_path='/static', template_folder='/static/front')

#: Flask-Session
Session(app)

#: Flask-CORS
cors = CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": "true"}})

# API Version
from app.status.urls import status
app.register_blueprint(status, url_prefix='/api/block/status')

from app.action.urls import action
app.register_blueprint(action, url_prefix='/api/block/action')

#: 등록된 url 확인하기
print(app.url_map)

#####################################################################################

@app.before_request
def before_request():
    """
    모든 API 실행 전 실행하는 부분
    """
    pass


@app.teardown_request
def teardown_request(exception):
    """
    모든 API 실행 후 실행하는 부분. 여기서는 DB 연결종료.
    """
    pass


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(result_ko='존재하지 않는 페이지입니다'
                                 , result_en='Not Found!'
                                 , result=404), 404)


@app.errorhandler(401)
def not_unauthorized(error):
    return make_response(jsonify(result_ko='인증되지 않음'
                                 , result_en='Unauthenticated'
                                 , result=401), 401)


@app.errorhandler(403)
def forbidden(error):
    # return abort(403)
    return make_response(jsonify(result_ko='접근 금지!'
                                 , result_en='Forbidden!'
                                 , result=403), 403)


