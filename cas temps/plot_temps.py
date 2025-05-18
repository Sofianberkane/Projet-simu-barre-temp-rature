import matplotlib.pyplot as plt

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        block = []
        for line in f:
            line = line.strip()
            if line == "":
                if block:
                    data.append(block)
                    block = []
            else:
                values = list(map(float, line.split()))
                block.append(values)
        if block:
            data.append(block)  # dernier bloc
    return data

# Lire les fichiers
data_R = read_data("C:\\Users\\todo\\Documents\\Documents cours\\U lille\\simu\\simu barre échauffement\\cas temps\\posR.txt")  # pour y = R
data_0 = read_data("C:\\Users\\todo\\Documents\\Documents cours\\U lille\\simu\\simu barre échauffement\\cas temps\\pos0.txt")  # pour y = 0

data_R_cond = read_data("C:\\Users\\todo\\Documents\\Documents cours\\U lille\\simu\\simu barre échauffement\\cas temps\\posR_cond.txt")  # pour y = R
data_R_conv = read_data("C:\\Users\\todo\\Documents\\Documents cours\\U lille\\simu\\simu barre échauffement\\cas temps\\posR_conv.txt")  # pour y = R

# Plot de u(x) à y = R pour quelques instants
plt.figure(figsize=(10, 6))
for i, snapshot in enumerate(data_R):
    if i % 2 == 0:  # afficher 1 snapshot sur 2 pour lisibilité
        times = [row[0] for row in snapshot]
        xs = [row[1] for row in snapshot]
        us = [row[2] for row in snapshot]
        plt.plot(xs, us, 'r')
# for i, snapshot in enumerate(data_R_conv):
#     if i % 2 == 0:
#         times = [row[0] for row in snapshot]
#         xs = [row[1] for row in snapshot]
#         us = [row[2] for row in snapshot]
#         plt.plot(xs, us, 'y')

# plt.title("Évolution de u(x) à y=R")
plt.xlabel("Position sur la barre")
plt.ylabel("Température")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()