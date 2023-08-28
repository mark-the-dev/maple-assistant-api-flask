from flask_restx import Resource, Namespace, reqparse
from main.services.auth import *

character = Namespace("characters")

@character.route('/<user>')
class PlayerCharacters(Resource):
    @character.doc(description="Return list of all characters under **user**")
    def get(self):
        return {
            
        }, 200
        
@character.route('/<user>/character')
class Character(Resource):
    @character.doc(description="Register character to user")
    def post(self):
        return {
            
        }, 200
    
    @character.doc(description="Edit character information to user")
    def put(self):
        return {
            
        }, 200
    
    @character.doc(description="Delete character from user")
    def delete(self):
        return {
            
        }, 200

@character.route('/<user>/character/<character>')
class PlayerCharacter(Resource):
    @character.doc(description="Get the information of given **character** under a **user**")
    def get(self):
        return {
            
        }, 200