import speech_recognition as sr
from tkinter import *
import pyttsx3
engine=pyttsx3.init()
voiceId="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voiceId)
engine. setProperty("rate", 135)
recognizer=sr.Recognizer()
mic=sr.Microphone(device_index=2)
root=Tk()
root.geometry("800x600")
root.title("0PyBot")
root.configure(bg='white')
def aboutBot():
    engine.say("I'm 0PyBot, here's some informations about me")
    engine.runAndWait()
    root=Tk()
    root.geometry("800x600")
    root.title("About 0PyBot")
    root.configure(bg='white')
    l=Label(root,text="About 0PyBot",font=("Helvetica",20,"bold"),bg='white')
    l.pack()
    root.mainloop()
def recognize():
    rc=Label(root,text="Recognizing ...",bg='White',fg='Black',font=("helvetica", 10,"italic"),border=0)
    rc.pack()
    with mic as source :
        recognizer.adjust_for_ambient_noise(source)
        request=recognizer.listen(source)
        return str(recognizer.recognize_google(request)).lower()
def rec():
    engine.say("Hi, how can I help you ?")
    engine.runAndWait()
    if recognize()=="hi":
        engine.say("Hi Yassine, how is it going ?")
        engine.runAndWait()
    elif recognize()=="exit":
        engine.say("Alright, see you soon !")
        engine.runAndWait()
        root.destroy()
menu=Label(root,text="Welcome to 0PyBot",font=("helvetica", 30,"bold"),bg='white',fg='black')
menu.pack(pady=20)
menu2=Label(root,text="Please choose an option from the menu below",font=("bold", 10),bg='white',fg='black')
menu2.pack(pady=10)
auth=Button(root,text="Recognize requests",width=20,height=4,border=0,font=("helvetica",10,"bold"),bg='black',fg='white',command=rec)
auth.pack(pady=20)
about=Button(root,text="Authenticate",width=20,height=4,border=0,font=("helvetica",10,"bold"),bg='black',fg='white')
about.pack(pady=20)
exit=Button(root,text="About the bot",width=20,height=4,border=0,font=("helvetica",10,"bold"),bg='black',fg='white',command=aboutBot)
exit.pack(pady=20)
root.mainloop()