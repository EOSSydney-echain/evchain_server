# -*- coding: utf-8 -*-
from app import app
from gevent.pywsgi import WSGIServer

https = WSGIServer(('0.0.0.0', 5000), app)
https.serve_forever()

