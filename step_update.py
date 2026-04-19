from entity_class import entity



def step_update(entities, root_cell, param_dict):
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
            # entity.kNN()   # update the prioq in the entity with the ones that are 
                                            # sorrounding it at the moment
            entity.zombie_walk()            # update velocity and direction of zombie walk based on 
                                            # prioq
            
        elif entity.mode == "H": 
            # entity.kill_radius()            # check if human is in the kill radius of zombie
                                            # needs to happen at "end of last step" so at beginning
                                            # of this one is also possible. otherwise there would
                                            # have to be another for loop after the location update
            entity.kNN()   # update the prioq in the entity with the ones that are 
                                            # sorrounding it at the moment
            
            entity.human_walk(entities)             # update velocity and direction of zombie walk based on 
                                            # prioq
    for entity in entities:
        # this has to happen in its own loop because if not, the gradual updating of the location
        # will change the way the simulation runs. some humans will be updated before some zombies
        # even have the chance to move. 
        entity.update_location(param_dict["timestep"])

        ## check if silent/dead/deceased/gone/in hell




