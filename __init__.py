from flask import Flask, render_template, request, redirect, g, url_for
import db
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def Home():
	return render_template("index.html")

@app.route("/About")
def About():
	return render_template("about.html")

@app.route("/Service")
def Service():
	return render_template("service.html")

@app.route("/Activities")
def Activitites():
	return render_template("activities.html")

@app.route("/Year2")
def Year2():
	return render_template("cards.html")

@app.route("/Year3")
def Year3():
	return render_template("cards3.html")

@app.route("/Html")
def Html():
	return render_template("html.html")

@app.route("/Python")
def Python():
	return render_template("python.html")

@app.route("/Java")
def Java():
	return render_template("java.html")

@app.route("/Login")
def Login():
	return render_template("login.html")

@app.route("/Admin")
def Admin():
	return render_template("admin.html")
@app.route("/newsfeed")
def newsfeed():
	return render_template("newsfeed.html")

if __name__ == "__main__":
	app.run(debug=True)