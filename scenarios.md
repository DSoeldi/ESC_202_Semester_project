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

#--->world war z zombies, 
plot 1 begininig of apocalpse day 1, newyork time square on new years eve (about 0.5km x 0.5 km), rushhour people 68,000
newyork city time square, people are so close to each other they only feel closest people


-zombis still very fast, faster than humans, human when the lonly walk, have fast speed because agitated
-there are alot of people so awarness radius not that big, 
-zombies smewll so they have bigger awarness radius, everything really close so only people close to you 
-count in flocking

#adjust here
#30 min, density per m^2 is 4–5 people/m² highly pact, 
#1. will take about 5 hours, with rendering maybe 7 hours ???
#------------------------------------------------------------------------------
side = 0.015 #km #would be whole
xbounds = (0.0,side)
ybounds = (0.,side)



param_dict = create_parameter_dict(
                                   timestep= 1 * 0.000278, n_steps= int(3600/4),  
                                   smooth_rand_walk = 0.2,
                                   bite_r_Z_H = 0.0001,
                                   
                                   n_H= int(5 * (side * 1000)**2), n_Z=1, 
                                   walking_speed_Z = 5., lonely_walk_speed_H = 20.,
                                   max_speed_Z = 30., max_speed_H = 25.,
                                   awareness_r_Z = 0.050, awareness_r_H = 0.040,
                                   H_contr_flocking=4,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.8,0.8,0.8), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = True
                                   )
                                   
#------------------------------------------------------------------------------




#-->2..walking dead zombies, same place, 
they are severly slower and they cant really sprint, fastes is 9kmh, they rest is similar
#will take about 5,3hours and with render maybe 7''
#------------------------------------------------------------------------------
side = 0.015 #km #would be whole
xbounds = (0.0,side)
ybounds = (0.,side)
param_dict = create_parameter_dict(
                                   timestep= 1 * 0.000278, n_steps=int(3600/4),  
                                   smooth_rand_walk = 0.2,
                                   bite_r_Z_H = 0.0001,
                                   
                                   n_H= int(5 * (side * 1000)**2), n_Z=1, 
                                   walking_speed_Z = 4., lonely_walk_speed_H = 20.,
                                   max_speed_Z = 9., max_speed_H = 25.,
                                   awareness_r_Z = 0.050, awareness_r_H = 0.040,
                                   H_contr_flocking=4,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.8,0.8,0.8), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = True
                                   )
#------------------------------------------------------------------------------
------------------------
------------------------
###after 10 years, low energy
in a migro MM supermarket, size 1500m^2, 300 people those people now zombies density zombie 0.2 zombies /m^2
was hit hard, really quit during rush hour, still alot of food left becuase everybody was scared to scavenge for food there

#-->5 people, mission get food in 1 hour without being eaten, NOT trying to stay together
the zombies used alot of energy early on in the days and are worn down they are severöy slower than before
the are kind of jsut standin still the zombies, you need to get really close to activate them 1meter
humans can see far meters becuase light is off, they want to stay together, scared to split up
#also about 5.30 runtime without rendering
#------------------------------------------------------------------------------
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
                                   awareness_r_Z = 0.001, awareness_r_H = 0.90,
                                   H_contr_flocking=0,
                                   
                                   x_bounds=np.array(xbounds), y_bounds=np.array(ybounds), 
                                   flocking_factors=(0.8,0.8,0.8), # avoidfactor, matchingfactor and centeringfactor
                                   analyze = True
                                   )
#------------------------------------------------------------------------------

#-->5 people, mission get food in 1 hour without being eaten, WITH trying to stay together
the zombies used alot of energy early on in the days and are worn down they are severöy slower than before
the are kind of jsut standin still the zombies, you need to get really close to activate them 1meter
humans can see a bout 20 meters becuase light is off, they want to stay together, scared to split up.
humans are tired cannt do max speed anymore

#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------
------------------------
------------------------

----things that dont change
nsteps. with 1 second timestep, if we want 1 day -n = 86400
timestep is in hours, 1 second is timestep  0.000278
smoothed random walk


-----------------------

































