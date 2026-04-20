#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:02:14 2026

@author: raphaeltarabinicastellani
"""



import unittest 
from entity_class import entity
from  Initialization_functions import create_parameter_dict, Initialize_entities
import numpy as np



    # def random_walk(self):
    #     """
    #     Adjusts the zombie's velocity with a random walk.
    
    #     Args:
    #        None
    
    #     Returns:
    #         None: Updates self.velocity directly.
    #     """

    #     ##INFO
    #     #redirect the velocity direction according to the random walk without
    #     #changing the speed of the vector
        
        
    #     #choose a random angle (radians) in a full circle
    #     theta = rng.uniform(0, np.pi * 2)
        
    #     #new_direction has to be a unit vector
    #     new_direction = np.array([np.cos(theta), np.sin(theta)])
        
    #     #Scale new_direction by the current speed
    #     new_velocity = self.get_speed() * new_direction
        
    #     #update
    #     self.change_velocity(new_velocity)
        
    #     return 


class TestEntity(unittest.TestCase):
       #want to test
    #1. the magnitude of the velocity has to remain the same
    #2. the direction of the velocity has to be a unit vector
    #3.new velocity has to be the same type as input velocity
    
    def define_entities(self):
        human0 = entity("Z", np.array((1.0,2.0)), {"key": "value"}, 3, np.array((1.5,1.8)), alerted = True, pos_alerter = np.array((8.3, 1.0)))
        zombie1 = entity("Z", np.array((4.0,5.0)), {"key": "value"}, 2, np.array((1.6,1.0)), alerted = False, pos_alerter = np.array((4.3, 1.0)))
        return human0, zombie1
    
    def test_random_w_magnitude_remains_the_same(self):
        human0.random_walk()
        
        self.assert()
    
    def test_random_w_direction_remains_unit_vector(self):
        human0, zombie1 = self.define_entities()
        self.assert()
        
    def test_random_w_type_velocity_remains_the_same(self):
        human0, zombie1 = self.define_entities()
        Self.assert()
        

#------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()git branch -D