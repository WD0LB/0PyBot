import tkinter as tk
from tkinter import ttk
from db import tasksList
def add():
    print("adding")
def done(i):
    print("done: "+str(i))
def remove(i):
    print("remove: "+str(i))
def dayTask(pickedDate):
    root = tk.Tk()
    root.geometry("800x400")
    root.title("Tasks of the day")
    root.resizable(0,0)

    #configure grid
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    #title
    title = ttk.Label(root, text=pickedDate)
    title.grid(column=0,row=0,columnspan=4)
    #add task
    taskInput = ttk.Entry(root)
    taskInput.grid(column=0, row=1, columnspan=3)
    addBtn = ttk.Button(root, text="Add", command=add())
    addBtn.grid(column=3, row=1)
    #Tasks
    #task 1: example
    # task = ttk.Label(root, text="Task1 example")
    # task.grid(column=0, row=2, columnspan=2)
    # done = ttk.Button(root, text="Done")
    # done.grid(column=2, row=2)
    # remove = ttk.Button(root, text="Remove")
    # remove.grid(column=3, row=2)
    #looping
    tasksL = []
    doneL = []
    removeL = []
    print(len(tasksList ))
    for i in range(len(tasksList)):
        print(tasksList[i])
        tasksL.append(ttk.Label(root, text=tasksList[i]))
        tasksL[i].grid(column=0, row=i+4, columnspan=2)
        doneL.append(ttk.Button(root, text="done", command = done(i)))
        doneL[i].grid(column=2, row=i+4)
        removeL.append(ttk.Button(root, text="remove", command = remove(i)))
        removeL[i].grid(column=3, row=i+4)
        print(i)
    root.mainloop()
