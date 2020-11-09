# this is the intergration of the voice assistant with the gui

import tkinter as tk
import speech_recognition as sr
import webbrowser
root = tk.Tk()

r = sr.Recognizer() # speech recogniser

def speech_recognition():
    with sr.Microphone() as source:
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
            print("Sorry could not recognize what you said")

root.title("Welcome!")

#Sets the default window size
canvas = tk.Canvas(root, width = 1250, height = 700)
canvas.pack()

#Sets the background image
backgroung_image = tk.PhotoImage(file = "C:/Users/User/Documents/hackathon_progect/background1.png")
background_label = tk.Label(root, image = backgroung_image)
background_label.place(relwidth = 1, relheight = 1)

#Creates the left frame
lframe = tk.Frame(root, bg = "#38312d", bd = 5)
lframe.place(relx = 0, rely = 0, relwidth = 0.1, relheight = 1)

#Home Button
btn1 = tk.Button(lframe, text = "Home", font = ("Helvetica", 18), bg = "#ffd480")
btn1.place(relx = 0.01, rely = 0.01, relwidth = 0.95, relheight = 0.15)

#Timetable Button
btn2 = tk.Button(lframe, text = "Timetable", font = ("Helvetica", 18), bg =  "#ffd480")
btn2.place(relx = 0.01, rely= 0.18, relwidth = 0.95, relheight = 0.15)

#Links Button
btn3 = tk.Button(lframe, text = "Links", font = ("Helvetica", 18), bg = "#ffd480")
btn3.place(relx = 0.01, rely = 0.35, relwidth = 0.95, relheight = 0.15)

#Voice Assistant Button
btn4 = tk.Button(lframe, text = "Voice\n Assistant", font = ("Helvetica", 18), bg = "#ffd480", command=speech_recognition)
btn4.place(relx = 0, rely = 0.52, relwidth = 0.95, relheight = 0.15)

#Settings Button
btn5 = tk.Button(lframe, text = "Settings", font = ("Helvetica", 18), bg = "#ffd480")
btn5.place(relx = 0, rely = 0.69, relwidth = 0.95, relheight = 0.15)


root.mainloop()
