#Basically combining all the code so far


#So in this code, I've used the database that Eoin created and basically displayed it nicely to the screen
#I used 6 different sql queries to do this. One for each column. e.g. "SELECT Monday FROM timetables" for the monday column, "SELECT Tuesday FROM timetables" for the Tuesday column etc.
#Unfortunately, the results of the queries are displated in between ('  ')and with commas. I'm not sure if there's anything we can do about that
#For the headings of the columns, I just hardcoded them in since I don't think we can create a query to fetch those names
#To see what all this looks like just cclick the "timetable" button


'''import speech_recognition as sr
import webbrowser
r = sr.Recognizer()'''

import sqlite3
import tkinter as tk
import webbrowser
root = tk.Tk()


def go_to_programing():
    '''
    a function that opens the programing lab we will make a general function later but this will do for now
    '''
    webbrowser.open("https://teams.microsoft.com/l/meetup-join/19%3ameeting_N2U4MTk4ZDAtZjBmYi00MjU5LWJiNjAtMWRiYTg4ODhlYmJi%40thread.v2/0?context=%7b%22Tid%22%3a%2246fe5ca5-866f-4e42-92e9-ed8786245545%22%2c%22Oid%22%3a%2262b28634-96ed-4537-baea-4bd8ce87b3d3%22%7d", new=0, autoraise=True)

#Database
conn = sqlite3.connect('timetable.db')
c = conn.cursor()
def create_Table():
    c.execute('CREATE TABLE IF NOT EXISTS timetables(times VARCHAR(10), Monday VARCHAR(10), Tuesday VARCHAR(10), Wednesday VARCHAR(10), Thursday VARCHAR(10),Friday VARCHAR(10), Saturday VARCHAR(10))')
def data_Entry():
    c.execute("INSERT INTO timetables(times,Monday,Tuesday,Wednesday,Thursday, Friday, Saturday) VALUES ('9.00', 'CS1117','','CS1106','','',''),('10.00', '','','','','',''),('11.00', '','','','','CS1117',''),('12.00', '','CS1115','','','CS1112',''),('13.00', 'CS1115','CS1106','CS1111','','',''),('14.00', 'CS1117','CS1111','','CS1115','',''),('15.00', '','CS1117','CS1112','CS1111','',''),('16.00', '','CS1117','CS1106','','',''),('17.00', '','','','CS1115','','')")                                                                                                  
create_Table()  
data_Entry() 
conn.commit()
conn.close()



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

#Function for when the timetable button is clicked
def click_timetable():
    conn = sqlite3.connect("timetable.db")
    c = conn.cursor()

    label_bottom_main = tk.Label(rframe, bg ="#38312d")
    label_bottom_main.place(relwidth = 1, relheight = 1)

    #Times Column
    c.execute('SELECT times FROM timetables')
    all_items1 = c.fetchmany(9)

    print_items1 = " "
    for row in all_items1:
        print_items1 += str(row) + "\n\n" 

    label_times = tk.Label(rframe, bg = "#ffffff", text = print_items1, font = ("Helvetica", 15))
    label_times.place(rely = 0.2, relwidth = 0.95/6, relheight = 0.8)

    #Monday Column
    c.execute('SELECT Monday FROM timetables')
    all_items2 = c.fetchmany(9)

    print_items2 = " "
    for row in all_items2:
        print_items2 += str(row) + "\n\n" 

    label_monday = tk.Label(rframe, bg = "#ffffff", text = print_items2, font = ("Helvetica", 15))
    label_monday.place(relx = ((0.95/6)+0.01),rely = 0.2, relwidth = 0.95/6, relheight = 0.8)

    #Tuesday Column
    c.execute('SELECT Tuesday FROM timetables')
    all_items3 = c.fetchmany(9)

    print_items3 = " "
    for row in all_items3:
        print_items3 += str(row) + "\n\n" 

    label_monday = tk.Label(rframe, bg = "#ffffff", text = print_items3, font = ("Helvetica", 15))
    label_monday.place(relx = (((0.95/6)*2)+0.02),rely = 0.2, relwidth = 0.95/6, relheight = 0.8)

    #Wednesday Column
    c.execute('SELECT Wednesday FROM timetables')
    all_items4 = c.fetchmany(9)

    print_items4 = " "
    for row in all_items4:
        print_items4 += str(row) + "\n\n" 

    label_monday = tk.Label(rframe, bg = "#ffffff", text = print_items4, font = ("Helvetica", 15))
    label_monday.place(relx = (((0.95/6)*3)+0.03),rely = 0.2, relwidth = 0.95/6, relheight = 0.8)

    #Thursday Column
    c.execute('SELECT Thursday FROM timetables')
    all_items5 = c.fetchmany(9)

    print_items5 = " "
    for row in all_items5:
        print_items5 += str(row) + "\n\n" 

    label_monday = tk.Label(rframe, bg = "#ffffff", text = print_items5, font = ("Helvetica", 15))
    label_monday.place(relx = (((0.95/6)*4)+0.04),rely = 0.2, relwidth = 0.95/6, relheight = 0.8)

    #Friday Column
    c.execute('SELECT Friday FROM timetables')
    all_items6 = c.fetchmany(9)

    print_items6 = " "
    for row in all_items6:
        print_items6 += str(row) + "\n\n" 

    label_monday = tk.Label(rframe, bg = "#ffffff", text = print_items6, font = ("Helvetica", 15))
    label_monday.place(relx = (((0.95/6)*5)+0.05),rely = 0.2, relwidth = 0.95/6, relheight = 0.8)

    conn.commit()
    conn.close()

    #Top Row
    label_top = tk.Label(rframe, bg ="#ffffff")
    label_top.place(relx = 0 , rely = 0, relwidth = 1, relheight = 0.18)

    #Top Frame
    label_top_main = tk.Label(rframe, bg ="#38312d")
    label_top_main.place(relwidth = 1, relheight = 0.18)

    #"Times" Box 
    label_top1 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Times")
    label_top1.place(relx = 0, rely = 0, relwidth = 0.95/6, relheight = 0.18)

    #"Monday" Box 
    label_top2 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Monday")
    label_top2.place(relx = ((0.95/6)+0.01), rely = 0, relwidth = 0.95/6, relheight = 0.18 )

    #"Tuesday" Box 
    label_top3 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Tuesday")
    label_top3.place(relx = (((0.95/6)*2)+0.02), rely = 0, relwidth = 0.95/6, relheight = 0.18 )

    #"Wednesday" Box 
    label_top4 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Wednesday")
    label_top4.place(relx = (((0.95/6)*3)+0.03), rely = 0, relwidth = 0.95/6, relheight = 0.18 )

    #"Thursday" Box 
    label_top5 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Thursday")
    label_top5.place(relx = (((0.95/6)*4)+0.04), rely = 0, relwidth = 0.95/6, relheight = 0.18 )

    #"Friday" Box 
    label_top6 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Friday")
    label_top6.place(relx = (((0.95/6)*5)+0.05), rely = 0, relwidth = 0.95/6, relheight = 0.18 )

    
#Funtion for when the links button is clicked
def linksDisplay():
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    #c.execute('DROP TABLE subjects')

    c.execute('CREATE TABLE IF NOT EXISTS subjects(subject VARCHAR(10), forKey VARCHAR(10))')
    c.execute('CREATE TABLE IF NOT EXISTS notestable(key VARCHAR(10), link VARCHAR(10))')
    def addSubject():
        subjectName = subjectToAdd.get()
        listToInsert = [subjectName,subjectName.replace(" ","_")]
        #listToInsert2 = [subjectName.replace(" ","_"),"lol"]
        c.execute('INSERT INTO subjects VALUES(?,?)',listToInsert)
        #c.execute('INSERT INTO notestable VALUES(?,?)',listToInsert2)
        conn.commit()
    #
    def addLink():
        subjectName = dropdown.get()
        link = linkToAdd.get()
        listToInsert2 = [subjectName.replace(" ","_"),link]
        c.execute('INSERT INTO notestable VALUES(?,?)',listToInsert2)
        conn.commit()

    def getLinks(subjectName):
        subjectName = subjectName.replace(" ","_")
        out = []
        for row in c.execute('select link from notestable WHERE key=(?)',(subjectName,)):
            out.append(row[0])
        provOut = tk.Label(rframe, text = out)
        provOut.place(relx = 0.50, rely = 0.50,relwidth = 0.10, relheight = 0.10)
        return out
    def getSubjects():
        out = []
        for row in c.execute('select subject from subjects'):
            out.append(row[0])
        return out

    subjectToAdd = tk.Entry(label1,width = 15 ,bg = "white")
    subjectToAdd.place(relx = 0.01, rely = 0.01, relwidth = 0.20, relheight = 0.05)
    btnAdd = tk.Button(label1, text = "add subject", font = ("Helvetica", 12), bg = "#ffd480",command = addSubject)
    btnAdd.place(relx = 0.15, rely = 0.01, relwidth = 0.10, relheight = 0.05)

    menueList = getSubjects()
    dropdown = tk.StringVar(root)
    dropdown.set(menueList[0])
    w = tk.OptionMenu(label1, dropdown, menueList,command=getLinks)
    w.pack()
    w.place(relx = 0.30, rely = 0.01)

    # the add links part
    linkToAdd = tk.Entry(label1,width = 15 ,bg = "white")
    linkToAdd.place(relx = 0.50, rely = 0.01, relwidth = 0.20, relheight = 0.05)
    linkAdd = tk.Button(label1, text = "add link", font = ("Helvetica", 12), bg = "#ffd480",command = addLink)
    linkAdd.place(relx = 0.65, rely = 0.01, relwidth = 0.10, relheight = 0.05)

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
btn3 = tk.Button(lframe, text = "Links", font = ("Helvetica", 18), bg = "#ffd480", command = linksDisplay)
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
