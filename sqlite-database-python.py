import sqlite3


#Function that prints the results of an sqlite query to the screen of the gui when "timetable" is clicked.
#To use the database you have to us ctrl,shift,p to open the database so its connected to the python fuction
    
conn = sqlite3.connect('timetable.db')
c = conn.cursor()


def create_Table():
    c.execute('CREATE TABLE IF NOT EXISTS timetables(times VARCHAR(10), Monday VARCHAR(10), Tuesday VARCHAR(10), Wednesday VARCHAR(10), Thursday VARCHAR(10),Friday VARCHAR(10), Saturday VARCHAR(10))')

def data_Entry():
    c.execute("INSERT INTO timetables(times,Monday,Tuesday,Wednesday,Thursday, Friday, Saturday) VALUES ('9.00', 'CS1117','','CS1106','','',''),('10.00', '','','','','',''),('11.00', '','','','','CS1117',''),('12.00', '','CS1115','','','CS1112',''),('13.00', 'CS1115','CS1106','CS1111','','',''),('14.00', 'CS1117','CS1111','','CS1115','',''),('15.00', '','CS1117','CS1113','CS1111','',''),('16.00', '','CS1117','CS1106','','',''),('17.00', '','','','CS1115','','')")                                                                                                  
    conn.commit()
    c.close()
    conn.close()

for row in c.execute('SELECT * FROM timetables'): #input your sql in here  
        print(row)   
      
create_Table()  
data_Entry()  
