from entity_class import entity
import globals as g
from Initialization_functions import *
import numpy as np
from step_update import *
from anim_func import *

xbounds = (0.0,10.0)
ybounds = (0,10)

param_dict = create_parameter_dict(n_H=10, n_Z=10,timestep=0.1, n_steps=100, 
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds))

entities = Initialize_entities(param_dict)
root_cell = Initialize_root_cell(param_dict, entities)
param_dict["root_cell"] = root_cell
snapshots = []
for step in range(0,param_dict["n_steps"]):
    step_update(entities, root_cell, param_dict)
    print(step)
    snapshots.append([entity.pos for entity in entities])  # Store a copy of 

ani = run_animate(snapshots)
plt.show()