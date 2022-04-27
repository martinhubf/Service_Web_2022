# Web server
from sqlalchemy import create_engine

db_string ="postgresql://root:root@localhost:5432/store"

db = create_engine(db_string)
connection= db.connect()

#création de la table USER
#connection.execute("CREATE TABLE IF NOT EXISTS Users (id text PRIMARY KEY, firstname text, lastname text, age int,email text,job text)")
#connection.execute("CREATE TABLE IF NOT EXISTS Application (id text PRIMARY KEY, appname text, username text, lastconnection date,user_id text)")
bd = open('create.sql')
connection.execute(bd.read())
bd.close()


