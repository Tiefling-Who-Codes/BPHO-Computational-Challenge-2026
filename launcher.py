import customtkinter as ctk
import subprocess
import sys

class AppLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Quantum Mechanics Simulations Launcher")
        self.geometry("600x700")

        self.label = ctk.CTkLabel(self, text="Select a Program", font=("Arial", 20))
        self.label.pack(pady=20)

        # CH1: Random Walk
        self.btn1 = ctk.CTkButton(self, text="Challenge 1: Random Walk", command=lambda: self.run_script("CH1 Random Walk/CH1_Random_Walk.py"))
        self.btn1.pack(pady=10)

        # CH2: Random Walk with Collisions
        self.btn2 = ctk.CTkButton(self, text="Challenge 2: Random Walk with Collisions", command=lambda: self.run_script("CH2 Brownian Motion/CH2_Random_Walk_Collisions.py"))
        self.btn2.pack(pady=10)

        # CH3 Planc Spectrum & Einstein's model of heat capacity
        self.btn3 = ctk.CTkButton(self, text="Challenge 3: Planc Spectrum & Einstein's model of heat capacity", command  =lambda: self.run_script("CH3 Planc Spectrum & Einstein's model of heat capacity/CH3_launcher.py"))
        self.btn3.pack(pady=10)

        # CH4: Photo-Electric Effect
        self.btn4 = ctk.CTkButton(self, text="Challenge 4: Photo-Electric Effect", command=lambda: self.run_script("CH4 Photo-electric effect/CH4_launcher.py"))
        self.btn4.pack(pady=10) 

        # CH5: Hydrogen Emission Spectra
        self.btn5 = ctk.CTkButton(self, text="Challenge 5: Hydrogen Emission Spectra", command=lambda: self.run_script("CH5 Hydrogen Emission Spectra/CH5_launcher.py"))
        self.btn5.pack(pady=10)

        # CH6: Electron Diffraction Rings
        self.btn6 = ctk.CTkButton(self, text="Challenge 6: Electron Diffraction Rings", command=lambda: self.run_script("CH6 Electron Diffraction/CH6_launcher.py"))
        self.btn6.pack(pady=10)

        #CH7a Particle in a Box - Energy Levels
        self.btn7 = ctk.CTkButton(self, text="Challenge 7: Particle in a Box", command=lambda: self.run_script("CH7 Particle in a Box/CH7_launcher.py"))
        self.btn7.pack(pady=10)

        #CH8 Photon Mismatch Calculator
        self.btn8 = ctk.CTkButton(self, text="Challenge 8: Photon Mismatch Calculator", command=lambda: self.run_script("CH8 Photon mismatch calculator/CH8 Photon mismatch calc.py"))
        self.btn8.pack(pady=10)

        #CH9 Compton Scattering
        self.btn9 = ctk.CTkButton(self, text="Challenge 9: Compton Scattering of an X-Ray photon off an electron", command=lambda: self.run_script("CH9 Compton Scattering/CH9_launcher.py"))
        self.btn9.pack(pady=10)

    def run_script(self, script_name):
        # subprocess.Popen runs the script in a NEW window/process
        # This keeps the launcher open while the script runs
        subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()