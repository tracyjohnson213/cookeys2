import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myCookeys'
# TO-DO remove uri from code
# app.config["MONGO_URI"] = os.getenv('MONGO_URI',
#                                     'mongodb://localhost:27017/myCookeys')
app.config["MONGO_URI"] = os.getenv('MONGO_URI',
                                    "mongodb+srv://admin:1studentDeveloper@firstcluster.b5ihz.mongodb.net/myCookeys?retryWrites=true&w=majority")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    """ render all recipes """
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find(),
                           title='Recipes')


@app.route('/get_cookie/<cookie_name>')
def get_cookie(cookie_name):
    """ render individual recipe """
    the_cookie = mongo.db.recipes.find_one(
        {"cookie_name": cookie_name})
    return render_template('cookie.html',
                           recipe=mongo.db.recipes.find_one(
                               {'cookie_name': cookie_name}),
                           cookie=the_cookie,
                           categories=mongo.db.categories.find())


@app.route('/add_recipe')
def add_recipe():
    """ render form to input new recipe """
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    """ insert recipe into database """
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """ render form to edit recipe """
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editrecipe.html',
                           recipe=the_recipe,
                           categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    """ update recipe in database """
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
                   {
        'cookie_name': request.form.get('cookie_name'),
        'ingredients': request.form.get('ingredients'),
        'qty': request.form.get('qty'),
        'steps': request.form.get('steps'),
        'firstname': request.form.get('firstname'),
        'lastname': request.form.get('lastname'),
        'summary': request.form.get('summary'),
        'recipe_category': request.form.get('recipe_category'),
        'image_source': request.form.get('image_source')
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """ remove recipe from database """
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


@app.route('/get_categories')
def get_categories():
    """ render all categories """
    return render_template('categories.html',
                           categories=mongo.db.categories.find(),
                           title='Categories')


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
    return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    """ render form to edit category """
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                               {'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    """ update category in database """
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'recipe_category': request.form.get('recipe_category')},
        {'category_desc': request.form.get('category_desc')})
    return redirect(url_for('get_categories'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    """ remove category from database """
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


if __name__ == '__main__':
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', '5000')),
        debug=True
    )
