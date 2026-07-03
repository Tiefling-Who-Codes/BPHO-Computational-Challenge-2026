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

# Planck's Law function
def plancks_law(wavelength, temperature):
    numerator = 2 * h * (c**2)
    e_power = (h * c) / (wavelength * kb * temperature)
    denominator = (wavelength**5) * (np.exp(e_power) - 1)
    # CONVERSION STEPS:
    # 1. Multiply by pi to convert Radiance to Irradiance
    # 2. Divide by 1e9 to convert "per meter" to "per nanometer"
    return ((numerator / denominator) * np.pi) / 1e9

# Plotting
plt.figure(figsize=(10, 6))

max_intensity = 0.0
for T in temperatures_K:
    #intensities = [plancks_law(wavelength, T) for wavelength in wavelengths_m]
    intensities = plancks_law(np.array(wavelengths_m), T)
    max_intensity = max(max_intensity, max(intensities))
    plt.plot(wavelengths_nm, intensities, label=f'T = {T} K')

ax = plt.gca()
plt.title("Planck's Law: Solar Irradiance vs Wavelength")
plt.xlabel('Wavelength / nm')
plt.ylabel('Solar Irradiance / Wm⁻² / nm')
plt.xlim(0, max(wavelengths_nm))
plt.ylim(0, max_intensity * 1.1)
ax.yaxis.set_major_formatter(sf(useMathText=True))
ax.ticklabel_format(style='sci', axis='y', scilimits=(4, 4))
plt.legend()
plt.grid()
plt.show()






