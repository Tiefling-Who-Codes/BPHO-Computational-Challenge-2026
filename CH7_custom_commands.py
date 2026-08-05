# Imports
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# Constants
pi = np.pi 
h = 6.62607015e-34       # Planck's constant in J*s
h_bar = h / (2 * pi)     # Reduced Planck's constant in J*s
me = 9.10938356e-31      # Electron mass in kg
a = 5.29177210903e-11    # Bohr radius in m
e = 1.602176634e-19      # Elementary charge in C

# Variables
n = np.array([0, 1, 2, 3]) # Quantum numbers
smooth_x_axis = np.linspace(0, 3, 100) # Generate continuous points for the line of best fit

# Functions
def energy(n, a):
    numerator = h_bar**2 * pi**2 * n**2
    denominator = 2 * me * a**2
    return (numerator / denominator) * 6.242e+18

def setup_slider(parent, label_text, min_val, max_val, default_val, res, update_fn):
    # label
    lbl = tk.Label(parent, text=label_text)
    lbl.pack(pady=(10, 0))
    
    # slider
    slider = tk.Scale(
        parent,
        from_=min_val,
        to=max_val,
        resolution=res,
        orient='horizontal',
        command=update_fn
    )
    slider.set(default_val)
    slider.pack(fill='x', padx=20)
    
    return slider