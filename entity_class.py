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
    def __init__(self, start_position, start_velocity, zombie_max_speed):
        """
        Initializes a simulation entity (Human or Zombie).
        
        Args:
            start_position (tuple): Initial (x, y) coordinates.
            start_velocity (tuple): Initial (x, y) velocity vector. 
                                    Note: Should not be (0,0) to avoid division errors.
            zombie_max_speed (float): Fixed max speed of the zombie.
        """
        
        #shall be a bool
        self.alerted = False
        
        #is a vector from origin to position e.g. np.array((10.0, 5.0))
        self.position = np.array(start_position)
        
        #velocity is a vector e.g. np.array((10.0, 5.0))
        self.velocity = np.array(start_velocity)
        
        #---TEMPORARY-NOTES-RAPHAEL---
        #is quick math like this faster or with numpy?
        # (velocity[0]**2 + velocity[1]**2)**0.5   
        # np.linalg.norm(velocity) ?
        #-----------------------------
        
        #speed is a scalar, has no direction, (magnitude of velocity)
        self.velocity_speed= (self.velocity[0]**2 + self.velocity[1]**2)**0.5
        
        #direction will be a unit vector of velocity e.g.  np.array((0,-1)), or  np.array((1,1))
        self.velocity_direction = self.velocity / self.velocity_speed
        
        #speed is a scalar, has no direction, this needs to be defined
        #its the speed the zombie has when he wants to eat a human, 
        #meaning he alerted == True
        self.zombie_max_speed = zombie_max_speed
        

        
    #--------------------ZOMBIE-WALK-START-RAPHAEL-----------------------------
    
    def zombie_walk(self, position_nearest_human):
        """
        Checks the alert state and executes the appropriate walk behavior.
    
        Args:
            position_nearest_human (np.ndarray): The (x, y) coordinates of the target human.
            
        Returns:
            None: continues by calling the function for the type of walk the zombie will do
            
        """
        
        #INFO
        #this function calls functions that change the entity.velocity & 
        #entity.direction according to the if statements down below, it does
        #not however actually DO the step!
        
        #position_nearest_human ->this position_nearest_human should come 
        #from knn somehow, we defind it to come from there in our document 
        
        if self.alerted == True:
            #there is a humans close!
            #lets go check where the human is and adjust our velocity
            self.human_awareness_walk(position_nearest_human)
            
        else: 
            #mhm no food for me (zombie) right know...
            self.random_walk()
        
        return
    
    def random_walk(self):
        """
        Adjusts the zombie's velocity with a random walk.
    
        Args:
           None
    
        Returns:
            None: Updates self.velocity directly.
        """

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
    
    def human_awareness_walk(self, position_nearest_human):
        """
        Adjusts the zombie's velocity to chase the nearest human with max speed.
    
        Args:
            position_nearest_human (np.ndarray)): The (x, y) coordinates of the target human.
    
        Returns:
            None: Updates self.velocity directly.
            
        Raises:
            ValueError: If the zombie and human are at the exact same position.
        """
        #Check zombie_walk() for more informations
        
        #INFO
        #change the zombie velocity  vector, so that i points to the closes human 
        #and so that the vector velocity is at it max_zombie_speed
        
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
        
        #to this direction multiply the zombie_max_speed to get new velocity of zombie and store it there
        
        self.velocity =  new_zombie_direction * self.zombie_max_speed

        return 
    
    #--------------------ZOMBIE-WALK-FINISH-RAPHAEL----------------------------
    
    
    
    
    
    