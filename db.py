import dataset
import sqlite
import sqlalchemy

db = dataset.connect('postgres://ykjzzkipywzyuy:d69b35fcb9b5f29f2fc27b8077c54b8d454c969c61ba024ebec353f5c658a7e7@ec2-107-22-162-158.compute-1.amazonaws.com:5432/d85u0f3u62mvt1', engine_kwargs={'poolclass':sqlalchemy.pool.NullPool})

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


