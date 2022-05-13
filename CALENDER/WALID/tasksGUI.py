from tkinter import *
# from tasks import tasksList
def taskGUI(tasksList):
    # Create The Gui Object
    tk = Tk()

    # Adding the Button and Label
    def add_task():
        print("add task clicked :)")
        # task = Label(tk , text = "added task")
        # task.pack(pady = 20)
        print("value",value)
        print("entree", entree)
        Button(tk, text = "add task",
        command = add_task).pack(pady = 20)

    # Set the geometry of the GUI Interface
    tk.geometry("500x500")

    tasksList = tasksList
    tasksStr = '\n'.join(tasksList)
    print(tasksStr)

    tasks = Label(tk, text = tasksStr)

    tasks.pack(pady = 20)
    # entrée
    value = StringVar()
    value.set("texte par défaut")
    entree = Entry(tk, textvariable=value , width=30)
    entree.pack(pady = 20)

    # Execute Tkinter
    tk.mainloop()
