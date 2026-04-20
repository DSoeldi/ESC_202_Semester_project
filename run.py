from entity_class import entity
import globals as g
from Initialization_functions import *
import numpy as np
from step_update import *
from anim_func import *

xbounds = (0.0,100.0)
ybounds = (0,100)

param_dict = create_parameter_dict(n_H=100, n_Z=0,timestep=1., n_steps=100, 
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds))

entities = Initialize_entities(param_dict)
root_cell = Initialize_root_cell(param_dict, entities)
param_dict["root_cell"] = root_cell

for step in range(0,param_dict["n_steps"]):
    step_update(entities, root_cell, param_dict)
    print(step)
    ani = run_animate(10, entities)

ani.save("test.gif")
