from flask import Blueprint, render_template, redirect, url_for, request, flash
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

@main.route('/create_meal')
@login_required
def create_meal():
    ingredients = Ingredient.query.filter_by(creator_id=current_user.id)
    return render_template('create_meal.html', ingredients=ingredients)

@main.route('/create_meal', method=['POST'])
@login_required
def create_meal_post():
    name = request.form.get('meal_name')
    description = request.form.get('meal_description')
    prep_time = request.form.get('meal_prep_time')
    prep_instructions = request.form.get('meal_prep_instructions')
    labor_cost = request.form.get('meal_labor_cost')

    if not prep_time.isnumeric():
        flash('Please enter preparation time in minutes, using only numbers.')
        return redirect(url_for('main.create_meal'))

    if not labor_cost.isdecimal():
        flash('Please enter a decimal number for labor cost.')
        return redirect(url_for('main.create_meal'))

    meal = Meal.query.filter_by(name=name).first()

    if meal:
        flash('A meal with this name already exists.')
        return redirect(url_for('main.create_meal'))

    new_meal = Meal(
        creator_id=current_user.id,
        name=name,
        description=description,
        labor_cost=labor_cost,
        prep_time=prep_time,
        prep_instructions=prep_instructions
        )

    db.session.add(new_meal)
    db.session.commit()

    return redirect(url_for('main.meals'))
