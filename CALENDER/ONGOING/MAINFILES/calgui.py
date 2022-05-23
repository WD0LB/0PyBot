# Importing The Essential Libraries
from tkinter import *
from tkcalendar import Calendar
from tasks import tasksList
from tkinterGridTest import dayTask
#getting the current day
from datetime import date
today = str(date.today()).split('-')
year = int(today[0])
month = int(today[1])
day = int(today[2])
def calgui():

    # Create The Gui Object
    tk = Tk()

    # Set the geometry of the GUI Interface
    tk.geometry("700x700")

    # Add the Calendar module
    cal = Calendar(tk,cursor="hand1", selectmode = 'day',
                   year = year, month = month,
                   day = day)

    # adding EVENTS
    today_date = cal.datetime.today()
    cal.calevent_create(today_date, "testing","message")
    cal.calevent_create(today_date + cal.timedelta(days=-2), "testing","reminder")
    cal.calevent_create(today_date + cal.timedelta(days=5), "testing","message")
    cal.tag_config('reminder', background='red', foreground='yellow')
    # algorithm:
    '''
    first determine month // example may
    second grab 1st day events // important urgent
    add them with red color
    if there is no imporant urgent move to important not urgent
    and going on brother ;)
    and loop for all month days

    '''
    cal.pack(pady = 20, fill="both", expand=True)

    # Function to grab the selected date
    def grad_date():
        print(cal.get_date())
        date.config(text = "Selected Date is: " + cal.get_date())
        # taskGUI(tasksList)
        dayTask()



    # Adding the Button and Label
    Button(tk, text = "Get Day Tasks",
           command = grad_date).pack(pady = 20)

    date = Label(tk, text = "")
    date.pack(pady = 20)


    # Execute Tkinter
    tk.mainloop()
calgui()
