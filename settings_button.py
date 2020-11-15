
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

    #Left side of page
    label_settings1 = tk.Label(label1, bg = "#ffffff")
    label_settings1.place(relwidth = 0.495, relheight = 1)

    text_add_command = tk.Label(label_settings1,text = "Enter a command name of your choice:", font = ("Helvetica", 12))
    text_add_command.place(relx = 0.1, rely = 0.05)
    #add_voice_command('Patrick','https://en.wikipedia.org/wiki/The_Greatest_(Sia_song)')
    voiceCommandToAdd = tk.Entry(label_settings1, bg ="#ffffff")
    voiceCommandToAdd.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.15)

    text_add_link = tk.Label(label_settings1,text = "Enter a link:", font = ("Helvetica", 12))
    text_add_link.place(relx = 0.1, rely = 0.3)
    voiceLinkToAdd = tk.Entry(label_settings1,bg = "#ffffff")
    voiceLinkToAdd.place(relx = 0.1, rely = 0.35, relwidth = 0.8, relheight = 0.15)

    btnVoiceLinkAdd = tk.Button(label_settings1, text = "Create voice command", font = ("Helvetica", 12), bg = "#ffd480")
    btnVoiceLinkAdd.place(relx = 0.325, rely = 0.55, relwidth = 0.35, relheight = 0.1)

    settings_info = tk.Label(label_settings1, font = ("Helvetica", 11), text="The above is to add a custom voice command. The first input is the\n command you want, and the second one is the link you want to go\n to. You will be able to use this voice command when you press the\n 'Voice Assistant' button. ")
    settings_info.place(relx = 0.05, rely = 0.75, relwidth = 0.9)

    #Divider Line
    settings_line = tk.Label(label1, bg ="#38312d")
    settings_line.place(relx = 0.495, rely = 0, relwidth = 0.01, relheight = 1)
       
    def add_event(entry_time,entry_day,entry_name):
        name = '"'+name+'"'
        time = '"'+time+'"'
        execute = 'update timetables SET '+day+' = '+name+' where times = '+time
        c.execute(execute)
        conn.commit()
 
        button_timetable = tk.Button(label_settings2, bg = "#ffd480",font = ("Helvetica", 12), text = "Enter\n info\n to DB.", opmmand = add_event)
        button_timetable.place(relx = 0.8, rely = 0.1, relwidth = 0.15, relheight = 0.65)
 
    
    #Right side of page
    label_settings2 = tk.Label(label1, bg = "#ffffff")
    label_settings2.place(relx = 0.505,rely = 0, relwidth = 0.495, relheight = 1)

    time_text = tk.Label(label_settings2, font = ("Helvetica", 12), text = "Enter time:" )
    time_text.place(relx = 0.1, rely =0.05)
    entry_time = tk.Entry(label_settings2, bg ="#ffffff")
    entry_time.place(relx = 0.1, rely = 0.1, relwidth = 0.7, relheight = 0.15)
    
    day_text = tk.Label(label_settings2, font = ("Helvetica", 12), text = "Enter day:" )
    day_text.place(relx = 0.1, rely = 0.3)
    entry_day = tk.Entry(label_settings2, bg ="#ffffff")
    entry_day.place(relx = 0.1, rely = 0.35, relwidth = 0.7, relheight = 0.15)

    time_text = tk.Label(label_settings2, font = ("Helvetica", 12), text = "Enter module name:" )
    time_text.place(relx = 0.1, rely = 0.55)
    entry_name = tk.Entry(label_settings2, bg ="#ffffff")
    entry_name.place(relx = 0.1, rely = 0.6, relwidth = 0.7, relheight = 0.15)

    button_timetable = tk.Button(label_settings2, bg = "#ffd480",font = ("Helvetica", 12), text = "Enter\n info\n to DB.")
    button_timetable.place(relx = 0.8, rely = 0.1, relwidth = 0.15, relheight = 0.65)

    text_timetable = tk.Label(label_settings2, font = ("Helvetica", 12), text = "The above is to enter a time,day and name which will be\n added to the database and used to display your\n timetable, plan events etc." )
    text_timetable.place(relx = 0.1, rely = 0.8, relwidth = 0.8)
