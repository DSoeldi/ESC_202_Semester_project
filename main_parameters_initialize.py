from Initialization_functions import create_parameter_dict, Initialize_entities, Initialize_root_cell
import numpy as np
from entity_class import entity
from copy import copy


parameter_dict = create_parameter_dict(None, None, 5, None, 50, 20, 0.00028, 30, np.array((0.0,100.0)), np.array((0.0,100.0)))
entities = Initialize_entities(parameter_dict)
root_cell = Initialize_root_cell(parameter_dict, entities)



root_cell.partition()

