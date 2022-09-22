from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("home")
def home():
    name_image_tuple = [("Air-Fried Korean Chicken", "chickenwings.png"),
                        ("Karaage", "karaage.png"),
                        ("Shoyu Chicken", "shoyuchicken.png")]

    return render_template("index.html", items=name_image_tuple)
