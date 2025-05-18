import numpy as np
import matplotlib.pyplot as plt

data_al = np.loadtxt('C:\\Users\\todo\\Documents\\Documents cours\\U lille\\simu\\simu barre échauffement\\cas équilibre\\resultats.txt')
data_cui = np.loadtxt('C:\\Users\\todo\\Documents\\Documents cours\\U lille\\simu\\simu barre échauffement\\cas équilibre\\resultats_cuivre.txt')
data_fer = np.loadtxt('C:\\Users\\todo\\Documents\\Documents cours\\U lille\\simu\\simu barre échauffement\\cas équilibre\\resultats_fer.txt')
data_eau = np.loadtxt('C:\\Users\\todo\\Documents\\Documents cours\\U lille\\simu\\simu barre échauffement\\cas équilibre\\resultats_eau.txt')

x_al = data_al[:, 0]  # abscisse
y1_al = data_al[:, 1]  # u(x, y=0)
y2_al = data_al[:, 2]  # u(x, y=R)

x_cui = data_cui[:, 0]  # abscisse
y1_cui = data_cui[:, 1]  # u(x, y=0)
y2_cui = data_cui[:, 2]  # u(x, y=R)

x_fer = data_fer[:, 0]  # abscisse
y1_fer = data_fer[:, 1]  # u(x, y=0)
y2_fer = data_fer[:, 2]  # u(x, y=R)

x_eau = data_fer[:, 0]  # abscisse
y1_eau = data_fer[:, 1]  # u(x, y=0)
y2_eau = data_fer[:, 2]  # u(x, y=R)



lambd = 230
h=10
R=1

yth = (200-25)*np.exp(-x_al*np.sqrt(2*h/(R*lambd)))+25

plt.figure(figsize=(8, 6))

plt.plot(x_al, y1_al,'.b', label='temp à y = 0')

plt.plot(x_al, y2_al,'.r', label='temp à y = R')

plt.plot(x_al, yth,'y', label='temp théo à y = R')

# plt.plot(x_cui, y2_cui,'.r', label='cui')

# plt.plot(x_fer, y2_fer,'.y', label='fer')

plt.xlabel('position sur la barre')
plt.ylabel('température')
# plt.title('température en fonction de la position sur la barre')
plt.legend()
plt.grid(True)
plt.show()