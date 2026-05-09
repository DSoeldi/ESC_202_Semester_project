import sys
import os
import random as rd
import numpy as np
import matplotlib.pyplot as plt


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from classes.cell_class import cell
from classes.entity_class import entity
from Initialization_functions import *


# path to save file to <--- filenmae still needs to be added
output_path = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'anais_plots_präsi')


def plot_ents(entities): 
    for e in entities:
        ax.plot(e.pos[0], e.pos[1], 'o', markersize = 1.5, color = "red" if e.mode == "Z" else "blue")

    ax.set_xlabel('[km]')
    ax.set_ylabel('[km]')
    ax.set_aspect('equal')

    # ----- save first version (only entities)
    plt.savefig(output_path + "/Visualize_Partition_0.png", dpi = 200)


# recursively plot cells
def plot_cells(curr_cell, step):
    # code to see there are to child_cells left, if that is the case, draw ALL cell boundaries

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
    ax.set_aspect('equal')
    
    # ----- save version for each partition step 
    plt.savefig(output_path + f"/Visualize_Partition_{step}.png", dpi = 200)
    
    if not curr_cell.isleaf():
        plot_cells(curr_cell.d_cells[0], step + 1)
        plot_cells(curr_cell.d_cells[1], step + 2)
        
def draw_periodic_circle(ax, cx, cy, radius, bounds, fill_col, edge_col):
    L = bounds[1] - bounds[0]  # assuming square, same for x and y
    
    offsets = [0, L, -L]
    for dx in offsets:
        for dy in offsets:
            circle = plt.Circle((cx + dx, cy + dy), radius, facecolor = fill_col, 
                                edgecolor = edge_col, alpha = 0.4)
            ax.add_patch(circle)

def highlight_random_entities_and_neighbours(n): # n = number of random entities to highlight
    # plot kNN nieghbours heap((distance of particle to query particle, particle_idx), ...)
    # randomly choose 2 entities:
    for _ in range(n):
        i = rd.randint(0, len(entities)-1)
        ent = entities[i]

        # plot periodic circle with radius = awareness_r_H 
        radius = parameter_dict["awareness_r_H"] if ent.mode == "H" else parameter_dict["awareness_r_Z"]
        draw_periodic_circle(ax, ent.pos[0], ent.pos[1], radius = radius, 
                             bounds = (parameter_dict["x_bounds"][0], parameter_dict["x_bounds"][1]),
                             fill_col = "turquoise" if ent.mode == "H" else "lightcoral",
                             edge_col = "lightseagreen" if ent.mode == "H" else "indianred")
    
        # plot randomly chosen entity
        ax.plot(ent.pos[0], ent.pos[1], '.', markersize = 10, color = "blue" if ent.mode == "H" else "red") 

        # make sure square and axes are labelled equally
        ax.set_aspect('equal')
        ax.set_xlim(parameter_dict["x_bounds"][0], parameter_dict["x_bounds"][1])
        ax.set_ylim(parameter_dict["y_bounds"][0], parameter_dict["y_bounds"][1])

        # plot neighbours of randomly chosen p
        for p in ent.pq.heap:
            ax.plot(entities[p[1]].pos[0], entities[p[1]].pos[1], 'x', markersize = 4, color = "red" if entities[p[1]].mode == "Z" else "blue")
        


#-----------------------------------------------Innitialize parameters--------------------------------------------
parameter_dict = create_parameter_dict(n_H = 30,
                                       n_Z = 20,
                                       timestep = 0.1, 
                                       n_steps = 1,
                                       x_bounds = np.array((0.0,0.4)),
                                       y_bounds = np.array((0.0,0.4)),
                                       awareness_r_H = 0.05,
                                       awareness_r_Z = 0.025)
entities = Initialize_entities(parameter_dict)
root_cell = Initialize_root_cell(parameter_dict, entities)
parameter_dict["root_cell"] = root_cell

#-----------------------------------------------Initialize partitioning--------------------------------------------
root_cell.partition()

#-----------------------------------------------Initialize kNN--------------------------------------------
for e in entities:
    e.kNN()

# create fig
plt.figure()
fig, ax = plt.subplots()

# ------------------------------------------Call Plotting Functions------------------------------------------
plot_ents(entities)
plot_cells(root_cell, 1)
highlight_random_entities_and_neighbours(3)

plt.savefig(output_path + f"/Visualize_kNN_final.png", dpi = 200)