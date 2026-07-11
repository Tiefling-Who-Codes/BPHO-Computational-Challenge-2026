#Imports
import numpy as np
import matplotlib.pyplot as plt

#Constants
me = 9.10938356e-31 #electron mass in kg
mp = 1.6726219e-27 #proton mass in kg
mn = 1.674927471e-27 #neutron mass in kg


#Lets plot the hydrogen spectra for visible light
m = 2
for n in range(3,7):
    wavelength = 91.2 * (1/m**2 - 1/n**2) ** -1 #wavelength in nm
    print(wavelength, n)