import customtkinter as ctk
import subprocess
import sys

class AppLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Quantum Mechanics Simulations Launcher")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Select a Program", font=("Arial", 20))
        self.label.pack(pady=20)

        # CH1: Random Walk
        self.btn1 = ctk.CTkButton(self, text="Challenge 1: Random Walk", command=lambda: self.run_script("CH1_Random_Walk.py"))
        self.btn1.pack(pady=10)

        # CH2: Random Walk with Collisions
        self.btn2 = ctk.CTkButton(self, text="Challenge 2: Random Walk with Collisions", command=lambda: self.run_script("CH2_Random_Walk_Collisions.py"))
        self.btn2.pack(pady=10)

        # CH3a: Planck's Spectrum
        self.btn3 = ctk.CTkButton(self, text="Challenge 3a: Planck's Spectrum", command  =lambda: self.run_script("CH3-a Planck spectrum.py"))
        self.btn3.pack(pady=10)

        # CH3b: Einstein's Model of Heat Capacity
        self.btn4 = ctk.CTkButton(self, text="Challenge 3b: Einstein's Model of Heat Capacity", command=lambda: self.run_script("CH3-b Einsteins model of the heat capacity C of solids.py"))
        self.btn4.pack(pady=10)

        # CH4: Photo-Electric Effect
        self.btn5 = ctk.CTkButton(self, text="Challenge 4: Photo-Electric Effect", command=lambda: self.run_script("CH4 Photo-Electric Effect.py"))
        self.btn5.pack(pady=10) 

        # CH4 Simulation: Photo-Electric Effect Simulation
        self.btn6 = ctk.CTkButton(self, text="Challenge 4: Photo-Electric Effect Simulation", command=lambda: self.run_script("CH4 Photo-Electric Effect Sim.py"))
        self.btn6.pack(pady=10)



    def run_script(self, script_name):
        # subprocess.Popen runs the script in a NEW window/process
        # This keeps the launcher open while the script runs
        subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()