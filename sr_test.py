#this program opens canvas when the user speaks open canvas
# this will not work uless you have speech recognition and its dependencys installed
# intalling speechRecognition proved chalenging since its not supported by python 3.7 but there is a way to do it
import speech_recognition as sr
import webbrowser
chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        if text == 'open canvas'or text=='open pandas':
            webbrowser.get(chromedir).open('https://ucc.instructure.com/')
            
    except:
        print("Sorry could not recognize what you said")

