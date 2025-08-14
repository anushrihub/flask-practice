# import click
# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)  

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///froshims.db"

# db = SQLAlchemy(app)

# SPORTS = ('BasketBall', 'Soccer', 'Ultimate Frisbee')

# class Registrant(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     sport = db.Column(db.String(100), nullable=False)

# with app.app_context():
#     db.create_all()

# @app.route("/")
# def index():
#     return render_template("froshims_index.html", sports=SPORTS)

# @app.route("/register", methods=["POST"])
# def register():
#     name = request.form.get("name")
#     sport = request.form.get("sport")

#     if not name:
#         return render_template("error.html",message="Please enter a name.")
#     if not sport:
#         return render_template("error.html",message="Please enter a sport.")
#     elif sport not in SPORTS:
#         return render_template("error.html",message="Please enter valid sport.")
    
#     registrant = Registrant(name=name, sport=sport)
#     db.session.add(registrant)
#     db.session.commit()

#     return render_template("success.html")

# @app.route("/registrants")
# def registrants():
#     all_registrants = Registrant.query.all()
#     return render_template("registrants.html", registrants=all_registrants)
