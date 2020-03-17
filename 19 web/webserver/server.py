from flask import Flask
app = Flask(__name__)
FLASK_DEBUG=1
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Ud!'