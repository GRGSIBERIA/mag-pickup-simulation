#-*- encoding: utf-8
import numpy as np 
import matplotlib.pyplot as plot
from system.simulation import FieldStrengthOfMagneticMonopole

height = 2.5
x = np.linspace(-125, 125, 500)
wire_points = [np.array([_x, height, 0]) for _x in x]
origin = np.array([0, 0, 0])

total = 0
answers = []
for wire in wire_points:
    fsmm = FieldStrengthOfMagneticMonopole(origin, wire, 1, 1)
    answer = fsmm.computeBw()[0]
    total += answer
    answers.append(answer)
print(total)


plot.plot(x, answers)
plot.xlabel("-> horizontal position [mm]")
plot.ylabel("-> $B_w$")
plot.xlim(-10, 10)
plot.show()
