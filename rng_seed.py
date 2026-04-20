import numpy as np


# Create ONCE a generator instance globaly
#everytime you use rng, it will give you a different starting point/seed

rng = np.random.default_rng(seed=48)