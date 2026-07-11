#Imports
import numpy as np
import matplotlib.pyplot as plt
from wavelength_to_hex import wavelength_to_hex_bruton as w2h
#Constants
me = 9.10938356e-31 #electron mass in kg
mp = 1.6726219e-27 #proton mass in kg
mn = 1.674927471e-27 #neutron mass in kg
h = 6.62607015e-34 #Planck's constant in J*s
c = 3e8 #speed of light in m/s
eV = 1.602176634e-19 #electron volt in Joules
#intensity = 65536 #intensity for the wavelength to hex function (MAX intensity... too bright for the plot)
intensity = 3000 #intensity for the wavelength to hex function (~70% brightness) (going for 3000 removes some of the brightness that makes the turquoise stand out, but is a good compromise as it is easer on the eyes.)

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

def color_wavelength(wavelength):
    if 380 <= wavelength < 450:
        return 'violet'
    elif 450 <= wavelength < 495:
        return 'blue'
    elif 495 <= wavelength < 570:
        return 'green'
    elif 570 <= wavelength < 590:
        return 'yellow'
    elif 590 <= wavelength < 620:
        return 'orange'
    elif 620 <= wavelength <= 750:
        return 'red'
    else:
        return 'invisible'

#Hydrogen spectra for visible light
wavelengths = np.array([])
for n in range(3,8):
    w = calc_wavelength_nm(n, 2)
    wavelengths = np.append(wavelengths, w)

# Calculating photon energies for the wavelengths (convert to eV)
energies = np.array([])
for w in wavelengths:
    energy_j = photon_energy(w)
    energy_ev = Joule_Ev(energy_j)
    energies = np.append(energies, energy_ev)

# Calculating colors for the wavelengths
colors = [w2h(w, intensity) for w in wavelengths]

#Plotting the hydrogen emision spectra: wavelength vs photon energy
plt.scatter(wavelengths, energies, c=colors, marker='x', s=50)

#Plotting lines for hydrogen emission spectra
for w in range(len(wavelengths)):
    plt.axvline(x=wavelengths[w], color=colors[w], linestyle='--', alpha=0.5)

#Graph labels and title
plt.xlabel('Wavelength (nm)')
plt.ylabel('Photon Energy (eV)')
plt.title('Hydrogen Emission Spectra for Visible Light')
plt.show()