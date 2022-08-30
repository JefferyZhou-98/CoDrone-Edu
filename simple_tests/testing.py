from codrone_edu.drone import *
import numpy as np
import sys

# copy and paste the src folder path
sys.path.insert(0, r'C:\Users\Jeffz\Desktop\Purdue 2022\CoDrone-Edu\src')
from user_GUI import user_input

# drone = Drone()
# print("Getting Ready to Pair...")
# drone.pair()
# print("Paired!")

#? taking in user inputs
speed, throttle, duration = user_input()

#? Setting Trim --------------
# if the drone is drifting right, so trim to roll left a little bit
# this alters the thrust/power input to the motors to counter drift
# drone.set_trim(0, 0)
# # viewing the current trim
# print(drone.get_trim())
# #? Setting Trim --------------
# # Add a time.sleep(1) before takeoff if you're planning to set the trim before takeoff
# time.sleep(1)
# drone.takeoff()
# print("Taking off...")
# drone.hover(duration)
# print("Hovering...")
# drone.set_pitch(throttle)
# drone.move(duration)
# drone.set_pitch(0)
# drone.land()
# print("Landing...")
# drone.close()

