#-*- encoding: utf-8
import theano
import theano.tensor as T 
from integrate import Integrate
import numpy as np

x, y, z = T.dscalars("x", "y", "z")
xd, yd, zd = T.dscalars("x'", "y'", "z'")
px, py, pz = T.dscalars("p_x", "p_y", "p_z")

sigma = T.dscalar("\\sigma")
rho = T.dscalar("\\rho")
phi = T.dscalar("\\phi")
Psi = T.dscalar("\\Psi")

x_distance = (xd - (x - rho * T.cos(phi)))**2
y_distance = (yd - (y - rho * T.sin(phi)))**2
z_distance = (zd - z)**2

Bz_inner_int = (sigma * (zd - z) * rho) / \
    (x_distance + y_distance + z_distance)**(3/2)

Bw_inner_int = (sigma * rho) / \
    (x_distance + y_distance + z_distance)

# 頭にポインタをつけないと引数が展開されない
func_list = [x, y, z, xd, yd, zd, sigma, Psi]
Bz = Integrate(
    Integrate(Bz_inner_int, rho, 0, Psi)(*func_list), 
    phi, 0, 2 * np.pi)(*func_list)

Bw_abs = Integrate(
    Integrate(Bw_inner_int, rho, 0, Psi)(*func_list), 
    phi, 0, 2 * np.pi)(*func_list)
