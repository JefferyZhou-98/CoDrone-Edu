# Record sensor data after giving each command

from codrone_edu.drone import *
import numpy as np
import time
import csv
import keyboard

def save_file(t, roll, pitch, yaw):
    header = ['time(s)', 'roll_deg', 'pitch_deg', 'yall_deg']
    with open('data.csv', 'a', encoding='UTF8', newline="") as f:
        data = [t, roll, pitch, yaw]
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

def emergency_landing(event):
    print("Emergency landing!!!")
    drone.land()

keyboard.on_press_key("space", emergency_landing)

# Command param: power(-100~100), duration(s)
power = 50
duration = 1
record_times = duration/0.01 # delay=0.01s

drone = Drone()
# drone.pair()
print("Paired!")

print("Press enter to take off")
keyboard.wait('enter')
print("Taking off...")
drone.takeoff()
drone.hover()

print("Press enter to start testing")
keyboard.wait('enter')
print("Test start...")
drone.go(power, 0, 0, 0, duration)


# t_k = time.time()
# for i in np.arange(0,100):
#     t_k1 = time.time()
    # r = drone.get_x_angle()
#     p = drone.get_y_angle()
#     y = drone.get_z_angle()
#     save_file(t_k1-t_k, r, p, y)
#     t_k = t_k1