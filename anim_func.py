"""provides the animation functions for the animated run"""
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

def animate(i, entities):
    ax.clear()
    coords_list = []
    for entity in entities:
        coords_list.append(entity.pos)
    ax.plot(coords_list)

def run_animate(i, entities):
    ani = FuncAnimation(fig, animate(entities), frames = 20, interval=i, repeat = False)
    

