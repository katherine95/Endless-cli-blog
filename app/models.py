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
        self.username = ""
        self.is_logged_in = False
        self.comment = comments
        self.password = ''
        self.signup("Joe","1234")
    def signup(self,username,password,is_admin=False,is_moderator=False):
        """
            This method registers the user to the app
        """
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.is_moderator = is_moderator
        self.users.append(self)
        
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
        self.is_admin = is_admin
        for user in self.users:
            if user.username == username and user.password == password:
                user.last_logged_in = datetime.datetime.now()
                user.is_logged_in  = True
                print("Login successful")
                return True
        print("Login failed")
        return False


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
    def delete_comment(self, message_id):
        """
            This method can delete a comment from any user.
        """
        if self.is_moderator or self.is_admin:
            for comment in self.comments:
                if comment["id"] == message_id:
                    self.comments.remove(comment)
                    print ("Comment has been deleted")
                    return
                print("Message: No comment found")
                return
        print("Not authorized to delete comments")
        return
          

class Admin(Moderator):
    """ 
        This class holds mthods for the admin user
    """
    def edit_any_comment(self, message_id, comment):
        """ 
            An admin can edit any comment
        """
        pass
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

class Comment(object):

    def __init__(self):
        """ 
            This method creates a comment for a logged in user
        """
        self.comment = comments

    def create_comment(self, message, author, reply):
        comment_details = {}
        comment_details['author'] = author
        comment_details['message'] = message
        comment_details['createdAt'] = datetime.datetime.now()
        comment_details['reply'] = reply
        comment_details['id'] = len(comments) + 1

        comments.append(comment_details)
        return comment_details
