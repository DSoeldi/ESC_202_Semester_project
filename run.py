from classes.entity_class import entity
import globals as g
from Initialization_functions import *
import numpy as np
from step_update import *
from vis.anim_func import *


#they are severly slower and they cant really sprint, fastes is 9kmh, they rest is similar

side = 0.062 #km #
xbounds = (0.,side)
ybounds = (0.,side)
param_dict = create_parameter_dict(
                                   timestep= 1 * 0.000278, n_steps=3600,  
                                   smooth_rand_walk = 0.2,
                                   bite_r_Z_H = 0.001,
                                   
                                   n_H= 5, n_Z=int(0.2 * (side * 1000)**2), 
                                   walking_speed_Z = 0., lonely_walk_speed_H = 5.,
                                   max_speed_Z = 9., max_speed_H = 20.,
                                   awareness_r_Z = 0.001, awareness_r_H = 0.50,
                                   H_contr_flocking=5,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.8,0.8,0.8), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = True
                                   )
np.random.seed(42)
snapshots, analyze = run(param_dict)
ani = run_animate(snapshots, param_dict)
ani.save("outputs/zombies_succeeding_animation.gif")

if param_dict["analyze"]:
    analyze.pop_dynamics_plot(output_path = "outputs/pop_analytics.png" )
 