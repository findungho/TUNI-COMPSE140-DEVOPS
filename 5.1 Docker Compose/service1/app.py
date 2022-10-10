from flask import Flask, request
import os, requests, socket

app = Flask(__name__)


@app.route('/')
def home():
    request2_to_service2 = requests.get('http://service2:5001')

    ip_address_service1 = socket.gethostbyname(socket.gethostname())
    request1_result = f'Hello came from {request.environ["REMOTE_ADDR"]}:{request.environ["REMOTE_PORT"]} to {ip_address_service1}:{port}'

    return f'{request1_result}\n{request2_to_service2.text}'


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)