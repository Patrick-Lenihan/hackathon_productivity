# patrick
# this program compresses the information about the timetable into a code and then decompresses it
# this will be used for the finding a time where multable people are free
# needs more optimisation
# edit made for optimisateion now takes binary as entry 
# edit made to impliment binary matching algoritham to find the times where everybody is free 
import tkinter as tk
import sqlite3
    
conn = sqlite3.connect('timetable.db')
c = conn.cursor()
root = tk.Tk()
canvas = tk.Canvas(root, width = 1250, height = 700)
canvas.pack()

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
  
    label1 = tk.Label(root, bg ="#FFFF00", text = outputToTK)
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
    
    label2 = tk.Label(root, bg ="#FFFF00", text = code)
    label2.place(relwidth = 0.50, relheight = 0.10, relx = 0.50, rely = 0.50)   

codesEntryButton = tk.Button(text = "generate code", font = ("Helvetica", 12), bg = "#ffd480",command = generate_code)
codesEntryButton.place(relx = 0.30, rely = 0.10, relwidth = 0.15, relheight = 0.15)

codesEntryBox = tk.Entry(root,width = 15 ,bg = "white")
codesEntryBox.place(relx = 0.10, rely = 0.50, relwidth = 0.30, relheight = 0.30)

codesEntryButton = tk.Button(text = "add subject", font = ("Helvetica", 12), bg = "#ffd480",command = binaryMatchingInput)
codesEntryButton.place(relx = 0.30, rely = 0.50, relwidth = 0.15, relheight = 0.15)

'''ann = dec_to_patnum(111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)

print(ann)
print('\n')
print(patnum_to_dec(ann))'''
