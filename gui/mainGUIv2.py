import speech_recognition as sr
import threading
from tkinter import *
import smtplib
import pyttsx3
import re
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

#the email sending function
def emailSending():
    #Creating the Gmail credentials widnow
    w3=Toplevel(root)
    w3.resizable(0,0)
    w3.title("Password checking")
    w3.geometry('300x100')
    l3=Label(w3,text="Gmail address :")
    l3.grid(row=0,column=0)
    gmail=Entry(w3,width=30)
    gmail.grid(row=0,column=1)
    l4=Label(w3,text="Gmail password :")
    l4.grid(row=1,column=0)
    passwd=Entry(w3,show="*",width=30)
    passwd.grid(row=1,column=1)
    l5=Label(w3,text="Confirm password :")
    l5.grid(row=2,column=0)
    passwd2=Entry(w3,show="*",width=30)
    passwd2.grid(row=2,column=1)

    #comparing the passwords and sending the email
    def storePassword():
        #need a regex control for email validity !
        if passwd.get()==passwd2.get() and (len(str(passwd.get()))!=0 and len(str(passwd2.get()))!=0 and len(str(gmail.get()))!=0):
            mail=gmail.get()
            password=passwd.get()
            w3.destroy()
            w4=Toplevel(root)
            w4.resizable(0,0)
            w4.title("Send the email")
            w4.geometry("800x400")
            l6=Label(w4,text="The receiver email address :")
            l6.grid(row=0,column=0)
            eR=Entry(w4,width=30)
            eR.grid(row=0,column=1)
            l7=Label(w4,text="Your message : ")
            l7.grid(row=1,column=0)
            emailMessage=Text(w4,width=30,height=4)
            emailMessage.grid(row=1,column=1)
            def send():
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(mail,password)
                server.sendmail(mail,eR.get(),emailMessage.get("1.0","end-1c"))
            btn2=Button(w4,text='Send',command=send)
            btn2.grid(row=2,column=1)
            w4.mainloop()
        if len(str(passwd.get()))==0 or len(str(passwd2.get()))==0 or len(str(gmail.get()))==0:
            engine.say("Be careful, a field is missing")
        else:
            engine.say("The passwords fields don't match")
    btnSend=Button(w3,text="Confirm",command=storePassword,border=0)
    btnSend.grid(row=3,column=1)
    #engine.runAndWait()
    w3.mainloop()

#the aboutBot button function
def aboutBot():
    engine.say("I'm Julia, here's some informations about me")
    root=Tk()
    root.geometry("800x600")
    root.title("About 0PyBot")
    root.configure(bg='white')
    l=Label(root,text="About 0PyBot",font=("Helvetica",20,"bold"),bg='white')
    l.pack()
    root.mainloop()

#the "recognizing" message shown while bot is recognizing the speech
def recEntry():
    rc.insert(0,"Recognizing ...")

#deleting the "recognizing" message when the bot has recognized the speech
def clearRecEntry():
    rc.delete(0,END)

#recognition function
def rec():
    engine.say("Hi, how can I help you ?")
    engine.runAndWait()
    while TRUE:
        with mic as source :
            #threading to keep the gui useful and in the same time printing the "recognition" message
            threading.Thread(target=recEntry).start()
            recognizer.adjust_for_ambient_noise(source)
            request=recognizer.listen(source)
            recognize=str(recognizer.recognize_google(request)).lower()

        if recognize=="hi julia":
            #threading to keep the gui useful and in the same time printing the "recognition" message
            threading.Thread(target=clearRecEntry).start()
            engine.say("Hi Yassine, how is it going ?")

        elif recognize=="close":
            threading.Thread(target=clearRecEntry).start()
            engine.say("Alright, see you soon !")
            root.destroy()

        elif recognize=="stop listening":
            threading.Thread(target=clearRecEntry).start()
            engine.say("Okay, feel free to choose an option from the menu.")
            engine.runAndWait()
            break

        elif recognize=="send an email":
            threading.Thread(target=clearRecEntry).start()
            engine.say("Opening email sending window right now")
            threading.Thread(target=emailSending).start()
        

        elif recognize=="who are you":
            threading.Thread(target=clearRecEntry).start()
            threading.Thread(target=aboutBot).start()
        engine.runAndWait()
            

#threading to keep the gui useful when the rec function is being executed        
threading.Thread(target=rec).start()
menu=Label(root,text="Welcome to Julia !",font=("helvetica", 30,"bold"),bg='white',fg='black')
menu.pack(pady=20)
menu2=Label(root,text="Please choose an option from the menu below",font=("bold", 10),bg='white',fg='black')
menu2.pack(pady=10)
rc=Entry(root,bg='White',fg='Black',font=("helvetica", 10,"italic"),border=0)
rc.pack()
auth=Button(root,text="Recognize requests",width=20,height=4,border=0,font=("helvetica",10,"bold"),bg='black',fg='white',command=rec)
auth.pack(pady=20)
about=Button(root,text="Authenticate",width=20,height=4,border=0,font=("helvetica",10,"bold"),bg='black',fg='white')
about.pack(pady=20)
#exit=Button(root,text="About the bot",width=20,height=4,border=0,font=("helvetica",10,"bold"),bg='black',fg='white',command=aboutBot)
#exit.pack(pady=20)
root.mainloop()