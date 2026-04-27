#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:02:14 2026

@author: raphaeltarabinicastellani
"""



import unittest 
from classes.entity_class import entity
import numpy as np
from classes.priority_queue_class import prio_q
from unittest.mock import MagicMock
import pytest

class test_entity(unittest.TestCase):
    #------------------------random walk tests---------------------------------------

    def test_that_random_walk_changes_direction_of_velocity(self):
        """test if random walk changes direction of velocity of zombie"""
        subject = make_subject(pos=(0, 0), velocity=(10, 0), heap_entries = None)
        subject.param_dict = {"walking_speed_Z": 2.0, "smooth_rand_walk": 1}
        #--
        
        sub_direction_before = subject.get_direction()
        subject.random_walk()
        sub_direction_after = subject.get_direction()
        
        assert not np.array_equal(sub_direction_before, sub_direction_after), "entity should change direction"
        
    def test_that_random_walk_changes_speed_of_velocity_to_zombi_speed(self):
        """test if random walk changes speed of velocity of zombie"""
        subject = make_subject(pos=(0, 0), velocity=(10, 8), heap_entries = None)
        subject.param_dict = {"walking_speed_Z": 2.0, "smooth_rand_walk": 1}
        #--
        subject.random_walk()
        #--
        speed_after = subject.get_speed()

        assert speed_after == subject.param_dict["walking_speed_Z"], "entity should have walking_speed_Z speed after walk"
        
    def test_that_entiy_makes_a_random_walk_with_smooth_factor(self):
        """new direction should have an angle to the right and left not more than smoothing factor of x pi"""
        #
        subject = make_subject(pos=(0, 0), velocity=(10, 0), heap_entries = None)
        for factor in np.arange(0.0, 1.3,0.1):
            angles = []
            for _ in range(1000):
                #if you make alot of walks the anges should be a uniform distribution from -pi to plus pi
                subject.param_dict = {"walking_speed_Z": 2.0, "smooth_rand_walk": factor}
                #--
                #1 get old direction
                #2calc new velocity, get new direction
                #3get angle between new direction and old direction
                #4this angle should be uniform random
                
                #1
                old_dir =  subject.get_direction()
                
                #2
                subject.random_walk()
                new_dir = subject.get_direction()
                
                #3
                # Returns angle from -180 to 180 degrees
                angle_rad = np.arctan2(old_dir[0]*new_dir[1] - old_dir[1]*new_dir[0], np.dot(old_dir, new_dir))
                
                #4
                angles.append(angle_rad)
                
            # Statistical checks
            # For a uniform distribution U(-pi x smooth_factor, pi x smooth_factor):
            expected_mean = 0
            actual_mean = np.mean(angles)

            assert actual_mean == pytest.approx(expected_mean, abs=0.2), "mean of choosen radians of random walk should be about zero"
            #also should break logic the angles
            assert min(angles) >= -np.pi * subject.param_dict["smooth_rand_walk"], "random walk angle is outside of einschränkung"
            assert max(angles) <= np.pi  * subject.param_dict["smooth_rand_walk"], "random walk angle is outside of einschränkung"
            if factor == 0.0:
                assert actual_mean == 0.0, "if smooth factor 0, angle should be zero, straight walk"

    #-------------------------zombie_walk tests--------------------
    def test_zombie_chases_human_when_alerted(self):
        """Tests if the zombie moves directly toward a human at max speed."""
    
        #position zombie
        subject = make_subject(pos=(0, 0), velocity=(0, 0), heap_entries = None)
        subject.alerted = True
        subject.pos_alerter = np.array((3.0, 4.0))
        
        subject.param_dict = {
            "awareness_r_Z": 10.0,
            "max_speed_Z": 5.0  
        }
        
        # mock the awareness check so it doesn't overwrite our 'subject.alerted = True'
        subject.update_alerted_state_alerter_pos = MagicMock()
        
        # Action
        subject.zombie_walk([])
        
        # Calculation: 
        # Direction vector is (3,4) / 5 = (0.6, 0.8)
        # Velocity should be direction * speed (5.0) = (3.0, 4.0)
        expected_velocity = np.array([3.0, 4.0])

        
        assert expected_velocity == pytest.approx(subject.velocity), "zombi should redirect velocity to clostest human"
        subject.random_walk.assert_not_called(), "random walk should be called when alerted"
    
    def test_zombie_wanders_when_not_alerted(self):
        """Tests if zombie calls random_walk when no humans are detected."""
        subject = make_subject(pos=(0, 0), velocity=(0, 0), heap_entries = None)
        subject.alerted = False
        subject.update_alerted_state_alerter_pos = MagicMock()
        
        # We mock random_walk to see if it gets called
        subject.random_walk = MagicMock()
        
        subject.params = {"awareness_r_Z": 10.0, "smooth_rand_walk": 0.5}
        #call the walk
        subject.zombie_walk([])
        
        # Assert that random_walk was the fallback behavior
        subject.random_walk.assert_called_once_with()
        
    #---------------------update_alerted_state_alerter_pos tsts ----------------
    def test_update_alerted_true_when_within_radius(self):
        pass
    
    def test_update_alerted_false_when_outside_radius(self):
        pass


        
#-------------------------------
def make_entity(pos, velocity):
    """Creates a minimal mock entity with position and velocity."""
    e = MagicMock()
    e.pos = np.array(pos, dtype=float)
    e.velocity = np.array(velocity, dtype=float)
    return e

def make_subject(pos, velocity, heap_entries=None):
    subject = make_entity(pos, velocity)
    subject.pq = MagicMock()
    subject.pq.heap = heap_entries if heap_entries is not None else []
    
    #Initialize an empty dict so the real code doesn't crash 
    # when it looks for self.param_dict
    subject.param_dict = {}
    
    #This gives the function "Memory" (for asserts) and "Logic" (the real code)
    subject.random_walk = MagicMock(side_effect=lambda: entity.random_walk(subject))
    subject.zombie_walk = MagicMock(side_effect=lambda ents: entity.zombie_walk(subject, ents))
    
    # Helpers
    subject.get_direction = lambda: entity.get_direction(subject)
    subject.get_speed = lambda: entity.get_speed(subject)
    subject.change_velocity = lambda v: setattr(subject, 'velocity', v)
    subject.get_distance = lambda other_pos: np.linalg.norm(subject.pos - other_pos)
    
    return subject

#------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
    
    