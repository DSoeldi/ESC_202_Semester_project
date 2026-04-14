from cell_class import cell
from globals import entities, parameter_dict
from entity_class import entity
import random as rd
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------Initiate kNN---------------------------
for e in entities:
    if e.mode == "H": e.kNN()

# create fig
plt.figure(figsize = (10,10))
fig, ax = plt.subplots()


# ---------------------------Start Plotting---------------------------
# plot particles 
for e in entities:
    ax.plot(e.pos[0], e.pos[1], 'o', markersize = 1.5, color = "red" if e.mode == "Z" else "blue")

ax.set_title("blue: humans, red: zombies\nsquare: randomly chosen entity, x: neighbours of that entity", color = "grey")
ax.set_xlabel('x')
ax.set_ylabel('y')


# recursively plot cells
def plot_cells(curr_cell):
    # code to see there are to child_cells left, if that is the case, draw ALL cell boundaries
    if not curr_cell.isleaf():
        plot_cells(curr_cell.d_cells[0])
        plot_cells(curr_cell.d_cells[1])
    else:
        ax.hlines(y = [curr_cell.LL[1], curr_cell.RH[1]], 
                xmin = curr_cell.LL[0], 
                xmax = curr_cell.RH[0], 
                color = "violet",
                linewidths = 0.5)
        ax.vlines(x = [curr_cell.LL[0], curr_cell.RH[0]], 
                ymin = curr_cell.LL[1], 
                ymax = curr_cell.RH[1],
                color = "violet",
                linewidths = 0.5)
        
def highlight_random_entities_and_neighbours(n): # n = number of random entities to highlight
    # plot kNN nieghbours heap((distance of particle to query particle, particle_idx), ...)

    # randomly choose 2 entities:
    for _ in range(n):
        i = rd.randint(0, len(entities)-1)
        while entities[i].mode != "H": # Zombies do not have a pq!!!!!
            i = rd.randint(0, len(entities)-1)
        ent = entities[i]

        # plot circle with radius = awareness_r_H 
        circ = plt.Circle((ent.pos[0], ent.pos[1]), radius = parameter_dict["awareness_r_H"]* 1000, 
                          facecolor = "turquoise", edgecolor = "black", alpha = 0.7)
        ax.add_patch(circ)

        # plot randomly chosen entity
        ax.plot(ent.pos[0], ent.pos[1], 's', markersize = 4, color = "blue") 

        # plot nieghbours of randomly chosen p
        for p in ent.pq.heap:
            ax.plot(entities[p[1]].pos[0], entities[p[1]].pos[1], 'x', markersize = 4, color = "red" if entities[p[1]].mode == "Z" else "blue")
        


# ------------------------------------------Call Plotting Functions------------------------------------------
plot_cells(parameter_dict["root_cell"])
highlight_random_entities_and_neighbours(3)

plt.savefig("Visualize_Partition_kNN.png", dpi = 200)