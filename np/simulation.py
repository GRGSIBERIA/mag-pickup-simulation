#-*- encoding: utf-8
"""
Author: Eiichi Takebuchi(GRGSIBERIA)
"""
import numpy as np 
from scipy import integrate

class FieldStrengthOfMagneticMonopole:
    """
    磁気単極子の磁束密度を求める
    """
    def __init__(self, origin: np.array, target: np.array, _sigma: float, _Psi: float):
        """
        :param origin: 原点
        :param target: 測定点（ワイヤー位置）
        :param _sigma: 電荷密度
        :param _Psi: 測定半径
        """
        self.sigma = _sigma 
        self.Psi = _Psi
        self.xi = np.array([1, 0, 0])
        self.origin = origin 
        self.target = target

    def _phi(self, theta: float) -> np.matrix:
        """
        theta [rad] の回転行列を求める
        """
        return np.matrix((
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]))
    
    def _frac_under_out(self, _d_rho, _d_theta):
        frac_under_in = _d_rho * self.xi * self._phi(_d_theta) + self.target - self.origin
        return np.power(np.linalg.norm(frac_under_in), 2.)

    def _compute_Bz_in(self, _d_rho: float, _d_theta: float):
        """
        磁束密度の内側の式
        """
        frac_under_out = self._frac_under_out(_d_rho, _d_theta)
        frac_upper = self.sigma * (self.target[2] - self.origin[2]) * _d_rho
        return frac_upper / frac_under_out

    def _compute_Bw_in(self, _d_rho: float, _d_theta: float):
        """
        ワイヤ上の磁束密度の内側の式
        """
        frac_under_out = self._frac_under_out(_d_rho, _d_theta)
        frac_upper = self.sigma * _d_rho
        return frac_upper / frac_under_out

    def computeBz(self):
        """
        原点から対象位置にかけて原点X-Y平面の磁束密度を求める
        :return: [0]は値, [1]は推定誤差
        """
        return integrate.nquad(self._compute_Bz_in, [[0, self.Psi], [0, 2. * np.pi]])
    
    def computeBw(self):
        """
        原点から対象位置にかけて原点X-Y平面の磁束密度を求める
        :return: [0]は値, [1]は推定誤差
        """
        return integrate.nquad(self._compute_Bz_in, [[0, self.Psi], [0, 2. * np.pi]])

    def computeBwz(self, _P: np.array, _gamma: float):
        """
        :param _P: ワイヤから誘導された磁場の測定点
        :param _gamma: ワイヤの局所磁場の比例定数
        :return: ワイヤから見たときの磁束密度
        """
        upper = _gamma * self.computeBw()[0] * (self.target[2] - _P[2])
        under = np.power(np.linalg.norm(self.target - _P), 2.)
        return upper / under

if __name__ == "__main__":
    p = np.array([0, 0, 0])
    pd = np.array([2, 2, 2])
    P = np.array([3, 3, 3])
    
    sigma = 5   # 電荷密度
    Psi = 3     # 磁気単極子の半径
    gamma = 1   # 永久磁石で誘導されたワイヤの局所磁場

    fsmm = FieldStrengthOfMagneticMonopole(p, pd, sigma, Psi)

    print(fsmm.computeBwz(P, gamma))
