# %%

import numpy as np
from IS_A_T_Calc_2 import IS_A_T_Calc
import matplotlib.pyplot as plt
from matplotlib import cm

# %%
K = .01
tau = 3

ome_vec = np.pi * np.arange(.5,10,.5)
zet_vec = np.arange(0, .90, .05)
ome, zet = np.meshgrid(ome_vec, zet_vec)
A = np.zeros_like(ome)
T = np.zeros_like(ome)

calc = IS_A_T_Calc(tau, K)

# %%

# i = 1
# j = 1
# calc.calculate_zet(ome[j,i], zet[j,i])

# %%

# test_ome = np.pi
# test_zet = .75
# calc.calculate_zet(test_ome, test_zet)

# %%
for j in range(len(zet_vec)): # zet
    for i in range(len(ome_vec)): # ome
        # print(str(j) + ' , ' + str(i))
        # print('start solve')
        A_i, T_i = calc.calculate_zet(ome[j,i], zet[j,i])
        # print('finish solve')
        A[j,i] = A_i
        T[j,i] = T_i

# %%
ax = plt.figure().add_subplot(projection = '3d')
ax.plot_surface(ome, zet, A, cmap = cm.coolwarm, lw=0.5, rstride=1, cstride=1, alpha=0.7)
ax.set(xlim=(0,35), ylim=(0,1), zlim=(0.5,1),
       xlabel=r'$\omega$', ylabel=r'$\zeta$', zlabel='Z')
ax.set_title('A')

ax = plt.figure().add_subplot(projection = '3d')
ax.plot_surface(ome, zet, T, cmap = cm.coolwarm, lw=0.5, rstride=1, cstride=1, alpha=0.7)
ax.set(xlim=(0,35), ylim=(0,1), zlim=(0,5),
       xlabel=r'$\omega$', ylabel=r'$\zeta$', zlabel='Z')
ax.set_title('T')

# %%
