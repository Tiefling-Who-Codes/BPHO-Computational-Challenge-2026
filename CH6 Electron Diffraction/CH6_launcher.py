import customtkinter as ctk
import subprocess
import sys

class AppLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Electron Diffraction Rings")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Select a Program", font=("Arial", 20))
        self.label.pack(pady=20)

        # Electron Diffraction Rings (d = 0.123 nm)
        self.btn1 = ctk.CTkButton(self, text="Electron Diffraction Rings (d = 0.123 nm)", command=lambda: self.run_script("CH6 Electron Diffraction/CH6 Electron Diffraction (d = 0.123 nm).py"))
        self.btn1.pack(pady=10)

        # CH6a: Electron Diffraction Model Check (d = 0.123 nm)
        self.btn2 = ctk.CTkButton(self, text="Electron Diffraction Model Check (d = 0.123 nm)", command=lambda: self.run_script("CH6 Electron Diffraction/CH6a Electron Diffraction Check (d = 0.123 nm).py"))
        self.btn2.pack(pady=10)

        # Electron Diffraction Rings (d = 0.213 nm)
        self.btn3 = ctk.CTkButton(self, text="Electron Diffraction Rings (d = 0.213 nm)", command=lambda: self.run_script("CH6 Electron Diffraction/CH6 Electron Diffraction (d = 0.213 nm).py"))
        self.btn3.pack(pady=10)

        # CH6a: Electron Diffraction Model Check (d = 0.213 nm)
        self.btn4 = ctk.CTkButton(self, text="Electron Diffraction Model Check (d = 0.213 nm)", command=lambda: self.run_script("CH6 Electron Diffraction/CH6a Electron Diffraction Check (d = 0.213 nm).py"))
        self.btn4.pack(pady=10)

    def run_script(self, script_name):
        # subprocess.Popen runs the script in a NEW window/process
        # This keeps the launcher open while the script runs
        subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()