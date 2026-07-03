# Imports
import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.62607015e-34  # Planck's constant (J·s)
c = 299792458  # Speed of light (m/s)
e = 1.602176634e-19  # Elementary charge (C)

# Work per element / eV
Ag = 4.3
Al = 4.3
Au = 5.1
Cu = 4.7
Sn = 4.4
Pb = 4.3
Tungsten = 4.5
Ni = 4.6
Na = 2.4

# Convert exponent to sci notation
def fmt(val):
    base = val / 1e15
    return f"${base:.2f} \\times 10^{{15}}$"

# Photoelectric effect function
def photoelectric_effect(frequency, work):
    # Convert frequency to energy (E = hf)
    energy = h * frequency
    # Calculate kinetic energy of emitted electron (KE = hf - work function)
    kinetic_energy = energy - work
    return kinetic_energy

# Stopping voltage function
def stopping_voltage(frequency, work):
    term_1 = h / e 
    term_2 = -1 * (work / e)
    return term_1 * frequency + term_2

# Cutoff frequency function
def cutoff_frequency(work):
    return work / h

# Plotting
frequencies = np.linspace(0, 2e15, 1000)  # Frequency range (Hz)
plt.figure(figsize=(10, 6))

Ag_Cutoff = cutoff_frequency(Ag * e)
Ag_Stopping_Voltage = np.array([stopping_voltage(f, Ag * e) for f in frequencies])
plt.plot(frequencies, Ag_Stopping_Voltage, label='Ag', color='red')
plt.axvline(x=Ag_Cutoff, color='red', linestyle='--', alpha=0.7, label=f'Cutoff Frequency (Ag): {fmt(Ag_Cutoff)} Hz')

Al_Cutoff = cutoff_frequency(Al * e)
Al_Stopping_Voltage = np.array([stopping_voltage(f, Al * e) for f in frequencies])
plt.plot(frequencies, Al_Stopping_Voltage, label='Al', color='orange')
plt.axvline(x=Al_Cutoff, color='orange', linestyle='--', alpha=0.7, label=f'Cutoff Frequency (Al): {fmt(Al_Cutoff)} Hz')

Au_Cutoff = cutoff_frequency(Au * e)   
Au_Stopping_Voltage = np.array([stopping_voltage(f, Au * e) for f in frequencies])
plt.plot(frequencies, Au_Stopping_Voltage, label='Au', color='green')
plt.axvline(x=Au_Cutoff, color='green', linestyle='--', alpha=0.7, label=f'Cutoff Frequency (Au): {fmt(Au_Cutoff)} Hz')

Cu_Cutoff = cutoff_frequency(Cu * e)
Cu_Stopping_Voltage = np.array([stopping_voltage(f, Cu * e) for f in frequencies])
plt.plot(frequencies, Cu_Stopping_Voltage, label='Cu', color='blue')
plt.axvline(x=Cu_Cutoff, color='blue', linestyle='--', alpha=0.7, label=f'Cutoff Frequency (Cu): {fmt(Cu_Cutoff)} Hz')

Sn_Cutoff = cutoff_frequency(Sn * e)
Sn_Stopping_Voltage = np.array([stopping_voltage(f, Sn * e) for f in frequencies])
plt.plot(frequencies, Sn_Stopping_Voltage, label='Sn', color='purple')
plt.axvline(x=Sn_Cutoff, color='purple', linestyle='--', alpha=0.7, label=f'Cutoff Frequency (Sn): {fmt(Sn_Cutoff)} Hz')

Pb_Cutoff = cutoff_frequency(Pb * e)
Pb_Stopping_Voltage = np.array([stopping_voltage(f, Pb * e) for f in frequencies])
plt.plot(frequencies, Pb_Stopping_Voltage, label='Pb', color='brown')
plt.axvline(x=Pb_Cutoff, color='brown', linestyle='--', alpha=0.7, label=f'Cutoff Frequency (Pb): {fmt(Pb_Cutoff)} Hz')

Tungsten_Cutoff = cutoff_frequency(Tungsten * e)
Tungsten_Stopping_Voltage = np.array([stopping_voltage(f, Tungsten * e) for f in frequencies])
plt.plot(frequencies, Tungsten_Stopping_Voltage, label='Tungsten', color='black')
plt.axvline(x=Tungsten_Cutoff, color='black', linestyle='--', alpha=0.7, label=f'Cutoff Frequency (Tungsten): {fmt(Tungsten_Cutoff)} Hz')

Ni_Cutoff = cutoff_frequency(Ni * e)
Ni_Stopping_Voltage = np.array([stopping_voltage(f, Ni * e) for f in frequencies])
plt.plot(frequencies, Ni_Stopping_Voltage, label='Ni', color='cyan')
plt.axvline(x=Ni_Cutoff, color='cyan', linestyle='--', alpha=0.7, label=f'Cutoff Frequency (Ni): {fmt(Ni_Cutoff)} Hz')

Na_Cutoff = cutoff_frequency(Na * e)
Na_Stopping_Voltage = np.array([stopping_voltage(f, Na * e) for f in frequencies])
plt.plot(frequencies, Na_Stopping_Voltage, label='Na', color='magenta')
plt.axvline(x=Na_Cutoff, color='magenta', linestyle='--', alpha=0.7, label=f'Cutoff Frequency (Na): {fmt(Na_Cutoff)} Hz')

# Plotting visible light range
visible_frequencies = np.linspace(4e14, 7.5e14, 100)
for f in visible_frequencies:
    plt.axvline(x=f, color='yellow', linestyle='--', alpha=0.3)



# Graph Setup
plt.title("Photoelectric Effect: Stopping Voltage vs Frequency")
plt.xlabel('Frequency / Hz')
plt.ticklabel_format(axis='x', style='sci', useMathText=True) # Use scientific notation for x-axis
plt.ylabel('Stopping Voltage / V')
plt.xlim(0, max(frequencies))
#plt.legend()
# Place the legend outside the plot (top-right corner) and reduce font size
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
plt.tight_layout() # Crucial: Adjust layout so the legend isn't cut off on your screen
plt.grid()
plt.show()
#plt.savefig("Photoelectric_Effect_Stopping_Voltage_vs_Frequency.png")