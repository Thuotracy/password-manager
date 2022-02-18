from tkinter import Y
from tkinter.messagebox import YES
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

    # @classmethod
def show_user(tracy):
    return tracy.user_list

def delete_user(self):
    """   
    method that deletes a saved account
    """
    User.user_list.remove(self)

class Credentials():
   """
   Creates credential class so as to create new object
   """ 
   credentils_list = []
#    @classmethod
       
def verify_user(tracy,username,password):   
    """
    method to confirm whether the user is in our user_list
    """
a_user = ""
for user in User.user_list:
    if(user.username == username and user.password == password):
      a_user == user.username
    return a_user 
def _init_(self,account,userName,password):
  """ 
   method that tells user credentials to be stored
   """
   self.account = account
   self.userName = userName
   self.password = password 

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

    # @classmethod
def find_credentials(tracy,account):
    """
    method that collects an account_name and outputs the credential that matches the account_name
    """
    for credentials in tracy.credentials_list:
        if credentials.account == account:
            return credentials

    # @classmethod
def copy_password  (tracy,account):
    found_credentials =Credentials.find_credential(account)
    pyperclip.copy(found_credentials.password)
   
    # @classmethod
def if_credential_exist(tracy,account)
   """
   method to check if credential is in credential list then returns yes if credential exist and no if credential does not exist
   """
   for credential in tracy.credentials_list:
       if credential.account == account:
           return YES
       return NO 

    #   @aclassmethod 
def display_credentials(tracy):
    """
    method that returns all items in credential list
    """    
    return tracy.credentials_list

def generatePassword:
    """
    generate random password
    """
    






