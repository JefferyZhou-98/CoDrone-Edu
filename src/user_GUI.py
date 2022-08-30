from codrone_edu.drone import *
import numpy as np
import tkinter as tk
from tkinter import *
import tkinter.font as font


def user_input():
    HEIGHT = 400
    WIDTH = 400
    #? Creating the GUI Box
    root = tk.Tk()
    root.title("CoDrone Controller")
    canvas = Canvas(root, height = HEIGHT, width = WIDTH)
    canvas.pack()

    frame=Frame(root, bg='#a3a1ad', bd=3)
    frame.place(relx=0.5, rely = 0.1, relwidth = 0.85, relheight = 0.3, anchor='n')

    # setting font type
    f = font.Font(weight="bold")
    # button pressed for specific functionality
    button1 = Button(frame, text="! ! ! ABORT ! ! !", background="red", foreground="white", font=("Helvetica bold", 12)); button1['font'] = f
    button1.place(relx=0.02, rely = 0.05, relheight=0.5, relwidth=0.4)
    button2 = Button(frame, text="Save Flight Data", font=("Helvetica", 12))
    button2.place(relx=0.3, rely=0.6, relheight=0.4, relwidth=0.4)

    text1 = Label(text="Enter Testing Parameters:", font=("Helvetica bold", 12)); text1['font'] = f
    text1.place(relx=0.08, rely=0.42)

    # saving variable so that we can access it later outside the tkinter mainloop()
    # need to call StringVar() n times for n inputs since StringVar() is not iterable
    variable1=StringVar(); variable2=StringVar(); variable3=StringVar()
    def search():
        return float(variable1.get()), float(variable2.get()), float(variable3.get())

    #? User enter inputs for speed, duration, power
    text2 = Label(text="Speed:", font=("Helvetica bold", 12)) 
    text2.place(relx=0.08, rely=0.49)
    entry1 = tk.Entry(root, textvariable=variable1)
    entry1.place(relx=0.08, rely=0.55, relheight=0.1, relwidth=0.5)
    entry_1 = entry1.get()

    text3 = Label(text="Throttle:", font=("Helvetica bold", 12))
    text3.place(relx=0.08, rely=0.65)
    entry2 = tk.Entry(root, textvariable=variable2)
    entry2.place(relx=0.08, rely=0.71, relheight=0.1, relwidth=0.5)
    entry_2 = entry2.get()

    text4 = Label(text="Duration:", font=("Helvetica bold", 12))
    text4.place(relx=0.08, rely=0.81)
    entry3 = tk.Entry(root, textvariable=variable3)
    entry3.place(relx=0.08, rely=0.87, relheight=0.1, relwidth=0.5)
    entry_3 = entry3.get()

    #? Ready to Fly Button
    button3 = Button(frame, text="TAKE OFF", font=("Helvetica", 14), background="green", foreground="white"); button3['font'] = f
    button3.place(relx=0.55, rely=0.05, relheight=0.5, relwidth=0.4)



    root.mainloop()
    speed, throttle, duration = search()
    return speed, throttle, duration

