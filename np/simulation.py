import numpy as np 
from scipy import integrate

p = pd = P = np.array([0, 0, 0])
xi = np.array([1, 0, 0])

def phi(theta):
    return np.matrix((
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]))

sigma = 0
rho = 1
Psi = 1

class FieldStrengthOfMagneticMonopole:
    @classmethod
    def compute_Bz(cls, p: np.array, pd: np.array, rho: float, Psi: float):
        frac_under = rho * xi * phi(Psi) + pd - p
        frac_under = np.power(np.linalg.norm(frac_under), 2.)
        return (sigma * (pd[2] - p[2]) * rho) / frac_under

    @classmethod 
    def compute_Bw(cls, p: np.array, pd: np.array, rho: float, Psi: float):
        pass 
