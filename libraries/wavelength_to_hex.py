#outsourced this code from https://www.eureca.de/5116-1-Bruton-color-mapping.html
import math
def wavelength_to_hex_bruton(wavelength, intensity, gamma=0.8):
    #  Approximates the screen color of a wavelength (380–780 nm) with brightness based on the sensor signal.
    #  Parameters:
    #    wavelength : float : Wavelength in nm
    #    intensity  : float : Sensor signal (0–65536)
    #    gamma      : float : Gamma correction (standard 0.8)
    #   
    #    Returns:
    #    str : RGB-Hex string as e.g. '#rrggbb'
    import math
    # --- Bruton Color assignment ---
    if wavelength < 380 or wavelength > 780:
        R = G = B = 0.0
    elif 380 <= wavelength < 440:
        R = -(wavelength - 440) / (440 - 380)
        G = 0.0
        B = 1.0
    elif 440 <= wavelength < 490:
        R = 0.0
        G = (wavelength - 440) / (490 - 440)
        B = 1.0
    elif 490 <= wavelength < 510:
        R = 0.0
        G = 1.0
        B = -(wavelength - 510) / (510 - 490)
    elif 510 <= wavelength < 580:
        R = (wavelength - 510) / (580 - 510)
        G = 1.0
        B = 0.0
    elif 580 <= wavelength < 645:
        R = 1.0
        G = -(wavelength - 645) / (645 - 580)
        B = 0.0
    else:  # 645–780
        R = 1.0
        G = 0.0
        B = 0.0

    # --- Intensity correction at the spectrum edges ---
    if 380 <= wavelength < 420:
        factor = 0.3 + 0.7*(wavelength - 380)/(420 - 380)
    elif 420 <= wavelength < 701:
        factor = 1.0
    elif 701 <= wavelength <= 780:
        factor = 0.3 + 0.7*(780 - wavelength)/(780 - 700)
    else:
        factor = 0.0

    # --- Logarithmic brightness scale ---
    # Minimum value 1, to avoid log(0) 
    intensity = max(intensity, 1)
    brightness = math.log(intensity) / math.log(65536)  # 0..1
    brightness *= factor  # Factor from Bruton correction

    # --- Gamma correction und 0–255 scaling ---
    def adjust(c):
        return int(round((c * brightness) ** gamma * 255))

    r, g, b = adjust(R), adjust(G), adjust(B)
    return f'#{r:02x}{g:02x}{b:02x}'