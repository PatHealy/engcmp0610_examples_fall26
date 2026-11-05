from flask import Flask

app = Flask(__name__)

count = 0

@app.route("/")
def visit():
    global count
    count = count + 1
    return "This page has been visited " + str(count) + " times"

