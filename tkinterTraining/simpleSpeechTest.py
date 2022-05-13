from tkinter import *
import pyttsx3
import speech_recognition as sr
import webbrowser
engine=pyttsx3.init()
#Initializing the recognizer class
recognizer=sr.Recognizer()
recognizer.phrase_threshold = 0.5
mic=sr.Microphone(device_index=2)
#print(sr.Microphone.list_microphone_names())
#Reading Microphone as a source
#Linstening the speech and storing it into a variable
root=Tk()
root.geometry('800x600')
def speak():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        at=recognizer.listen(source)
        if str(recognizer.recognize_google(at,language="fr-FR")).lower()=='quelle heure est-il':
            engine.say('presque minuit Yassine, temps pour aller dormir')
        elif str(recognizer.recognize_google(at,language="fr-FR")).lower()=='bonsoir':
            engine.say('Veuiller vous authentifier premièrement pour que je vous reconnaisse')
        elif str(recognizer.recognize_google(at,language="fr-FR")).lower()=='Alexa':
            engine.say('Comment je peux vous aider ?')
        else:
            engine.say('Désolé je vous ai pas bien compris')
    engine.runAndWait()
            

b=Button(root,text='Text to speech',command=speak)
b.pack()
root.mainloop()