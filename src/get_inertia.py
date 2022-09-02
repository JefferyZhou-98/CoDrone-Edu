from codrone_edu.drone import *
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks
import sympy as sym
import time
import csv
import pandas as pd
#? Preparing CSV to save roll pitch yaw data 
def save_file(t, roll, pitch, yaw):
    header = ['time(s)', 'roll_deg', 'pitch_deg', 'yall_deg']
    with open('euler.csv', 'a', encoding='UTF8', newline="") as f:
        data = [t, roll, pitch, yaw]
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
# t_k = time.time()
# t = []; roll = []; pitch = []; yaw = []
# for i in np.arange(0,1000):
#     t_k1 = time.time()
#     r = drone.get_x_angle()
#     p = drone.get_y_angle()
#     y = drone.get_z_angle()
#     t.append(t_k)
#     roll.append(r); pitch.append(p); yaw.append(y)
#     save_file(t_k1, r, p, y)
#     t_k = t_k1

# pulling data from recorded csv 
euler_data = pd.read_csv("euler.csv")
t = euler_data.time_s.values; roll_deg = euler_data.roll_deg.values
pitch_deg = euler_data.pitch_deg.values; yaw_deg = euler_data.yaw_deg.values

# cleaning up data 
def clean_up(data):
    cleaned_up = []
    for i in np.arange(0, len(data)):
        if i % 2 == 0:
            cleaned_up.append(float(data[i]))
    return cleaned_up

# extracting the useful data sets to visualize 
t_clean = clean_up(t)[920:]; roll_clean = clean_up(roll_deg)[920:]; 
pitch_clean = clean_up(pitch_deg)[920:]; yaw_clean = clean_up(yaw_deg)[920:]

#? Estimate the moment of inertia about the three principle axes 
# plotting the three components of angular velocity 
# the component of angular velocity about the x-axis should be the largest 
# plt.figure(dpi = 200)
# plt.plot(t_clean, roll_clean, label=r"$\omega_x$", color="tab:blue", linewidth = 2)
# plt.plot(t_clean, pitch_clean, label=r"$\omega_y$", color="tab:green", linewidth = 2)
# plt.plot(t_clean, yaw_clean, label=r"$\omega_z$", color="tab:orange", linewidth = 2)
# plt.legend(fontsize = 11)
# plt.xlabel("Time (s)", fontsize = 12); plt.ylabel("Angular Speed (rad/s)", fontsize = 12)
# plt.grid()
# plt.show()

# dividing the data into three to separate roll, pitch yaw data
t_roll = t_clean[0:230]; roll_final = roll_clean[0:230]
t_pitch = t_clean[300:500]; pitch_final = pitch_clean[300:500]
t_yaw = t_clean[620:850]; yaw_final = yaw_clean[620:850]

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

x_mean_t_diff, x_t_peaks, w_x_peaks = peak_finder(roll_final, t_roll)
y_mean_t_diff, y_t_peaks, w_y_peaks = peak_finder(pitch_final, t_pitch)
z_mean_t_diff, z_t_peaks, w_z_peaks = peak_finder(yaw_final, t_yaw)
# Plotting the peaks 
plt.figure(dpi = 200)
plt.plot(t_yaw, yaw_final, label=r"$\omega_z$", color="tab:blue", linewidth = 2)
plt.scatter(z_t_peaks, w_z_peaks, s = 50, label="Peaks", color="tab:orange")
plt.xlabel("Time (s)", fontsize = 12); plt.ylabel("Angular Velocity (rad/s)", fontsize = 12)
plt.legend(); plt.grid()
plt.show()

# #? Function to solve for moment of inertia 
# def moment(mean_t):
#     J = sym.symbols('J')
#     eq = ((2*np.pi/mean_t)**2) - (m*g*r/(J + m*r**2))

#     ans = sym.solve(eq, J)

#     return ans

