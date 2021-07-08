#-*- encoding: utf-8

import matplotlib.pyplot as plot
import numpy as np
from system.simulation import FieldStrengthOfMagneticMonopole

def plotBz(divpi, xpos, radius):
    bws = []

    vec = np.array([0, xpos, 0])
    itheta = np.pi / 2. / (divpi-1)
    
    count = divpi
    for _i in range(count):
        theta = itheta * _i
        rot = np.matrix((
            [1, 0, 0], 
            [0, np.cos(theta), -np.sin(theta)], 
            [0, np.sin(theta), np.cos(theta)]))
        vector = -np.ravel(vec * rot)
        print(vector)
        fsmm = FieldStrengthOfMagneticMonopole(np.array([0, 0, 0]), vector, 1, radius)
        bws.append(fsmm.computeBz()[0])
    bws = np.array(bws)

    rads = np.linspace(0, np.pi / 2., count)

    plot.plot(rads, bws)

for i in range(10):
    plotBz(10, i+1, 0.00000000000001)

plot.xlabel("-> Radian [rad]")
plot.ylabel("-> Relative magnetic flux density [G]")
plot.show()
