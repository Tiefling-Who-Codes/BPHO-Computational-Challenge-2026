# Imports
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter as sf

# Constants
h = 6.62607015e-34  # Planck's constant (J·s)
c = 299792458  # Speed of light (m/s)
kb = 1.380649e-23  # Boltzmann constant (J/K)
r = 8.314462618  # Gas constant (J/(mol·K))

wavelengths_nm = np.linspace(10, 2500, 10000)  # Wavelength range (nm)
wavelengths_m = wavelengths_nm * 1e-9  # Convert to meters
temperatures_K = [4000, 5000, 6000]  # Temperatures (K)

##### Einstein's Molar Heating Capacity of Solids #####

# Einstein frequencey (Hz)
Au = 0.2855e13
Cu = 0.5769e13
Ti = 0.7054e13
Al = 0.7188e13
Fe = 0.7893e13
Si = 1.0832e13
Carbon  = 3.7451e13

def find_x (temperature, frequency):
    return (h * frequency) / (kb * temperature)

def molar_heat_capacity(t, f):
    x = find_x(t, f)
    return 3 * r * (x ** 2) * np.exp(x) / (np.exp(x) - 1) ** 2

temperatures = np.linspace(1, 1000, 1000)  # Temperature range (K)
Au = molar_heat_capacity(temperatures, Au)
Cu = molar_heat_capacity(temperatures, Cu)
Ti = molar_heat_capacity(temperatures, Ti)
Al = molar_heat_capacity(temperatures, Al)
Fe = molar_heat_capacity(temperatures, Fe)
Si = molar_heat_capacity(temperatures, Si)
Carbon = molar_heat_capacity(temperatures, Carbon)

plt.figure(figsize=(10, 6))
plt.plot(temperatures, Au, label='Au')
plt.plot(temperatures, Cu, label='Cu')
plt.plot(temperatures, Ti, label='Ti')
plt.plot(temperatures, Al, label='Al')
plt.plot(temperatures, Fe, label='Fe')
plt.plot(temperatures, Si, label='Si')
plt.plot(temperatures, Carbon, label='Carbon')
plt.title("Einstein's Molar Heat Capacity of Solids")
plt.xlabel('Temperature / K')
plt.ylabel('Molar Heat Capacity / J/(mol·K)')
plt.xlim(0, 1000)
plt.ylim(0, 3 * r * 1.1)
plt.legend()
plt.grid()
plt.show()