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