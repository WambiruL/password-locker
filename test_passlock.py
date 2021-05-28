import unittest
from passlock import User, credential_exists
from passlock import Credentials

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

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credential class
    """

    def setUp(self):
            """
            Method that runs before each credentials test
            """

            self.new_credential=Credentials("Gmail", "Lorraine Wambui", "Salamander")

    def test_init(self):
        """
        Test case to check if new credentials has been initialized correctly
        """

        self.assertEqual(self.new_credential.account, "Gmail")
        self.assertEqual(self.new_credential.username, "Lorraine Wambui")
        self.assertEqual(self.new_credential.password, "Salamander")

    def tearDown(self):
            """
            Method that does clean up after each test case has run
            """

            Credentials.credentials_list=[]

    def save_credential_test(self):
        """
        Test case to test if credential object is saved into the credentials list
        """

        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

      

    def test_save_multiple_credentials(self):
        """
        test case to check if we can save multiple credentials
        """
        self.new_credential.save_credentials()
        test_credentials=Credentials("Instagram", "lorrainewambui", "marimar")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):

        """
        Test if we can remove a credential from the list
        """

        self.new_credential.save_credentials()
        test_credential=Credentials("Instagram", "lorrainewambui", "marimar")
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials(self):

        """
        Check if we can find a credential by account name and display information
        """

        self.new_credential.save_credentials()
        test_credential=Credentials("Instagram", "lorrainewambui", "marimar")
        test_credential.save_credentials()

        found_credential=Credentials.find_credentials("Instagram")

        self.assertEqual(found_credential.account, test_credential.account)

    def test_credential_exists(self):
        """
        test if we can return true or false if we cannot find credential
        """

        self.new_credential.save_credentials()
        test_credential=Credentials("Instagram", "lorrainewambui", "marimar")
        test_credential.save_credentials()

        credential_exists=Credentials.credential_exist("Instagram")

        self.assertTrue(credential_exists) 



if __name__=='__main__':
    unittest.main()




