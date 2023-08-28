from flask_restx import Resource, Namespace, reqparse
from main.services.auth import *

auth = Namespace("auth")

@auth.route('/register')
class Register(Resource):
    def post(self):
        # Define arguments in request body
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        
        # Grab arguments from the request body
        args = parser.parse_args()
        
        username = args['username']
        password = args['password']
        
        # Create new user, throwing error if failed
        try:
            user = create_new_user(
                username=username,
                password=password
            )
        except Exception:
            return {
                "errors": {
                    "username": f"Issue with inputed username"
                },
                "message": f"User with username [{username}] already exists!"
            }, 409
        
        return {
            "message": f"Success!",
            "user": f"{user}"
        }, 200
        
        