import pyperclip


class User:
    """
    Create user class to add new user
    """
    user_list = []

def __init__(self, username, password):
    """
    method that allows us to define properties of a user
    """
    self.username = username
    self.password = password

def save_user(self): 
    """  
    method that saves a new user
    """
    User.user_list.append(self)

    @classmethod 
    def show_user(cls):
      return cls.user_list

class Credentials():
   """
   Creates credential class so as to create new object
   """ 
   credentials_list = []

   def _init_(self,account,userName,password):
        """ 
        method that tells user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password 

@classmethod
def verify_user(cls,username,password):   
    """
    method to confirm whether the user is in our user_list
    """
    for details in cls.credential_list:
      if details.username ==username:
          return details  

def save_details(self):
        """
        method to save a new credential to the credentials list
        """   
        Credentials.credentials_list.append(self)

def delete_credentials(self):
    """
    method used to delete credentials from the credentials list
    """
    Credentials.credentials_list.remove(self)

@classmethod
def find_credentials(cls,account):
    """
    method that collects an account_name and outputs the credential that matches the account_name
    """
    for credentials in cls.credentials_list:
        if credentials.account == account:
            return credentials

@classmethod
def copy_password  (cls,account):
    found_credentials =Credentials.find_credential(account)
    pyperclip.copy(found_credentials.password)
   
@classmethod
def if_credential_exist(cls,account):
   """
   method to check if credential is in credential list then returns true if credential exist and false if credential does not exist
   """
   for credential in cls.credentials_list:
       if credential.account == account:
           return True
       return False

@classmethod 

def display_credentials(cls):
    """
    method that returns all items in credential list
    """    
    return cls.credentials_list

def generate_password():
    """
    generate random password
    """
    






