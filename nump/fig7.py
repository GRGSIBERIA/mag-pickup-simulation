#-*- encoding: utf-8
import numpy as np

from system.simulation import FieldStrengthOfMagneticMonopole
from figbase import FigBase

class Figure7(FigBase):
    def __init__(self, radius=6.5, _height=2.5):
        super().__init__("csv/Fig7.csv", radius, _height)
        for i, _ in enumerate(self.positions):
            pos = np.array([self.positions[i], 0, self.height + 7.1])
            mag = FieldStrengthOfMagneticMonopole(self.origin, pos, self.sigma, self.psi)
            self.bws.append(mag.computeBw()[0])
        self.xlabel = "-> Horizontal displacement from top of magnet [mm]"

fig = Figure7()
fig.showCompareBw()
fig.printSigma()
