# Imports
import numpy as np
from numpy import sin, cos
import tkinter as tk
import customtkinter as ctk

#Functions
def prob_classical(theta_deg, phsi_deg):
    theta = np.radians(theta_deg)
    phsi = np.radians(phsi_deg)
    term_1 = cos(theta)**2 * cos(phsi)**2
    term_2 = sin(theta)**2 * sin(phsi)**2
    return 1 - term_1 - term_2

def prob_quantum(theta_deg, phsi_deg):
    theta = np.radians(theta_deg)
    phsi = np.radians(phsi_deg)
    return sin(phsi - theta)**2

def update_function(val = None):
    theta = theta_slider.get()
    phsi = phsi_slider.get()

    theta_label.configure(text = f"Theta Angle ({theta:.1f}°)")
    phsi_label.configure(text = f"Phsi Angle ({phsi:.1f}°)")

    classical_prob = prob_classical(theta, phsi)
    quantum_prob = prob_quantum(theta, phsi)

    classical_output.configure(text = f"{classical_prob:.4f}")
    quantum_output.configure(text = f"{quantum_prob:.4f}")

# App Setup
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("400x500")
app.title("Photon Mismatch Probability Calculator")

#Outputs Frame
outputs_frame = ctk.CTkFrame(master=app)
outputs_frame.pack(pady=20)

# Inputs Frame
inputs_frame = ctk.CTkFrame(master=app)
inputs_frame.pack(pady=20)

# Classical Frame
classical_frame = ctk.CTkFrame(master=outputs_frame)
classical_frame.pack(side="left", padx=15, pady=20)

info_label_classical = ctk.CTkLabel(master=classical_frame, text = "Classical Probability", font = ("Arial", 16), padx=10)
info_label_classical.pack(pady = 10)

classical_output = ctk.CTkLabel(master=classical_frame, text = "", font = ("Arial", 15))
classical_output.pack(pady = 10)

#Quantum Frame
quantum_frame = ctk.CTkFrame(master=outputs_frame)
quantum_frame.pack(side="right", padx=15, pady=20)

info_label_quantum = ctk.CTkLabel(master=quantum_frame, text = "Quantum Probability", font = ("Arial", 16), padx=10)
info_label_quantum.pack(pady = 10)

quantum_output = ctk.CTkLabel(master=quantum_frame, text = "", font = ("Arial", 15))
quantum_output.pack(pady = 10)

# Theta Label
theta_label = ctk.CTkLabel(master=inputs_frame, text = "Theta Angle (°)", font = ("Arial", 16))
theta_label.pack(pady=10)

# Theta Slider
theta_frame = ctk.CTkFrame(master=inputs_frame)
theta_frame.pack(padx=20, pady=15)
theta_slider = ctk.CTkSlider(master=theta_frame, from_=-180, to=180, number_of_steps=360, command=update_function)
theta_slider.pack(padx=20, pady=20)

#Phsi Label
phsi_label = ctk.CTkLabel(master=inputs_frame, text = "Phsi Angle (°)", font = ("Arial", 16))
phsi_label.pack(pady=10)

# Phi Slider
phsi_frame = ctk.CTkFrame(master=inputs_frame)
phsi_frame.pack(padx=20, pady=15)
phsi_slider = ctk.CTkSlider(master=phsi_frame, from_=-180, to=180, number_of_steps=360, command=update_function,)
phsi_slider.pack(padx=20, pady=20)

app.mainloop()