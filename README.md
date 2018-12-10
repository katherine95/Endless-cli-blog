# Endless-cli-blog
The app provides a platform where users can login , comment and edit their own comments.
## Users: 
> Users come in 3 roles: normal users, moderators, and admins.
```
Normal users can only create new comments, and edit the their own comments.
Moderators have the added ability to delete comments (to remove trolls), 
while admins have the ability to edit or delete any comment. 
```
> Users can log in and out, and we track when they last logged in Comments:
``` Comments are simply a message, a timestamp, and the author.
Comments can also be a reply, so we'll store what the parent comment was. 
```
**NOTE: User Users can be logged in and out. When logging in, set the lastLoggedInAt timestamp**

*Do not modify this timestamp when logging out*

```
Users can only edit their own comments Users cannot delete any comments
```

```
Moderator is a User Moderators can only edit their own comments Moderators can delete any comments
```
```
Admin is both a User and a Moderator Admins can edit any comments Admins can delete any comments Comments contain a reference to the User who created it (author)
```
## How to use
> to Use the app
* clone the repo

`git clone https://github.com/katherine95/Endless-cli-blog.git`

* cd into the project folder and run

` python run.py `

* You will be prompted with login or sign up

## Contributors
* Catherine Chepkirui
* Lawrence Chege
* Kyppy Simani
* Joseph Mutiga

[Pivotal tracker] (https://www.pivotaltracker.com/n/projects/2230917)

