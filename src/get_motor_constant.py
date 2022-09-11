from codrone_edu.drone import *
import numpy as np
from matplotlib import pyplot as plt
import sympy as sym
import csv
import pandas as pd
from scipy.interpolate import interp1d
from pathlib import Path

def linear_reg(y, x, m):
    # function inputs: 
    # 1) y = accelerameter output for z 
    # 2) x = motor command
    # Since the force generated by singular motor is: F = Kf*(sigma**2)
    # where sigma is motor speed and it can be approximated by a constant c*(m1) = sigma**2
    # where m1 is the motor command
    # combining everything we can obtain: F = Kf*c*m1 but since Kf and c are both constants we can say: 
    # Kf = Kf*c then the equation can be simplified to F = Kf*(sigma**2)
    # The thrust force F is also related to m*a_z where a_z is the linear acceleration of the drone in the z direction
    # a_z = Kf*(sigma**2)/m, combining the Kf/m constant into C we can obtain the following relationship: 
    # a_z = C*(sigma**2) where C = Kf/m, Kf = C*m where m = mass of the drone
    #* Estimated C constant based on least-squares linear regression of the data set 
    C = np.sum(y * x) / (np.sum(x**2))
    # the accuracy of the estimation of the slope C will improve with more data set
    Kf = C/m

    return Kf

def save_file(motion_data):
    # designating file location
    path = Path(r'C:\Users\Jeffz\Desktop\Purdue 2022\CoDrone-Edu\data')
    path.mkdir(parents=True)
    fpath = (path / 'force_parameter').with_suffix('.csv')
    # defining the structure of csv
    header = ['time_s', 'a_x', 'a_y', 'a_z']
    with fpath.open('a', encoding='UTF8', newline="") as f:
        data = [motion_data()[0], motion_data()[1], motion_data()[2], motion_data()[3]]
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

def get_data(csv, lower_bound):
    time = csv.time_s.values
    a_x = csv.a_x.values; 
    a_y = csv.a_y.values; 
    a_z = csv.a_z.values
    
    # cleaning up data
    time_cleaned = []; a_x_cleaned = []; a_y_cleaned = []; a_z_cleaned = []
    for i in np.arange(0, len(time)):
        if i % 2 == 0:
            time_cleaned.append(float(time[i]))
            # accelerometer measurements are in g's, multiple by 10 as shown in drone.py source code
            a_x_cleaned.append(10 * float(a_x[i]))
            a_y_cleaned.append(10 * float(a_y[i]))
            a_z_cleaned.append(10 * float(a_z[i]))
    return time_cleaned[lower_bound:], a_x_cleaned[lower_bound:], a_y_cleaned[lower_bound:], a_z_cleaned[lower_bound:]

#* Define Constants 
g = 9.81 # m/s**2
m = 0.0571 # kg


#* Pairing
drone = Drone()
drone.pair()
print("Paired!")

#? Saving yaw, pitch, roll data to csv
data_list = []
for i in np.arange(0,200):
    data = drone.get_motion_data
    data_list.append(data)
    save_file(data)

#* Obtaining usable data
motion_data = pd.read_csv('force_parameter.csv')
t, a_x, a_y, a_z = get_data(motion_data)

#* Obtaining k_f
