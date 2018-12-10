"""
Holds the data for the cli app
"""

class User():
    """
        This class holds methods for the user 
    """
    def __init__(self):
        """
            This constructor initializes the user class
        """
        pass


    def signup(self):
        """
            This method registers the user to the app
        """
        pass

    def login(self):
        """ This method logs in a registered user
        """
        pass

    def create_my_comment(self):
        """ 
            This method creates a comment for a logged in user
        """
        pass

    def edit_comment(self):
        """
            This method edits a comment from a logged in user
        """
        pass


class Moderator(User):
    """ 
        this class holds methods for the moderator
    """
    def delete_comment(self):
        """
            This method can delete a comment from any user
        """
        pass

class Admin(User):
    """ 
        This class holds mthods for the admin user
    """
    def edit_any_comment(self):
        """ 
            An admin can edit any comment
        """
        pass
