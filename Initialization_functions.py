import numpy as np
from entity_class import entity
from cell_class import cell

def validate_bounds(bounds):
    """
    Function to validate: x_bounds, y_bounds
    """
    if not isinstance(bounds, np.ndarray): raise(TypeError)
    if not (isinstance(bounds[0], np.float64) or not isinstance(bounds[1], np.float64)): raise(TypeError)
    if bounds[0] > bounds[1]: raise(ValueError)


def validate_max_speed(max_speed):
    """
    Function to validate: max_speed_H, max_speed_Z
    """
    #---TEMPORARY-NOTES-ANAIS-----
        # test if the max speed is within some range?... so if at some point we have variable max_speeds,
        # we make sure it always is within some realistic range?
    #-----------------------------
    if not isinstance(max_speed, float): raise(ValueError)


def validate_awareness_radius(awareness_r):
    """
    Function to validate: awareness_r_H, awareness_r_Z
    """
    #---TEMPORARY-NOTES-ANAIS-----
        # test if the max awareness radius is within some realistic range?
    #-----------------------------
    if not isinstance(awareness_r, float): raise(ValueError)
    


def create_parameter_dict(n_H, n_Z, timestep, n_steps, x_bounds, y_bounds, root_cell = None, 
                          awareness_r_H = None, awareness_r_Z = None, max_speed_H = None, max_speed_Z = None, 
                          walking_speed_Z = None, H_contr_flocking = None, max_ents_cell = None):
    """
    function that creates the parameter dictionary

    Args:
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

        root_cell (cell):
            The root cell containing all entities and all daughter cells.
        
        awareness_r_H (float) in [km]:
            Awareness radius for a human in which it can sense Zombies (& other humans). 
            If None is given, default value will be used.

        awareness_r_Z (float) in [km]:
            Awareness radius for a zombie in which it can sense Humans (& other zombie). 
            If None is given, default value will be used.
        
        max_speed_H (float) in [km/h]: 
            Fixed max speed for zombies. It's the speed the zombie has when he wants to eat a human, meaning alerted == True.
            If None is given, default value will be used.
        
        max_speed_Z (float) in [km/h]: 
            Fixed max speed for humans.
            If None is given, default value will be used.
            
        walking_speed_Z (float) in [km/h]:
            Walking speed for a Zombie (when no human is within it's awareness_r_Z). 
            If None is given, default value will be used.
        
        H_contr_flocking (int):
            Number of Humans that contribute to flocking computations.
            If None is given, default value will be used.

        max_ents_cell (int):
            Maximum number of entities allowed within 1 cell. 
            If None is given, default value will be used.
        

    Returns:
        A dictionary containing all the above values
    """
    # if some variables == None, change to default values
    awareness_r_H = 0.02 if awareness_r_H == None else awareness_r_H
    awareness_r_Z = 0.015 if awareness_r_Z == None else awareness_r_Z
    max_speed_H = 28.0 if max_speed_H == None else max_speed_H
    max_speed_Z = 20.0 if max_speed_Z == None else max_speed_Z
    walking_speed_Z = 4.0 if walking_speed_Z == None else walking_speed_Z
    H_contr_flocking = 4 if H_contr_flocking == None else H_contr_flocking
    max_ents_cell = 6 if max_ents_cell == None else max_ents_cell

    # validate correct types were given
    if not isinstance(n_H, int): raise(TypeError)
    if not isinstance(n_Z, int): raise(TypeError)
    if not isinstance(timestep, float): raise(TypeError)
    if not isinstance(n_steps, int): raise(TypeError)
    validate_bounds(x_bounds)
    validate_bounds(y_bounds)
    # validate root cell?
    validate_awareness_radius(awareness_r_H)
    validate_awareness_radius(awareness_r_Z)
    validate_max_speed(max_speed_H)
    validate_max_speed(max_speed_Z)
    if not isinstance(walking_speed_Z, float): raise(TypeError)
    if not isinstance(H_contr_flocking, int): raise(TypeError)
    if not isinstance(max_ents_cell, int): raise(TypeError)

    return {"n_H": n_H,                          
            "n_Z": n_Z,
            "timestep": timestep,
            "n_steps": n_steps,
            "x_bounds": x_bounds,
            "y_bounds": y_bounds,
            "awareness_r_H": awareness_r_H, 
            "awareness_r_Z": awareness_r_Z,
            "max_speed_H": max_speed_H,
            "max_speed_Z": max_speed_Z,
            "walking_speed_Z": walking_speed_Z,
            "H_contr_flocking": H_contr_flocking,
            "max_ents_cell": max_ents_cell}


def Initialize_entities(param_dict):
    """
    Creates a list of entities from given parameters.
    """
    # create human entities
    ents = [entity("H", np.array((np.random.uniform(param_dict["x_bounds"][0], param_dict["x_bounds"][1]), 
                                  np.random.uniform(param_dict["y_bounds"][0], param_dict["y_bounds"][1]))),
                                  param_dict,
                                  i) 
            for i in range(param_dict["n_H"])]
    # create zombie entities
    ents.extend([entity("Z", np.array((np.random.uniform(param_dict["x_bounds"][0], param_dict["x_bounds"][1]), 
                                       np.random.uniform(param_dict["y_bounds"][0], param_dict["y_bounds"][1]))),
                                       param_dict,
                                       i) 
            for i in range(param_dict["n_Z"])])
    
    return ents



def Initialize_root_cell(param_dict, entities):
    """
    Creates a root cell from given parameters.
    """
    return cell(LL = np.array((param_dict["x_bounds"][0], param_dict["y_bounds"][0])), 
                RH = np.array((param_dict["x_bounds"][1], param_dict["y_bounds"][1])),
                all_ents = entities,
                max_ents = param_dict["max_ents_cell"])