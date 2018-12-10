from .models import User
from .models import Comment
import random
import pprint

print("WELCOME TO CLI_BLOG")
welcome = input('Enter 1 => login 2=> Sign Up')
if welcome == 1:
    username = input("please enter Username")
    password = input("please enter Password")
    if (u = User.login(username, password)):
        print("Welcome")
        print(" 1 => create comment \n \
        2 => edit comment \n \
        3 => views comment \n \
        4 => exit \n \
        ")
        choice =  input("Choice +>")

        if choice == 1:
            msg = input("Enter the comment")
            a_comment = Comment.create_comment(msg,u.user_id,random(0,6))
            print("Comment saved")
            pprint.print(a_comment)

        elif choice == 2:
            input("")



