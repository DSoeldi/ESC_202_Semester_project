"""provides the animation functions for the animated run"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Animation function
def animate(i, snapshots,param_dict, ax, entities):
    ax.clear()
    coords_list = snapshots[i]  # Get the i-th snapshot
    xs, ys = zip(*coords_list)
    color_map = {"H": "blue", "Z": "red"}
    colors = [color_map[entity.mode] for entity in entities]
    ax.scatter(xs, ys, c = colors)
    ax.set_ylim(param_dict["y_bounds"])
    ax.set_xlim(param_dict["x_bounds"])
    ax.set_title(f"Step {i}")
    return ax
    

def run_animate(snapshots, param_dict, entities):
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate, frames=len(snapshots), interval=100, repeat=False, fargs=(snapshots,param_dict, ax, entities))
    return ani


def plot_entities(entities):
    x_list, y_list, mode = zip(*[(entity.pos[0], entity.pos[1], entity.mode) for entity in entities])
    color_map = {"H": "blue", "Z": "red"}
    colors = [color_map[entity.mode] for entity in entities]
    plt.scatter(x_list, y_list, c = colors)
    
