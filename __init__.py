from flask import Flask, render_template, request, redirect, g, url_for, session, escape
import db
import os
import time
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

@app.route("/Year1")
def Year1():
	return render_template("cards2.html")

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


@app.route("/SignUp")
def SignUp():
	return render_template("register.html")
	
# @app.route("/newsfeed")
# def newsfeed():
# 	return render_template("newsfeed.html")


@app.route("/SignUpForm", methods=['POST','GET'])
def SignUpForm():
	if request.method == 'POST':
		form = request.form
		username = form['username']
		password = form['password']
		email = form['email']
		user = db.getUserByUsername(username)
		if(user != None):
			return render_template("staken.html")
		if(db.signup(username, password, email)):
			return render_template("success.html")
		return "something went wrong"

@app.route("/SignInForm", methods = ['GET','POST'])
def SignInForm():
	if request.method == 'POST':
		form = request.form
		username = form['username']
		password = form['password']
		user = db.getUserByUsername(username)
		if(user == None):
			return render_template("wronglog.html")
		if(db.signin(username, password)):
			session['username'] = request.form['username']
			return redirect("/")
		return "something went wrong"

@app.route("/FeedBack", methods = ['GET', 'POST'])
def FeedBack():
	if request.method == 'GET':
		message = request.args.get('message')
		if(db.feedback(message)):
			return render_template("feedback.html")
		return "something went wrong"


# @app.route("/insert")
# def insert():
# 	userfeed = request.args.get('userid')
# 	passfeed = request.args.get('pswrd')
# 	messfeed = request.args.get('message')
# 	x2 = db.insert(userfeed, passfeed, messfeed)
# 	allfeed = db.showusers2()
# 	feedlist = list(allfeed)
# 	print userfeed
# 	return render_template("success.html", feed = feedlist)

	# return userid

@app.route("/showfeed")
def showfeed():
	allfeed = db.allfeeds()
	feedlist = list(allfeed)
	return render_template("showusers.html", feeds = feedlist)

# @app.route("/insert2")
# def insert2():
# 	x3 = db.insert(request.args.get('email'),request.args.get('psw'))
# 	return render_template("data.html", yousef2 = x3)


@app.route("/showall")
def showall():
	allusers = db.allUsers()
	userlist = list(allusers)
	return render_template("showall.html", users = userlist)

@app.route("/newsfeeds", methods = ['GET', 'POST'])
def newsfeeds():
	if request.method == 'GET':
		if 'username' in session:
			return render_template("newsfeed.html"), escape(session['username'])
		return redirect ('/Login')
		allnews = db.allnews()
		newslist = list(allnews)
		print 'get',newslist
		return render_template('newsfeed.html',newsfeed = newslist)
	else:
		form = request.form
		emailfeed = form['emailfeed']
		text = form['text']
		time_string = time.strftime('%l:%M on %b %d, %Y')
#		time = time.strftime('%1:%M on %b %d, %Y')
		print(emailfeed, text, time_string)
		newsfeed = db.newsfeed(emailfeed, text)
		allnews = db.allnews()
		newslist = list(allnews)[::-1]
		print 'post',newslist
		return render_template('newsfeed.html',newsfeed = newslist, time_string= time_string)



@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect('/')


# @app.route("/shownews")
# def shownews():
	
# 	return render_template("showusers.html", news = newslist)


# @app.route("/select", methods= ["get", "post"])
# def select():
# 	username = request.form['username']
# 	password = request.form['password']
# 	print username, password
# 	x1 = db.select(username,password)
# 	if x1 == None:
# 		return "error"
# 	else:
# 		return "success"

# @app.route("/select2", methods = ["get", "post"])
# def select2():
# 	username = request.form['email']
# 	password = request.form['psw']
# 	print username
# 	x2 = db.select(username,password)
# 	print x2
# 	if x2 is None:
# 		if (db.insert(password, username)):
# 			return render_template("signsuccess.html")
# 		else:
# 			return "already taken"
# 	else:
# 		return "already taken"

# 	return render_template("showusers.html")
# @app.route("/select2", methods = ["get", "post"])
# def register():
# 	Email = request.form['email']
# 	laith2 = db.select2(Email,'username2','password2')
# 	if laith2 == True:
# 		return "already taken"
# 	else:
# 		return "success"

# @app.route("/login" ,methods = ["get", "post"])
# def login():
# 	Email = request.form['email']
# 	password = request.form['password2']
# 	laith = db.select2('username', password, Email)
# 	if laith == True:
# 		return "success"
# 	else:
# 		return "dosnt exist"


# @app.route("/select3", methods = ["get", "post"])
# def select3():
# 	username  = request.form['username2']
# 	password = request.form['password2']
# 	x4 = db.select(username, password)
# 	print username
# 	if x4 != None:
# 		return render_template("showlogin.html", loguser = x4)
	# else:
	# 	return "username or password is wrong"


@app.route("/delete", methods = ["POST", "GET"])
def delete():
	print "sakdjahjkdah"
	if request.method == "GET":
		return render_template("delete.html")
	else:
		username = request.form['username']
		password = request.form['password']
		print username
		if db.delete(username, password) == True:
			return render_template("wrongdel.html")
		else:
			return render_template("accdel.html")

if __name__ == "__main__":
	app.run(debug = True)