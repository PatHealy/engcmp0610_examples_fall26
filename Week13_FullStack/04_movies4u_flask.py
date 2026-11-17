from flask import Flask, render_template

app = Flask(__name__)

teamA = ["It", "Mean Girls", "The Hunger Games", "The Matrix"]
pat = ["Nowhere", "True Stories", "The Gleaners and I", "Wiener-dog"]
owen = ["Die Hard", "Harry Potter and the Sorcerer's Stone", "Christmas Vacation", "The Batman"]

@app.route("/<string:name>")
def movie_page(name):
    if name == "teamA":
        return render_template("movies.html", movies=teamA)
    elif name == "pat":
        return render_template("movies.html", movies=pat)
    elif name == "owen":
        return render_template("movies.html", movies=owen)
    return name + " is not present in our dictionary."