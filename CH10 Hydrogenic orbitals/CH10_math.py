# Imports
import numpy as np
import math
import scipy.special as scp
from numpy import sin, cos, tan, arcsin, arccos, arctan

# Functions
def cart_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    r_safe = np.where(r == 0, 1e-10, r)
    theta = np.arccos(z / r_safe)
    phi = np.arctan2(y, x)
    return r, theta, phi

def normalisation(n, l):
    term1 = (2 / n) ** 3
    term2 = math.factorial(n - l - 1)
    term3 = (2 * n) * (math.factorial(n + l) ** 3)
    return np.sqrt(term1 * (term2 / term3))

def radial_nodes(p, n, l):
    degree = n - l -1
    order = (2 * l) + 1
    return scp.assoc_laguerre(p, degree, order)

def radial_wave_func(n, l, r):
    p = (2 * r) / n # Scaled distance (charge Z = 1, Bhor radius = 1)
    term1 = normalisation(n, l)
    term2 = p ** l
    term3 = radial_nodes(p, n, l)
    term4 = np.exp(-p / 2)
    return term1 * term2 * term3 * term4

def prob_density(x, y, z, n, l, m):
    r, theta, phi = cart_to_spherical(x, y, z)
    radial = radial_wave_func(n, l, r)
    angular = scp.sph_harm_y(l, m, theta, phi)
    psi = radial * angular
    return np.abs(psi)**2

