from ipaddress import ip_address
import re
from flask import Flask, request
import os, socket

app = Flask(__name__)


@app.route('/')
def home():
    ip_address_service2 = socket.gethostbyname(socket.gethostname())

    return f'Hello came from {request.environ["REMOTE_ADDR"]}:{request.environ["REMOTE_PORT"]} to {ip_address_service2}:{port}'


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8002))
    app.run(debug=True, host='0.0.0.0', port=port)