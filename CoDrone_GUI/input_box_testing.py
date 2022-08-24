from codrone_edu.drone import *
import numpy as np
from tkinter import *

#? User enter inputs for speed, duration, power

root = Tk()
root.title("CoDrone Controller")
frame=Frame(root, width=500, height=260)
frame.pack()
button1 = Button(frame, text="! ! ! ABORT ! ! !")
button1.place(x=10, y=10, height=30, width=100)
button2 = Button(frame, text="Justice!")
button2.place(x=10, y=50, height=30, width=100)
text1 = Label(text="Verdict:")
text1.place(x=10, y=90)
tbox1 = Text(frame)
tbox1.place(x=10, y=115, height=30, width=200)

root.mainloop()
