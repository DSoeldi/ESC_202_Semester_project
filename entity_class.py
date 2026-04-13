#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 08:58:11 2026

@author: raphaeltarabinicastellani
"""
from globals import rng
from priority_queue_class import prio_q
import numpy as np
from copy import deepcopy


 #--------------------CLASS-ENTITY-START-ANAïS-----------------------------

 
class entity:
    @ staticmethod
    def validate_mode(mode):
        """
        static method to validate: mode
        """
        if mode not in ("H", "Z"): raise(ValueError)

    @ staticmethod
    def validate_vector(vector):
        """
        static method to validate: pos, velocity, pos_alerted vectors
        """
        if not isinstance(vector, np.ndarray): raise(ValueError)
        if not isinstance(vector[0], np.float64): raise(ValueError)
        if not isinstance(vector[1], np.float64): raise(ValueError)
        if not np.shape(vector) == (2,): raise(ValueError)
    
    @ staticmethod
    def validate_alerted(alerted):
        """
        static method to validate: alerted
        """
        if not isinstance(alerted, bool): raise(ValueError)

        # if alerted == True, pos_alerter, should not be None!!!
        # if alerted = False, pos_alerter should be None!!

    @ staticmethod
    def validate_pq(pq):
        """
        static method to validate: pq
        """
        if not isinstance(pq, prio_q): raise(TypeError)
        if not isinstance(pq.heap, list): raise (TypeError)

    @ staticmethod
    def validate_max_speed(max_speed):
        """
        static method to validate: max_speed_H, max_speed_Z
        """
        #---TEMPORARY-NOTES-ANAIS-----
            # test if the max speed is within some range?... so if at some point we have variable max_speeds,
            # we make sure it always is within some realistic range?
        #-----------------------------
        if not isinstance(max_speed, float): raise(ValueError)
    
    @ staticmethod
    def validate_awareness_radius(awareness_r):
        """
        static method to validate: awareness_r_H,awareness_r_Z
        """
        if not isinstance(awareness_r, float): raise(ValueError)
        #---TEMPORARY-NOTES-ANAIS-----
            # test if the max awareness radius is within some realistic range?
        #-----------------------------


    def __init__(self, mode, pos, velocity = np.array((0.0,0.0)), alerted = False, 
                 pos_alerter = None, max_speed_Z = 20.0, max_speed_H = 28.0, awareness_r_H = 0.02, awareness_r_Z = 0.015):
        """
        Initializes a simulation entity (Human or Zombie).
        
        Positional Args:
            mode (str):  
                "Z" or "H" defines whether entity is a human or a zombie 
            pos (np.array((x,y))):  
                current position vector of entity                
        
        Keyword Args:
            velocity (np.array((x,y))): 
                current velocity vector of entity
                Note: Should not be (0,0) to avoid division errors. ????
            alerted (bool):
                Is a zombie/human in my awareness radius?  
            pos_alerter (np.array((x,y))):
                position vector of alerting entity   
            max_speed_Z (float) in [km/h]: 
                Fixed max speed for zombies. It's the speed the zombie has when he wants to eat a human, meaning alerted == True
            max_speed_H (float) in [km/h]: 
                Fixed max speed for humans.
            awareness_r_H (float) in [km]:
                Awareness radius for a Human
            awareness_r_Z (float) in [km]:
                Awareness radius for a Zombie

        Additional Attrb:
            pq (prio_q):
                Priority queue attribute for entity
        """
        
        self.mode = mode
        self.pos = pos
        self.velocity = velocity
        self.alerted = alerted
        self.pos_alerter = pos_alerter 
        self.pq = pq()
        self.max_speed_Z = max_speed_Z
        self.max_speed_H = max_speed_H  # avg human sprint: 24-32km/h
        self.awareness_r_H = awareness_r_H
        self.awareness_r_Z = awareness_r_Z

        
        #---TEMPORARY-NOTES-ANAIS-----
            # Should we add a variable, which stores the capacity of an entity to keep on running, 
            # which is somehow calculated through some function of time/distance & velocity??
        #-----------------------------
        
        # Raise Value Error for wrong input
        self.validate_mode(self.mode)
        self.validate_vector(self.pos)
        self.validate_vector(self.velocity)
        self.validate_alerted(self.alerted)
        if isinstance(pos_alerter, np.ndarray) or pos_alerter != None: self.validate_vector(self.pos_alerter)
        if pq != None: self.validate_pq(self.pq)
        self.validate_max_speed(self.max_speed_Z)
        self.validate_max_speed(self.max_speed_H)
        self.validate_awareness_radius(awareness_r_H)
        self.validate_awareness_radius(awareness_r_Z)

    def __repr__(self):
        """ 
        For printing entity within a collection

        Returns:
            A string in the form of: "entity_mode(pos, velocity, alerted, pos_alerter)
        """ 
        #---HElP-NOTES-RAPHAEL-------
        # Dunder Methods (Double Underscore like __repr__, __eq__)
        # - The "Standardized Plug": Instead of remembering a custom name like 
        #   print_data_zombi(), I can use standard Python tools like print(zombie1).
        # - Automatic Hooks: Python triggers these automatically behind the scenes.
        # - Replaces memory addresses (<entity object at...>) with whatever is returned here
        #-----------------------------
        
        return f"{self.mode}(pos: {np.round(self.pos, 2)}, v: {np.round(self.velocity, 2)}, alert: {self.alerted}, pos: {self.pos_alerter})"
    
    def __eq__(self, other):
        """
        Checks if 2 instances of entity are equal (all attributes are equal)
        Returns: 
            (bool)
        """
        #---HElP-NOTES-RAPHAEL-------
            #1. this you can use just by using  is entity1 == entity2 ("shortcut to ask"), 
            #   python will understand entity1.__eq__(entity2) and go in here
            
            #2. NotImplemented is fancy way to say False, and then try other way around
            #    python will call entity2.__eq__(entity1)
            #  try A==B, -> false, ok so then try B==A
        #-----------------------------
        
        if not isinstance(other, entity): return NotImplemented
        return ((self.mode == other.mode) and
                (self.pos == other.pos).all() and 
                (self.velocity == other.velocity).all() and
                (self.alerted == other.alerted) and
                ((self.pos_alerter == other.pos_alerter).all() if (isinstance(self.pos_alerter, np.ndarray) or isinstance(other.pos_alerter, np.ndarray)) else self.pos_alerter == other.pos_alerter) and
                (self.pq == other.pq) and 
                (self.max_speed_Z == other.max_speed_Z) and 
                (self.max_speed_H == other.max_speed_H))
    
    def get_speed(self):
        """
        calculates speed (scalar, no direction) from velocity vector
        
        Returns:
            speed (int)
        """

        #---TEMPORARY-NOTES-RAPHAEL---
            #is quick math like this faster or with numpy?
            # (velocity[0]**2 + velocity[1]**2)**0.5   
            # np.linalg.norm(velocity) ?
        #-----------------------------
        return (self.velocity[0]**2 + self.velocity[1]**2)**0.5 # magnitude of velocity vector
    
    def get_direction(self):
        #---TEMPORARY-NOTES-ANAIS-----
            # isch die Funktion nötig ????
            #vll bruchts de diego den im flocking behavior??
            #--> when velocity 0,0 isch, isch speed 0,0, den gits da eh geteilt durch 0, wege
            #    dem hani obe gschriebe Note: Should not be (0,0) to avoid division errors.
            #    aber eigentlich au nice wenn amigs paar entities eifach ümestönd ? also mues mehr sicher
            #    generell na apasse/ lösig finde
        #-----------------------------
        """
        calculates direction (unit vector) from velocity vector
        
        Returns:
            direction (np.array((x,y)))
        """
        return self.velocity / self.get_speed()
        
    def change_mode(self, new_mode):
        """
        changes mode attribute for entity & validates it's type
        
        Args:
            self (entity)
            new_mode (bool)
        """
        self.validate_mode(new_mode) 
        self.mode = deepcopy(new_mode)

    def change_pos(self, new_pos):
        """
        changes pos attribute for entity & validates it's type
        
        Args:
            self (entity)
            new_pos (np.array((x,y)))
        """
        self.validate_vector(new_pos)
        self.pos = deepcopy(new_pos)

    def change_velocity(self, new_velocity):
        """
        changes velocity attribute for entity & validates it's type
        
        Args:
            self (entity)
            new_velocity (np.array((x,y)))
        """
        self.validate_vector(new_velocity)
        self.velocity = deepcopy(new_velocity)

    def change_alerted(self, new_alerted):
        """
        changes alerted attribute for entity & validates it's type
        
        Args:
            self (entity)
            new_alerted (bool)
        """
        self.validate_alerted(new_alerted) 
        self.alerted = deepcopy(new_alerted)

    def change_pos_alerter(self, new_pos_alerter):
        """
        changes alerted attribute for entity & validates it's type
        
        Args:
            self (entity)
            new_alerted (bool)
        """
        if isinstance(new_pos_alerter, np.ndarray) or new_pos_alerter != None: self.validate_vector(new_pos_alerter) 
        self.pos_alerter = deepcopy(new_pos_alerter)
    
    def change_pq(self, new_pq):
        """
        changes pq attribute for entity & validates it's type
        
        Args:
            self (entity)
            new_pq (bool)
        """
        self.validate_pq(new_pq) 
        self.pq = deepcopy(new_pq)
        
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
        
        if self.alerted:
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

        ##INFO
        #redirect the velocity direction according to the random walk without
        #changing the speed of the vector
        
        
        #choose a random angle (radians) in a full circle
        theta = rng.uniform(0, np.pi * 2)
        
        #new_direction has to be a unit vector
        new_direction = np.array([np.cos(theta), np.sin(theta)])
        
        #Scale new_direction by the current speed
        new_velocity = self.get_speed() * new_direction
        
        #update
        self.change_velocity(new_velocity)
        
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
        ##INFO
        #change the zombie velocity  vector, so that i points to the closes human & with max_zombie_speed

        #get vector from position zombie pointing to position human
        zombie_to_human_vector = position_nearest_human - self.pos
        
        #get the distance
        distance_zombie_to_human = self.get_distance(position_nearest_human) 
        
        #---TEMPORARY-NOTES-RAPHAEL---
            #depending a bit where we end up actually checking if zombie can bite 
            #human or not this can be changed
            #(in plan kill radius function is placed in if entity == human branch)
            #if we dont do kill radius here we have to pay attention, that we dont, 
            #divided by zero uf they are perfectly on top of each other.
            #for now:
        if distance_zombie_to_human == 0:
            raise ValueError("Division by zero in human_awareness_walk(): Zombie and Human are at the EXACT same spot! Check function for more Information; Raphael")
            #possible solution?
            #store this globaly ? epsilon = 1e-9 
            # if distance_zombie_to_human > epsilon: or just do if == 0 make array 0.0,0.0
            #     new_zombie_direction = zombie_to_human_vector / distance_zombie_to_human
            # else:
            #     # They are effectively in the same spot
            #     new_zombie_direction = np.array([0.0, 0.0])
        #-----------------------------
        
        
        new_zombie_direction = zombie_to_human_vector / distance_zombie_to_human
        
        #to this direction multiply the max_speed_Z to get new velocity of zombie and store it there
        self.change_velocity(new_zombie_direction * self.max_speed_Z)

        return 
    
    #--------------------ZOMBIE-WALK-FINISH-RAPHAEL----------------------------
    
    
    
    
    
    