#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 08:58:11 2026

@author: raphaeltarabinicastellani
"""
from globals import rng
import numpy as np


 #--------------------CLASS-ENTITY-START-ANAïS-----------------------------
 #Raphael: i already started a bit for clarity for my functions inside this class
 
class entity:
    def __init__(self):
        
        #shall be a bool
        self.alerted = ... 
        
        #is a vector from origin to position e.g. (?) np.array([10.0, 5.0])
        self.position = ...
        
        #velocity is a vector e.g. (?) np.array([10.0, 5.0])
        self.velocity = ...
        
        #---TEMPORARY-NOTES-RAPHAEL---
        #is quick math like this faster or with numpy?
        # (velocity[0]**2 + velocity[1]**2)**0.5   
        # np.linalg.norm(velocity) ?
        #-----------------------------
        
        #speed is a scalar, has no direction, (magnitude of velocity)
        self.velocity_speed= (velocity[0]**2 + velocity[1]**2)**0.5
        
        #direction will be a unit vector of velocity e.g.  np.array([0,-1]), or  np.array([1,1])
        self.velocity_direction = velocity / velocity_speed
        
        #speed is a scalar, has no direction, this needs to be defined
        #its the speed the zombie has when he wants to eat a human
        self.zombie_max_alerted_speed = ...
        

        
    #--------------------ZOMBIE-WALK-START-RAPHAEL-----------------------------
    
    def zombie_walk(self, here_still_needs_pos_nearest_human_from_knn):
        
        #INFO
        #this function calls functions that change the entity.velocity & 
        #entity.direction according to the if statements down below, it does
        #not however actually DO the step!
        
        #check if zombie has been alerted in self.knn()->anais
        
        if self.alerted == True:
            #there is a humans close!
            #lets go check where the human is and adjust our velocity
            self.human_awareness_walk(here_still_needs_pos_nearest_human_from_knn)
            
        else: 
            #mhm no food for me (zombie) right know...
            self.random_walk()
        
        return
    
    def random_walk(self):
        #Check zombie_walk() for more informations
        #redirect the velocity direction according to the random walk without
        #changing the magnitude of the vector
        #-> new velocity (same magnitude but different direction) 
        
        # Define directions if the walk
        DIRECTIONS = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])
        
        #pick random integer from 0 to 3
        choice = rng.integers(0, 4) 
        
        #change direction, but not speed of velocity
        self.velocity = self.velocity_speed * DIRECTIONS[choice]
        
        return 
    
    def human_awareness_walk(self, here_still_needs_pos_nearest_human_from_knn):
        #Check zombie_walk() for more informations
        
        #INFO
        #change the zombie velocity  vector, so that i points to the closes human 
        #and so that the vector velocity is at it max_zombie_speed
        
        #---TEMPORARY-NOTES-RAPHAEL---
        #?? knn() should pull out human or zombie position if there is one close by->have to see
        #how implemented by anais
        #for now lets act like pos is position of nearest human 
        
        #position_nearest_human = here_still_needs_pos_nearest_human_from_knn= e.g.np.array([10.0, 5.0])
        #-----------------------------
        position_nearest_human = ...
        
        #get vector from position zombie pointing to position human
        zombie_to_human_vector = position_nearest_human - self.position
        
        #of this vector get the unit vector
        
        #---TEMPORARY-NOTES-RAPHAEL---
        #is quick math like this faster or with numpy?
        #-velocity / (velocity[0]**2 + velocity[1]**2)**0.5   
        #-velocity / np.linalg.norm(velocity) ?
        #-----------------------------
        #get the distance
        distance_zombie_to_human = (zombie_to_human_vector[0]**2 + zombie_to_human_vector[1]**2)**0.5  
        
        #---TEMPORARY-NOTES-RAPHAEL---
        #depending a bit where we end up actually checking if zombie can bite 
        #human or not this can be changed
        #(in plan kill radius function is placed in if entity == human branch)
        #if we dont do kill radius here we have to pay attention, that we dont, 
        #divided by zero uf they are perfectly on top of each other.
        #for now:
        if distance_zombie_to_human == 0:
            raise ValueError("Division by zero in human_awareness_walk(): Zombie and Human are at the EXACT same spot! Check function for more Information; Raphael")
        #-----------------------------
        
        new_zombie_direction = zombie_to_human_vector / distance_zombie_to_human
        
        #to this direction multiply the zombie_max_alerted_speed to get new velocity of zombie and store it there
        
        self.velocity =  new_zombie_direction * self.zombie_max_alerted_speed

        return 
    
    #--------------------ZOMBIE-WALK-FINISH-RAPHAEL----------------------------
    
    
    
    
    
    