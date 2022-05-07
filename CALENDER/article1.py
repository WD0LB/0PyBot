#https://towardsdatascience.com/develop-your-own-calendar-to-track-important-dates-with-python-c1af9e98ffc3
# Importing The Essential Libraries
from tkinter import *
from tkcalendar import Calendar

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
cal = Calendar(tk, selectmode = 'day',
               year = year, month = month,
               day = day)

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

# Execute Tkinter
tk.mainloop()
