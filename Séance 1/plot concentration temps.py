import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
R = np.array([1.27, 1.26, 1.24, 1.22, 1.21, 1.21, 1.20, 1.20, 1.19, 1.19, 1.18, 1.18, 1.18, 1.16, 1.17])

def model_exp(t, a, b, c):
    return a * np.exp(-b * t) + c

p0 = [0.1, 0.1, 1.17]

popt, pcov = curve_fit(model_exp, t, R, p0=p0)
a, b, c = popt

residuals = R - model_exp(t, *popt)
r_squared = 1 - (np.sum(residuals**2) / np.sum((R - np.mean(R))**2))

plt.figure(figsize=(10, 6))
plt.scatter(t, R, color='red', label='Données réelles')
t_fine = np.linspace(0, 28, 100)
plt.plot(t_fine, model_exp(t_fine, *popt), label=f'Régression ($R^2={r_squared:.4f}$)', color='blue')

plt.title(r'Modélisation de la synérèse : $R(t) = a \cdot e^{-bt} + c$')
plt.xlabel('Temps (min)')
plt.ylabel('Rayon (mm)')
plt.legend()
plt.grid(True)
plt.show()

print(f"Équation : R(t) = {a:.3f} * exp(-{b:.3f} * t) + {c:.3f}")
