from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "<h1>Hello, this is my first project!</h1>"