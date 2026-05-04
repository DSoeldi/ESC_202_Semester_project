from classes.entity_class import entity
import globals as g
from Initialization_functions import *
import numpy as np
from step_update import *
from vis.anim_func import *

xbounds = (0.0,0.015)
ybounds = (0.,0.015)
param_dict = create_parameter_dict(
                                   timestep= 1 * 0.000278, n_steps=3600,  
                                   smooth_rand_walk = 0.2,
                                   bite_r_Z_H = 0.0001,
                                   
                                   n_H= 200, n_Z=1, 
                                   walking_speed_Z = 5., lonely_walk_speed_H = 20.,
                                   max_speed_Z = 30., max_speed_H = 25.,
                                   awareness_r_Z = 0.010, awareness_r_H = 0.004,
                                   H_contr_flocking=4,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.8,0.8,0.8), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = True
                                   )

np.random.seed(42)
snapshots, analyze = run(param_dict)
ani = run_animate(snapshots, param_dict)
ani.save("outputs/long_animation.gif")

if param_dict["analyze"]:
    analyze.pop_dynamics_plot(output_path = "outputs/pop_analytics.png" )
 