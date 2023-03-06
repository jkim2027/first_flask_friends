from flask import Flask, render_template, request, redirect
from friend import Friend

app = Flask(__name__)

@app.route("/")
def index():
    pass

@app.route("/create-friend", methods = ['POST'])
def create_friend():
    pass


if __name__ = "__main__":
    app.run(debug = True, port = 5001)