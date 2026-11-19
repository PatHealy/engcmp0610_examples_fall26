from flask import Flask, render_template, request

app = Flask(__name__)

def read_list():
    with open("movie_list.txt") as read_file:
        return read_file.readlines()

movie_list = read_list()

def write_list():
    with open("movie_list.txt", "w") as write_file:
        write_file.writelines(movie_list)

@app.route("/", methods=["GET","POST"])
def movie_page():
    if request.method == "POST":
        new_movie = request.form["newMovie"]
        movie_list.append(new_movie + "\n")
        write_list()
    return render_template("dynamic_movies.html", movies=movie_list)
