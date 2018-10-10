# -*- encoding: utf-8
"""
Author: Eiichi Takebuchi(GRGSIBERIA)
"""
import sympy as sym
x = sym.Symbol("x")
y = sym.Symbol("y")
z = sym.Symbol("z")
xd = sym.Symbol("x'")
yd = sym.Symbol("y'")
zd = sym.Symbol("z'")
x_p = sym.Symbol("x_\\rho")
y_p = sym.Symbol("y_\\rho")
z_p = sym.Symbol("z_\\rho")

sigma = sym.Symbol("\\sigma")
rho = sym.Symbol("\\rho")
psi = sym.Symbol("\\psi")
Phi = sym.Symbol("\\Phi")
gamma = sym.Symbol("\\gamma")

# B_z = sym.integrate(sym.integrate(
#     (sigma * (zd - z) * rho) /
#     (((xd - (x - rho * sym.cos(Phi)))**2 + (yd - (y - rho * sym.sin(Phi)))**2 + (zd - z)**2)**(3/2))
#     , (rho, 0, psi)), (Phi, 0, 2 * sym.pi))

#print("compiled B_z")

abs_B_w = sym.integrate(sym.integrate(
    (sigma * rho) /
    ((xd - (x - rho * sym.cos(Phi)))**2 + (yd - (y - rho * sym.sin(Phi)))**2 + (zd - z)**2)
    , (rho, 0, psi)), (Phi, 0, 2 * sym.pi))

print("compiled |B_w|")

B_wz = gamma * abs_B_w * (zd - z_p) / ((xd - x_p)**2 + (yd - y_p)**2 + (zd - z_p)**2)**(3/2)

print("compiled B_wz")
