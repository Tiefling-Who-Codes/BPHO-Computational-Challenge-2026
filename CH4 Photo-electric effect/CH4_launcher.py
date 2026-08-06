import customtkinter as ctk
import subprocess
import sys

class AppLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Photo-Electric Effect")
        self.geometry("300x200")

        self.label = ctk.CTkLabel(self, text="Select a Program", font=("Arial", 20))
        self.label.pack(pady=20)

        # CH4: Photo-Electric Effect
        self.btn4 = ctk.CTkButton(self, text="Photo-Electric Effect Plot", command=lambda: self.run_script("CH4 Photo-Electric Effect/CH4 Photo-Electric Effect.py"))
        self.btn4.pack(pady=10) 

        # CH4 Simulation: Photo-Electric Effect Simulation
        self.btn5 = ctk.CTkButton(self, text="Photo-Electric Effect Simulation", command=lambda: self.run_script("CH4 Photo-Electric Effect/CH4 Photo-Electric Effect Sim.py"))
        self.btn5.pack(pady=10)

    def run_script(self, script_name):
        # subprocess.Popen runs the script in a NEW window/process
        # This keeps the launcher open while the script runs
        subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()