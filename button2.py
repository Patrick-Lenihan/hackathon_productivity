#This code is improving upon the code in button1.py
#I've changed the background for the gui here for the sake of you being able to run the code if you wanted to
#So what this code basically does is;
    #1. Opens the gui
    #2. When you click "Timetable" it queries everything in the friends database and displays the result in the gui

import sqlite3
import tkinter as tk
root = tk.Tk()

#Function that prints the results of an sqlite query to the screen of the gui when "timetable" is clicked.
def clicked():
    conn = sqlite3.connect(r"C:\Users\epusi\Documents\Computer Science\1st Year\CS1106 - Databases\Week 2\friends.sqlite")
    c = conn.cursor()

    c.execute('SELECT * FROM persons')
    all_items = c.fetchall()
    
    print_items = " "
    for row in all_items:
        print_items += str(row) + "\n"
    
    label1 = tk.Label(rframe, bg ="#ffffff", text = print_items)
    label1.place(relwidth = 1, relheight = 1)

    conn.commit()
    conn.close()

#Sets the default window size
canvas = tk.Canvas(root, width = 1250, height = 700)
canvas.pack()

#Sets the background image
'''backgroung_image = tk.PhotoImage(file = "background.png")
background_label = tk.Label(root, image = backgroung_image)
background_label.place(relwidth = 1, relheight = 1)'''
background = tk.Label(root, bg = "#ffd480")
background.place(relwidth = 1, relheight = 1)

#Creates the left frame
lframe = tk.Frame(root,bg = "#38312d",bd = 5)
lframe.place(relx = 0, rely = 0, relwidth = 0.1, relheight = 1)

#Home Button
btn1 = tk.Button(lframe, text = "Home", font = ("Helvetica", 18), bg = "#ffd480")
btn1.place(relx = 0.01, rely = 0.01, relwidth = 0.95, relheight = 0.15)

#Timetable Button
btn2 = tk.Button(lframe, text = "Timetable", font = ("Helvetica", 18), bg = "#ffd480",command = clicked)
btn2.place(relx = 0.01, rely= 0.18, relwidth = 0.95, relheight = 0.15)

#Links Button
btn3 = tk.Button(lframe, text = "Links", font = ("Helvetica", 18), bg = "#ffd480")
btn3.place(relx = 0.01, rely = 0.35, relwidth = 0.95, relheight = 0.15)

#Voice Assistant Button
btn4 = tk.Button(lframe, text = "Voice\n Assistant", font = ("Helvetica", 18), bg = "#ffd480")
btn4.place(relx = 0, rely = 0.52, relwidth = 0.95, relheight = 0.15)

#Settings Button
btn5 = tk.Button(lframe, text = "Settings", font = ("Helvetica", 18), bg = "#ffd480")
btn5.place(relx = 0, rely = 0.69, relwidth = 0.95, relheight = 0.15)

#Right Frame
rframe = tk.Frame(root, bg = "#38312d",bd = 5)
rframe.place(relx = 0.15, rely = 0.1, relwidth = 0.8, relheight = 0.8)

#Label in right frame
label1 = tk.Label(rframe, bg ="#ffffff")
label1.place(relwidth = 1, relheight = 1)


root.mainloop()