#-*- encoding: utf-8
import numpy as np
from nump.system.simulation import FieldStrengthOfMagneticMonopole

from nump.fig6 import Figure6

if __name__ == "__main__":
    # p = np.array([0, 0, 0.0])
    # pd = np.array([15, 0, 7.1])
    # P = np.array([2, 2, 2])
    
    # sigma = 1   # 電荷密度
    # Psi = 6.5     # 磁気単極子の半径
    # gamma = 1   # 永久磁石で誘導されたワイヤの局所磁場

    # fsmm = FieldStrengthOfMagneticMonopole(p, pd, sigma, Psi)

    # print(fsmm.computeBwz(P, gamma))
    instance = Figure6()
    