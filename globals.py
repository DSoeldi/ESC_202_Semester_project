#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:18:46 2026

@author: raphaeltarabinicastellani
"""

import numpy as np

#---TEMPORARY-NOTES-RAPHAEL---
# when you need to use a random number just import globals file and use rng like this
#from globals import rng
#e.g. random_number_for_random_walk = rng.random()
#and we will not have to worry that we will use the same random numbers because
#of seeds we set and imported
#-----------------------------

# Create ONCE a generator instance globaly
#everytime you use rng, it will give you a different starting point/seed

rng = np.random.default_rng(seed=48)

