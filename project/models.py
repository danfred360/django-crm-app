from flask_login import UserMixin
from . import db

# https://docs.sqlalchemy.org/en/14/core/type_basics.html

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

association_table = db.Table('association', db.metadata,
    db.Column('meal_id', db.ForeignKey('meal.id')),
    db.Column('ingredient_id', db.ForeignKey('ingredient.id'))
)

class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(1000), unique=True)
    description = db.Column(db.UnicodeText)
    cost = db.Column(db.Numeric)
    obtained_from = db.Column(db.String(1000))
    meals = db.relationship(
        "Meal",
        secondary=association_table,
        back_populates="ingredients"
    )

class Meal(db.Model):
    __tablename__ = 'meal'
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(1000), unique=True)
    labor_cost = db.Column(db.Numeric)
    description = db.Column(db.UnicodeText)
    prep_time = db.Column(db.Integer)
    prep_instructions = db.Column(db.UnicodeText)
    ingredients = db.relationship(
        "Ingredient",
        secondary=association_table,
        back_populates="meals"
    )
