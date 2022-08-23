from codrone_edu.drone import *
import numpy as np

drone = Drone()
print("Getting Ready to Pair...")
drone.pair()
print("Paired!")
#? Setting Trim --------------
# if the drone is drifting right, so trim to roll left a little bit
# this alters the thrust/power input to the motors to counter drift
drone.set_trim(0, 0)
# viewing the current trim
print(drone.get_trim())
#? Setting Trim --------------
# Add a time.sleep(1) before takeoff if you're planning to set the trim before takeoff
time.sleep(1)
drone.takeoff()
print("Taking off...")
drone.hover(5)
print("Hovering...")
drone.land()
print("Landing...")
drone.close()