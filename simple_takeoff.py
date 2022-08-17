from codrone_edu.drone import *
drone = Drone()
drone.pair()
# if the drone is drifting right, so trim to roll left a little bit
# this alters the thrust/power input to the motors to counter drift
drone.set_trim(-5, 0)
# viewing the current trim
drone.get_trim()
# Add a time.sleep(1) before takeoff if you're planning to set the trim before takeoff
time.sleep(1)
drone.takeoff()
drone.hover(3)
drone.land()
drone.close()