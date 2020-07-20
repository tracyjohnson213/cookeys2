import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myCookeys'
# TO-DO remove uri from code
# app.config["MONGO_URI"] = os.getenv('MONGO_URI',
#                                     'mongodb://localhost:27017/myCookeys')
app.config["MONGO_URI"] = os.getenv('MONGO_URI',
                                    "mongodb+srv://tracyj:1studentDeveloper@firstcluster.b5ihz.mongodb.net/myCookeys?retryWrites=true&w=majority")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    """ render all recipes """
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find(),
                           title='Recipes')


if __name__ == '__main__':
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', '5000')),
        debug=True
    )
