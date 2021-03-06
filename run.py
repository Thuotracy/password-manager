from password import User, find_credentials 
from password import Credentials
from password_test import save_credential_test

def create_new_user(account,username,password):
    """
    function to create new account details
    """
    new_user = User(account,username,password)
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

def check_credential(account):
    """
    function that checks if credential exists and returns true or false
    """
    return Credentials.if_credential_exist(account)

def generate_password():
    """
    function that generates random password 
    """
    auto_password = Credentials.generatepassword()
    return auto_password

def passlocker():
    print("Hello welcome to your account password manager... \n Please enter one of the following to proceed. \n CREATE --- Create new account \n LIST --- Have an account \n")
    short_code=input("").lower().strip()
    if short_code == "create":
        print("Sign up")
        username = input("User_name:")
        while True:
            print("TYPE - To type password of your choice: \n GENERATE - To generate a random password")
            password_Choice = input().lower().strip()
            if password_Choice == 'type':
                password = input("Enter password \n")
                break
            elif password_Choice == 'generate':
                password = generate_password() 
                break
            else:
                print("Invalid password please try again")
            save_user(create_new_user(username,password,))
            print(f"{username}, your account has been created! Your password is :{password}")
    elif short_code == "list":
        print("Enter your user name and password to login")
        username = input ("user name:")
        password = input ("password:")
        login = login_user(username,password)
        if login_user == login:
            print(f"{username}.Welcome to password manager")
            print('\n')
    while True:
        print("use these short codes:\n new -Create new credential \n DISPLAY -Display credential \n FIND -Find credential \n GENERATE - Generate a random password \n DELETE -Delete credential \n EXIT - Exit \n")
        short_code = input().lower().strip()
        if short_code == "new":
            print("Create new account")
            print ("Account name....")
            account = input().lower()
            print("Your username")
            username = input()      
            while True:
                print ("CP - To create your own password if you already have an account: \n GENERATE - To generate a new pasaword")
                password_choice = input().lower().strip()
                if password_choice == 'type':
                    password = input ("Type password of your choice \n")
                    break
                elif password_choice == 'generate':
                    password_choice = generate_password()
                    break
                else:
                    print("Invalid password.Please try again")
            save_credential_test(create_new_credential(account,username,password))  
            print('\n')
            print(f"Account credentials for: {account} - UserName: {username} - password: {password} created successfully")
            print ('\n')
        elif short_code == "display":
         if display_account_details():
            print("Here are your accounts: ")
            for account in display_account_details():
                print(f"Account:{account.account} \n User name:{username} \n Password:{password}")    
            else:
                print("You do not have any credentials saved yet")
        elif short_code == "find": 
          print("Write the account name you want to search for")
        search_name = input().lower()
        if check_credential(search_name):
            search_credential = find_credentials(search_name)
            search_credential.delete_credential()
            print('\n')
        else:
         print("The credential does not exist")
if __name__ == '__main__':
            passlocker()
