import numpy as np
from classes.entity_class import entity
from classes.cell_class import cell
import warnings

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
    
def validate_bite_r_Z_H(bite_r_Z_H):
    """
    Validates the bite radius (in km). 
    Expects a non-negative float; warns if unrealistic (> 2m).
    """
    if not isinstance(bite_r_Z_H, float): raise TypeError(
            f'bite_r_Z_H must be a float, got {type(bite_r_Z_H)}'
        )
    
    if (bite_r_Z_H < 0): raise ValueError(
            f'bite_r_Z_H must be non-negative, got {bite_r_Z_H}'
            )
    
    #bite radius bigger than 0.002km abit unrealistic, dont do raise Warning, which will stop simulation
    #i want to keep it running, but with a warning
    if (bite_r_Z_H > 0.002): warnings.warn(
            "you choose a bite radius bigger than 2 meters which can be unrealistic for this simulation"
            )
    return

def validate_smooth_rand_walk(smooth_rand_walk):
    '''
    Validated the param for smooth_rand_walk
    Expects a float or int between 0.0 - 1.0
    '''
    if not (0.0 <= smooth_rand_walk <= 1.0):
        raise TypeError(
            f'smooth_rand_walk must be a between 0.0 - 1.0, got {smooth_rand_walk}'
        )
    return

def validate_flocking_factors(flocking_factors):
    '''
    validates the flocking factors. expects a tuple of three floats
    '''
    if not isinstance(flocking_factors, tuple):
        raise TypeError("flocking factors must be saved as tuple object")
    
    for factor in flocking_factors:
        if not isinstance(factor, float):
            raise TypeError("flocking factors must be of float type")


def create_parameter_dict(n_H, n_Z, timestep, n_steps, x_bounds, y_bounds, root_cell = None, 
                          awareness_r_H = None, awareness_r_Z = None, max_speed_H = None, max_speed_Z = None, 
                          walking_speed_Z = None, walking_speed_H = None, H_contr_flocking = None,flocking_factors = None, 
                          max_ents_cell = None, bite_r_Z_H = None, smooth_rand_walk = None,
                          analyze = None):
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
        
        walking_speed_H(float) in [km/h]:
            Walking speed for a Human (when lonely walk). 
            If None is given, default value will be used.
        
        H_contr_flocking (int):
            Number of Humans that contribute to flocking computations.
            If None is given, default value will be used.

        flocking_factors (tuple(float, float, float)):
            factors for flocking subcalculations. 
            avoidfactor, matchingfactor and centeringfactor

        max_ents_cell (int):
            Maximum number of entities allowed within 1 cell. 
            If None is given, default value will be used.
            
        bite_r_Z_H (float) in [km]:
            Bite Radius, for distance Zombie to Human, for which the Zombie can bite the Human.
            If None is given, default value will be used.
        
        smooth_rand_walk (float/int):
            Between 0 - 1 (straight line - random walk), smooth_rand_walk * pi (half a circle) 
            gives a spectrum in radans an entity can randomly deviated into in the direction 
            of its velocity to the left and to the right hemisphere.

        analyze (Bool):
            Checks if analysis functions should be run after simulation. 
            Normally set to false
            
        

    Returns:
        A dictionary containing all the above values
    """
    # if some variables == None, change to default values
    awareness_r_H = 0.02 if awareness_r_H == None else awareness_r_H
    awareness_r_Z = 0.015 if awareness_r_Z == None else awareness_r_Z
    max_speed_H = 28.0 if max_speed_H == None else max_speed_H
    max_speed_Z = 20.0 if max_speed_Z == None else max_speed_Z
    walking_speed_Z = 4.0 if walking_speed_Z == None else walking_speed_Z
    walking_speed_H = 5.0 if walking_speed_H == None else walking_speed_H
    H_contr_flocking = 4 if H_contr_flocking == None else H_contr_flocking
    flocking_factors = (0.2,0.3,0.2) if flocking_factors == None else flocking_factors
    max_ents_cell = 6 if max_ents_cell == None else max_ents_cell
    bite_r_Z_H = 0.0002 if bite_r_Z_H == None else bite_r_Z_H
    smooth_rand_walk = 0.2 if smooth_rand_walk == None else smooth_rand_walk
    analyze = False if analyze == None else analyze

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
    if not isinstance(walking_speed_H, float): raise(TypeError)
    if not isinstance(H_contr_flocking, int): raise(TypeError)
    if not isinstance(max_ents_cell, int): raise(TypeError)
    validate_bite_r_Z_H(bite_r_Z_H)
    validate_smooth_rand_walk(smooth_rand_walk)
    validate_flocking_factors(flocking_factors)

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
            "walking_speed_H": walking_speed_H,
            "H_contr_flocking": H_contr_flocking,
            "flocking_factors": flocking_factors,
            "max_ents_cell": max_ents_cell,
            "bite_r_Z_H": bite_r_Z_H,
            "smooth_rand_walk": smooth_rand_walk,
            "analyze": analyze}


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
            for i in range(param_dict["n_H"], param_dict["n_H"] +param_dict["n_Z"])])
    
    return ents



def Initialize_root_cell(param_dict, entities):
    """
    Creates a root cell from given parameters.
    """
    return cell(LL = np.array((param_dict["x_bounds"][0], param_dict["y_bounds"][0])), 
                RH = np.array((param_dict["x_bounds"][1], param_dict["y_bounds"][1])),
                all_ents = entities,
                max_ents = param_dict["max_ents_cell"])