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

def login_user(username,password):
    """
    function to check whether the user already exists and logs them in
    """
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,username,password):
    """
    function that creates new credential for a user
    """    
    new_credential = Credentials(account,username,password)
    return new_credential

def save_credential(credentials):
    """
    function to save credentials to the credential list
    """    
    credentials.save_details()

def display_account_details():
     """
     function that returns all saved credentials
     """
     return Credentials.display_credentials()
 
def delete_credentials(credentials):
     """
     function to delete credential from credentials list 
     """
     credentials.delete_credentials()

     

