from classes.entity_class import entity
import numpy as np
from Initialization_functions import *
from tqdm import tqdm
from classes.analytics import *



def step_update(entities):
    """
    Does a single timestep forward for all entities in the entities list. 

    Args: 
        timestep [double]:      Timestep with unit Hours
        entities [List (?)]:    List of entity objects that have been initialized, 
                                includes zombies and humans
        root_cell [cell obj]:   partitioned cell object  
    """

    for entity in entities:

        if entity.mode == "Z":
            entity.kNN()   # update the prioq in the entity with the ones that are 
                                            # sorrounding it at the moment
            entity.zombie_walk(entities)            # update velocity and direction of zombie walk based on 
                                            # prioq
        
        
        elif entity.mode == "H": 
                                            # needs to happen at "end of last step" so at beginning
                                            # of this one is also possible. otherwise there would
                                            # have to be another for loop after the location update
            entity.kNN()   # update the prioq in the entity with the ones that are 
                                            # sorrounding it at the moment
            
            entity.human_walk(entities)             # update velocity and direction of zombie walk based on 
                                            # prioq

            entity.adj_max_speed(0.999999) # reduce max speed of each human at each timestep by  multiplying with factor
        
        
    for entity in entities:
        if entity.mode == "H" and entity.alerted is True: 
            entity.check_infection_H()            # check if human is in the kill radius of zombie
        # this has to happen in its own loop because if not, the gradual updating of the location
        # will change the way the simulation runs. some humans will be updated before some zombies
        # even have the chance to move. 
        entity.update_location()
        

        ## check if silent/dead/deceased/gone/in hell


def run(param_dict):
    entities = Initialize_entities(param_dict)
    root_cell = Initialize_root_cell(param_dict, entities)
    param_dict["root_cell"] = root_cell
    snapshots = []
    print("---simulating horde---")
    for step in tqdm(range(0,param_dict["n_steps"])):
        step_update(entities)
        snapshots.append([(entity.pos.copy(), entity.mode) for entity in entities])  # Store a copy of 
    
    if param_dict["analyze"]:
        sim_analytics = Analytics(snapshots, param_dict)
        return snapshots, sim_analytics

    return snapshots, None





