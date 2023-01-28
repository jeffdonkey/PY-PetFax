# THIS FILE FOR THE FLASK "APPLICATION FACTORY"

from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    # '@app.route('/)' in part of Flask.  It is used to create routes
    # Flask defautls the route to 'GET'
    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    # Register the pet blueprint.  This connects the blueprint
    # from 'pet.py' to '__init__.py'
    from . import pet
    app.register_blueprint(pet.bp)

    # Register the fact blueprint.  This connects the blueprint 
    # from 'fact.py' to '__init__.py'
    from . import fact
    app.register_blueprint(fact.bp)

    return app
