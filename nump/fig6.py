#-*- encoding: utf-8
import numpy as np

from system.simulation import FieldStrengthOfMagneticMonopole
from figbase import FigBase

class Figure6(FigBase):
    def __init__(self, radius=6.5, _height=2.5):
        super().__init__("csv/Fig6.csv", radius, _height)
        for i, _ in enumerate(self.positions):
            pos = np.array([0, 0, self.positions[i] + self.height])
            mag = FieldStrengthOfMagneticMonopole(self.origin, pos, self.sigma, self.psi)
            self.bws.append(mag.computeBw()[0])
        self.xlabel = "-> Vertical displacement from top of magnet [mm]"
    
fig = Figure6()
fig.showCompareBw()
fig.printSigma()
