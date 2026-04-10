from cell_class import cell
from globals import entities, parameter_dict, root_cell
from entity_class import entity

import matplotlib.pyplot as plt

# create fig
plt.figure(figsize = (10,10))
fig, ax = plt.subplots()
fig.suptitle("Binary tree")


# plot particles 
for e in entities:
    ax.plot(e.pos[0], e.pos[1], 'o', markersize = 1.5, color = "red" if e.mode == "Z" else "blue")

ax.set_title(f"# entities: {len(entities)}", color = "grey")
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

plot_cells(root_cell)

plt.savefig("Visualize_Ents_Partition.png", dpi = 200)