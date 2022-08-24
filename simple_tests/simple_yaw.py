from codrone_edu.drone import *
import numpy as np

drone = Drone()
print("Getting Ready to Pair...")
drone.pair()
print("Paired!")
#? Yaw
drone.takeoff()
print("Taking off...")
# value inside the () range from (-100, 100) indicates power level in %
# + or - indicate direction
drone.hover(3)

drone.set_yaw(10)
drone.move(2)

drone.land()
drone.close()