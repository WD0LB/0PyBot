from tkinter import *

top = Tk()
top.geometry("500x500")
frame = Frame(top)
frame.pack()

leftframe = Frame(top)
leftframe.pack(side = LEFT)

rightframe = Frame(top)
rightframe.pack(side = RIGHT)

btn1 = Button(frame, text="Submit", fg="red",activebackground = "red")
btn1.pack(side = LEFT)

btn2 = Button(frame, text="Remove", fg="brown", activebackground = "brown")
btn2.pack(side = RIGHT)

btn3 = Button(rightframe, text="Add", fg="blue", activebackground = "blue")
btn3.pack(side = LEFT)

done = Button(rightframe, text="done", fg="blue", activebackground = "blue")
done.pack(side = LEFT)

# btn4 = Button(leftframe, text="Modify", fg="black", activebackground = "white")
# btn4.pack(side = RIGHT)

btn4 = Label(leftframe, text="Modify")
btn4.pack(side = RIGHT)

frame2 = Label(top)
frame2.pack()
lf2 = Frame(frame2).pack(side = LEFT)
rf2 = Frame(frame2).pack(side = RIGHT)

btnrf = Button(rf2, text="add", fg="blue", activebackground="blue").pack(side=LEFT)


top.mainloop()
