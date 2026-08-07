# Imports
from CH10_math import *
import customtkinter as ctk
import pyvista as pv

# Constants

# Variables
n = 3
l = 0
m = 0

# Create a 3D grid structure
grid = pv.ImageData()
grid_res = 50
grid.dimensions = (grid_res, grid_res, grid_res)  # Number of points along X, Y, Z
grid.origin = (-15, -15, -15)   # Lower corner
grid.spacing = (0.6, 0.6, 0.6)   # Distance between points

cord_res = 50
x = np.linspace(-15, 15, cord_res)
z = np.linspace(-15, 15, cord_res)
y = np.linspace(-15, 15, cord_res)

x_cords, y_cords, z_cords = np.meshgrid(x, y, z)

# Functions
def plot_graph(x, y, z, n, l, m):
    densities = prob_density(x, y, z, n, l, m)
    grid.point_data["density"] = densities.flatten(order="F")

    # Extract surfaces at 20% and 60% of peak density
    max_val = densities.max()
    contours = grid.contour(isosurfaces=[max_val * 0.1, max_val * 0.5], scalars="density")

    plotter = pv.Plotter()
    plotter.add_mesh(contours, cmap="inferno", opacity=[0, 0.9], scalar_bar_args={'title': 'Probability Density', 'vertical': True, 'position_x': 0.85}, smooth_shading=True)
    plotter.add_title( f"Hydrogenic Orbital (n={n}, l={l}, m={m})", font_size=16, color="black")
    plotter.show_grid()
    plotter.show(interactive_update=True)
 
    

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
    global x_cords, y_cords, z_cords
    new_n = int(round(n_slider.get()))
    new_l = int(round(l_slider.get()))
    new_m = int(round(m_slider.get()))

    # Fix slider vals
    new_max_l = new_n - 1
    l_slider.configure(to=new_max_l, number_of_steps=new_max_l if new_max_l > 0 else 1)

    if new_l >= new_n:
        new_l = 1
        l_slider.set(new_l)

    m_slider.configure(from_=-new_l, to=new_l, number_of_steps=2 * new_l if new_l > 0 else 1)
    if abs(new_m) > new_l:
        new_m = 0
        m_slider.set(new_m)

    n_label.configure(text=f'n = {new_n}')
    l_label.configure(text=f'l = {new_l}')
    m_label.configure(text=f'm = {new_m}')
    plot_graph(x_cords, y_cords, z_cords, new_n, new_l, new_m)

# Setup plot
plot_graph(x_cords, y_cords, z_cords, n, l, m)

# Interactive Window Setup
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("400x550")
app.title("Variable Controller")

# Sliders
n_frame, n_label, n_slider = setup_slider(app, f'n = {n}', min=1, max=5, default=n, res=4, func=update_plot)
l_frame, l_label, l_slider = setup_slider(app, f'l = {l}', min=0, max=4, default=l, res=1, func=update_plot)
m_frame, m_label, m_slider = setup_slider(app, f'm = {m}', min=-4, max=4, default=m, res=1, func=update_plot)

app.mainloop()


