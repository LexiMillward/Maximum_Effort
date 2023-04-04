from flask import Flask, render_template


app = Flask (__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    return render_template("homepage.html")

    return app

# app test