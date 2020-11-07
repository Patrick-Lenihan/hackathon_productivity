import sqlite3# importing the library if you don't have it installed ill show you how
conn = sqlite3.connect('C:/Users/User/Documents/databases_labs4/friends.sqlite')#contecting to the database use your own file path
c = conn.cursor()# creating a sutable object to work on (just the way this library works

for row in c.execute('SELECT * FROM persons'):#input your sql in here
        print(row)#outputing the code to the shell/terminal

# using this you can do anything we can do in the DB labs
