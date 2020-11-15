import sqlite3
import tkinter as tk
import speech_recognition as sr
import webbrowser
r = sr.Recognizer()
conn = sqlite3.connect('timetable.db')
c = conn.cursor()
root = tk.Tk()
canvas = tk.Canvas(root, width = 1250, height = 700)
canvas.pack()

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
        provOut = tk.Button(links_label, text = out)
        provOut.place(relx = 0.1, rely = 0.7,relwidth = 0.8, relheight = 0.20)
        return out
    def getSubjects():
        out = []
        for row in c.execute('select subject from subjects'):
            out.append(row[0])
        return out

    #Temporary root
    links_label = tk.Label(rframe, bg ="#ffffff")
    links_label.place(relwidth = 1, relheight = 1)
    
    #Divider Line
    label_line = tk.Label(links_label, bg = "#38312d")
    label_line.place(relx = 0, rely = 0.5, relheight = 0.01, relwidth = 1)

    #text
    text3_frame = tk.Frame(links_label, bg ="#dddddd")
    text3_frame.place(relx = 0.01, rely = 0.05, relheight = 0.4, relwidth = 0.4)
    label_text3 = tk.Label(text3_frame, font = ("Helvetica", 12), text = "Enter one of your module names and\n the link which will take you to this subject's\n Teams/Zoom/Hangouts meeting.\n This information will be saved so you can access it later.")
    label_text3.place( relwidth = 1, relheight = 1)

    #Add Subject 
    subjectToAdd = tk.Entry(links_label, bg = "white")
    subjectToAdd.place(relx = 0.45, rely = 0.1, relwidth = 0.4, relheight = 0.1)
    btnAdd = tk.Button(links_label, text = "add subject", font = ("Helvetica", 12),  bg = "#ffd480",command = addSubject)
    btnAdd.place(relx = 0.85, rely = 0.1, relwidth = 0.10, relheight = 0.1)
    #Add links
    linkToAdd = tk.Entry(links_label,width = 15 ,bg = "white")
    linkToAdd.place(relx = 0.45, rely = 0.25, relwidth = 0.4, relheight = 0.1)
    linkAdd = tk.Button(links_label, text = "add link", font = ("Helvetica", 12), bg = "#ffd480",command = addLink)
    linkAdd.place(relx = 0.85, rely = 0.25, relwidth = 0.10, relheight = 0.1)

    #Dropdown Menu
    menueList = getSubjects()
    dropdown = tk.StringVar(root)
    dropdown.set(menueList[0])
    w = tk.OptionMenu(links_label, dropdown, *menueList,command=getLinks)
    w.pack()
    w.place(relx = 0.05, rely = 0.7, relwidth = 0.4, relheight = 0.15)
    label_text2 = tk.Label(links_label,bg ="#ffffff",text = "Choose a link:",font = ("Helvetica", 14))
    label_text2.place(relx = 0.05, rely = 0.6, relwidth = 0.35, relheight = 0.1)

    #Button to go to link
    label_text1 = tk.Label(links_label,bg ="#ffffff",text = "Press this button to go to your chosen link:",  font = ("Helvetica", 14),)
    label_text1.place(relx = 0.5, rely = 0.6, relwidth = 0.45, relheight = 0.1)
    provOut = tk.Button(links_label)
    provOut.place(relx = 0.5, rely = 0.7,relwidth = 0.45, relheight = 0.15)


def sched_matching():
    def dec_to_patnum(num):
      num = int(str(num),2)
      out = ''
      symbols = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','£','$','%','^','&','*','(',')','_','+','-','=','@','#','?']
      for i in range(26,-1,-1):
        ans = num//(78**i)
        if ans < 78:
          out += symbols[ans]
          num = num%(78**i)
        else:
          out+= '?'
          num = num - ((78**i)*78)
      #print('output',bin(patnum_to_dec(out)))
      return out

    def patnum_to_dec(num):
      symbols = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,'i':18,'j':19,'k':20,'l':21,'m':22,'n':23,'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,'v':31,'w':32,'x':33,'y':34,'z':35,'A':36,'B':37,'C':38,'D':39,'E':40,'F':41,'G':42,'H':43,'I':44,'J':45,'K':46,'L':47,'M':48,'N':49,'O':50,'P':51,'Q':52,'R':53,'S':54,'T':55,'U':56,'V':57,'W':58,'X':59,'Y':60,'Z':61,'!':62,'£':63,'$':64,'%':65,'^':66,'&':67,'*':68,'(':69,')':70,'_':71,'+':72,'-':73,'=':74,'@':75,'#':76,'?':77}
      num = num[::-1]
      out = 0
      for i in range(0,len(num)):
        out+= (78**i)*symbols[num[i]]
      return out
     
    def binary_matching(group):
        """
        takes list of biary strings as an input  
        """
        output = []
        i = 0
        match = True
        while not i==164:
          match = True
          for elem in group:
            #print(len(elem))
            if elem[i] == '1':
              match = False
          if match == True:
            output.append(i)
            match = True
          i+=1
        return output

    def binaryMatchingInput():
        inputList = codesEntryBox.get()
        inputList=inputList.split(' ')
        #print('input List:',inputList)
        inputList[:] = [patnum_to_dec(elem) for elem in inputList]
        inputList[:] = [bin(elem)[2:].zfill(168) for elem in inputList]
        #inputList[:] = [elem.replace("0b","") for elem in inputList]
        print(inputList)
        timesFreeList = binary_matching(inputList)
        outputToTK = []
        for elem in timesFreeList:
            day = elem//24
            hour = elem%24
            if day == 0:
                outputToTK.append("monday")
            elif day == 1:
                outputToTK.append("tuesday")
            elif day == 2:
                outputToTK.append("wensday")
            elif day == 3:
                outputToTK.append("thursday")
            elif day ==4:
                outputToTK.append('friday')
            elif day == 5:
                outputToTK.append("saterday")
            elif day == 6:
                outputToTK.append("sunday")
            outputToTK.append(hour)
        print(outputToTK)
        label1 = tk.Label(rframe, bg ="#ffd480", text = outputToTK)
        label1.place(relwidth = 0.50, relheight = 0.50, relx = 0.50, rely = 0.50)    

    def generate_code():
        schedual = [[],[],[],[],[],[],[]]
        for row in c.execute('select * from timetables'):
            for i in range(1,8):
                schedual[i-1].append(row[i])
        for item in range(7):
            for time in range(24):
                if schedual[item][time] == '':schedual[item][time]= '0'
                else: schedual[item][time] ='1'
        schedual = sum(schedual, [])
        schedual = ''.join(schedual)
        print('schedul:',schedual)
        #print(len(schedual))
        code = dec_to_patnum(schedual)
        print('code',code)
        
        label2 = tk.Label(label1, bg ="#ffd480", text = code)
        label2.place(relwidth = 0.50, relheight = 0.10, relx = 0.30, rely = 0.10)   

    codesEntryButton = tk.Button(label1,text = "generate code", font = ("Helvetica", 12), bg = "#ffd480",command = generate_code)
    codesEntryButton.place(relx = 0.10, rely = 0.10, relwidth = 0.15, relheight = 0.15)

    codesEntryBox = tk.Entry(label1,width = 15 ,bg = "white")
    codesEntryBox.place(relx = 0.10, rely = 0.50, relwidth = 0.30, relheight = 0.30)

    codesEntryButton = tk.Button(label1,text = "add subject", font = ("Helvetica", 12), bg = "#ffd480",command = binaryMatchingInput)
    codesEntryButton.place(relx = 0.40, rely = 0.50, relwidth = 0.15, relheight = 0.15)

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

    w = tk.Label(label1, text="the above is to add a custom voice command. the first input is the command you want and the second one is the link you want to go to")
    w.place(relx = 0.10, rely = 0.15)


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

#Function for when the timetable button is clicked
def click_timetable():
    conn = sqlite3.connect("timetable.db")
    c = conn.cursor()

    label_bottom_main = tk.Label(rframe, bg ="#38312d")
    label_bottom_main.place(relwidth = 1, relheight = 1)

    #Times Column
    c.execute('SELECT times FROM timetables')
    all_items1 = c.fetchmany(23)

    print_items1 = " "
    for row in all_items1:
        print_items1 += str(row[0]) + "\n" 

    label_times = tk.Label(rframe, bg = "#ffffff", text = print_items1, font = ("Helvetica", 12))
    label_times.place(rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Monday Column
    c.execute('SELECT Monday FROM timetables')
    all_items2 = c.fetchmany(23)

    print_items2 = " "
    for row in all_items2:
        print_items2 += str(row[0]) + "\n" 

    label_monday = tk.Label(rframe, bg = "#ffffff", text = print_items2, font = ("Helvetica", 12))
    label_monday.place(relx = (0.93/8)+0.01, rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Tuesday Column
    c.execute('SELECT Tuesday FROM timetables')
    all_items3 = c.fetchmany(23)

    print_items3 = " "
    for row in all_items3:
        print_items3 += str(row[0]) + "\n" 

    label_tuesday = tk.Label(rframe, bg = "#ffffff", text = print_items3, font = ("Helvetica", 12))
    label_tuesday.place(relx = (((0.93/8)*2)+0.02),rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Wednesday Column
    c.execute('SELECT Wednesday FROM timetables')
    all_items4 = c.fetchmany(23)

    print_items4 = " "
    for row in all_items4:
        print_items4 += str(row[0]) + "\n" 

    label_wednesday = tk.Label(rframe, bg = "#ffffff", text = print_items4, font = ("Helvetica", 12))
    label_wednesday.place(relx = (((0.93/8)*3)+0.03),rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Thursday Column
    c.execute('SELECT Thursday FROM timetables')
    all_items5 = c.fetchmany(23)

    print_items5 = " "
    for row in all_items5:
        print_items5 += str(row[0]) + "\n" 

    label_thursday = tk.Label(rframe, bg = "#ffffff", text = print_items5, font = ("Helvetica", 12))
    label_thursday.place(relx = (((0.93/8)*4)+0.04),rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Friday Column
    c.execute('SELECT Friday FROM timetables')
    all_items6 = c.fetchmany(23)

    print_items6 = " "
    for row in all_items6:
        print_items6 += str(row[0]) + "\n" 

    label_friday = tk.Label(rframe, bg = "#ffffff", text = print_items6, font = ("Helvetica", 12))
    label_friday.place(relx = (((0.93/8)*5)+0.05), rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Saturday Column
    c.execute('SELECT Saturday FROM timetables')
    all_items7 = c.fetchmany(23)

    print_items7 = " "
    for row in all_items7:
        print_items7 += str(row[0]) + "\n" 

    label_saturday = tk.Label(rframe, bg = "#ffffff", text = print_items7, font = ("Helvetica", 12))
    label_saturday.place(relx = (((0.93/8)*6)+0.06), rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Sunday Column
    c.execute('SELECT Sunday FROM timetables')
    all_items8 = c.fetchmany(23)

    print_items8 = " "
    for row in all_items8:
        print_items8 += str(row[0]) + "\n" 

    label_sunday = tk.Label(rframe, bg = "#ffffff", text = print_items8, font = ("Helvetica", 12))
    label_sunday.place(relx = (((0.93/8)*7)+0.07),rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    conn.commit()
    conn.close()

    #Top Row
    label_top = tk.Label(rframe, bg ="#ffffff")
    label_top.place(relx = 0 , rely = 0, relwidth = 1, relheight = 0.15)

    #Top Frame
    label_top_main = tk.Label(rframe, bg ="#38312d")
    label_top_main.place(relwidth = 1, relheight = 0.18)

    #"Times" Box 
    label_top1 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Times")
    label_top1.place(relx = 0, rely = 0, relwidth = 0.93/8, relheight = 0.18)

    #"Monday" Box 
    label_top2 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Monday")
    label_top2.place(relx = ((0.93/8)+0.01), rely = 0, relwidth = 0.93/8, relheight = 0.18 )

    #"Tuesday" Box 
    label_top3 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Tuesday")
    label_top3.place(relx = (((0.93/8)*2)+0.02), rely = 0, relwidth = 0.93/8, relheight = 0.18 )

    #"Wednesday" Box 
    label_top4 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Wednesday")
    label_top4.place(relx = (((0.93/8)*3)+0.03), rely = 0, relwidth = 0.93/8, relheight = 0.18 )

    #"Thursday" Box 
    label_top5 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Thursday")
    label_top5.place(relx = (((0.93/8)*4)+0.04), rely = 0, relwidth = 0.93/8, relheight = 0.18 )

    #"Friday" Box 
    label_top6 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Friday")
    label_top6.place(relx = (((0.93/8)*5)+0.05), rely = 0, relwidth = 0.93/8, relheight = 0.18 )

    #"Saturday" Box 
    label_top7 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Saturday")
    label_top7.place(relx = (((0.93/8)*6)+0.06), rely = 0, relwidth = 0.93/8, relheight = 0.18 )

    #"Sunday" Box 
    label_top7 = tk.Label(rframe, bg = "#ffffff",  font = ("Helvetica", 15), text = "Sunday")
    label_top7.place(relx = (((0.93/8)*7)+0.07), rely = 0, relwidth = 0.93/8, relheight = 0.18 )

#Sets the background image
backgroung_image = tk.PhotoImage(file = "C:/Users/User/Documents/hackathon_progect/background1.png")
background_label = tk.Label(root, image = backgroung_image)
background_label.place(relwidth = 1, relheight = 1)

#Creates the left frame
lframe = tk.Frame(root, bg = "#38312d", bd = 5)
lframe.place(relx = 0, rely = 0, relwidth = 0.1, relheight = 1)

#Right Frame
rframe = tk.Frame(root, bg = "#38312d", bd = 6)
rframe.place(relx = 0.15, rely = 0.1, relwidth = 0.8, relheight = 0.8)

#Label in right frame
label1 = tk.Label(rframe, bg ="#ffffff")
label1.place(relwidth = 1, relheight = 1)


#Home Button
btn1 = tk.Button(lframe, text = "Home", font = ("Helvetica", 18), bg = "#ffd480")
btn1.place(relx = 0.01, rely = 0.01, relwidth = 0.95, relheight = 0.15)

#Timetable Button
btn2 = tk.Button(lframe, text = "Timetable", font = ("Helvetica", 18), bg =  "#ffd480", command=click_timetable)
btn2.place(relx = 0.01, rely= 0.18, relwidth = 0.95, relheight = 0.15)

#Links Button
btn3 = tk.Button(lframe, text = "Links", font = ("Helvetica", 18), bg = "#ffd480",command=linksDisplay)
btn3.place(relx = 0.01, rely = 0.35, relwidth = 0.95, relheight = 0.15)

#Voice Assistant Button
btn4 = tk.Button(lframe, text = "Voice\n Assistant", font = ("Helvetica", 18), bg = "#ffd480", command = openFromVoice)
btn4.place(relx = 0.01, rely = 0.52, relwidth = 0.95, relheight = 0.15)

#Settings Button
btn5 = tk.Button(lframe, text = "Settings", font = ("Helvetica", 18), bg = "#ffd480",command=setingsPage)
btn5.place(relx = 0.01, rely = 0.69, relwidth = 0.95, relheight = 0.15)

btn6 = tk.Button(lframe, text = "plan an event", font = ("Helvetica", 10), bg = "#ffd480",command=sched_matching)
btn6.place(relx = 0.01, rely = 0.82, relwidth = 0.95, relheight = 0.15)



root.mainloop()