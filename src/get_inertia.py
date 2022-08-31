from codrone_edu.drone import *
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks
import sympy as sym

#? Defining Constants 
# gravitational acceleration
g = 9.81
# mass of drone (kg)
m = 0.1

#? Estimate the moment of inertia about the three principle axes 
# define the distance (m) between the axis of rotation and the center of mass:
r = 0.01
# after recording the rotation parse data for t, w_x, w_y, w_z
t = 
w_x = 
w_y = 
w_z = 

# plotting the three components of angular velocity 
# the component of angular velocity about the x-axis should be the largest 
plt.figure(dpi = 200)
plt.plot(t, w_x, label=r"$\omega_x$", color="tab:blue", linewidth = 2)
# plt.plot(t, w_y, label=r"$\omega_y$", color="tab:green", linewidth = 2)
# plt.plot(t, w_z, label=r"$\omega_z$", color="tab:orange", linewidth = 2)
plt.legend(fontsize = 11)
plt.xlabel("Time (s)", fontsize = 12); plt.ylabel("Angular Speed (rad/s)", fontsize = 12)
plt.grid()
plt.show()

#? Finding the Period 
# all three components of the angular velocities are oscillatory. The period of this oscillation is the peak-to-peak time. 
# This period could be measured by hand, but let's automate the process 
# 1) Find the index i_k of each peak in the data 
# 2) find the time t_k at each peak 
# 3) Find the difference T_k = t_k+1 - t_k between each consecutive peak times 
# 4) find the mean difference 

def peak_finder(omega):
    # Find the inex of each peak (increase "prominence" if you get bad results)
    peaks = find_peaks(omega, prominence=0)
    # number of total peaks 
    i_peaks = peaks[0]

    # Find the time at each peak 
    t_peaks = t[i_peaks]

    # find w_x at each peak 
    w_peaks = omega[i_peaks]

    # taking away the first and last peak due to possibilities of bad data 
    t_diff = t_peaks[1:] - t_peaks[:-1]

    # Finding the mean difference as an estimate of the oscillation period 
    mean_t_diff = np.mean(t_diff)

    return mean_t_diff, t_peaks, w_peaks

x_mean_t_diff, x_t_peaks, w_x_peaks = peak_finder(w_x)

# Plotting the peaks 
plt.figure(dpi = 200)
plt.plot(t, w_x, label=r"$\omega_x$", color="tab:blue", linewidth = 2)
plt.scatter(x_t_peaks, w_x_peaks, s = 70, label="Peaks")
plt.xlabel("Time (s)", fontsize = 12); plt.ylabel("Angular Velocity (rad/s)", fontsize = 12)
plt.legend(); plt.grid()
plt.show()

#? Function to solve for moment of inertia 
def moment(mean_t):
    J = sym.symbols('J')
    eq = ((2*np.pi/mean_t)**2) - (m*g*r/(J + m*r**2))

    ans = sym.solve(eq, J)

    return ans

