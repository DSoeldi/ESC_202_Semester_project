from entity_class import entity
import globals as g
from Initialization_functions import *
import numpy as np
from step_update import *

xbounds = (0.0,100.0)
ybounds = (0,100)

param_dict = create_parameter_dict(n_H=100, n_Z=1,timestep=0.1, n_steps=10, 
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds))

entities = Initialize_entities(param_dict)
root_cell = Initialize_root_cell(param_dict, entities)
param_dict["root_cell"] = root_cell
for step in range(0,param_dict["n_steps"]):
    step_update(entities, root_cell, param_dict)
    print(step)