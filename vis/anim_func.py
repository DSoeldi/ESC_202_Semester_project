"""provides the animation functions for the animated run"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Animation function
def animate(i, snapshots,param_dict, ax):
    ax.clear()
    positions, modes = zip(*snapshots[i])
    xs, ys = zip(*positions)
    color_map = {"H": "blue", "Z": "green"}
    #so we can spot infections have to change here, mode of the snapshot
    colors = [color_map[m] for m in modes]
    
    #size = 0.1 is about ...
    ax.scatter(xs, ys, c = colors, s = 0.1)
    ax.set_ylim(param_dict["y_bounds"])
    ax.set_xlim(param_dict["x_bounds"])
    ax.set_title(f"Step {i}")
    return ax
    

def run_animate(snapshots, param_dict):
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate, frames=len(snapshots), interval=100, repeat=False, 
                        fargs=(snapshots,param_dict, ax))
    return ani


def plot_entities(entities):
    x_list, y_list, mode = zip(*[(entity.pos[0], entity.pos[1], entity.mode) for entity in entities])
    color_map = {"H": "blue", "Z": "red"}
    colors = [color_map[entity.mode] for entity in entities]
    plt.scatter(x_list, y_list, c = colors)
    
