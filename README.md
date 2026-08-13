# BPHO Computational Challenge 2026: Quantum Mechanics

Hey! You should read this first... :D

Hello fellow programmer or physicist!  
Or both!  
Or neither!

My name is **Adrian D'Costa**, and I made this project!

If you want to use it... go ahead! I made it for the **BPHO Computational Challenge 2026**, but if you like it... feel free to use it! Just give me credit.

---

## Challenge Video
Check out the full video walkthrough here:  
** [Watch on YouTube](https://www.youtube.com/watch?v=oEvkfLqGpjI)**

---

## Credits & External Libraries

`wavelength_to_hex.py` is an external library I imported. Credits go to **[eureca.de](https://www.eureca.de/5116-1-Bruton-color-mapping.html)**.

I made use of it as the `w2h` function, which I imported and used in **Challenge 5: Hydrogen Emission Spectra (Visible Light)**:
* It converts calculated wavelengths into exact hex colours for the emission lines.
* The function takes two inputs: **wavelength** (calculated) and **intensity** (set to 3000); and outputs a hex colour corresponding to the wavelength.

Check out their website for more details on how this function works!

---

## Notes on AI Usage

AI was used in moderation for my convenience and to help me understand some concepts:
* **What AI was used for:** Looking up specific syntax/commands and clarifying physics/programming concepts.
* **What AI was not used for:** AI was **NOT** used to generate any code for any of the challenges. All code in this project is my own work.

---

## How to Run the App

I designed a custom launcher using **CustomTkinter**. To run the project:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Tiefling-Who-Codes/BPHO-Computational-Challenge-2026.git
   cd BPHO-Computational-Challenge-2026
2. Ensure you have Python 3 installed along with the required dependencies:
   ```bash
   pip install customtkinter tkinter matplotlib pyvista numpy scipy
3. Run the main launcher:
  ```bash
  python launcher.py
