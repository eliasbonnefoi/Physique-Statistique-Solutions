import matplotlib.pyplot as plt
import numpy as np

C = np.array([0, 5, 10, 20, 30, 50])
R = np.array([1.21, 1.16, 1.11, 1.09, 1.11, 1.14])
Conc = np.array([0.1, 0.5, 1, 10]) * 10**(-3)

plt.figure(figsize=(8, 5))
plt.plot(C, R, '+')

plt.title("Rayon de la bille en fonction de la concentration")
plt.xlabel("Concentration en mM")
plt.ylabel("Rayon en mm ")

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
