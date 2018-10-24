#-*- encoding: utf-8

import matplotlib.pyplot as plot
import numpy as np
from system.simulation import FieldStrengthOfMagneticMonopole

bws = []
count = 100
for radius in range(count):
    fsmm = FieldStrengthOfMagneticMonopole(np.array([0, 0, 0]), np.array([0, 0, 5]), 1, radius)
    bws.append(fsmm.computeBz()[0])
bws = np.array(bws)

rads = np.linspace(0, count, count)

plot.plot(rads, bws)
plot.xlabel("-> Radius [mm]")
plot.ylabel("-> Relative magnetic flux density [G]")
plot.show()
