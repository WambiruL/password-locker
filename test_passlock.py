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

        self.new_user= User("LorraineW", "Ziklag") #create user object

    def test_init(self):
        """
        Test case to test if the object is initalised properly
        """

        self.assertEqual(self.new_user.username,"LorraineW")
        self.assertEqual(self.new_user.password, "Ziklag")  #assertEqual checks for an expected result

    def test_save_user(self):
        """
        Test if the user object is saved into the user list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

