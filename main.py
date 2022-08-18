from flask import Flask, jsonify
import os
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    
    print(request.remote_addr)
    return jsonify({"IP Address": f"{request.remote_addr}"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
