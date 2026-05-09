"""provides the animation functions for the animated run"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import floor

# helper functions for strings in animation title
def get_time_str(d, i):
    hours_float = i * d["timestep"]
    hours_int = floor(hours_float)
    minutes_float = (hours_float - hours_int) * 60
    minutes_int = floor(minutes_float)
    seconds_int = round((minutes_float - minutes_int)*60)
    time = "Time: %02d:%02d:%02d" %(hours_int, minutes_int, seconds_int)
    return time

def get_count_str(modes):
    Z_H_count = "Zombies:% 4d\n Humans:% 3d" %("".join(modes).count("Z"), "".join(modes).count("H"))
    return Z_H_count

# Animation function
def animate(i, snapshots, param_dict, ax, fig):
    ax.clear()
    for txt in fig.texts:  # remove old fig-level text (Zombie and Human count str)
        txt.remove()

    positions, modes = zip(*snapshots[i])
    xs, ys = zip(*positions)
    color_map = {"H": "dodgerblue", "Z": "crimson"}
    #so we can spot infections have to change here, mode of the snapshot
    colors = [color_map[m] for m in modes]
    
    #size = 0.1 is about ...
    ax.scatter(xs, ys, c = colors, s = 0.1)
    ax.set_ylim(param_dict["y_bounds"])
    ax.set_xlim(param_dict["x_bounds"])
    ax.set_xlabel("[km]")
    ax.set_ylabel("[km]")

    ax.set_title(get_time_str(param_dict, i), loc = "left")
    fig.text(0.9, 0.96, get_count_str(modes), ha='right', va='top', 
             size=12, fontfamily="monospace")
    return ax


def run_animate(snapshots, param_dict):
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate, frames=len(snapshots), interval=100, repeat=False, 
                        fargs=(snapshots,param_dict, ax, fig))
    return ani


def plot_entities(entities):
    x_list, y_list, mode = zip(*[(entity.pos[0], entity.pos[1], entity.mode) for entity in entities])
    color_map = {"H": "blue", "Z": "red"}
    colors = [color_map[entity.mode] for entity in entities]
    plt.scatter(x_list, y_list, c = colors)
    
