import unittest
from password import  User, Credentials

class TestClass(unittest.TestCase):
    """
    a test class that defines test cases for the User class
    """

def setUp(self):
    """
    method that is executed before each individual tets methods run
    """
    self.new_user = User('Tracy Wangari','thuo')

def test_init(self):
    """
    a test to confirm whether the object is working correctly
    """
    self.assertEqual(self.new_user.username,'Tracy Wngari')
    self.assertEqual(self.new_user.password,'thuo')

def test_save_user(self):
    """
    a test to check if new user has been added to User list
    """
    self.new_user.save_user()
    self.assertEqual(User.user_list)

class TestCredentials(unittest.TestCase):
    """
    a test that defines test casee for the credentials class
    """    

def setUp(self):
    """
    method that is executed before each individual credentialtest method runs
    """
    self.new_credential= Credentials('Gmail', 'Tracy Wangari', 'thuo')

def test_init(self):
    """
    test to check whether a new credential information has been entered correctly
    """
    self.assertEqual(self.new_credential.account,'Gmail')
    self.assertEqual(self.new_credential.username,'Tracy Wangari')
    self.assertEqual(self.new_credential.passwword,'thuo')

def save_credential_test(self):
    """
    test to check whether the credential is saved to the credential list
    """
    self.new_credential.save_detail()
    self.assertEqual(Credentials.credentials_list)

Credentials.credentils_list = []

def test_save_many_accounts(self):
    """
    test to see if we can save many accounts
    """
    