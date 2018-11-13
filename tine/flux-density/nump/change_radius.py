#-*- encoding: utf-8

import matplotlib.pyplot as plot
import numpy as np
from system.simulation import FieldStrengthOfMagneticMonopole

def plotBz(zlength):
    bws = []
    count = 100
    for radius in range(count):
        fsmm = FieldStrengthOfMagneticMonopole(np.array([0, 0, 0]), np.array([0, 0, zlength]), 1, radius)
        bws.append(fsmm.computeBz()[0])
    bws = np.array(bws)

    rads = np.linspace(0, count, count)

    plot.plot(rads, bws, label="Displacement of z-axis on {0} mm".format(zlength))

plotBz(5)
plotBz(10)
plotBz(15)
plotBz(20)
plotBz(25)

plot.xlabel("-> Radius [mm]")
plot.ylabel("-> Relative magnetic flux density [G]")
plot.legend()
plot.show()
