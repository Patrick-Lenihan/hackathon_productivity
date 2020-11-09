#This the most up to date version of the gui
#All the buttons work
#The main new feature is the "Plan An Event" button. When pressed, it shows two boxes; one for the user to input information and another for the ouput.
#This will be where the user enters times and displays when people are free. For now it just allows you to enter characters and prints those characters in the output box.

'''import speech_recognition as sr
import webbrowser
r = sr.Recognizer()'''

import sqlite3
import tkinter as tk
root = tk.Tk()

#Sets the default window size
canvas = tk.Canvas(root, width = 1250, height = 700)
canvas.pack()

#Sets the background image
'''background_image = tk.PhotoImage(file = "background1.png")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)'''
background = tk.Label(root, bg = "#ffd480")
background.place(relwidth = 1, relheight = 1)

#Funtion for when the home button is clicked
def click_home():
    label1 = tk.Label(rframe, bg ="#ffffff", text = "Welcome", font = ("Helvetica", 24))
    label1.place(relwidth = 1, relheight = 1)

#Function that prints the results of an sqlite query to the screen of the gui when "timetable" is clicked.
def click_timetable():
    conn = sqlite3.connect(r"C:\Users\epusi\Documents\Computer Science\1st Year\CS1106 - Databases\Week 2\friends.sqlite")
    c = conn.cursor()

    c.execute('SELECT * FROM persons')
    all_items = c.fetchall()
    
    print_items = " "
    for row in all_items:
        print_items += str(row) + "\n"
    
    label1 = tk.Label(rframe, bg ="#ffffff", text = print_items, font = ("Helvetica", 18))
    label1.place(relwidth = 1, relheight = 1)

    conn.commit()
    conn.close()

#Funtion for when the links button is clicked
def click_linksbtn():
    label1 = tk.Label(rframe, bg ="#ffffff", text = "(Links will be here)", font = ("Helvetica", 24))
    label1.place(relwidth = 1, relheight = 1)

#Function for Voice Assistant Button
def speech_recognition():
    '''with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            if text == 'open canvas'or text=='open pandas':
                webbrowser.open('https://ucc.instructure.com/', new=0, autoraise=True)
            elif text == 'go to lecture':
                webbrowser.open('https://teams.microsoft.com/l/meetup-join/19%3ameeting_N2U4MTk4ZDAtZjBmYi00MjU5LWJiNjAtMWRiYTg4ODhlYmJi%40thread.v2/0?context=%7b%22Tid%22%3a%2246fe5ca5-866f-4e42-92e9-ed8786245545%22%2c%22Oid%22%3a%2262b28634-96ed-4537-baea-4bd8ce87b3d3%22%7d', new=0, autoraise=True)
                
        except:
            print("Sorry could not recognize what you said")'''


    label1 = tk.Label(rframe, bg ="#ffffff", text = "Ask the voice assistant for assistance.\n e.g. 'Open Canvas' or 'go to lecture' ", font = ("Helvetica", 24))
    label1.place(relwidth = 1, relheight = 1)

#Funtion for when the event button is clicked
def click_event():

    label1 = tk.Label(rframe, bg ="#38312d")
    label1.place(relwidth = 1, relheight = 1)

    tframe_ev = tk.Frame(label1, bg ="#aaaaaa")
    tframe_ev.place(relwidth = 1, relheight = 0.495)

    entry_box = tk.Entry(tframe_ev, font = ("Helvetica",15), text = "Enter times here")
    entry_box.place(relx = 0, rely = 0, relwidth = 0.775, relheight = 1)

    entry_btn = tk.Button(tframe_ev, relief = "ridge", font = ("Helvetica",15), text = "Press here to\n find matches", command = lambda: event_entry(entry_box.get()))
    entry_btn.place(relx = 0.79, rely = 0.05, relwidth = 0.2, relheight = 0.9)

    bframe_ev = tk.Frame(label1, bg ="#ffffff")
    bframe_ev.place(relx = 0, rely = 0.505, relwidth = 1, relheight = 0.495)

    #Prints the entry from entry_box into the bottom box
    def event_entry(entry_box):
        label_bframe = tk.Label(bframe_ev, bg ="#FFFFFF", font = ("Helvetica",15), text = entry_box)
        label_bframe.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

#Creates the left frame
lframe = tk.Frame(root,bg = "#38312d",bd = 5)
lframe.place(relx = 0, rely = 0, relwidth = 0.1, relheight = 1)

#Home Button
btn1 = tk.Button(lframe, text = "Home", font = ("Helvetica", 18), bg = "#ffd480", command = click_home)
btn1.place(relx = 0.01, rely = 0.01, relwidth = 0.95, relheight = 0.15)

#Timetable Button
btn2 = tk.Button(lframe, text = "Timetable", font = ("Helvetica", 18), bg = "#ffd480", command = click_timetable)
btn2.place(relx = 0.01, rely= 0.18, relwidth = 0.95, relheight = 0.15)

#Links Button
btn3 = tk.Button(lframe, text = "Links", font = ("Helvetica", 18), bg = "#ffd480", command = click_linksbtn)
btn3.place(relx = 0.01, rely = 0.35, relwidth = 0.95, relheight = 0.15)

#Voice Assistant Button
btn4 = tk.Button(lframe, text = "Voice\n Assistant", font = ("Helvetica", 18), bg = "#ffd480", command = speech_recognition)
btn4.place(relx = 0.01, rely = 0.52, relwidth = 0.95, relheight = 0.15)

#Event Button
btn5 = tk.Button(lframe, text = "\n Plan An\n Event\n", font = ("Helvetica", 18), bg = "#ffd480", command = click_event)
btn5.place(relx = 0.01, rely = 0.69, relwidth = 0.95, relheight = 0.15)

#Right Frame
rframe = tk.Frame(root, bg = "#38312d", bd = 6)
rframe.place(relx = 0.15, rely = 0.1, relwidth = 0.8, relheight = 0.8)

#Label in right frame
label1 = tk.Label(rframe, bg ="#ffffff")
label1.place(relwidth = 1, relheight = 1)

root.mainloop()