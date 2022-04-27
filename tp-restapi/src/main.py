from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from random import randint
import random
from datetime import date
fake = Faker() #créer des fausses data
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/store"  # on definie l'url de la database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)  # creation de la db permettant l'interraction avec la base de données


def populate_table():
    for i in range(0,100):
        #création des fausses personnes
         app=["Facebook","Twitter","LinkedIn","Messenger","Discord","Instagram","Skype","Teams"]
         nb_app=randint(1,4)
         applications=[]
         name =fake.first_name()
         last=fake.last_name()
         mail=name+"."+last+"@gmail.com"
         job = fake.job()
         new_user = User(name,last,randint(20,60),mail, job)
         for p in range(1,nb_app):
             choice = random.choice(app)
             applications.append(choice)
         for name in applications:
             username = fake.user_name()
             lastconnection = randint(0,10)
             new_app = Application(name, username,lastconnection,mail,job)
             new_user.application.append(new_app)


         db.session.add(new_user)
    db.session.commit()


@app.route("/", methods=["POST", "GET"])  # on défini la route de l'api
def users():
    if request.method == "GET" : #création de la méthode get
        result = User.query.all()
        users = []
        for row in result :
            user = {
                "id":row.id,
                "firstname": row.firstname,
                "lastname":row.lastname,
                "age":row.age,
                "email":row.email,
                "job":row.job
            }
            users.append(user)
        return jsonify(users)

    if request.method == "POST": #création de la méthode post
        data = request.json
        n_user = {
            data["firstname"],
            data["lastname"],
            data["age"],
            data["email"],
            data["job"]
        }
        db.session.add(n_user)
        db.session.commit()
        return Response(status=100)



class User(db.Model):  # le db est crée grâce à la commande flask
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    job = db.Column(db.String(100))
    application = db.relationship('Application')

    def __init__(self, firstname, lastname, age, email, job):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.job = job


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appname = db.Column(db.String(100))
    username = db.Column(db.String(100))
    lastconnection = db.Column(db.Integer)
    email = db.Column(db.String(100))
    job = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, appname, username, lastconnection,email,job):
        self.appname = appname
        self.username = username
        self.lastconnection = lastconnection
        self.email = email
        self.job=job


if __name__ == '__main__':  # point d'entrée de l'application
    db.drop_all()  # ca supprime tout et ca recreer par la suite
    db.create_all()
    populate_table()
    app.run(host="0.0.0.0", port=8080, debug=True)