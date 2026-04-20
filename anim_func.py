"""provides the animation functions for the animated run"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Animation function
def animate(i, snapshots):
    ax.clear()
    coords_list = snapshots[i]  # Get the i-th snapshot
    xs, ys = zip(*coords_list)
    ax.scatter(xs, ys)
    ax.set_title(f"Step {i}")
    

fig, ax = plt.subplots()
def run_animate(snapshots):

    # ani = FuncAnimation(fig_anim, animate, frames = 20, interval=i, repeat = False, fargs=(entities,))
    # return ani
    ani = FuncAnimation(fig, animate, frames=len(snapshots), interval=200, repeat=False, fargs=(snapshots,))
    return ani


