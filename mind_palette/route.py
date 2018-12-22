from mind_palette import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/major")
def major():
    return render_template("major.html")


@app.route("/job")
def job():
    return render_template("job.html")


@app.route("/university")
def university():
    return render_template("university.html")


@app.route("/certificate")
def certificate():
    return render_template("certificate.html")


@app.route("/competition")
def competition():
    return render_template("competition.html")
