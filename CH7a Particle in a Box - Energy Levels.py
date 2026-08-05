# Imports
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from CH7_custom_commands import *

# Variables
n_max_default = 3
x_fit = np.linspace(0, 3, 100)
a_default = 5.29177210903e-11  # Bohr radius in m

def plot_graph(n_max, x_fit, a):
    # Create an array n values from 0 to n_max
    n = np.arange(0, n_max + 1)

    # Plot quantum energy states
    ax.scatter(n, energy(n, a))

    # Plot line of best fit (*curve of best fit)
    ax.plot(x_fit, energy(x_fit, a), linestyle='--')

    # Labels & Title
    ax.set_xlabel('Quantum Number (n)')
    ax.set_ylabel('Energy (eV)')
    ax.set_title('Energy Levels for a Particle in a Box')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()

def update_plot(val = None):
    a_angstrom = float(slider_a.get())
    n_max = int(slider_n.get())
    current_a = a_angstrom * 1e-10  # Convert Å to meters
    x_fit = np.linspace(0, n_max, 100)  # Update x_fit based on n_max
    ax.clear()  # Clear the previous plot
    plot_graph(n_max, x_fit, current_a)
    fig.canvas.draw_idle()

# Setup plot
plt.ion()
fig, ax = plt.subplots(figsize=(6, 4.5))

# Initial plot
plot_graph(n_max_default, x_fit, a_default)
plt.show(block = False)

# Tkinter Control Window
root = tk.Tk()
root.title("Controls")
root.geometry("300x120")

# Add Tkinter sliders
slider_a = setup_slider(root, "Box Width (a / Å):", 0.1, 2.0, a_default / 1e-10, 0.01, update_plot)
slider_n = setup_slider(root, "Max Quantum Number (n):", 1, 10, n_max_default, 1, update_plot)

# Keep Tkinter window running
root.mainloop()