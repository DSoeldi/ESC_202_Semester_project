from heapq import *
import numpy as np

class pq:
    @staticmethod
    def validate_k():
        pass

    @staticmethod
    def validate_k():
        pass

    def __init__(self, k):
        """
        Stores k best (nearest) candidates; heap[0] is the current worst among them.

        Args: 
            k (int):
                ????????????????
        """
        self.heap = []
        sentinel = (-np.inf, None) # starter value (infinitely far away, so that any entity found will intially be "close enough")

        # find a way to not store k nearest, but all nearest within x distance!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # this has to be chnaged somehow!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        for i in range(k):
            heappush(self.heap, sentinel) # pushes the new element (sentinel) to a place in the binary tree structure of a heap wich is valid
    
    def replace(self, dist2, ent_idx):
        """
        Replaces current worst element among the k kept ones in the heap.

        Args:
            self (pq): 
                pq instance for which to change heap
             dist2 ():
                distance**2 between the entity to which this pq belongs and ent_idx (- distance of entity to query entity)
             ent_idx (int):
                index of the entity within entities, which was added to the heap
        
        Returns:
            None
        """
        heapreplace(self.heap, (-dist2, ent_idx))

    def key(self):
        """
        Returns the current "cutoff" key, largest dist**2 within current heap = kth nearest neighbour
        Equals to maximum search radius.
        """
        return -self.heap[0][0] # key = - dist2 (we want a max heap!)
    
    def __str__(self):
        """Function for printing the Priotity queue."""
        return f"pq({self.heap})"



