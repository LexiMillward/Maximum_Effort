from flask import Flask, render_template


app = Flask (__name__)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/useful-links/")
def usefulLinks():

    return render_template("useful_links.html")


@app.route("/Q&A/")
def qanda():

    return render_template("qanda.html")


@app.route("/EYFS/")
def eyfs():

    return render_template("eyfs.html")


app.run(debug=True)


