from tkinter import*
import smtplib
from tkinter import messagebox
import speech_recognition as sr
root=Tk()
root.geometry('800x600')
rec=sr.Recognizer()
#The mail sending function
def credentialsWindow():
    messagebox.showinfo("Password","You need to give your Gmail password so I can connect to your gmail account and send the email.\n Don't worry, the transmission is over TLS.")
    #Creating the Gmail credentials widnow
    w3=Toplevel()
    w3.title("Password checking")
    w3.geometry('300x100')
    l3=Label(w3,text="Your Gmail password :")
    l3.grid(row=0,column=0)
    passwd=Entry(w3,show="*",width=20)
    passwd.grid(row=0,column=1)
    l4=Label(w3,text="Confirm password :")
    l4.grid(row=1,column=0)
    passwd2=Entry(w3,show="*",width=20)
    passwd2.grid(row=1,column=1)
    #comparing the passwords and sending the email
    def storePassword():
        if passwd.get()==passwd2.get() and (len(str(passwd.get()))!=0 or len(str(passwd2.get()))!=0):
            password=passwd.get()
            #write the password into a file, so we can pull it and use it to connect to gmail
            #We need to encrypt the password and write the cipher in the file not the password in plaintext(for later)
            w3.destroy()
            w4=Toplevel(root)
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
                server.login("botpython261@gmail.com",password)
                server.sendmail("botpython261@gmail.com",eR.get(),emailMessage.get("1.0","end-1c"))
            btn2=Button(w4,text='Send',command=send)
            btn2.grid(row=2,column=1)
            w4.mainloop()
        elif len(str(passwd.get()))==0 or len(str(passwd2.get()))==0:
            messagebox.showerror("Error","A field is missing !")
        else:
            messagebox.showerror("Error","The passwords don't match !")
    btnSend=Button(w3,text="Confirm",command=storePassword)
    btnSend.grid(row=2,column=1)
    w3.mainloop()
    #Use the Speech Recognition instead
b1=Button(root,text="Send Email",command=credentialsWindow)
b1.pack()
root.mainloop()