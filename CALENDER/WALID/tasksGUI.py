from tkinter import *
from tasks import tasksList
def taskGUI(tasksList):
    # Create The Gui Object
    tk = Tk()

    # Set the geometry of the GUI Interface
    tk.geometry("500x500")

    # Adding the Button and Label
    def add_task():
        print("add task clicked :)")
        # task = Label(tk , text = "added task")
        # task.pack(pady = 20)
        print("value",value)
        print("entree", entree)
    frame = Frame(tk)
    frame.pack(pady=20)

    Button(frame, text = "add task",
        command = add_task).pack(pady = 20, side = RIGHT)

    # entrée
    value = StringVar()
    value.set("texte par défaut")
    entree = Entry(frame, textvariable=value , width=30)
    entree.pack(pady = 20, side = LEFT)

    tasks = Frame(tk).pack(pady=20)
    # frm = Label(tasks, text="test").pack(pady = 20, side = LEFT)
    # btn = Button(tasks, text = "remove").pack(pady=20, side= RIGHT)
    frm = []
    btn = []
    taskLabel = []
    i = 0
    for task in tasksList:
        taskLabel.append(Label(tasks).pack())
        frm.append(Label(taskLabel[i], text=task).pack(side = LEFT))
        btn.append(Button(taskLabel[i], text = "remove").pack(side= RIGHT))
        i+=1
        print(i)
        print(task)



    # Execute Tkinter
    tk.mainloop()

taskGUI(tasksList)
