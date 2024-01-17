from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/<username>")
def hello_world(username=None):
    return render_template('index.html', name=username)

@app.route("/blog.html")
def hello_world():
    return '<p>It\'s blog about dogs!</p>'