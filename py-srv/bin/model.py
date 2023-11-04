# app/models.py
from tortoise.models import Model
from tortoise import fields

class Dog(Model):
    breed = fields.TextField()
    color = fields.TextField()

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def __repr__(self):
        return "<Dog('%s', '%s')>" % (self.breed, self.color)
