import datetime
"""
Holds the data for the cli app
"""
users = []
comments = []
class User():
    """
        This class holds methods for the user 
    """
    def __init__(self):
        """
            This constructor initializes the user class
        """
        self.users = users    
        self.last_logged_in = ""
        self.is_admin = False
        self.is_moderator =  False
        self.username = username
        self.is_logged_in = False
        self.comment = comments
        self.password = password
        

    def signup(self,username,password,is_admin=False,is_moderator=False):
        """
            This method registers the user to the app
        """
        for user in self.users:
            if username  == user.username:
                print("Username already exists")
                return False
            else:
                self.user_id = len(self.users) + 1
                self.username = username
                self.password = password
                self.is_admin = is_admin
                self.is_moderator = is_moderator
                self.users.append(self)
                print("Successful signup")
                return True


    def login(self,username, password):
        """ This method logs in a registered user
        """
        for user in self.users:
            if user.username == username and user.password == password:
                user.last_logged_in = datetime.datetime.now()
                user.is_logged_in  = True
                print("Login successful")
                return True
        print("Login failed")
        return False

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

class Admin(Moderator):
    """ 
        This class holds mthods for the admin user
    """
    def edit_any_comment(self):
        """ 
            An admin can edit any comment
        """
        pass


