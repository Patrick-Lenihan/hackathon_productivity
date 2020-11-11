# patrick
import sqlite3
import tkinter as tk
import webbrowser
root = tk.Tk()

def go_to_programing():
    '''
    a function that opens the programing lab we will make a general function later but this will do for now
    '''
    webbrowser.open('https://teams.microsoft.com/l/meetup-join/19%3ameeting_N2U4MTk4ZDAtZjBmYi00MjU5LWJiNjAtMWRiYTg4ODhlYmJi%40thread.v2/0?context=%7b%22Tid%22%3a%2246fe5ca5-866f-4e42-92e9-ed8786245545%22%2c%22Oid%22%3a%2262b28634-96ed-4537-baea-4bd8ce87b3d3%22%7d', new=0, autoraise=True)
#Function that prints the results of an sqlite query to the screen of the gui when "timetable" is clicked.
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
    conn.commit()
    conn.close()

def linksDisplay():
    conn = sqlite3.connect('timetable.db')
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
    w = tk.OptionMenu(label1, dropdown, *menueList,command=getLinks)
    w.pack()
    w.place(relx = 0.30, rely = 0.01)

    # the add links part
    linkToAdd = tk.Entry(label1,width = 15 ,bg = "white")
    linkToAdd.place(relx = 0.50, rely = 0.01, relwidth = 0.20, relheight = 0.05)
    linkAdd = tk.Button(label1, text = "add link", font = ("Helvetica", 12), bg = "#ffd480",command = addLink)
    linkAdd.place(relx = 0.65, rely = 0.01, relwidth = 0.10, relheight = 0.05)
    

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
btn3 = tk.Button(lframe, text = "Links", font = ("Helvetica", 18), bg = "#ffd480",command = linksDisplay)
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
