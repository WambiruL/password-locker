import pyperclip

class User:
    """
    A class that generates new instances of users
    """

    user_list=[] # will store created user objects

    def __init__(self,username, password):

        """
        Method that defines the attributes of a user
        """
    
        self.username=username
        self.password=password

    def save_user(self):

        """
        This method saves user objects into user_list
        """

        User.user_list.append(self) 

@classmethod
def user_exist(cls,username,password):
        """
        Method that checks if a user exists from the user_list
        """
        a_user=""
        for user in User.user_list:
            if (user.username==username and user.password==password):
                a_user==user.username
        return a_user

class Credentials:
    """
    Class that generates new instances of credentials
    """ 

    credentials_list=[]
    
    

    def __init__(self,account,username,password):
        """
        Method that defines user credentials to be stored
        """

        self.account=account
        self.username=username
        self.password=password

    def save_credentials(self):
        """
        Method to store a new credential to the credentials list
        """

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        Method that deletes a saved credential
        """

        Credentials.credentials_list.remove(self)

@classmethod
def find_credentials(cls,account):
    """
    Method that takes in account name and returns credentials that match that account
    """

    for credential in cls.credentials_list:
        if credential.account==account:
                return credential

@classmethod
def if_credential_exist(cls,account):
    """
    Method that checks if credentials exists from credentials list
    """

    for credential in cls.credentials_list:
        if credential.account==account:
            return True
    return False

@classmethod
def display_credentials(cls):
    """
    Method that returns the contact list
    """

    return cls.credentials_list

@classmethod
def copy_password(cls,account):
    found_credentials=Credentials.find_credential(account)
    pyperclip.copy(found_credentials.password)




  