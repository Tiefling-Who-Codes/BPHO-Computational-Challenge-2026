import customtkinter as ctk
import subprocess
import sys

class AppLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Planc Spectrum & Einstein's Model of Heat Capacity")
        self.geometry("450x200")

        self.label = ctk.CTkLabel(self, text="Select a Program", font=("Arial", 20))
        self.label.pack(pady=20)

        # CH3a: Planck's Spectrum
        self.btn3 = ctk.CTkButton(self, text="Challenge 3a: Planck's Spectrum", command  =lambda: self.run_script("CH3 Planc Spectrum & Einstein's model of heat capacity/CH3-a Planck spectrum.py"))
        self.btn3.pack(pady=10)

        # CH3b: Einstein's Model of Heat Capacity
        self.btn4 = ctk.CTkButton(self, text="Challenge 3b: Einstein's Model of Heat Capacity", command=lambda: self.run_script("CH3 Planc Spectrum & Einstein's model of heat capacity/CH3-b Einsteins model of the heat capacity C of solids.py"))
        self.btn4.pack(pady=10)

    def run_script(self, script_name):
        # subprocess.Popen runs the script in a NEW window/process
        # This keeps the launcher open while the script runs
        subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()