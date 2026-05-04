#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:46:47 2026

@author: raphaeltarabinicastellani
"""


want to plot tjer pop dynamics of zombies and humans
for different starting codnitions
https://zombie.fandom.com/wiki/Zombie_Comparison_Chart
----things that change---
zombie walk speed
world war z the movie--fast, sligthly faster speed as average human sprint panick speed
                       -awarness radius big, the same as human
                       -but later in apocalpyse they are lose alot of their power
walking dead         --slow, below average human walking speed, dangerous in big groups
                    -- awarness radius half of humans
                    --remain cosntan through out 


2 scenes , 
------------------------
####first day apocalypse, all full of energy
Dynanmo werk 21, 250 m^2, fits 200 people, party 1 hours

#--->world war z zombies, 
plot 1 begininig of apocalpse day 1, newyork time square (about 0.5km x 0.5 km), rushhour people 68,000
newyork city time square, people are so close to each other they only feel closest people

-zombis still very fast, faster than humans, human when the lonly walk, have fast speed because agitated
-there are alot of people so awarness radius not that big, smoke in the air also,
-zombies smewll so they have bigger awarness radius, everything really close so only people close to you 
-count in flocking

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
                                   
--> 

#-->walking dead zombies, same place, same club
they are severly slower and they cant really sprint, fastes is 9kmh, they rest is similar

xbounds = (0.0,0.015)
ybounds = (0.,0.015)
param_dict = create_parameter_dict(
                                   timestep= 1 * 0.000278, n_steps=60*15,  
                                   smooth_rand_walk = 0.2,
                                   bite_r_Z_H = 0.001,
                                   
                                   n_H= 200, n_Z=1, 
                                   walking_speed_Z = 4., lonely_walk_speed_H = 20.,
                                   max_speed_Z = 9., max_speed_H = 25.,
                                   awareness_r_Z = 0.010, awareness_r_H = 0.004,
                                   H_contr_flocking=4,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.8,0.8,0.8), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = True
                                   )
------------------------
------------------------
###after 10 years, low energy
in a migro MM supermarket, size 1500m^2, 300 people
was hit hard, really quit during rush hour, still alot of food left becuase everybody was scared to scavenge for food there

#-->5 people, mission get food in 1 hour without being eaten, NOT trying to stay together
the zombies used alot of energy early on in the days and are worn down they are severöy slower than before
the are kind of jsut standin still the zombies, you need to get really close to activate them 1meter
humans can see a bout 20 meters becuase light is off, they want to stay together, scared to split up

xbounds = (0.,0.040)
ybounds = (0.,0.040)
param_dict = create_parameter_dict(
                                   timestep= 1 * 0.000278, n_steps=3600,  
                                   smooth_rand_walk = 0.2,
                                   bite_r_Z_H = 0.001,
                                   
                                   n_H= 5, n_Z=300, 
                                   walking_speed_Z = 0., lonely_walk_speed_H = 5.,
                                   max_speed_Z = 9., max_speed_H = 20.,
                                   awareness_r_Z = 0.001, awareness_r_H = 0.020,
                                   H_contr_flocking=0,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.8,0.8,0.8), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = True
                                   )

#-->5 people, mission get food in 1 hour without being eaten, WITH trying to stay together
the zombies used alot of energy early on in the days and are worn down they are severöy slower than before
the are kind of jsut standin still the zombies, you need to get really close to activate them 1meter
humans can see a bout 20 meters becuase light is off, they want to stay together, scared to split up.
humans are tired cannt do max speed anymore

xbounds = (0.,0.040)
ybounds = (0.,0.040)
param_dict = create_parameter_dict(
                                   timestep= 1 * 0.000278, n_steps=3600,  
                                   smooth_rand_walk = 0.2,
                                   bite_r_Z_H = 0.001,
                                   
                                   n_H= 5, n_Z=300, 
                                   walking_speed_Z = 0., lonely_walk_speed_H = 5.,
                                   max_speed_Z = 9., max_speed_H = 20.,
                                   awareness_r_Z = 0.001, awareness_r_H = 0.020,
                                   H_contr_flocking=5,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.8,0.8,0.8), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = True
                                   )

------------------------
------------------------

----things that dont change
nsteps. with 1 second timestep, if we want 1 day -n = 86400
timestep is in hours, 1 second is timestep  0.000278
smoothed random walk


-----------------------

































