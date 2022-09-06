from codrone_edu.drone import *
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks
import sympy as sym
import time
import csv
import pandas as pd
#? Preparing CSV to save roll pitch yaw data 
def save_file(motion_data):
    header = ['time_s', 'roll_deg_s', 'pitch_deg_s', 'yaw_deg_s']
    with open('pitch.csv', 'a', encoding='UTF8', newline="") as f:
        data = [motion_data()[0], motion_data()[4], motion_data()[5], motion_data()[6]]
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

# Pairing
# drone = Drone()
# drone.pair()
# print("Paired!")
#? Defining Constants 
# gravitational acceleration
g = 9.81
# mass of drone (kg)
m = 0.0571
# define the distance (m) between the axis of rotation and the center of mass:
r = 0.052

#? Saving yaw, pitch, roll data to csv
# data_list = []
# for i in np.arange(0,200):
#     data = drone.get_motion_data
#     data_list.append(data)
#     save_file(data)

# pulling data from recorded csv 
roll_data = pd.read_csv("roll.csv"); pitch_data = pd.read_csv("pitch.csv"); yaw_data = pd.read_csv("yaw.csv")
def get_data(csv):
    time = csv.time_s.values
    omega_x = csv.roll_deg_s.values; 
    omega_y = csv.pitch_deg_s.values; 
    omega_z = csv.yaw_deg_s.values
    return time, omega_x, omega_y, omega_z

# cleaning up data 
def clean_up(time, omega_x, omega_y, omega_z, lower_bound):
    time_cleaned = []; omega_x_cleaned = []; omega_y_cleaned = []; omega_z_cleaned = []
    for i in np.arange(0, len(time)):
        if i % 2 == 0:
            time_cleaned.append(float(time[i]))
            # converting from deg/s to rad/s
            omega_x_cleaned.append(np.deg2rad(float(omega_x[i])))
            omega_y_cleaned.append(np.deg2rad(float(omega_y[i])))
            omega_z_cleaned.append(np.deg2rad(float(omega_z[i])))
    return time_cleaned[lower_bound:], omega_x_cleaned[lower_bound:], omega_y_cleaned[lower_bound:], omega_z_cleaned[lower_bound:]

roll_time, omega_x_roll, omega_y_roll, omega_z_roll = get_data(roll_data)
pitch_time, omega_x_pitch, omega_y_pitch, omega_z_pitch = get_data(pitch_data)
yaw_time, omega_x_yaw, omega_y_yaw, omega_z_yaw = get_data(yaw_data)


# extracting the useful data sets to visualize 
t_clean_roll, omega_x_clean_roll, omega_y_clean_roll, omega_z_clean_roll = clean_up(roll_time, omega_x_roll, omega_y_roll, omega_z_roll, 30)
t_clean_pitch, omega_x_clean_pitch, omega_y_clean_pitch, omega_z_clean_pitch = clean_up(pitch_time, omega_x_pitch, omega_y_pitch, omega_z_pitch, 20)
t_clean_yaw, omega_x_clean_yaw, omega_y_clean_yaw, omega_z_clean_yaw = clean_up(yaw_time, omega_x_yaw, omega_y_yaw, omega_z_yaw, 20)

# #? Estimate the moment of inertia about the three principle axes 
# # plotting the three components of angular velocity 
# # the component of angular velocity about the x-axis should be the largest 
# plt.figure(dpi = 200)
# # plt.plot(t_clean_yaw, omega_x_clean_yaw, label=r"$\omega_x$", color="tab:blue", linewidth = 2)
# # plt.plot(t_clean_yaw, omega_y_clean_yaw, label=r"$\omega_y$", color="tab:green", linewidth = 2)
# plt.plot(t_clean_yaw, omega_z_clean_yaw, label=r"$\omega_z$", color="tab:orange", linewidth = 2)
# plt.legend(fontsize = 11)
# plt.xlabel("Time (s)", fontsize = 12); plt.ylabel("Angular Speed (rad/s)", fontsize = 12)
# plt.grid()
# plt.show()


#? Finding the Period 
# all three components of the angular velocities are oscillatory. The period of this oscillation is the peak-to-peak time. 
# This period could be measured by hand, but let's automate the process 
# 1) Find the index i_k of each peak in the data 
# 2) find the time t_k at each peak 
# 3) Find the difference T_k = t_k+1 - t_k between each consecutive peak times 
# 4) find the mean difference 

def peak_finder(omega, time):
    # Find the inex of each peak (increase "prominence" if you get bad results)
    peaks = find_peaks(omega, prominence=0)
    # number of total peaks 
    i_peaks = peaks[0]
    # Find the time at each peak 
    # find w_x at each peak 
    t_peaks = []; w_peaks = []
    for i in i_peaks:
        t_peaks.append(time[i])
        w_peaks.append(omega[i])

    # finding the time difference between peaks
    t_diff = []
    for i in np.arange(0, len(t_peaks) - 1):
        diff = t_peaks[i + 1] - t_peaks[i]
        t_diff.append(diff)

    # Finding the mean difference as an estimate of the oscillation period 
    mean_t_diff = np.mean(t_diff)

    return mean_t_diff, t_peaks, w_peaks

x_mean_t_diff, x_t_peaks, w_x_peaks = peak_finder(omega_x_clean_roll, t_clean_roll)
y_mean_t_diff, y_t_peaks, w_y_peaks = peak_finder(omega_y_clean_pitch, t_clean_pitch)
z_mean_t_diff, z_t_peaks, w_z_peaks = peak_finder(omega_z_clean_yaw, t_clean_yaw)

# z_mean_t_diff, z_t_peaks, w_z_peaks = peak_finder(yaw_final, t_yaw)
# Plotting the peaks 
# plt.figure(dpi = 200)
# plt.plot(t_clean_yaw, omega_z_clean_yaw, label=r"$\omega_z$", color="tab:blue", linewidth = 2)
# plt.scatter(z_t_peaks, w_z_peaks, s = 50, label="Peaks", color="tab:orange")
# plt.xlabel("Time (s)", fontsize = 12); plt.ylabel("Angular Velocity (rad/s)", fontsize = 12)
# plt.legend(); plt.grid()
# plt.show()

#? Function to solve for moment of inertia 
def moment(mean_t):
    J = sym.symbols('J')
    eq = ((2*np.pi/mean_t)**2) - (m*g*r/(J + m*r**2))

    ans = sym.solve(eq, J)

    return ans

j_x = moment(x_mean_t_diff)
j_y = moment(y_mean_t_diff)
j_z = moment(z_mean_t_diff)

print(f"Jxx: {j_x[0]}, Jyy: {j_y[0]}, Jzz: {j_z[0]}")
