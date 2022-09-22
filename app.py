from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    name_image_tuple = [("Air-Fried Korean Chicken", "chickenwings.png", "wings"),
                        ("Karaage", "karaage.png", "karaage"),
                        ("Shoyu Chicken", "shoyuchicken.png", "shoyuchicken")]

    return render_template("index.html", items=name_image_tuple)

@app.route("/chickenwings")
def wings():
    return render_template("chickenwings.html")

@app.route("/karaage")
def karaage():
    return render_template("karaage.html")

@app.route("/shoyuchicken")
def shoyuchicken():
    return render_template("shoyuchicken.html")


