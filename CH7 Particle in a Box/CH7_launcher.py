import customtkinter as ctk
import subprocess
import sys

class AppLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Particle in a Box")
        self.geometry("275x175")

        self.label = ctk.CTkLabel(self, text="Select a Program", font=("Arial", 20))
        self.label.pack(pady=20)

        #CH7a Particle in a Box - Energy Levels
        self.btn1 = ctk.CTkButton(self, text="Energy Levels", command=lambda: self.run_script("CH7 Particle in a Box/CH7a Particle in a Box - Energy Levels.py"))
        self.btn1.pack(pady=10)

        #CH7b Particle in a Box - Probability Densities vs Displacement
        self.btn2 = ctk.CTkButton(self, text="Probability Densities vs Displacement", command=lambda: self.run_script("CH7 Particle in a Box/CH7b Particle in a Box - probability densities vs displacement.py"))
        self.btn2.pack(pady=10)

    def run_script(self, script_name):
        # subprocess.Popen runs the script in a NEW window/process
        # This keeps the launcher open while the script runs
        subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()