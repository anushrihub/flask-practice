from flask import Flask, render_template, request

app = Flask(__name__)   


@app.route("/")
def hello_world():
    name = request.args.get("name", "world")
    return render_template("index.html", name=name)

@app.route("/post")
def hello_world_post():
    return render_template("index_post.html", show_form=True)


@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("username")
    return render_template("index_post.html", show_form=False, username=name)