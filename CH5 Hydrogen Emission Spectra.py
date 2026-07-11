#Imports
import numpy as np
import matplotlib.pyplot as plt

#Constants
me = 9.10938356e-31 #electron mass in kg
mp = 1.6726219e-27 #proton mass in kg
mn = 1.674927471e-27 #neutron mass in kg
h = 6.62607015e-34 #Planck's constant in J*s
c = 3e8 #speed of light in m/s
eV = 1.602176634e-19 #electron volt in Joules


#functions
def photon_energy(wavelength):
    global h, c
    energy = h * c / (wavelength * 1e-9) #energy in Joules
    return energy

def Joule_Ev(energy_joules):
    energy_ev = energy_joules / eV #energy in eV
    return energy_ev

def calc_wavelength_nm(n, m):
    return 91.2 * (1/m**2 - 1/n**2) ** -1

def wavelengths(m):
    return [calc_wavelength_nm(n, m) for n in range(m + 1, m + 8)]

def energy_ev(w):
    energy_j = photon_energy(w)
    energy_ev = Joule_Ev(energy_j)
    return energy_ev

#series: 
series = {
    "lyman" : "pink",
    "balmer" : "red",
    "paschen" : "blue",
    "bracket" : "green",
    "pfund" : "black"
}

# series wavelengths
series_wavelengths = {
    "lyman": wavelengths(1),
    "balmer": wavelengths(2),
    "paschen": wavelengths(3),
    "bracket": wavelengths(4),
    "pfund": wavelengths(5)
}

#series energies
series_photon_energy = {
    "lyman": [energy_ev(w) for w in series_wavelengths["lyman"]],
    "balmer": [energy_ev(w) for w in series_wavelengths["balmer"]],
    "paschen": [energy_ev(w) for w in series_wavelengths["paschen"]],
    "bracket": [energy_ev(w) for w in series_wavelengths["bracket"]],
    "pfund": [energy_ev(w) for w in series_wavelengths["pfund"]]
}

# Plotting the hydrogen emission spectra: wavelength vs photon energy
for series_name, series_wls in series_wavelengths.items():
    energies = series_photon_energy[series_name]
    color = series[series_name]
    plt.scatter(series_wls, energies, label=series_name.capitalize(), marker='x', s=50, c=color)
    for w in series_wls:
        plt.axvline(x=w, color=color, linestyle='--', alpha=0.5)

# Graph labels and title
plt.xlabel('Wavelength (nm)')
plt.ylabel('Photon Energy (eV)')
plt.title('Hydrogen Emission Spectra')
plt.legend()
plt.show()