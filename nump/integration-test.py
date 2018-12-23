from system.simulation import FieldStrengthOfMagneticMonopole

fsmm = FieldStrengthOfMagneticMonopole([0, 0, 0], [0, 0, 1], 1, 1)

print(fsmm.computeBw())