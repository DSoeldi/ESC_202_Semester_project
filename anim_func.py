"""provides the animation functions for the animated run"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate(i, entities):
    fig, ax = plt.subplots()
    ax.clear()
    coords_list = []
    for entity in entities:
        coords_list.append(entity.pos)
    # ax.plot(coords_list)
    xs, ys = zip(*coords_list)  # Unpack x and y coordinates
    ax.scatter(xs, ys)


fig_anim = plt.figure()
def run_animate(i, entities):

    ani = FuncAnimation(fig_anim, animate, frames = 20, interval=i, repeat = False, fargs=(entities,))
    return ani

    

