# Imports
from CH10_math import *
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import tkinter as tk
import customtkinter as ctk

# Constants

# Variables
n = 3
l = 1
m = 1
x = np.linspace(-10, 10, 300)
z = np.linspace(-10, 10, 300)
x_cords, z_cords = np.meshgrid(x, z)
y = 0

# Functions
def plot_graph(x, y, z, n, l, m):
    densities = prob_density(x, y, z, n, l, m)
    ax.scatter(x.flatten(), z.flatten(), c=densities, cmap='inferno', s=1)
    ax.set_title('Hydrogenic orbitals')

def setup_slider(parent, label_text, min, max, default, res, func):
    frame = ctk.CTkFrame(master=parent)
    frame.pack(padx=20, pady=15)
    label = ctk.CTkLabel(master=frame, text = label_text, font = ("Arial", 16))
    label.pack(padx=20, pady=15)
    slider = ctk.CTkSlider(master=frame, from_=min, to=max, number_of_steps=res, command=func)
    slider.set(default)
    slider.pack(padx=20, pady=15)
    return frame, label, slider

def update_plot(val = None):
    global x_cords, z_cords
    new_n = int(round(n_slider.get()))
    new_l = int(round(l_slider.get()))
    new_m = int(round(m_slider.get()))
    new_y = float(y_slider.get())

    # Fix slider vals
    new_max_l = new_n - 1
    l_slider.configure(to=new_max_l, number_of_steps=new_max_l if new_max_l > 0 else 1)

    if new_l >= new_n:
        new_l = new_n - 1
        l_slider.set(new_l)

    m_slider.configure(from_=-new_l, to=new_l, number_of_steps=2 * new_l if new_l > 0 else 1)
    if abs(new_m) > new_l:
        new_m = 0
        m_slider.set(new_m)

    n_label.configure(text=f'n = {new_n}')
    l_label.configure(text=f'l = {new_l}')
    m_label.configure(text=f'm = {new_m}')
    y_label.configure(text=f'y = {new_y}')

    ax.clear()  # Clear the previous plot
    plot_graph(x_cords, new_y, z_cords, new_n, new_l, new_m)
    fig.canvas.draw_idle()

# Setup plot
plt.ion()
fig, ax = plt.subplots(figsize=(6, 4.5))
plot_graph(x_cords, y, z_cords, n, l, m)
plt.show()

# Interactive Window Setup
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("400x550")
app.title("Variable Controller")

# Sliders
n_frame, n_label, n_slider = setup_slider(app, f'n = {n}', min=1, max=5, default=n, res=4, func=update_plot)
l_frame, l_label, l_slider = setup_slider(app, f'l = {l}', min=0, max=4, default=l, res=1, func=update_plot)
m_frame, m_label, m_slider = setup_slider(app, f'm = {m}', min=-4, max=4, default=m, res=1, func=update_plot)
y_frame, y_label, y_slider = setup_slider(app, f'y = {y}', min=-15, max=15, default=y, res=30, func=update_plot)

app.mainloop()


