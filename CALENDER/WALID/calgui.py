#https://towardsdatascience.com/develop-your-own-calendar-to-track-important-dates-with-python-c1af9e98ffc3
# Importing The Essential Libraries
from tkinter import *
from tkcalendar import Calendar

#getting the current day
from datetime import date
today = str(date.today()).split('-')
year = int(today[0])
month = int(today[1])
day = int(today[2])

# Create The Gui Object
tk = Tk()

# Set the geometry of the GUI Interface
tk.geometry("700x700")

# Add the Calendar module
cal = Calendar(tk,cursor="hand1", selectmode = 'day',
               year = year, month = month,
               day = day)
today_date = cal.datetime.today()
cal.calevent_create(today_date, "testing","message")
cal.calevent_create(today_date + cal.timedelta(days=-2), "testing","reminder")
cal.calevent_create(today_date + cal.timedelta(days=5), "testing","message")
cal.tag_config('reminder', background='red', foreground='yellow')

cal.pack(pady = 20, fill="both", expand=True)

# Function to grab the selected date
def grad_date():
    print(cal.get_date())
    date.config(text = "Selected Date is: " + cal.get_date())

# Adding the Button and Label
Button(tk, text = "Get Date",
       command = grad_date).pack(pady = 20)

date = Label(tk, text = "")
date.pack(pady = 20)

from tasks import tasksList
tasksList = tasksList
tasksStr = '\n'.join(tasksList)
print(tasksStr)

tasks = Label(tk, text = tasksStr)

tasks.pack(pady = 20)

# Adding the Button and Label
def add_task():
    print("add task clicked :)")
    # task = Label(tk , text = "added task")
    # task.pack(pady = 20)
    print("value",value)
    print("entree", entree)
Button(tk, text = "add task",
command = add_task).pack(pady = 20)

# entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(tk, textvariable=value , width=30)
entree.pack(pady = 20)
# fenetre['bg']='white'

# # frame 1
# Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
# Frame1.pack(side=LEFT, padx=30, pady=30)
#
# # frame 2
# Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
# Frame2.pack(side=LEFT, padx=10, pady=10)
#
# # frame 3 dans frame 2
# Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
# Frame3.pack(side=RIGHT, padx=5, pady=5)
#
# # Ajout de labels
# Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
# Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
# Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)

#menu idea

# Execute Tkinter
tk.mainloop()
