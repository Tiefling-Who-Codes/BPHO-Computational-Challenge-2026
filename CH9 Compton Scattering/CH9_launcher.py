import customtkinter as ctk
import subprocess
import sys

class AppLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Compton Scattering of an X-Ray photon off an electron")
        self.geometry("475x250")

        self.label = ctk.CTkLabel(self, text="Select a Program", font=("Arial", 20))
        self.label.pack(pady=20)

        # CH9a Fractional Wavelength Shift vs Photon Scattering Angle.py
        self.btn1 = ctk.CTkButton(self, text="Fractional Wavelength Shift vs Photon Scattering Angle", command=lambda: self.run_script("CH9 Compton Scattering/CH9a Fractional Wavelength Shift vs Photon Scattering Angle.py"))
        self.btn1.pack(pady=10)

        # CH9b Electron Recoil Speed vs Photon Scattering Angle.py
        self.btn2 = ctk.CTkButton(self, text="Electron Recoil Speed vs Photon Scattering Angle", command=lambda: self.run_script("CH9 Compton Scattering/CH9b Electron Recoil Speed vs Photon Scattering Angle.py"))
        self.btn2.pack(pady=10)

        # CH9c Electron Recoil Angle vs Photon Scattering Angle.py
        self.btn3 = ctk.CTkButton(self, text="Electron Recoil Angle vs Photon Scattering Angle", command  =lambda: self.run_script("CH9 Compton Scattering/CH9c Electron Recoil Angle vs Photon Scattering Angle.py"))
        self.btn3.pack(pady=10)


    def run_script(self, script_name):
        # subprocess.Popen runs the script in a NEW window/process
        # This keeps the launcher open while the script runs
        subprocess.Popen([sys.executable, script_name])

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()