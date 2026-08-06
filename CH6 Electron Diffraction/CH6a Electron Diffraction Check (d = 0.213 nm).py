#Imports
import numpy as np
import matplotlib.pyplot as plt
from math import *

#Constants
me = 9.10938356e-31 #electron mass in kg
e = 1.602176634e-19 #elementary charge in C
h = 6.62607015e-34 #Planck's constant in J*s
c = 299792458 #speed of light in m/s

#variables
resolution_voltage = 1000 # 1000 intervals
d = [0.123, 0.213] #grating spacing in nanometers
r = 0.065  # distance from the diffraction grating to the screen in m


#functions
def wavelength_from_voltage(V):
    global h, c, e
    eV = e * V
    wavelength = h / sqrt(2 * me * eV) #wavelength in meters
    return wavelength * 1e9 #convert to nanometers

def calculate_n_max(wavelength, d):
    return floor((2 * d) / wavelength)

def theta_rad_from_n(n, wavelength, d):
    numerator = n * wavelength
    denominator = 2 * d
    if numerator / denominator > 1:
        return None #return None if the value is greater than 1, as arcsin cannot be computed
    return asin(numerator / denominator) #leave answer in radians, as math module works better with radians

def phi_from_theta(theta):
    return 2 * theta

def radius_from_phi(phi):
    return r * sin(phi) #return radius in m
    # phi lets us account for the angle of incidence being equal to the angle of reflection

def dval_from_gradients(k, n):
    numerator = k * n * h
    denominator = 2 * sqrt(2 * me * e)
    return numerator / denominator

def choose_colors(iteration_number):
    colors = plt.cm.hsv(np.linspace(0, 0.95, iteration_number))
    return colors

def plot_graph(d_val, voltages):
    val = {}
    for V in voltages:
        wavelength = wavelength_from_voltage(V)
        n_max = calculate_n_max(wavelength, d_val)
        for n in range(1, n_max + 1):
            theta = theta_rad_from_n(n, wavelength, d_val)
            if theta is not None:
                x = sin(theta)
                y = 1/sqrt(V)
                if n in val:
                    val[n].append([x, y])
                else:
                    val[n] = [[x, y]]
    #plot graph
    gradients = {}
    colors = choose_colors(len(val))
    for n in val:
        x_vals = [i[0] for i in val[n]]
        y_vals = [i[1] for i in val[n]]
        plt.plot(x_vals, y_vals, label=f"n={n}", color=colors[n-1])
        #Get Gradient
        k, intercept = np.polyfit(x_vals, y_vals, 1)
        gradients[n] = k

    #Get D vals from gradients
    d_vals = {}
    for n in gradients:
        d_vals[n] = dval_from_gradients(gradients[n], n)
    
    #Title and labels
    plt.title(f"Electron Diffraction Rings for d = {d_val} nm")
    plt.xlabel("sin(theta)")
    plt.ylabel("1/sqrt(V)")
    plt.legend()
    print(f"Gradients for d = {d_val} nm: {gradients}")
    print(f"D values for d = {d_val} nm: {d_vals}")
    plt.show()
#list of voltages 
voltages = np.linspace(1000, 5000, resolution_voltage) # 1kV to 5kV in resolution_voltage intervals

#Itterate for d = 0.213 nm
d_val = d[1]
plot_graph(d_val, voltages)


