from flask import Flask, jsonify
import os
from flask import request
import logging

app = Flask(__name__)


@app.route('/')
def index():
    app.logger.error("We were sent a request")
    request_ip = request.remote_addr
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        request_ip = request.environ['REMOTE_ADDR']
    else:
        request_ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy

    app.logger.error(f"{request_ip}")
    return jsonify({"IP Address": f"{request_ip}"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
