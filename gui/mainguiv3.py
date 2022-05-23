import speech_recognition as sr
import threading
import tkinter as tk
import smtplib
import pyttsx3
import re
import calGUI
import Faceid

#constantes
DESCRIPTION_BOT = '''the julia bot is a bot made by a groupe of cyber-defense students, it has functionality to allow speech recognition
facial recognition and also a calendar , it can do alot of tasks'''

#check which button was clicked
RECOGNIZE_BUTTON = 1
AUTHENTICATE_BUTTON = 2

#to check if it's the first speech recognition of the bot  
first_time = True

#intanciate result to not give error if we want to give command first
result = 5

#python text to speech
engine=pyttsx3.init()
voiceId="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voiceId)
engine. setProperty("rate", 135)

#speech recognition
recognizer=sr.Recognizer()
mic=sr.Microphone()

#root window
root=tk.Tk()
root.geometry("800x600")
root.title("juliaBot")
root.configure(bg='white')

#the email sending function
def emailSending():
    #Creating the Gmail credentials widnow
    w3=tk.Toplevel(root)
    w3.resizable(0,0)
    w3.title("Password checking")
    w3.geometry('300x100')
    l3=tk.Label(w3,text="Gmail address :")
    l3.grid(row=0,column=0)
    gmail=tk.Entry(w3,width=30)
    gmail.grid(row=0,column=1)
    l4=tk.Label(w3,text="Gmail password :")
    l4.grid(row=1,column=0)
    passwd=tk.Entry(w3,show="*",width=30)
    passwd.grid(row=1,column=1)
    l5=tk.Label(w3,text="Confirm password :")
    l5.grid(row=2,column=0)
    passwd2=tk.Entry(w3,show="*",width=30)
    passwd2.grid(row=2,column=1)

    #comparing the passwords and sending the email
    def storePassword():
        #need a regex control for email validity !
        if passwd.get()==passwd2.get() and (len(str(passwd.get()))!=0 and len(str(passwd2.get()))!=0 and len(str(gmail.get()))!=0):
            mail=gmail.get()
            password=passwd.get()
            w3.destroy()
            w4=tk.Toplevel(root)
            w4.resizable(0,0)
            w4.title("Send the email")
            w4.geometry("800x400")
            l6=tk.Label(w4,text="The receiver email address :")
            l6.grid(row=0,column=0)
            eR=tk.Entry(w4,width=30)
            eR.grid(row=0,column=1)
            l7=tk.Label(w4,text="Your message : ")
            l7.grid(row=1,column=0)
            emailMessage=tk.Text(w4,width=30,height=4)
            emailMessage.grid(row=1,column=1)
            def send():
                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(mail,password)
                server.sendmail(mail,eR.get(),emailMessage.get("1.0","end-1c"))
            btn2=tk.Button(w4,text='Send',command=send)
            btn2.grid(row=2,column=1)
            w4.mainloop()
        if len(str(passwd.get()))==0 or len(str(passwd2.get()))==0 or len(str(gmail.get()))==0:
            engine.say("Be careful, a field is missing")
        else:
            engine.say("The passwords fields don't match")
    btnSend=tk.Button(w3,text="Confirm",command=storePassword,border=0)
    btnSend.grid(row=3,column=1)
    #engine.runAndWait()
    w3.mainloop()

#the aboutBot button function
def aboutBot():
    say("I'm Julia, here's some informations about me")
    root=tk.Tk()
    root.geometry("800x600")
    root.title("About julia Bot")
    root.configure(bg='white')
    title_label=tk.Label(root,text="About julia Bot",font=("Helvetica",20,"bold"),bg='white')
    title_label.pack()
    description = tk.StringVar()
    description_label = tk.Label(root, textvariable=description)
    description.set(DESCRIPTION_BOT)
    root.mainloop()

#the "recognizing" message shown while bot is recognizing the speech
def recEntry():
    rc.insert(0,"Recognizing ...")

#deleting the "recognizing" message when the bot has recognized the speech
def clearRecEntry():
    rc.delete(0,tk.END)

def start_thread(buttonClicked):
    if(buttonClicked == RECOGNIZE_BUTTON):#recognize speech button
        record_thread = threading.Thread(target=request_recognition)
        record_thread.daemon = True
        record_thread.start()
    else:#authenticate button
        record_thread = threading.Thread(target=request_recognition)
        record_thread.daemon = True
        record_thread.start()

def say(text):
    engine.say(text)
    engine.runAndWait()

def open_calendar():
    calGUI.calGUI()

#recognition function
def rec():
    with mic as source :
        #threading to keep the gui useful and in the same time printing the "recognition" message
        recognizer.adjust_for_ambient_noise(source)
        recEntry()
        request=recognizer.listen(source, phrase_time_limit = 3)

    #exception handling in case google couldn't translate speech
    try:
        recognize=str(recognizer.recognize_google(request)).lower()

    except:
        #implement an error message
        recognize = ""    
        
    clearRecEntry()
    #return the speech that was recognized
    return recognize

#function called if recognize requests button was clicked
def request_recognition():
    if(first_time):
        say("hi , i'm juila bot , how can i help you ?")
    else:
        say("what else can i do for you ?")
    #call rec to recognize speech
    recognize = rec()

    if recognize == "":
        say("i could not understand what you have said , please repeat yourself more clearly")    


    elif "hi bot" in recognize:
        say("Hi Yassine, how is it going ?")
            

    elif "close" in recognize:
        say("Alright, see you soon !")
        root.destroy()
        quit()
            

    elif "stop listening" in recognize:
        say("Okay, feel free to choose an option from the menu.")
            
        
    elif "who are you" in recognize:
        aboutBot_thread = threading.Thread(target=aboutBot)
        aboutBot_thread.daemon = True
        aboutBot_thread.start()

    elif "authenticate" in recognize:
        #authenticate command via speech
        authenticate_me()
    #separate if elif for commands that need authentication
    
    if "calendar" in recognize and result == 1:        
        say("opening calendar")
        open_calendar()

    elif "send email" in recognize and result == 1:
        say("Opening email window")
        email_thread = threading.Thread(target=emailSending)    
        email_thread.daemon = True
        email_thread.start()

    else:
        say("these actions need you to be authenticated first . you can authenticate by voice command or the button")        

#function called if the authenticate button was clicked
def authenticate_me():
    global result
    say("do you want to register , or are you already registered ?")
    #update value of recognize , listen to voice 
    recognize = rec()
    #if he wants to register , it will register him first then go to authenticating him
    username = getUsername()
    say("i'm going to take 4 pictures of you , please look straight at the camera")
    facialRecognition = Faceid.Faceid()
    if "register" in recognize:
        facialRecognition.register()
        #then proceed to authenticate the user 
        say("now i'm going to authenticate you to see if i'm able to recognize you")
    else:
        say("ok , i'm going to authenticate you now")
    #warn them that you will take 4 pictures so they look at the camera
    username = getUsername()
    say("i'm now going to take 1 picture of you , please look directly at the camera in a well lit area")
    result = facialRecognition.authenticate()
    if(result == 1):
        say(f"you have been successfully authenticated as {username}, you may now use the entirety of juila bot")
    elif(result == 2):
        say("the bot wasn't able to authenticate you because you haven't registered yet")
    else:
        say("the bot wasn't able to facially recognize you , please try again ")
    return result

#function to get username for registering and authenticating to add text version
def getUsername():
    say("could you please state only your username in a clear voice : ")
    return rec()


menu=tk.Label(root,text="Welcome to Julia !",font=("helvetica", 30,"bold"), bg='white', fg='black')
menu.pack(pady=20)
menu2=tk.Label(root,text="Please choose an option from the menu below",font=("bold", 10),bg='white',fg='black')
menu2.pack(pady=10)
rc=tk.Entry(root,bg='White',fg='Black',font=("helvetica", 10,"italic"),border=0)
rc.pack()
recognize_requests=tk.Button(root,text="Recognize requests",width=20,height=4,border=0,font=("helvetica",10,"bold"),bg='black',fg='white',command=lambda: start_thread(RECOGNIZE_BUTTON))
recognize_requests.pack(pady=20)
authenticate_button=tk.Button(root,text="Authenticate",width=20,height=4,border=0,font=("helvetica",10,"bold"),bg='black',fg='white', command=lambda: start_thread(AUTHENTICATE_BUTTON))
authenticate_button.pack(pady=20)
#exit=Button(root,text="About the bot",width=20,height=4,border=0,font=("helvetica",10,"bold"),bg='black',fg='white',command=aboutBot)
#exit.pack(pady=20)
root.mainloop()