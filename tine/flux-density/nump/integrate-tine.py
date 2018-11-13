#-*- encoding: utf-8
import numpy as np 
import matplotlib.pyplot as plot
from system.simulation import FieldStrengthOfMagneticMonopole

height = 4
x = np.linspace(height, 90, 100)
width = 0
wire_points = [np.array([width, 0, height + _x]) for _x in x]
origin = np.array([0, 0, 0])

total = 0
answers = []
for wire in wire_points:
    print(wire)
    fsmm = FieldStrengthOfMagneticMonopole(origin, wire, 1, 1)
    answer = fsmm.computeBw()[0]
    total += answer
    answers.append(answer)
print(total)


plot.plot(x, answers)
plot.xlabel("-> horizontal position [mm]")
plot.ylabel("-> $B_w$")
plot.xlim(0, 94)
plot.show()
