#-*- encoding: utf-8

import matplotlib.pyplot as plot
import numpy as np
from system.simulation import FieldStrengthOfMagneticMonopole

def plotBz(divpi):
    bws = []

    vec = np.array([0, 1, 0])
    itheta = np.pi / 2. / (divpi-1)
    
    count = divpi
    for i in range(count):
        theta = itheta * i
        rot = np.matrix((
            [1, 0, 0], 
            [0, np.cos(theta), -np.sin(theta)], 
            [0, np.sin(theta), np.cos(theta)]))
        vector = -np.ravel(vec * rot)
        print(vector)
        fsmm = FieldStrengthOfMagneticMonopole(np.array([0, 0, 0]), vector, 1, 1)
        bws.append(fsmm.computeBz()[0])
    bws = np.array(bws)

    rads = np.linspace(0, np.pi / 2., count)

    plot.plot(rads, bws)

plotBz(100)

plot.xlabel("-> Radian [rad]")
plot.ylabel("-> Relative magnetic flux density [G]")
plot.legend()
plot.show()
