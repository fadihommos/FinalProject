import dataset
import sqlalchemy
import time
# sadek's db
#db = dataset.connect('postgres://ykjzzkipywzyuy:d69b35fcb9b5f29f2fc27b8077c54b8d454c969c61ba024ebec353f5c658a7e7@ec2-107-22-162-158.compute-1.amazonaws.com:5432/d85u0f3u62mvt1', engine_kwargs={'poolclass':sqlalchemy.pool.NullPool})

# heroku db linked to codepalestine
db = dataset.connect('postgres://gekfeekpdeldpr:b9aeb07051bb27207f972128b045e2e0a2a20b07be2d2c86147914fe538b7043@ec2-54-204-32-145.compute-1.amazonaws.com:5432/dchaerkmjsv0dn', engine_kwargs={'poolclass':sqlalchemy.pool.NullPool})

def signup(username, password, email):
	table = db["users"]
	entry = {"username": username, "password" : password, "email" : email}
	generatedid = table.insert(entry)
	if generatedid > 0:
		return True
	return False

def getUserByUsername(username):
	table = db["users"]
	user = table.find_one(username=username)
	return user

def allUsers():
	table = db['users']
	return table.all()

def signin(username, password):
	table = db['users']
	generatedid = table.find_one(username=username, password=password)
	print generatedid
	if generatedid > 0:
		return True
	return False

def feedback(message):
	table = db['feeds']
	entry = {"message":message}
	insert = table.insert(entry)
	return insert

def allfeeds():
	table = db['feeds']
	return table.all()


def newsfeed(emailfeed,text,time_string):
	newsfeed = db['newsfeeds']
	entry = {'emailfeed':emailfeed, 'text':text, 'time_string':time_string}
	insert = newsfeed.insert(entry)
	#print insert
	return insert

def allnews():
	newsfeeds = db['newsfeeds']
	return newsfeeds.all()

def delete(username, password):
	table = db['users']
	table.delete(username = username, password = password)

	#when somebody create an account they can deleted by this function
	#if the function found the username in the database it will deleted
	#first found the username by found_one
	#table.delete()

