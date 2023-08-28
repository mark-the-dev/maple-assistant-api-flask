from .. import db
from main.models.user import User
import hashlib

"""
Creates a new user in the database.

Parameters:
- username (str): The username for the new user.
- password (str): The password for the new user.

Hashes the password using SHA256 before storing in the database. 
Creates a new User instance and attempts to commit to the database.
Rolls back and raises exception on failure.

Returns:
- User: The newly created User instance.

Raises:
- Exception: Any error during database commit.
"""
def create_new_user(username, password):
    # Hash the password
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    # Create instance of User
    user = User(
        username=username,
        password=password_hash
    )
    
    # Add instance to the database, throw exception if failure
    try:
        db.session.add(user)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    
    return user

"""
Verifies user login credentials.

Parameters:
- username (str): The username of the user trying to log in.  
- password (str): The password of the user trying to log in.

Queries the database for a user with the given username. 
If a user is found, hashes the given password and compares it to the 
stored hash. 

Returns:
- User object if username and password are valid.
- False if username found but password invalid.  
- None if username not found.

"""
def verify_login(username, password):
    # Query for user
    user = User.query.filter_by(username=username).first()
    
    if user:
        # Verify password
        password_hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if user.password == password_hashed:
            return user
        else:
            return False
    else:
        return None