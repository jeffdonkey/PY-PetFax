# 'Blueprint"s are used to organize related routes and views together
#  a 'one stop shop' for routes and views.
#  similar to JavaScript Express controllers
#  'render_template' accesses views stored in the templates folder
from flask import ( Blueprint, render_template )
#  line below used to access json type files
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def Index():
    return render_template('index.html', pets=pets)

@bp.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)