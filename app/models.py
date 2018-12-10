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

    def create_my_comment(self):
        """ 
            This method creates a comment for a logged in user
        """
        pass

    def edit_comment(self, message_id, comment):
        """
            This method edits a comment from a logged in user
        """
        if self.is_logged_in:
            comments = [comment for comment in self.comment if comment['id'] == message_id]
            comment = comments[0]
            if comment:
                if comment['author'] == self.user_id:                    
                    comment.update('comment', comment)
                    print("comment successfully updated ")
                    return "comment successfully updated"
                print(" you do not have permissions to edit this comment")
                return "You do not have permission to edit this comment"
            print('comment not found')
            return "comment not found"
        print('please log in first')
        return "Please log in first"




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
    def edit_any_comment(self, message_id, comment):
        """ 
            An admin can edit any comment
        """
        if self.is_logged_in and self.is_admin:
            comments = [comment for comment in self.comment if comment['id'] == message_id]
            comment = comments[0]
            if comment:
                comment.update('comment', comment)
                print("comment successfully updated ")
                return "comment successfully updated"
            print("comment does not exist")
            return "comment does not exist"
        print("You do not have permissions to edit any comment")
        return "You do not have permission to edit any comment "




