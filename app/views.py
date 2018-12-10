from models import User
from models import Comment
import random

user = User()

print("WELCOME TO CLI_BLOG")
welcome = input('Enter 1 => login 2=> Sign Up \n')
welcome = int(welcome)
if welcome == 1:
    username = str(input("please enter Username \n"))
    password = str(input("please enter Password \n"))
    u = user.login(username, password)
    if u:
        print("Welcome")
        print(" 1 => create comment \n \
        2 => edit comment \n \
        3 => views comment \n \
        4 => exit \n \
        ")
        choice =  input("Choice +>")

        if choice == 1:
            msg = input("Enter the comment \n")
            a_comment = Comment.create_comment(msg,u.user_id,random.random(0,6))
            print("Comment saved")
            print(a_comment)

        elif choice == 2:
            input("")



