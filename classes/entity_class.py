#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 08:58:11 2026

@author: raphaeltarabinicastellani
"""
from rng_seed import rng
from classes.priority_queue_class import prio_q
import numpy as np
from copy import deepcopy
import math
import warnings
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
        if not isinstance(vector, np.ndarray): raise(TypeError)
        if not isinstance(vector[0], np.float64): raise(TypeError)
        if not isinstance(vector[1], np.float64): raise(TypeError)
        if not np.shape(vector) == (2,): raise(ValueError)
    
    @ staticmethod
    def validate_param_dict(d):
        """
        static method to validate: param_dict
        """
        if not isinstance(d, dict): raise(TypeError)

    @ staticmethod
    def validate_idx_all_ents(i):
        """
        static method to validate: idx_all_ents
        """
        if not isinstance(i, int): raise(TypeError)
        if i < 0: raise(ValueError)
    

    @ staticmethod
    def validate_alerted(alerted):
        """
        static method to validate: alerted
        """
        if not isinstance(alerted, bool): raise(TypeError)

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


    def __init__(self, mode, pos, param_dict, idx_all_ents, velocity = np.array((0.0,0.0)), 
                 alerted = False, pos_alerter = None, infected = False):
        """
        Initializes a simulation entity (Human or Zombie).
        
        Positional Args:
            mode (str):  
                "Z" or "H" defines whether entity is a human or a zombie 
            
            pos (np.array((x,y))):  
                current position vector of entity 
            
            param_dict (dictionary):
                Containing import values. 

            idx_all_ents (int):
                Index of this entity instance within the list containing all entities.     
        
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
            preferred_dir (np.array):
                Preferred direction that a human walks in, gets set first time they are alone (empty pq)
        """
        self.mode = mode
        self.pos = pos
        self.param_dict = param_dict
        self.idx_all_ents = idx_all_ents
        self.velocity = velocity
        self.alerted = alerted
        self.pos_alerter = pos_alerter
        self.pq = prio_q()
        self.preferred_dir = None
        
        # Raise Type/Value Error for wrong input
        self.validate_mode(self.mode)
        self.validate_vector(self.pos)
        self.validate_param_dict(self.param_dict)
        self.validate_idx_all_ents(self.idx_all_ents)
        self.validate_vector(self.velocity)
        self.validate_alerted(self.alerted)
        if isinstance(pos_alerter, np.ndarray) or pos_alerter != None: self.validate_vector(self.pos_alerter)
        if prio_q != None: self.validate_pq(self.pq)

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
                (self.idx_all_ents == other.idx_all_ents) and
                (self.velocity == other.velocity).all() and
                (self.alerted == other.alerted) and
                ((self.pos_alerter == other.pos_alerter).all() if (isinstance(self.pos_alerter, np.ndarray) or isinstance(other.pos_alerter, np.ndarray)) else self.pos_alerter == other.pos_alerter) and
                (self.pq == other.pq)
                )
    
    def set_preferred_dir(self):
        
        angle = np.random.uniform(0, 2 * np.pi)
        self.preferred_dir = np.array([np.cos(angle), np.sin(angle)])

    def get_speed(self):
        """
        calculates speed (scalar, no direction) from velocity vector
        
        Returns:
            speed (int)
        """
        return (self.velocity[0]**2 + self.velocity[1]**2)**0.5 # magnitude of velocity vector
    
    def get_direction(self):
        #---TEMPORARY-NOTES-ANAIS-----
            # isch die Funktion nötig ????
        #-----------------------------
        """
        calculates direction (unit vector) from velocity vector. 
        
        Returns:
            direction (np.array((x,y)))
        """
        #since velocity is not initalizes get_speed can return 0, which mean we get an invalid number here!!!!!!
        #which can cause entities to not get a position in step_update, menaing they dont appear
        return self.velocity / self.get_speed()

    
    def get_distance(self, coords):
        """
        calculates distance between self and given coordinates

        Args: 
            coords[ndarray]: Coordinates to which the distance should be calculated
        
        Returns:
            [double]: distance to coordinates
        """
        direction = self.pos - coords
        return np.sqrt(direction[0]**2 + direction[1]**2)
        
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
        changes pos_alerter attribute for entity & validates it's type
        
        Args:
            self (entity)
            new_pos_alerter (np.ndarray((x,y)))
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

    #--------------------kNN-START-ANAIS---------------------------------------
    def calculate_dist2_entity(self, other_ent, offset):
        """
        Calculates the squared distance between 2 entities. 
        Args:
            self (entity)
            other_ent (entity)
            offset (np.ndarray(float, float)):
                The offset by which to "move" the entity, to create periodic boundaries. 
        Returns:
            (float) the squared distance
        """
        dx = self.pos[0] + offset[0] - other_ent.pos[0]
        dy = self.pos[1] + offset[1] - other_ent.pos[1]
        return dx*dx + dy*dy
    

    def kNN(self):
        """
        Replaces old pq of entity with empty prio_q, then initiates kNN algorithm for this entity instance. And updates it's pq. 
        
        Args: 
            self (entity with mode == "H)
        """
        self.change_pq(prio_q()) # initiate a new pq for the next step, otherwise it will grow with each step 
        self.kNN_loop_periodic_bounds() 


    def kNN_loop_periodic_bounds(self):
        """
        Generates all combinations of: (x, y) in {0, +- Lx} x {0, +- Ly} and calls recursive neighbour_search algorithm 
        on all of them to make sure that one can search "beyond edges".

        Args:
            self (entity):
                The entity for which to find neighbours across periodic bounds.

        Returns:
            (prio_q) with a heap containing all entities found within periodic bounds.
        """
        period = (self.param_dict["x_bounds"][1] - self.param_dict["x_bounds"][0], 
                  self.param_dict["y_bounds"][1] - self.param_dict["y_bounds"][0])

        for y in [0.0, -period[1], period[1]]:
            for x in [0.0, -period[0], period[0]]:
                offset = np.array([x, y])
                self.neighbor_search(self.param_dict["root_cell"], offset)

     
    def neighbor_search(self, curr_cell, offset):
        """
        Recursive Neighbour search algorithm which is recursive until a leaf cell is found. 
        Then it checks whether the leaf cell si within the awareness radius and whether it contains 
        entities (Z: only humans in pq, H: have Zombies and Humans in pq) within the awareness radius of self (entity.)

        Args:
            curr_cell (cell):
                The cell we are currently at within the binary tree.

            offset (np.ndarray(float, float)):
                The offset by which to "move" the entity, to create periodic boundaries. 
        """
        awarness_Z2 = self.param_dict['awareness_r_Z'] ** 2
        awarness_H2 = self.param_dict['awareness_r_H'] ** 2
                    
        if curr_cell.isleaf():
            for p in curr_cell.ents_idx_sort[0]: 
                if p != self.idx_all_ents: # compare indeces of both entities, to make sure we don't compare an entity with itself
                    curr_ent = curr_cell.all_ents[p]
                    d2 = self.calculate_dist2_entity(curr_ent, offset)
                    
                    #--zombies only want humans in pq
                    if self.mode == "Z" and d2 <= awarness_Z2 and curr_ent.mode != "Z":
                        self.pq.push((d2, p))
                    
                    #---humans need zombies and humans in pq
                    elif self.mode == "H" and d2 <= awarness_H2 :
                        self.pq.push((d2, p))
        else:
            dist2_c1 = curr_cell.d_cells[0].calc_dist2_cell_entity(self, offset)
            dist2_c2 = curr_cell.d_cells[1].calc_dist2_cell_entity(self, offset)

             # check if distance to daughter cell is (partially) within the awareness radius, if so do recursive call for daughter cell
            if dist2_c1 <= (awarness_H2):
                self.neighbor_search(curr_cell.d_cells[0], offset)
            if dist2_c2 <= (awarness_H2):
                self.neighbor_search(curr_cell.d_cells[1], offset)
        
    #--------------------ZOMBIE-WALK-START-RAPHAEL-----------------------------
    
    def zombie_walk(self, entities):
        """
        executes the appropriate walk behavior. 
        
        calls function to check for alerted state/direction
        if alerted: change direction to clostest human with max speed
        if not alerted: calls function random_walk()
    
        Args:
            entities (list): list filled with all entities.
            
        Returns:
            None: Updates self.change_velocity or self.random_walk directly
            
        """
        self.update_alerted_state_alerter_pos(entities)
        
        #---------------------executes walk type-------------
        if self.alerted: #there is a humans close!
        
            #---calc. direction to clostest human
            #pos closest human
            pos_closest_human = self.pos_alerter
            
            #get vector from position zombie pointing to position human
            zombie_to_human_vector = pos_closest_human - self.pos
            
            #distance between human and zombie
            distance_between_entities = self.get_distance(pos_closest_human)
            
            #compare distance to really small float, so we never to a div by zero 
            #in the line after
            safe_distance = max(distance_between_entities, math.nextafter(0, 1.0))
            
            #get the new unit vector whichs points the zombi to the human
            new_zombie_direction = zombie_to_human_vector / safe_distance
            #-------
            
            #there is a humans close!
            #lets change velocity to max speed of zombi
            self.change_velocity(new_zombie_direction * self.param_dict["max_speed_Z"])

        else: 
            #mhm no food for me (zombie) right know...
            self.random_walk()
        #--------------------------------------------------
        
        return
    

    def random_walk(self):
        """
        Adjusts the zombie's velocity to a smoothed random walk.
    
        Args:
            None
    
        Returns:
            None: Updates self.change_velocity directly.
        """
        #get the direction from last round
        old_direction = self.get_direction()
        
        #if old direction is na
        if np.isnan(old_direction).any(): 
            theta = rng.uniform(0, np.pi * 2)
            old_direction = np.array([np.cos(theta), np.sin(theta)])
            warnings.warn(f'invalid value encountered in self.get_direction, initialized a rand. direction: {old_direction}')
        
        #get the angle to of this direction, to x achis?
        old_phi = math.atan2(old_direction[1], old_direction[0])
        
        #get the random angle
        #this has to be between 0-1, zero means he will follow a straight line
        smoothing_param = self.param_dict["smooth_rand_walk"]

        smooth_phi = rng.uniform(-np.pi * smoothing_param, np.pi * smoothing_param)
        
        new_phi = old_phi + smooth_phi
        
        #get new direction which is depend on last direction +"slightly different angle
        new_direction = np.array([np.cos(new_phi), np.sin(new_phi)])
        
        #get the walking speed
        walking_speed_Z = self.param_dict["walking_speed_Z"]
        
        #Scale new_direction by the normal walking speed of zombie
        new_velocity = walking_speed_Z * new_direction
        
        #update
        self.change_velocity(new_velocity)
        
        return 

    
    def update_alerted_state_alerter_pos(self, entities):
        """
        checks if entity (with oposite mode) on clostest position in pq is closer than awarness_radius
        if : updated alerted state to True, update positon of alerter
        else update alerted state to false, update position alerter to None
    
        Args:
            entities (list): list filled with all entities.   
        
        Returns:
            None: Updates self.change_alerted and self change_pos_alerter directly.
        """
        #-------human have humans and zombies in pq
        #filter for zombies i human pq
        if self.mode == "H": 
            awareness_r2 = self.param_dict["awareness_r_H"] ** 2
            
            for dist2, idx in self.pq.heap:
                other = entities[idx]
                if other.mode == "Z": 
                    if dist2 <= awareness_r2:
                        self.change_alerted(True)
                        
                        #update position of alerter
                        self.change_pos_alerter(other.pos) 
                        return
                    else: break#if closte other is not close enough all others will be to
                    
            self.change_alerted(False)
            self.change_pos_alerter(None)
            
        #--------zombies have only zombies in pq
        elif self.mode == "Z":
            awareness_r2 = self.param_dict["awareness_r_Z"] ** 2
            
            #take first position in pq
            #check if pq empty just change to false and none and done with it
            if len(self.pq.heap) != 0:
                dist2, idx = self.pq.heap[0]
                other = entities[idx]
            
                if dist2 <= awareness_r2:
                    self.change_alerted(True)
                            
                    #update position of alerter
                    self.change_pos_alerter(other.pos) 
                    return
            

             #if closte other is not close enough all others will be to
                    
            self.change_alerted(False)
            self.change_pos_alerter(None)
        
        return 
    
    
    #--------------------ZOMBIE-WALK-FINISH-RAPHAEL----------------------------
    #--------------------check_infection-START-RAPHAEL-----------------------------
    def check_infection_H(self):
        """
        Checks if a Human is close enough to a Zombie to be bitten, if so, it will change its mode to a zombie.
        
        Args: 
            None
        
        Returns:
            None: updates change_mode directly
            

            
        """
        bite_r = self.param_dict["bite_r_Z_H"]
        
        #get position alerter
        pos_alerter = self.pos_alerter
        
        distance = self.get_distance(pos_alerter) 

        if distance <= bite_r:
            self.change_mode("Z")
        return
    #--------------------check_infection-FINISH-RAPHAEL----------------------------
    
    #---------------------HUMAN-WALK-START-DIEGO-------------------------------

    def zombie_awareness(self):
        """
        checks direction of entity that alerted entity, updates velocity and direction 
        in opposite direction.

        Args:
            position_nearest_zombie [vector (?)]: coordinates of nearest zombie 

        Returns:
            none
        
        Raises:
            ValueError: If the zombie and human are at the exact same position.
        """
        

        distance = self.get_distance(self.pos_alerter)
        if distance == 0:
            raise ValueError("Division by zero in human_awareness_walk(): " \
            "Zombie and Human are at the EXACT same spot! Check function for more Information")
 
        run_direction = -(self.pos_alerter - self.pos)/distance # unit vector of direction
        self.change_velocity(run_direction*self.param_dict["max_speed_H"])


    def flocking_behavior(self, entity_list, n_humans = 4, min_distance = 1, factors = (0.3,0.2,0.2)):
        """
        flocking behavior for humans when no zombies are close to them. they include the closest few 
        humans (n_humans) in their flocking behavior. 
        
        Args:
            n_humans [int]: number of relevant humans for flocking behavior, standard is 4
            min_distance [double]: minimal distance from other humans, supposed to be in a 
            parameters set
            factors [tuple]: factors for flocking subcalculations. 
                            avoidfactor, matchingfactor and centeringfactor
        
        Returns:
            none
        
        Raises:
            Relevant Entities needs to be at least 1 for the flocking to work
        """

        relevant_entities = self.pq.heap[0:n_humans] # number of relevant objects that are looped over
        if len(relevant_entities)<1:
            raise ValueError("relevant entities is zero when it should be at least 1")
        avoidfactor, matchingfactor, centeringfactor = factors

        # average values to influence pattern
        pos_avg = np.array((0.,0.))
        vel_avg = np.array((0.,0.))

        for _,ent_idx in relevant_entities:
            other = entity_list[ent_idx]
            

            # Separation if entity is in close range
            close = np.array((0.,0.))

            if self.get_distance(other.pos)<min_distance:
                close += self.pos - other.pos
            
            # add other entities position to average position
            pos_avg += other.pos
            vel_avg += other.velocity

        # contributions of other entities
        actual_n = len(relevant_entities)
        pos_avg = pos_avg/actual_n
        vel_avg = vel_avg/actual_n


        # not sure if this is correctly implemented
        self.velocity = (self.velocity + 
                            (pos_avg-self.pos)*centeringfactor +
                            (vel_avg-self.velocity)*matchingfactor +
                            (close*avoidfactor))
                                         

    def human_walk(self, entity_list):
        """
        defines the humans walk cycle by checking if there is a zombie in the prioq or not. 
        If there is none, flocking behavior is activated, if a zombie is present, 
        zombie awareness is activated. 
        If there is none, flocking behavior is activated, if a zombie is present, 
        zombie awareness is activated & alerted state turned True for Human.
        Changes the Human direction variable in self. 

        Args: 
            None            
        
        Returns:
            none
        """
        self.update_alerted_state_alerter_pos(entity_list)
        
        if self.alerted: #full speed away
        
            pos_closest_human = self.pos_alerter
            #get vector from position zombie pointing to position human
            human_to_zombie_vector = pos_closest_human - self.pos
            
            #distance between human and zombie
            distance_between_entities = self.get_distance(pos_closest_human)
            
            #compare distance to really small float, so we never to a div by zero 
            #in the line after
            safe_distance = max(distance_between_entities, math.nextafter(0, 1.0))
            
            #get the new unit vector whichs points the zombi to the human
            new_human_direction = - human_to_zombie_vector / safe_distance
            
            max_speed_H = self.param_dict["max_speed_H"]
            self.change_velocity(new_human_direction*max_speed_H)
            
        elif not self.alerted: #everything chill
            
            if len(self.pq.heap) == 0: #human is all alone
                self.lonely_walk()
                
            else: #has friends around
                self.flocking_behavior(entity_list, n_humans = 4, min_distance = 1)
                
        return
    
    
    def lonely_walk(self):
        """
        Sets a random distance that is that humans preferred direction to walk in when they are alone. 
        This is done by calling random uniform for x and y
        """
        if self.preferred_dir is None:
            self.set_preferred_dir()

        self.change_velocity(self.param_dict["max_speed_H"] * self.preferred_dir)



    def update_location(self):
        """
        function to update location of an entity based on velocity vector

        Args: 
            timestep[double]: Timestep used to update the location of entity
        """
        self.pos += self.velocity * self.param_dict["timestep"]

        # periodic boundaries
        if self.pos[0]>=self.param_dict["x_bounds"][1]: # check upper x bound
            self.pos[0]-=self.param_dict["x_bounds"][1]
        if self.pos[0]<self.param_dict["x_bounds"][0]: # check lower x bound
            self.pos[0]+=self.param_dict["x_bounds"][1]
        if self.pos[1]>=self.param_dict["y_bounds"][1]: # check upper y bound
            self.pos[1]-=self.param_dict["y_bounds"][1]
        if self.pos[1]<self.param_dict["y_bounds"][0]: # check lower y bound
            self.pos[1]+=self.param_dict["y_bounds"][1]

        
            
    
