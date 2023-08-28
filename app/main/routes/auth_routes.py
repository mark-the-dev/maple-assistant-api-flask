from flask_restx import Resource, Namespace, reqparse
from main.services.auth import *

auth = Namespace("auth")

@auth.route('/register')
class Register(Resource):
    @auth.doc(description="Registering new user")
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
                    "username": f"Issue with inputed value"
                },
                "message": f"User with username [{username}] already exists!"
            }, 409
        
        return {
            "message": f"Success!",
            "user": f"{user}"
        }, 200

@auth.route('/login')
class Login(Resource):
    @auth.doc(description="Logging in user")
    def post(self):
        # Define arguments in request body
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        
        # Grab arguments from the request body
        args = parser.parse_args()
        
        username = args['username']
        password = args['password']
        
        user = verify_login(username, password)
        
        if user is not None:
            if user:
                return {
                    "message": f"Success!",
                    "user": f"{user}"
                }, 200
            else:
                return {
                    "errors": {
                        "password": f"Issue with inputed value"
                    },
                    "message": f"Incorrect password!"
                }, 401
        else:
            return {
                "errors": {
                    "username": f"Issue with inputed value"
                },
                "message": f"User with username [{username}] doesn't exist!"
            }, 401
