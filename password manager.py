from password import User 
from password import Credentials

def create_new_user(username,password):
    """
    function to create new user
    """
    new_user = User(username,password)
    return new_user

def save_user(user):
    """
    function to save new user
    """    
    user.save_user()

def display_user():
    """
    function to show existing user
    """    
    return User.display_user()

    