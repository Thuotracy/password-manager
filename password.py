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
     a_user == user.usename
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
    method used to delete credentialsfreom the credentials list
    """
    Credentials.credentials_list.remove(self)

