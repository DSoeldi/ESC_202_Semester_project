from Initialization_functions import create_parameter_dict, Initialize_entities, Initialize_root_cell
import numpy as np


#-----------------------------------------------Innitialize parameters--------------------------------------------
parameter_dict = create_parameter_dict(n_H = 100,
                                       n_Z = 10,
                                       timestep = 0.00028,                      
                                       n_steps = 30, 
                                       x_bounds = np.array((0.0,100.0)),
                                       y_bounds = np.array((0.0,100.0)), 
                                       awareness_r_H = None, 
                                       awareness_r_Z = None, 
                                       max_speed_H = None, 
                                       max_speed_Z = None,
                                       walking_speed_Z = None,
                                       H_contr_flocking = None, 
                                       max_ents_cell = None
                                       )
entities = Initialize_entities(parameter_dict)
root_cell = Initialize_root_cell(parameter_dict, entities)

#-----------------------------------------------Initialize partitioning--------------------------------------------
root_cell.partition()
#------------------------------------------------------------------------------------------------------------------

parameter_dict["root_cell"] = root_cell