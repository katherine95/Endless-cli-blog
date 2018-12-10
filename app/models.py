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
        self.username = ''
        self.is_logged_in = False
        self.comment = comments

    def signup(self,username,):
        """
            This method registers the user to the app
        """
        

    def login(self):
        """ This method logs in a registered user
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

class Comment(object):

    def __init__(self):
        """ 
            This method creates a comment for a logged in user
        """
        self.comment = comments

    def create_comment(self, message, author, createdAt, reply):
        comment_details = {}
        comment_details['author'] = author
        comment_details['message'] = message
        comment_details['createdAt'] = datetime.datetime.now()
        comment_details['reply'] = reply
        comment_details['id'] = len(comments) + 1

        comments.append(comment_details)
        return comment_details


