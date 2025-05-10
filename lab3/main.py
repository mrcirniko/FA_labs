import numpy as np
from scipy.integrate import quad

def f(x):
    if x < 1/3:
        return 2 * np.cos(8 * x) - x**2
    else:
        return 2 * np.cos(8 * x) + 2 - x**2

def F_ac_prime(x):
    return np.exp(x) + 3 * x**2

def integrand(x):
    return f(x) * F_ac_prime(x)

I_continuous, _ = quad(integrand, -8, 25)

f_minus1 = 2 * np.cos(8) - 1
f_2 = 2 * np.cos(16) - 2
I_atoms = 2 * f_minus1 + 2 * f_2

I_total = I_continuous + I_atoms

print(f"{I_total:.6f}")