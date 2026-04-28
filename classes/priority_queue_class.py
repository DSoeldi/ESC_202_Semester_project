from heapq import *

class prio_q:

    @staticmethod
    def validate_push_item(item):
        if not isinstance(item, tuple): raise(TypeError)
        if not isinstance(item[0], float): raise(TypeError)
        if item[0] < 0: raise(ValueError)
        if not isinstance(item[1], int): raise(TypeError)

    def __init__(self):
        """
        Stores candidates within entity's awareness radius; heap[0] is the current nearest among them.
        """
        self.heap = []
    
    def push(self, item):
        """
        pushes ent = (dist2, ent_idx) to a place in the binary tree structure of a heap which is valid
            Args:
                ent ((float, int)):
                    Tuple containing negative distance of query entity to the one this pq belongs to and it's index within the entities list ((-dist2, ent_idx))
            Returns: 
                None
        """
        self.validate_push_item(item)
        heappush(self.heap, item)  

    def key(self):
        """
        Returns the current nearest key, smallest dist**2 within current heap == nearest neighbour
        """
        return self.heap[0][0] # key = dist2
    
    def __str__(self):
        """Function for printing the Priotity queue."""
        return f"pq({self.heap})"
    
    def __eq__(self, other):
        if not isinstance(other, prio_q): return NotImplemented
        return self.heap == other.heap



