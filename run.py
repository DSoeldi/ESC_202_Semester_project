from entity_class import entity
import globals as g
from Initialization_functions import *
import numpy as np
from step_update import *
from anim_func import *

xbounds = (0.0,20.0)
ybounds = (0.,20.)

param_dict = create_parameter_dict(n_H=30, n_Z=30,timestep=.08, n_steps=150, 
                                   smooth_rand_walk = 0.5,
                                   bite_r_Z_H = 0.2,
                                   walking_speed_Z = 3.,
                                   max_speed_Z = 15., max_speed_H = 5.,
                                   awareness_r_Z = 0.9,awareness_r_H = 0.9,
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds))

entities = Initialize_entities(param_dict)

plt.figure()
plot_entities(entities)
plt.savefig("start.png")
plt.close()

root_cell = Initialize_root_cell(param_dict, entities)
param_dict["root_cell"] = root_cell
snapshots = []
for step in range(0,param_dict["n_steps"]):
    step_update(entities, root_cell, param_dict)
    print(step)
    snapshots.append([(entity.pos.copy(), entity.mode) for entity in entities])  # Store a copy of 

plt.figure()
plot_entities(entities)
plt.savefig("end.png")
plt.close()

ani = run_animate(snapshots, param_dict)
ani.save("testanimation.gif")