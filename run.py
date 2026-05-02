from classes.entity_class import entity
import globals as g
from Initialization_functions import *
import numpy as np
from step_update import *
from vis.anim_func import *

xbounds = (0.0,20.)
ybounds = (0.,20.)

param_dict = create_parameter_dict(n_H=100, n_Z=20,timestep=.008, n_steps=50, 
                                   smooth_rand_walk = 0.3,
                                   bite_r_Z_H = 0.001,
                                   walking_speed_Z = 3.,
                                   max_speed_Z = 20., max_speed_H = 26.,
                                   awareness_r_Z = 0.8,awareness_r_H = 0.9,
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.2,0.3,0.2),
                                   analyze=True)
np.random.seed(42)
snapshots, analyze = run(param_dict)
ani = run_animate(snapshots, param_dict)
ani.save("outputs/more_centering_factor_animation.gif")