import dataset
import sqlite
import sqlalchemy

db = dataset.connect('sqlite:///wocode', engine_kwargs={'poolclass':sqlalchemy.pool.NullPool})

def tempdata():
	table = db['sometable']
	table.insert(dict(name='John Doe', age=37, password='password', username='username'))
	table.insert(dict(name='Jane Doe', age=34, gender='female', password='pswrd', username='userid'))
	table.insert(dict(name='Joze Doe', password='password1', username='username1'))
	table.insert(dict(name= 'Hoje Doe', username='email', password='psw'))
	table.insert(dict(name= 'Joje Doe', username = 'username2', password = 'password2' ))


def insert(passs,user):
	table = db['sometable']
	generated_id = table.insert(dict(password=passs, username=user))
	print generated_id
	if generated_id and generated_id > 0:
	#if generated_id = None:
		return True
	else:
		return False

def showusers():
	table = db['sometable']
	Hoje = table.all()
	return Hoje

def showusers2():
	table = db['sometable']
	Jane = table.all()
	users = []
	for user in Jane:
		users.append(user)
	return users


def chat (email,feedback):
	table= db['sometable']
	generated_id = table.insert(dict(email= username ,feedback= password))
	if generated_id and generated_id > 0:
		return True
	else:
		return False


def select(username,password):
	table = db['sometable']
	Joze = table.find_one(username = username, password= password)
	return Joze


def select2(usertake):
	table = db["sometable"]
	Hoje = table.find_one(email = usertake)
	return Hoje


def select3(username2, password2):
	table = db["sometable"]
	Joje = table.find_one(username2 = username2, password2 = password2)
	return Joje
	
def delete(username2):
	table = db["sometable"]
	laith = table.find_one(username = username2)
	if laith == None:
		return True
	else:
		laith2 = table.delete(username = username2)
		return  False
	
#tempdata()