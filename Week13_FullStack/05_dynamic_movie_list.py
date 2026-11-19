from flask import Flask, render_template, request

app = Flask(__name__)

movie_list = []

@app.route("/", methods=["GET","POST"])
def movie_page():
    if request.method == "POST":
        new_movie = request.form["newMovie"]
        movie_list.append(new_movie)
    return render_template("dynamic_movies.html", movies=movie_list)
