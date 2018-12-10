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
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.is_moderator = is_moderator
        self.users.append(self)


    def login(self):
        """ This method logs in a registered user
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
    def edit_any_comment(self, message_id):
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




