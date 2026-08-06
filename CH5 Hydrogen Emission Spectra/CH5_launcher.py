import customtkinter as ctk
import subprocess
import sys

class AppLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hydrogen Emission Spectra")
        self.geometry("350x200")

        self.label = ctk.CTkLabel(self, text="Select a Program", font=("Arial", 20))
        self.label.pack(pady=20)

        # Hydrogen Emission Spectra
        self.btn1 = ctk.CTkButton(self, text="Hydrogen Emission Spectra", command=lambda: self.run_script("CH5 Hydrogen Emission Spectra/CH5 Hydrogen Emission Spectra.py"))
        self.btn1.pack(pady=10)

        # Hydrogen Emission Spectra for Visible Light
        self.btn2 = ctk.CTkButton(self, text="Hydrogen Emission Spectra for Visible Light", command=lambda: self.run_script("CH5 Hydrogen Emission Spectra/CH5 Hydrogen Emission Spectra for Visible Light.py"))
        self.btn2.pack(pady=10)

    def run_script(self, script_name):
        # subprocess.Popen runs the script in a NEW window/process
        # This keeps the launcher open while the script runs
        subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()