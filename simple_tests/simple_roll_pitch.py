from codrone_edu.drone import *
import numpy as np

drone = Drone()
print("Getting Ready to Pair...")
drone.pair()
print("Paired!")
#? Roll
drone.takeoff()
print("Taking off...")
# value inside the () range from (-100, 100) indicates power level in %
# + or - indicate direction
#? Moving in a square 
drone.set_pitch(30)
drone.move(0.8)
# need to reset to initiate different movement
drone.set_pitch(0)
drone.set_roll(30)
drone.move(0.8)

drone.set_roll(0)
drone.set_pitch(-30)
drone.move(0.8)

drone.set_pitch(0)
drone.set_roll(-30)
drone.move(0.8)

drone.set_roll(0)
drone.land()
drone.close()