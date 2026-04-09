from entity_class import entity


parameters = {"r_zombie": 1, "r_human": 2}

def step_update(timestep, entities, root_cell):
    """
    Does a single timestep forward for all entities in the entities list. 

    Args: 
        timestep [double]:      Timestep with unit Hours
        entities [List (?)]:    List of entity objects that have been initialized, 
                                includes zombies and humans
        root_cell [cell obj]:   partitioned cell object  
    """

    for entity in entities:
        pass