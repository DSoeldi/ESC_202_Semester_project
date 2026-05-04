from classes.entity_class import entity
import globals as g
from Initialization_functions import *
import numpy as np
from step_update import *
from vis.anim_func import *

xbounds = (0.0,10.)
ybounds = (0.,10.)

param_dict = create_parameter_dict(n_H=100, n_Z=10,timestep=.0008, n_steps=1000, 
                                   smooth_rand_walk = 0.3,
                                   bite_r_Z_H = 0.01,
                                   walking_speed_Z = 3.,
                                   max_speed_Z = 20., max_speed_H = 25.,
                                   awareness_r_Z = 0.8,awareness_r_H = 0.8,
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.8,0.8,0.8), # avoidfactor, matchingfactor and centeringfactor
                                   analyze=True, H_contr_flocking=8)
snapshots, analyze = run(param_dict)
ani = run_animate(snapshots, param_dict)
ani.save("outputs/long_animation.gif", fps = 60)