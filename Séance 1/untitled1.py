import numpy as np
import matplotlib.pyplot as plt

t = np.array([0, 5, 10])
R = np.array([1.207, 1.122, 1.205]) * 10**(-3)

plt.scatter(t, R, color='red')

plt.title('Évolution du rayon de la bille en fonction du temps')
plt.xlabel('Temps (min)')
plt.ylabel('Rayon (m)')
plt.legend()
plt.grid(True)
plt.show()
