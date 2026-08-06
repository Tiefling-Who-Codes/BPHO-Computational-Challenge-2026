# Imports
import numpy as np
from numpy import sin, cos

# Constants 
h = 6.62607015e-34 # Planck's constant in J*s
c = 3e8 # speed of light in m/s
me = 9.10938356e-31 # electron mass in kg

# Variables

# Functions
def keV_to_J(keV):
    return keV * 1.60218e-16

def fractional_wavelength_shift(energy, theta_deg):
    theta = np.radians(theta_deg)
    term1 = energy / (me * c**2)
    term2 = 1 - cos(theta) 
    return term1 * term2

def wavelengths_from_energy(energy, theta_deg):
    old_wavelength = (h * c) / energy
    new_wavelength = old_wavelength * (1 + fractional_wavelength_shift(energy, theta_deg))
    return old_wavelength, new_wavelength

def electron_recoil_speed(energy, theta_deg):
    old_wavelength, new_wavelength = wavelengths_from_energy(energy, theta_deg)
    term1 = me * c**2
    term2 = ((h * c) / old_wavelength) - ((h * c) / new_wavelength) + (me * c**2)
    return np.sqrt(1 - (term1 / term2)**2)

def electron_recoil_angle(energy, theta_deg):
    theta = np.radians(theta_deg)
    wavelength_shift = fractional_wavelength_shift(energy, theta_deg)
    numerator = sin(theta)
    denominator = (1 + wavelength_shift) - cos(theta)
    return np.degrees(np.arctan(numerator / denominator))


