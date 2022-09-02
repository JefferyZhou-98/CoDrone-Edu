# Record sensor data after giving each command

from turtle import delay
from codrone_edu.drone import *
import numpy as np
import time
import csv
import keyboard
import sys

def emergency_landing(event):
    print("Emergency landing!!!")
    drone.land()
    os.kill(os.getpid(), signal.SIGTERM)

def record_data(record_times, motion_data_list, drone):
    for i in range(record_times):
        motion_data = drone.get_motion_data()
        motion_data_list.append(motion_data)

keyboard.on_press_key("space", emergency_landing)

# Command param: power(-100~100), duration(s)
power = 50
duration = 1
record_times = duration*60 # each record takes 0.0167s

drone = Drone()
# drone.pair()
print("Paired!")

print("\nPress enter to take off.")
keyboard.wait('enter')
print("Taking off...")
# drone.takeoff()
# drone.hover()

print("\nPress enter to start \"Throttle\" testing.")
keyboard.wait('enter')
print("Test starts...")
time_start = time.time()
data = []
drone.sendControl(0, 0, 0, power)
record_data(record_times, data, drone)
drone.sendControl(0, 0, 0, -power)
record_data(record_times, data, drone)
drone.reset_move()
print("\nTest finished in", time.time()-time_start)
np.savetxt('Throttle_test.csv', np.array(data), delimiter=",")

drone.land()