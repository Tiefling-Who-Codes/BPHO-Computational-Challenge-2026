# Imports
from CH9_maths import *
import matplotlib.pyplot as plt

# Variables
energies = np.array([50, 100, 200, 500, 1000]) #keV
energies_J = keV_to_J(energies)
angles = np.linspace(0, 180, 1000)

# Plot Graph
i = 0
for energy in energies_J:
    plt.plot(angles, fractional_wavelength_shift(energy, angles), label=f'E={energies[i]}keV')
    i += 1

# Lables and title
plt.xlabel('Photon Scattering Angle (θ) /deg')
plt.ylabel('Fractional Wavelength Shift (Δλ/λ)')
plt.title('Fractional Wavelength Shift vs Photon Scattering Angle')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()
