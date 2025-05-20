from mongoengine import Document, StringField, IntField, ListField, ReferenceField

class User(Document):
    email = StringField(required=True, unique=True)
    name = StringField(max_length=100, required=True)
    password = StringField(max_length=100, required=True)

class Team(Document):
    name = StringField(max_length=100, required=True)
    members = ListField(ReferenceField(User))

class Activity(Document):
    user = ReferenceField(User, required=True)
    type = StringField(max_length=50, required=True)
    duration = IntField(required=True)

class Leaderboard(Document):
    team = ReferenceField(Team, required=True)
    points = IntField(required=True)

class Workout(Document):
    name = StringField(max_length=100, required=True)
    description = StringField()