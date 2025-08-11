from flask import Flask, render_template, request

app = Flask(__name__)   

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        # name= request.form.get("username")
        return render_template("greet_with_methods.html", name= request.form.get("username"))
    else:
        return render_template("index_with_methods.html")
        