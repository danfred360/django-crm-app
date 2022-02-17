from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Meal, Ingredient
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/meals')
@login_required
def meals():
    meals = Meal.query.filter_by(creator_id=current_user.id)
    ingredients = Ingredient.query.filter_by(creator_id=current_user.id)
    return render_template('meals.html', meals=meals, ingredients=ingredients)
