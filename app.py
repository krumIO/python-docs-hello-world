from flask import Flask
app = Flask(__name__)

@app.route("/api/examplepy")
def hello():
    return "Hello, World, it's me?!"
