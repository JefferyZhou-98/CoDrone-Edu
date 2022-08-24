from codrone_edu.drone import *
import numpy as np
import tkinter as tk
from tkinter import *

#? Creating the GUI Box
root = tk.Tk()
root.title("CoDrone Controller")
frame=Frame(root, width=360, height=320)
frame.pack()

# button pressed for specific functionality
button1 = Button(frame, text="! ! ! ABORT ! ! !", background="red", foreground="white", font=("Helvetica bold", 12))
button1.place(x=10, y=10, height=40, width=140)
button2 = Button(frame, text="Save Flight Data", font=("Helvetica", 12))
button2.place(x=10, y=60, height=40, width=140)

text1 = Label(text="Enter Testing Parameters:", font=("Helvetica bold", 10))
text1.place(x=10, y=110)

# saving variable so that we can access it later outside the tkinter mainloop()
# need to call StringVar() n times for n inputs since StringVar() is not iterable
variable1=StringVar(); variable2=StringVar(); variable3=StringVar()
def search():
    return float(variable1.get()), float(variable2.get()), float(variable3.get())

#? User enter inputs for speed, duration, power
text2 = Label(text="Speed:", font=("Helvetica bold", 10))
text2.place(x=10, y=130)
entry1 = tk.Entry(root, textvariable=variable1)
entry1.place(x=10, y=155, height=30, width=200)
entry_1 = entry1.get()

text3 = Label(text="Throttle:", font=("Helvetica bold", 10))
text3.place(x=10, y=190)
entry2 = tk.Entry(root, textvariable=variable2)
entry2.place(x=10, y=215, height=30, width=200)
entry_2 = entry2.get()

text4 = Label(text="Duration:", font=("Helvetica bold", 10))
text4.place(x=10, y=245)
entry3 = tk.Entry(root, textvariable=variable3)
entry3.place(x=10, y=270, height=30, width=200)
entry_3 = entry3.get()

#? Ready to Fly Button
button3 = Button(frame, text="Take Off", font=("Helvetica", 14), background="green", foreground="white")
button3.place(x=200, y=15, height=80, width=120)


root.mainloop()
