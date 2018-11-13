-#-*- encoding: utf-8
import numpy as np 
import matplotlib.pyplot as plot
from system.simulation import FieldStrengthOfMagneticMonopole

width_min = -25
width_max = 25
width_split = 100

width = np.linspace(width_min,width_max,width_split)
answers = []
for i in range(len(width)):
    height = width[i]
    x = np.linspace(4, 94, 128)
    wire_points = [np.array([_x, height, 0]) for _x in x]
    origin = np.array([0, 0, 0])
    
    total = 0

    for wire in wire_points:
        fsmm = FieldStrengthOfMagneticMonopole(origin, wire, 1, 1)
        answer = fsmm.computeBw()[0]
        total += answer
    answers.append(total)

dphi = []
for i in range(len(answers)-1):
    dphi.append((answers[i]-answers[i+1])/(width[i]-width[i+1]))
dphi.append(0)
plot.plot(width, answers)
plot.plot(width,dphi)
plot.xlabel("-> horizontal position [mm]")
plot.ylabel("-> $B_w$")
plot.xlim(-25, 25)
plot.show()