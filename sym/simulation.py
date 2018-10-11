# -*- encoding: utf-8
"""
Author: Eiichi Takebuchi(GRGSIBERIA)
"""
import sympy as sym
from sympy.vector import CoordSys3D

p = CoordSys3D("p")
pd = CoordSys3D("p'")
P = CoordSys3D("P")

sigma = sym.Symbol("\\sigma")
rho = sym.Symbol("\\rho")
psi = sym.Symbol("\\psi")
Phi = sym.Symbol("\\Phi")
theta = sym.Symbol("\\theta")
gamma = sym.Symbol("\\gamma")

xi = CoordSys3D("\\hat\{x\}")
zi = CoordSys3D("\\hat\{z\}")

phi = sym.Matrix((
    [sym.cos(theta), -sym.sin(theta), 0], 
    [sym.sin(theta), sym.cos(theta), 0],
    [0, 0, 1]))

frac_under = type(rho * xi * phi)
print(frac_under)

