import matplotlib.pyplot as plt
import numpy as np

C = np.array([3.5, 6.32, 6.82, 7.44]) * 10**(-3)  # mV
R = np.array([361.66, 227.84, 106.2])
Conc = np.array([0.1, 0.5, 1, 10]) * 10**(-3)

plt.figure(figsize=(8, 5))

a, b = np.polyfit(1 / np.sqrt(Conc), 1 / C, 1)
print(a)

plt.plot(1 / np.sqrt(Conc), 1 / C, '+')
plt.plot(1 / np.sqrt(Conc), a * 1 / np.sqrt(Conc) + b)

plt.title("Inverse de la capacité en fonction de l'inverse de la racine de la concentration")
plt.xlabel("Inverse de sqrt(Concentration)")
plt.ylabel("Inverse capacité (1/F) ")

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
