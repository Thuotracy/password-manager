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
    