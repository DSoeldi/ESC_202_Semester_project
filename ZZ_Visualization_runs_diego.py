from classes.entity_class import entity
import globals as g
from Initialization_functions import *
import numpy as np
from step_update import *
from vis.anim_func import *



########### Flocking behavior
xbounds = (0.0,0.1)
ybounds = (0.,0.1)
param_dict = create_parameter_dict(
                                   timestep= 1 * 0.000278, n_steps=100,  
                                   smooth_rand_walk = 0.2,
                                   bite_r_Z_H = 0.0001,
                                   
                                   n_H= 200, n_Z=0, 
                                   walking_speed_Z = 5., lonely_walk_speed_H = 20.,
                                   max_speed_Z = 30., max_speed_H = 25.,
                                   awareness_r_Z = 0.010, awareness_r_H = 0.004,
                                   H_contr_flocking=10,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.4,0.9,0.4), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = False
                                   )

np.random.seed(42)
snapshots, analyze = run(param_dict)
ani = run_animate(snapshots, param_dict)
ani.save("outputs/diego_slides/less_flocking_example.gif")

########### Zombie repulsion behavior
xbounds = (0.0,10.)
ybounds = (0.,10.)
param_dict = create_parameter_dict(
                                   timestep= 10 * 0.000278, n_steps=100,  
                                   smooth_rand_walk = 0.2,
                                   bite_r_Z_H = 0.0001,
                                   
                                   n_H= 200, n_Z=5, 
                                   walking_speed_Z = 5., lonely_walk_speed_H = 20.,
                                   max_speed_Z = 30., max_speed_H = 25.,
                                   awareness_r_Z = 0.010, awareness_r_H = 4.,
                                   H_contr_flocking=4,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.6,0.8,0.6), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = False
                                   )

np.random.seed(42)
snapshots, analyze = run(param_dict)
ani = run_animate(snapshots, param_dict)
ani.save("outputs/diego_slides/zombie_repulsion_example.gif")

########### Lonely behavior
xbounds = (0.0,1.)
ybounds = (0.,1.)
param_dict = create_parameter_dict(
                                   timestep= 5 * 0.000278, n_steps=100,  
                                   smooth_rand_walk = 0.2,
                                   bite_r_Z_H = 0.0001,
                                   
                                   n_H= 5, n_Z=0, 
                                   walking_speed_Z = 5., lonely_walk_speed_H = 20.,
                                   max_speed_Z = 30., max_speed_H = 25.,
                                   awareness_r_Z = 0.010, awareness_r_H = 0.004,
                                   H_contr_flocking=4,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.6,0.8,0.6), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = False
                                   )

np.random.seed(42)
snapshots, analyze = run(param_dict)
ani = run_animate(snapshots, param_dict)
ani.save("outputs/diego_slides/lonely_human_example.gif")