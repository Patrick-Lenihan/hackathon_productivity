
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
        print_items1 += str(row) + "\n" 

    label_times = tk.Label(rframe, bg = "#ffffff", text = print_items1, font = ("Helvetica", 15))
    label_times.place(rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Monday Column
    c.execute('SELECT Monday FROM timetables')
    all_items2 = c.fetchmany(9)

    print_items2 = " "
    for row in all_items2:
        print_items2 += str(row) + "\n" 

    label_monday = tk.Label(rframe, bg = "#ffffff", text = print_items2, font = ("Helvetica", 15))
    label_monday.place(relx = (0.93/8)+0.01, rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Tuesday Column
    c.execute('SELECT Tuesday FROM timetables')
    all_items3 = c.fetchmany(9)

    print_items3 = " "
    for row in all_items3:
        print_items3 += str(row) + "\n" 

    label_tuesday = tk.Label(rframe, bg = "#ffffff", text = print_items3, font = ("Helvetica", 15))
    label_tuesday.place(relx = (((0.93/8)*2)+0.02),rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Wednesday Column
    c.execute('SELECT Wednesday FROM timetables')
    all_items4 = c.fetchmany(9)

    print_items4 = " "
    for row in all_items4:
        print_items4 += str(row) + "\n" 

    label_wednesday = tk.Label(rframe, bg = "#ffffff", text = print_items4, font = ("Helvetica", 15))
    label_wednesday.place(relx = (((0.93/8)*3)+0.03),rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Thursday Column
    c.execute('SELECT Thursday FROM timetables')
    all_items5 = c.fetchmany(9)

    print_items5 = " "
    for row in all_items5:
        print_items5 += str(row) + "\n" 

    label_thursday = tk.Label(rframe, bg = "#ffffff", text = print_items5, font = ("Helvetica", 15))
    label_thursday.place(relx = (((0.93/8)*4)+0.04),rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Friday Column
    c.execute('SELECT Friday FROM timetables')
    all_items6 = c.fetchmany(9)

    print_items6 = " "
    for row in all_items6:
        print_items6 += str(row) + "\n" 

    label_friday = tk.Label(rframe, bg = "#ffffff", text = print_items6, font = ("Helvetica", 15))
    label_friday.place(relx = (((0.93/8)*5)+0.05), rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Saturday Column
    c.execute('SELECT Saturday FROM timetables')
    all_items7 = c.fetchmany(9)

    print_items7 = " "
    for row in all_items7:
        print_items7 += str(row) + "\n" 

    label_saturday = tk.Label(rframe, bg = "#ffffff", text = print_items7, font = ("Helvetica", 15))
    label_saturday.place(relx = (((0.93/8)*6)+0.06), rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

    #Sunday Column
    c.execute('SELECT Sunday FROM timetables')
    all_items8 = c.fetchmany(9)

    print_items8 = " "
    for row in all_items8:
        print_items8 += str(row) + "\n" 

    label_sunday = tk.Label(rframe, bg = "#ffffff", text = print_items8, font = ("Helvetica", 15))
    label_sunday.place(relx = (((0.93/8)*7)+0.07),rely = 0.2, relwidth = 0.93/8, relheight = 0.8)

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
    