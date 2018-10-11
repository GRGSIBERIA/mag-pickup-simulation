# -*- encoding: utf-8
"""
Author: Eiichi Takebuchi(GRGSIBERIA)
"""
import sympy as sym
import numpy as np

px, py, pz = sym.symbols("p_x p_y p_z")
pdx, pdy, pdz = sym.symbols("p'_x p'_y p'_z")
Px, Py, Pz = sym.symbols("P_x P_y P_z")

p = sym.Matrix([[px, py, pz]])
pd = sym.Matrix([[pdx, pdy, pdz]])
P = sym.Matrix([[Px, Py, Pz]])

sigma = sym.Symbol("\\sigma")
rho = sym.Symbol("\\rho")
psi = sym.Symbol("\\psi")
Phi = sym.Symbol("\\Phi")
theta = sym.Symbol("\\theta")
gamma = sym.Symbol("\\gamma")

xi = sym.Matrix([[1, 0, 0]])

phi = sym.Matrix((
    [sym.cos(theta), -sym.sin(theta), 0], 
    [sym.sin(theta), sym.cos(theta), 0],
    [0, 0, 1]))

func_under = (rho * xi * phi + pd + (-p)).norm()**2.
Bz = (sigma * (pdz - pz) * rho) / func_under

sym.integrate(sym.integrate(Bz, (rho, 0, psi)), (theta, 0, 2. * np.pi))
