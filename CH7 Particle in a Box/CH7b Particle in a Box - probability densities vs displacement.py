#Imports
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from CH7_custom_commands import * 

#Constants
pi = np.pi
e = 1.602176634e-19 #elementary charge in C

#Variables
default_a = 5.29177210903e-11 #Bohr radius in m
default_max_n = 3

#Functions
def psi_squared(n, x, a):
    term1 = 2/a
    term2 = np.sin( (n * pi * x) / a) **2
    return term1 * term2

def plot_graph(a, max_n):
    x = np.linspace(0, a, 1000)
    quantum_numbers = np.arange(1, max_n + 1)
    for n in quantum_numbers:
        plt.plot(x / 1e-10, psi_squared(n, x, a), label=f"n = {n} E = {energy(n, a):.4f} eV")

    #Labels & Titles
    plt.xlabel('Displacement (x) / Å')
    plt.ylabel('Probability Density')
    plt.title('Probability Densities for a Particle in a Box')
    plt.grid(True, linestyle=':', alpha=0.6)

    #Style the legend
    plt.legend(
        loc='upper center', 
        bbox_to_anchor=(0.5, 1), 
        ncols=3,
        fontsize=9,        
        framealpha=0.9    
    )
    plt.tight_layout()

def update_plot(val = None):
    # a = float(slider_a.get()) * 1e-10
    n_max = int(slider_n.get())
    ax.clear()  # Clear the previous plot
    plot_graph(default_a, n_max)
    fig.canvas.draw_idle()

# Setup plot
plt.ion()
fig, ax = plt.subplots(figsize=(6, 4.5))

# Initial plot
plot_graph(default_a, default_max_n)
plt.show(block = False)

# Tkinter Control Window
root = tk.Tk()
root.title("Controls")
root.geometry("300x120")

# Add Tkinter sliders
#slider_a = setup_slider(root, "Box Width (a / Å):", 0.1, 2.0, default_a / 1e-10, 0.01, update_plot)
slider_n = setup_slider(root, "Max Quantum Number (n):", 1, 10, default_max_n, 1, update_plot)

# Keep Tkinter window running
root.mainloop()