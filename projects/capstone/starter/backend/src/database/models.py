import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

from backend.settings import DB_NAME, DB_USER, DB_PASSWORD, DB_URL

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_name = DB_NAME
database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,DB_URL, database_name)

db = SQLAlchemy()
print(DB_NAME)
print(DB_USER)
print(DB_URL)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    print("Creating new DB")
    db.drop_all()
    db.create_all()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    print(database_path)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

film_actor = db.Table('film_actor',
                            db.Column('filmId', db.Integer, db.ForeignKey('film.id'), primary_key=True),
                            db.Column('actorId', db.Integer, db.ForeignKey('actor.id'), primary_key=True)
                         )

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.String)
    actors = db.relationship('Actor', secondary=film_actor, backref=db.backref('films', lazy=True))

    '''
    long()
        long form representation of the Film model
    '''
    def long(self):
        cast = []
        for a in self.actors:
            cast.append(a.short())

        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'cast' : cast
        }

    '''
    short()
        short form representation of the Film model
    '''
    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    '''
    insert()
        inserts a new film into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            film = Film(title=req_title, release_date=release_date)
            film.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a film from the database
        the model must exist in the database
        EXAMPLE
            film = Film(title=req_title, release_date=release_date)
            film.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    '''
    update()
        updates a film 
        the model must exist in the database
        EXAMPLE
            film = Film.query.filter(Film.id == id).one_or_none()
            film.title = 'New Title'
            film.update()
    '''

    def update(self):
        print('Update')
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)


    '''
    long()
        long form representation of the Actor model
    '''
    def long(self):
        roles = []
        for f in self.films:
            roles.append(f.short())

        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender' : self.gender,
            'roles' : roles
        }

    '''
    short()
        short form representation of the Actor model
    '''
    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender' : self.gender
        }

    '''
    insert()
        inserts a new actor into a database
        the actor must have a unique name
        EXAMPLE
            actor = Actor(name=req_name, age=req_age, gender = req_gender)
            actor.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes an actor from the database
        the model must exist in the database
        EXAMPLE
            actor = Actor(name=req_name, age=req_age, gender = req_gender)
            actor.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    '''
    update()
        updates an actor
        the model must exist in the database
        EXAMPLE
            actor = Film.query.filter(Film.id == id).one_or_none()
            actor.name = 'New Name'
            actor.update()
    '''

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())