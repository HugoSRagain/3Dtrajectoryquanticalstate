import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Supposons que ces tableaux proviennent de votre simulation avec QuTiP :
# t_list : liste des temps
# K_exp, L_exp, A_exp : valeurs d'espérance de K, L, A à chaque instant
# Pour l'exemple, nous générons des données fictives.
t_list = np.linspace(0, 10, 200)
K_exp = 2 + np.sin(t_list)              # Exemple: oscillation pour K
L_exp = 3 + np.cos(t_list/1.5)            # Exemple: oscillation pour L
A_exp = 4 + 0.2 * t_list + np.sin(2*t_list)  # Exemple: croissance linéaire avec oscillation pour A

# Création de la figure 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Tracé de la trajectoire comme une ligne continue
ax.plot(K_exp, L_exp, A_exp, 'b-', lw=2, label='Trajectory')

# Ajout de points colorés selon le temps pour visualiser l'évolution
sc = ax.scatter(K_exp, L_exp, A_exp, c=t_list, cmap='viridis', marker='o')

# Étiquettes et titre en anglais
ax.set_xlabel(r'$\langle K \rangle$')
ax.set_ylabel(r'$\langle L \rangle$')
ax.set_zlabel(r'$\langle A \rangle$')
ax.set_title("3D Trajectory of Expectation Values")

# Barre de couleur indiquant le temps
fig.colorbar(sc, ax=ax, label='Time')

ax.legend()
plt.show()
