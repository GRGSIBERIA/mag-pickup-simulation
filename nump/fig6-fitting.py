#-*- encoding: utf-8
import numpy as np
import csv
from system.simulation import FieldStrengthOfMagneticMonopole
from figbase import FigBase

bws = []
equ_pos = []
equ_bws = []
relative_err = []
timedB0 = []

class Figure6(FigBase):
    def __init__(self, radius=6.5, _height=2.5):
        super().__init__("csv/Fig6.csv", radius, _height)
        for i, _ in enumerate(self.positions):
            pos = np.array([0, 0, self.positions[i] + self.height])
            mag = FieldStrengthOfMagneticMonopole(self.origin, pos, self.sigma, self.psi)
            self.bws.append(mag.computeBz()[0])
        self.xlabel = "-> Vertical displacement from top of magnet [mm]"
        sigma = np.array(self.original_bws) / np.array(self.bws)
        intSigma = []
        for i in range(len(sigma)):
            num = sigma[0]
            for j in range(i):
                num += sigma[j]
            intSigma.append(num)
                    
        with open("csv/Fig6.csv", "r") as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                equ_pos.append(float(row[0]) * 10)   # 単位がセンチメートル
                equ_bws.append(1/((float(row[0]) * 10)**3))
                i += 1
        amp_bws = max(equ_bws)
        for i in range(len(equ_pos)):
            bws.append(equ_bws[i]/amp_bws)
        for i in range(len(equ_pos)):
            relative_err.append((bws[i]-(self.original_bws[i]/max(self.original_bws)))/self.original_bws[i])
            """
        for i in range(len(relative_err)):
            timedB0.append((self.original_bws[i]/max(self.original_bws))+relative_err[i]*(self.original_bws[i]/max(self.original_bws)))
            """
fig = Figure6(radius=0.00000000000001)
fig.setEquBws(bws)
fig.setEquPos(equ_pos)
fig.setRelativeErr(relative_err)
fig.showComputeBw()
fig.printSigma()
