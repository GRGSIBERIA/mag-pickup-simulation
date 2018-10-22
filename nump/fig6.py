#-*- encoding: utf-8
import csv
import numpy as np
import matplotlib.pyplot as plot

from system.simulation import FieldStrengthOfMagneticMonopole

class Figure6:
    def __init__(self):
        self.positions = []
        with open("nump/csv/Fig6.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                self.positions.append(float(row[0]) * 10)   # 単位がセンチメートル
        
        self.sigma = 1
        self.Psi = 6.5
        height = 0.25
        origin = np.array([0, 0, height])

        self.bws = []
        for i, _ in enumerate(self.positions):
            pos = np.array([0, 0, self.positions[i] + height])
            mag = FieldStrengthOfMagneticMonopole(origin, pos, self.sigma, self.Psi)
            self.bws.append(mag.computeBw()[0])

        plot.plot(self.positions, self.bws, "o")
        plot.show()

if __name__ == "__main__":
    print(2.7*6.5**2*np.pi*10**22 / 27)
    a = Figure6()