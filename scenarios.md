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
####first day apocalypse, 1 infection, new york time square, everbody full of energy

#--->nworld war z zombies
plot 1 begininig of apocalpse day 1, newyork time square (about 0.5km x 0.5 km), rushhour people 68,000
newyork city time square, people are so close to each other they only feel closest people
n_H= 20000, n_Z=1, 
walking_speed_Z = 5., walking_speed_H = 5.
max_speed_Z = 26., max_speed_H = 25.,
awareness_r_Z = 0.015,awareness_r_H = 0.015,
H_contr_flocking=4,

#-->walking dead zombies
n_H= 68000, n_Z=1, 
walking_speed_Z = 4., walking_speed_H = 5.
max_speed_Z = 15., max_speed_H = 25.,
awareness_r_Z = 0.007,awareness_r_H = 0.015,
H_contr_flocking=4,
------------------------
------------------------
##after 10 years, city of new york full of zombies , 15000km x15000km, 8.5 million people live there,  no energy in the zombvie left
after 10 year atleast 3/4 is zombie rest escaped only few left, a day in the city

# --->nworld war z zombies
n_H= 10000, n_Z= 6000000, 
walking_speed_Z = 1., walking_speed_H = 4.
max_speed_Z = 10., max_speed_H = 25.,
awareness_r_Z = 0.5,awareness_r_H = 0.015,
H_contr_flocking=4,

-->walking dead zombies, still some enrgy left
n_H= 10000, n_Z= 6000000, 
walking_speed_Z = 4., walking_speed_H = 4.
max_speed_Z = 15., max_speed_H = 25.,
awareness_r_Z = 0.5,awareness_r_H = 3.,
H_contr_flocking=10,

------------------------
------------------------

----things that dont change
nsteps. with 1 second timestep, if we want 1 day -n = 86400
timestep is in hours, 1 second is timestep  0.000278
biteradius lets do 1 meter, 
smoothed random walk


timestep= 1 * 0.000278, n_steps=86400, 
smooth_rand_walk = 0.2,
bite_r_Z_H = 0.001,
-----------------------

































