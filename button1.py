#This creates a GUI that pops up when the code is executed. I used tkinter to create the GUI
#The GUI has a button called "Database", which prints the database in the python terminal when clicked
#The next step here would probably be to figure out how to display the database in the GUI instead of the Python Terminal
#I've used Patrick's previous database_python_test.py to connect the Python with the SQL


#Imports tkinter, it usually comes installed with python
from tkinter import *

#First half of Patrick's code
import sqlite3
conn = sqlite3.connect(r"C:\Users\epusi\Documents\Computer Science\1st Year\CS1106 - Databases\Week 2\friends.sqlite")
c = conn.cursor()

#Creates a window
window = Tk() 
window.geometry("350x200") #Sets the default size of the window that pops up (you can change it to whatever size you want)

#Creates a button
def clicked():
    #Second half of Patrick's code
    for row in c.execute('SELECT * FROM persons'):
        print(row)
btn = Button(window, text = "Database", command = clicked) #Creates a button labeled "Database", which executes the function "clicked" when it is clicked
btn.grid(column = 0, row = 0) #Sets the position of the button in the window 

window.mainloop()


