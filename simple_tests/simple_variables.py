from codrone_edu.drone import *
import numpy as np
import tkinter as tk
from tkinter import simpledialog

#? User enter inputs for speed, duration, power
ROOT = tk.Tk()
ROOT.withdraw()
# input dialog
user_input = simpledialog.askinteger(title="User Input", prompt="Speed: ")


drone = Drone()
print("Getting Ready to Pair...")
drone.pair()
print("Paired!")
#? Yaw
drone.takeoff()
print("Taking off...")
# value inside the () range from (-100, 100) indicates power level in %
# + or - indicate direction

#? Setting up parameters 
speed = 15
duration = 3

drone.go(0, speed, speed, 0, duration)

drone.land()
drone.close()

