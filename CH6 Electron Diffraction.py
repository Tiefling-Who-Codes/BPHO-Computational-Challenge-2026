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

def choose_colors(iteration_number):
    colors = plt.cm.gist_ncar(np.linspace(0, 0.95, iteration_number))
    return colors

def plot_graph(d_val, voltages):
    val = {}
    for V in voltages:
        wavelength = wavelength_from_voltage(V)
        n_max = calculate_n_max(wavelength, d_val)
        for n in range(1, n_max + 1):
            theta = theta_rad_from_n(n, wavelength, d_val)
            if theta is not None:
                phi = phi_from_theta(theta)
                radius = radius_from_phi(phi)
                if n in val:
                    val[n].append([V, radius])
                else:
                    val[n] = [[V, radius]]
        

    #Setup Scatter Plot
    fig, ax = plt.subplots(figsize=(9,5))
    ax.grid(True, alpha=0.17)
    ax.set_xlabel("Accelerating voltage /V")
    ax.set_ylabel("Radii of rings /m")
    ax.set_title(f"Model of electron diffraction rings: d = {d_val}nm, r = {r}m")

    #Plot the points for each n value
    colors = choose_colors(len(val))
    i = 0
    for n, lst in val.items():
        arr = np.array(lst)
        ax.plot(arr[:,0], arr[:,1], color=colors[i], label=f"{n}") # Array slicing & Plotting
        i += 1
    fig.legend(title = "n", loc = "outside right")
    plt.show()

#list of voltages
voltages = np.linspace(1000, 5000, resolution_voltage) # 1kV to 5kV in resolution_voltage intervals

#Itterate for d = 0.123 nm
d_val = d[0]
plot_graph(d_val, voltages)

#Itterate for d = 0.213 nm
d_val = d[1]
plot_graph(d_val, voltages)


