import unittest
from passlock import User

class TestUser(unittest.TestCase): #Unittest.Testcase helps in creating test cases
    """
    Test class that defines test cases for the User class behaviours.
    """

def setUp(self):
    """
    Method that runs before each test cases
    """

    self.new_user= User("LorraineW", "Ziklag")

