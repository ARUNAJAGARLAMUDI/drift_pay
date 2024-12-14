from flask import Flask, render_template,request
from pymongo import MongoClient

app = Flask(__name__)


my_client = MongoClient("localhost", 27017)
my_db = my_client["driftpay"]
payments = my_db["payments"]


@app.route("/", methods = ["GET"])
def homepage():
    return render_template("index.html")

@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "POST":
        return "request"
    return render_template("marchent_register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("marchent_login.html")

@app.route("/marchadd", methods=["GET","POST"])
def adding():
    return render_template("marchadd.html")

app.run(debug = True,port = 5001)