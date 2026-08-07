import customtkinter as ctk
import subprocess
import sys

class AppLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hydrogenic Orbitals")
        self.geometry("300x200")

        self.label = ctk.CTkLabel(self, text="Select a Program", font=("Arial", 20))
        self.label.pack(pady=20)

        # 2d crossesctions
        self.btn1 = ctk.CTkButton(self, text="2D Cross-section", command=lambda: self.run_script("CH10 Hydrogenic orbitals/CH10 2D slices.py"))
        self.btn1.pack(pady=10)

        # 3d rendering
        self.btn2 = ctk.CTkButton(self, text="3D Render", command=lambda: self.run_script("CH10 Hydrogenic orbitals/CH10 3D visualisation pyVista.py"))
        self.btn2.pack(pady=10)


    def run_script(self, script_name):
        # subprocess.Popen runs the script in a NEW window/process
        # This keeps the launcher open while the script runs
        subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()