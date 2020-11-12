import sqlite3
import tkinter as tk
import webbrowser
import speech_recognition as sr
root = tk.Tk()

def setingsPage():
    conn = sqlite3.connect('timetable.db')
    c = conn.cursor()

    def add_voice_command():
        newCommand = voiceCommandToAdd.get()
        commandLink = voiceLinkToAdd.get()
        c.execute('CREATE TABLE IF NOT EXISTS voiceLinks(command VARCHAR(10),link VARCHAR(20))')
        l = [newCommand,commandLink]
        c.execute('INSERT INTO voiceLinks VALUES(?,?)',l)
        conn.commit()

    #add_voice_command('Patrick','https://en.wikipedia.org/wiki/The_Greatest_(Sia_song)')
    voiceCommandToAdd = tk.Entry(label1,width = 15 ,bg = "white")
    voiceCommandToAdd.place(relx = 0.01, rely = 0.01, relwidth = 0.20, relheight = 0.05)

    voiceLinkToAdd = tk.Entry(label1,width = 15 ,bg = "white",text="add a link")
    voiceLinkToAdd.place(relx = 0.30, rely = 0.01, relwidth = 0.20, relheight = 0.05)
    btnVoiceLinkAdd = tk.Button(label1, text = "add", font = ("Helvetica", 12), bg = "#ffd480",command = add_voice_command)
    btnVoiceLinkAdd.place(relx = 0.40, rely = 0.01, relwidth = 0.10, relheight = 0.05)   
#Function that prints the results of an sqlite query to the screen of the gui when "timetable" is clicked.
def openFromVoice():
        conn = sqlite3.connect('timetable.db')
        c = conn.cursor()
        r = sr.Recognizer()
        linkListForVoice = []
        linkCommandListForVoice = []
        for row in c.execute('select * from voiceLinks'):
            linkListForVoice.append(row[1])
            linkCommandListForVoice.append(row[0])
        print(linkListForVoice)    
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                if text in linkCommandListForVoice:
                    print('passed')
                    ind = linkCommandListForVoice.index(text)
                    webbrowser.open(linkListForVoice[ind], new=0, autoraise=True)
                    
            except:
                print("Sorry could not recognize what you said")
def clicked():
    conn = sqlite3.connect(r"C:\Users\User\Documents\databases_labs4\friends.sqlite")
    c = conn.cursor()

    c.execute('SELECT * FROM persons')
    all_items = c.fetchall()
    
    print_items = " "
    for row in all_items:
        print_items += str(row) + "\n"
        print(print_items)
    label1 = tk.Label(rframe, bg ="#FFFF00", text = print_items)
    label1.place(relwidth = 1, relheight = 1)
    #test buttons that prove the concept
    btna = tk.Button(label1, text = "intro to programing lecture", font = ("Helvetica", 8), bg = "#ffd480", command=go_to_programing)
    btna.place(relx = 0.01, rely = 0.01, relwidth = 0.12, relheight = 0.15)
    btnb = tk.Button(label1, text = "Home", font = ("Helvetica", 18), bg = "#ffd480")
    btnb.place(relx = 0.15, rely = 0.01, relwidth = 0.12, relheight = 0.15)
    btnc = tk.Button(label1, text = "Home", font = ("Helvetica", 18), bg = "#ffd480")
    btnc.place(relx = 0.29, rely = 0.01, relwidth = 0.12, relheight = 0.15)
    btnd = tk.Button(label1, text = "Home", font = ("Helvetica", 18), bg = "#ffd480")
    btnd.place(relx = 0.44, rely = 0.01, relwidth = 0.12, relheight = 0.15)
    btne = tk.Button(label1, text = "Home", font = ("Helvetica", 18), bg = "#ffd480")
    btne.place(relx = 0.59, rely = 0.01, relwidth = 0.12, relheight = 0.15)
    btnf = tk.Button(label1, text = "Home", font = ("Helvetica", 18), bg = "#ffd480")
    btnf.place(relx = 0.74, rely = 0.01, relwidth = 0.12, relheight = 0.15)

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
btn4 = tk.Button(lframe, text = "Voice\n Assistant", font = ("Helvetica", 18), bg = "#ffd480",command=openFromVoice)
btn4.place(relx = 0, rely = 0.52, relwidth = 0.95, relheight = 0.15)

#Settings Button
btn5 = tk.Button(lframe, text = "Settings", font = ("Helvetica", 18), bg = "#ffd480",command=setingsPage)
btn5.place(relx = 0, rely = 0.69, relwidth = 0.95, relheight = 0.15)

#Right Frame
rframe = tk.Frame(root, bg = "#38312d",bd = 5)
rframe.place(relx = 0.15, rely = 0.1, relwidth = 0.8, relheight = 0.8)

#Label in right frame
label1 = tk.Label(rframe, bg ="#ffffff")
label1.place(relwidth = 1, relheight = 1)


root.mainloop()
