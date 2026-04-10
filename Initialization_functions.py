import numpy as np
from entity_class import entity
from cell_class import cell

def validate_bounds(bounds):
    if not isinstance(bounds, np.ndarray): raise(TypeError)
    if not (isinstance(bounds[0], np.float64) or not isinstance(bounds[1], np.float64)): raise(TypeError)
    if bounds[0] > bounds[1]: raise(ValueError)


def create_parameter_dict(awareness_r_H, awareness_r_Z, H_contr_flocking, max_ents, n_H, n_Z, timestep, n_steps, x_bounds, y_bounds):
    """
    function that creates the parameter dictionary

    Args:
        awareness_r_H (float):
            Awareness radius for a human in which it can sense Zombies (& other humans). If None is given, default value will be used.

        awareness_r_Z (float):
            Awareness radius for a zombie in which it can sense Humans (& other zombie). If None is given, default value will be used.
        
        H_contr_flocking (int):
            Number of Humans that contribute to flocking computations.

        max_ents (int):
            Maximum number of entities allowed within 1 cell. Default is 6, if None is given.
        
        n_H (int):
            Number of human entities to be simulated.
        
        n_Z (int):
            Number of Zombie entities to be simulated.
        
        timestep (float) in [fraction of 1h]:
            the timestep to be simulated.
        
        n_steps (int):
            total amount of steps the simulation will last.
        
        x_bounds (np.ndarray((float, float))):
            The x coordinates, marking the bounds of the Area to be simulated. (x_bounds[0] < x_bounds[1])
        
        y_bounds (np.ndarray((float, float))):
            The y coordinates, marking the bounds of the Area to be simulated. (y_bounds[0] < y_bounds[1])

    Returns:
        A dictionary containing all the above values
    """
    # validate correct types were given
    if not isinstance(awareness_r_H, float) and awareness_r_H != None: raise(TypeError)
    if not isinstance(awareness_r_Z, float) and awareness_r_Z != None: raise(TypeError)
    if not isinstance(H_contr_flocking, int): raise(TypeError)
    if not isinstance(max_ents, int) and max_ents != None: raise(TypeError)
    if not isinstance(n_H, int): raise(TypeError)
    if not isinstance(n_Z, int): raise(TypeError)
    if not isinstance(timestep, float): raise(TypeError)
    if not isinstance(n_steps, int): raise(TypeError)
    validate_bounds(x_bounds)
    validate_bounds(y_bounds)

    return {"awareness_r_H": awareness_r_H, 
            "awareness_r_Z": awareness_r_Z,
            "H_contr_flocking": H_contr_flocking,
            "max_ents": max_ents,
            "n_H": n_H,                          
            "n_Z": n_Z,
            "timestep": timestep,
            "n_steps": n_steps,
            "x_bounds": x_bounds,
            "y_bounds": y_bounds}



def Initialize_entities(param_dict):
    """
    Creates a list of entities from given parameters.
    """
    # create human entities
    ents = [entity("H", np.array((np.random.uniform(param_dict["x_bounds"][0], param_dict["x_bounds"][1]), 
                                  np.random.uniform(param_dict["y_bounds"][0], param_dict["y_bounds"][1])))) 
            for _ in range(param_dict["n_H"])]
    # create zombie entities
    ents.extend([entity("Z", np.array((np.random.uniform(param_dict["x_bounds"][0], param_dict["x_bounds"][1]), 
                                       np.random.uniform(param_dict["y_bounds"][0], param_dict["y_bounds"][1])))) 
            for _ in range(param_dict["n_Z"])])
    
    return tuple(ents)



def Initialize_root_cell(param_dict, entities):
    """
    Creates a root cell from given parameters.
    """
    return cell(LL = np.array((param_dict["x_bounds"][0], param_dict["y_bounds"][0])), 
                RH = np.array((param_dict["x_bounds"][1], param_dict["y_bounds"][1])),
                all_ents = entities,
                max_ents = param_dict["max_ents"])