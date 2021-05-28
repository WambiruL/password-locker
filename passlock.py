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

class Credentials:
    """
    Class that generates new instances of credentials
    """