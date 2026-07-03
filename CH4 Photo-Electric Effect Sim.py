# Imports
import numpy as np
import turtle 
from time import sleep
import tkinter as tk
screen = turtle.Screen()

# Constants
h = 6.62607015e-34  # Planck's constant (J·s)
c = 299792458  # Speed of light (m/s)
e = 1.602176634e-19  # Elementary charge (C)
max_steps = 20
max_energy = 6.557176554738e-17  
scale = max_steps / max_energy
# Work per element / eV
work = {
    "Ag": 4.3,
    "Al": 4.3,
    "Au": 5.1, 
    "Cu": 4.7,
    "Sn": 4.4,
    "Pb": 4.3,
    "W" : 4.5,
    "Ni": 4.6,
    "Na": 2.4
}

# Variables
light_intensity = 10
metal = "Ag"
light_frequency = 1e15
voltage = 0
particles = []
spawn_counter = 0
spawn_interval = 3
current_cutoff_frequency= 0
current_stopping_voltage = 0
current_work = 0

# Photoelectric effect function
def photoelectric_effect(frequency, work):
    # Convert frequency to energy (E = hf)
    energy = h * frequency
    # Calculate kinetic energy of emitted electron (KE = hf - work function)
    kinetic_energy = energy - work
    # max ke is 6.557176554738e-17
    return kinetic_energy

# Stopping voltage function
def stopping_voltage(frequency, work):
    term_1 = h / e 
    term_2 = -1 * (work / e)
    return term_1 * frequency + term_2

# Cutoff frequency function
def cutoff_frequency(work):
    return work / h

def create_particle(kinetic_energy):
    if kinetic_energy <= 0:
        return
    # Create a turtle particle with kinetic energy proportional to its speed
    particle = turtle.Turtle()
    particle.hideturtle()
    particle.speed(0)
    particle.shape("circle")
    particle.color("yellow")
    particle.penup()
    particles.append(particle)
    # Position the particle at the cathode
    y = np.random.uniform(-190, 190)  # Random y position within the cathode
    particle.goto(-190, y)
    particle.setheading(0)  # Move to the right (towards the anode)
    #particle.forward(20)  # Move the particle forward to start the simulation
    particle.showturtle()  # Show the particle after setting its initial position and speed

# Create frame for the simulation
frame = turtle.Turtle()
frame.hideturtle()
frame.penup()
frame.goto(-200, -200)
frame.pendown()
for _ in range(4):
    frame.forward(400)
    frame.left(90)

# Create anode and cathode
anode = turtle.Turtle()
anode.shape("square")
anode.shapesize(stretch_wid=20, stretch_len=1)
anode.color("red")
anode.penup()
anode.goto(190, 0)
cathode = turtle.Turtle()
cathode.shape("square")
cathode.shapesize(stretch_wid=20, stretch_len=1)
cathode.color("blue")
cathode.penup()
cathode.goto(-190, 0)

# Create a control panel with sliders for all settings and a metal dropdown

def create_control_panel():
    control_window = tk.Toplevel(screen._root)
    control_window.title("Photoelectric Controls")
    control_window.geometry("1000x1000")
    control_window.resizable(False, False)

    control_frame = tk.Frame(control_window)
    control_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    tk.Label(control_frame, text="Metal:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
    metal_var = tk.StringVar(value=metal)
    def on_metal_select(value):
        global metal
        metal = value
    metal_menu = tk.OptionMenu(control_frame, metal_var, *work.keys(), command=on_metal_select)
    metal_menu.grid(row=0, column=1, sticky="w", padx=5, pady=2)

    tk.Label(control_frame, text="Frequency (Infrared to UV, Hz):").grid(row=1, column=0, sticky="w", padx=5, pady=2)
    frequency_value_label = tk.Label(control_frame, text=f"{light_frequency:.2e} Hz")
    frequency_value_label.grid(row=1, column=1, sticky="w", padx=5, pady=2)
    def on_frequency_slider(value):
        global light_frequency
        light_frequency = 10 ** float(value)
        frequency_value_label.config(text=f"{light_frequency:.2e} Hz")
    frequency_slider = tk.Scale(
        control_frame,
        from_=13,
        to=17,
        resolution=0.01,
        orient=tk.HORIZONTAL,
        length=320,
        command=on_frequency_slider
    )
    frequency_slider.set(np.log10(light_frequency))
    frequency_slider.grid(row=1, column=2, padx=5, pady=2)

    tk.Label(control_frame, text="Intensity (W/m²):").grid(row=2, column=0, sticky="w", padx=5, pady=2)
    intensity_value_label = tk.Label(control_frame, text=f"{light_intensity:.1f}")
    intensity_value_label.grid(row=2, column=1, sticky="w", padx=5, pady=2)
    def on_intensity_slider(value):
        global light_intensity
        light_intensity = float(value)
        intensity_value_label.config(text=f"{light_intensity:.1f}")
    intensity_slider = tk.Scale(
        control_frame,
        from_=0,
        to=100,
        resolution=1,
        orient=tk.HORIZONTAL,
        length=320,
        command=on_intensity_slider
    )
    intensity_slider.set(light_intensity)
    intensity_slider.grid(row=2, column=2, padx=5, pady=2)

    tk.Label(control_frame, text="Voltage (V):").grid(row=3, column=0, sticky="w", padx=5, pady=2)
    voltage_value_label = tk.Label(control_frame, text=f"{voltage:.1f}")
    voltage_value_label.grid(row=3, column=1, sticky="w", padx=5, pady=2)
    def on_voltage_slider(value):
        global voltage
        voltage = float(value)
        voltage_value_label.config(text=f"{voltage:.1f}")
    voltage_slider = tk.Scale(
        control_frame,
        from_=-5,
        to=20,
        resolution=0.1,
        orient=tk.HORIZONTAL,
        length=320,
        command=on_voltage_slider
    )
    voltage_slider.set(voltage)
    voltage_slider.grid(row=3, column=2, padx=5, pady=2)

    return control_window
print(metal)
print(light_frequency)
print(light_intensity)
print(voltage)

    
# Create the control panel
control_window = create_control_panel()

while True:
    turtle.speed(0)

    # Calculate the stopping voltage and cutoff frequency for the current parameters
    current_work = work[metal] * e # Convert work function from eV to J
    #print(current_work)
    current_stopping_voltage = stopping_voltage(light_frequency, current_work)
    current_cutoff_frequency = cutoff_frequency(current_work)
    current_kinetic_energy = photoelectric_effect(light_frequency, current_work)
    print(current_kinetic_energy * scale)

    if current_cutoff_frequency < light_frequency:
            for i in range(int(light_intensity / 10)):  # Spawn particles based on intensity
                create_particle(photoelectric_effect(light_frequency, current_work))

    for particle in particles:
        particle.speed(0)
        #print(current_stopping_voltage)
        #print(voltage)
        if current_stopping_voltage > voltage:  # If the stopping voltage is greater than the applied voltage
            particle.forward(current_kinetic_energy * scale)  # Move the particle forward if the stopping voltage is greater than the applied voltage
        else:
            particle.backward(current_kinetic_energy * scale)  # Move the particle backward if the stopping voltage is greater than or equal to the applied voltage
        # Check for collision with anode
        if particle.xcor() >= 190:  # If the particle reaches the anode
            particle.hideturtle()  # Hide the particle
            particles.remove(particle)  # Remove it from the list of particles
        elif particle.xcor() <= -190:  # If the particle reaches the cathode (should not happen, but just in case)
            particle.hideturtle()  # Hide the particle
            particles.remove(particle)  # Remove it from the list of particles
    screen.update()  # Update the turtle screen
    control_window.update()  # Process Tkinter slider events


    

    

    