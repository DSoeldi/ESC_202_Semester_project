import numpy as np
from entity_class import entity
from math import nextafter, inf

class cell:
    #---------------validate methods---------------
    @staticmethod
    def validate_coordinates(coords):
        if not isinstance(coords, np.ndarray): raise(TypeError)
        if not isinstance(coords[0], np.float64): raise(TypeError)
        if not isinstance(coords[1], np.float64): raise(TypeError)
        if not np.shape(coords) == (2,): raise(ValueError)
     
    @staticmethod
    def validate_entities(entities):
        if not isinstance(entities, tuple): raise(TypeError)
        for e in entities:
            if not isinstance(e, entity): raise(TypeError) 
    
    @staticmethod
    def validate_ents_idx_sort(idx_lst):
        if not isinstance(idx_lst, list): raise(TypeError)
        for i in idx_lst:
            if not isinstance(i, int): raise(TypeError)


    @staticmethod
    def validate_d_cells(d_cells):
        if not isinstance(d_cells, tuple): raise(TypeError)
        if not isinstance(d_cells[0], cell): raise(TypeError)
        if not isinstance(d_cells[0], cell): raise(TypeError)
    
    #---------------sort method--------------------
    @staticmethod
    def _sort_all_ents(all_ents):
        l = []
        for i in range(len(all_ents)):
            l.append((all_ents[i].pos[0], all_ents[i].pos[1], i))
        
        sorted_x = sorted(l, key = lambda x: x[0])
        sorted_y = sorted(l, key = lambda x: x[1])
    
        return [[e[2] for e in sorted_x], [e[2] for e in sorted_y]] # return tuples that contain only indeces of sorted entitiy lists
    

    def __init__(self, LL, RH, all_ents, ents_idx_sort = None, d_cells = None, max_ents = 6): 
        """
        pos args:
            LL (np.array((float, float))):
                the coordinates of the "Left Low" corner of the cell
                LL[0] = x, LL[1] = y
            RH (np.array((float, float))):
                the coordinates of the "Right High" corner of the cell
                RH[0] = x, RH[1] = y
            all_ents ((entity, entity, ...)):
                A tuple of entities contained within the ROOT cell

        keyword args:
            enteties_idx_sort (((int, int, ...), (int, int, ...))):
                A tuple of 2 tuples of indexes of all entities contained within THIS cell, the 1st sorted (ascending) by their x coordinates, the 2nd by their y coordinates
            d_cells ((cell, cell)):
                tuple containing both daughter cells (d_cells[0]: left or lower cell, d_cells[1]: right or higher) 
                if cell is a leaf cell, d_cells == None
            max_ents (int):
                Maximum amount of entities allowed per cell. Default is 6.
        """

        # sort the all_ents list (only necessary for root cell), all other cells will adapted forms of these lists from mother cell 
        if ents_idx_sort == None: ents_idx_sort = self._sort_all_ents(all_ents)
        
        self.LL = LL
        self.RH = RH
        self.all_ents = all_ents
        self.ents_idx_sort = ents_idx_sort
        self.d_cells = d_cells

        # validate input
        self.validate_coordinates(LL)
        self.validate_coordinates(RH)
        self.validate_entities(all_ents)
        self.validate_ents_idx_sort(ents_idx_sort[0])
        self.validate_ents_idx_sort(ents_idx_sort[1])
        if d_cells != None: self.validate(d_cells)
    
    def __repr__(self):
        return f"cell({self.LL, self.RH}, # entities: {len(self.ents_idx_sort[1])},\n children: {self.d_cells})"
    
    def isleaf(self):
        """
        returs True if cell is a leaf cell (has no daughter cells), False otherwise
        """
        return not self.d_cells
    

    def compute_ents_idx_sort_d_cell(self, part_side, d_cell):
        """
        Computes the sorted entity list for both daughter cells.
        
        Args:
            self (cell):
                cell for which to compute daughter cells
            part_side (int: 0 or 1):
                indicates in which direction to partition mother cell. 0 correspons to x-direction and 1 to y-direction
            d_cell (int: 1 or 2)
                interger corresponding to which daughter cell is computed: 1 refers to lower/left cell, 2 refers to right/upper cell
        
        Returns: 
            [[int, int, ...], [int, int, ...]]
            A list of 2 lists of indexes of all entities contained within THIS cell, the 1st sorted (ascending) by their x coordinates, the 2nd by their y coordinates
        """
        n = len(self.ents_idx_sort[0])
        start = 0 if d_cell == 1 else n//2 
        end = n//2 if d_cell == 1 else None 

        ents_idx_sort_d_cell = [0, 0]
        ents_idx_sort_d_cell[part_side] = self.ents_idx_sort[part_side][start:end]
        ents_idx_sort_d_cell[abs(part_side - 1)] = [i for i in self.ents_idx_sort[abs(part_side - 1)] if i in ents_idx_sort_d_cell[part_side]]

        return ents_idx_sort_d_cell

    def compute_corner_d_cell_1(self, corner, part_side, ents_idx_sort_d_cell):
        """
        calculates corner coordinates for 1st daughter cells: left or lower

        Args:
            self (cell):
                cell for which to compute daughter cells
            corner (str: "RH" or "LL"):
                indicating which corner coordinates are being computed
            part_side (int: 0 or 1):
                indicates in which direction to partition mother cell. 0 correspons to x-direction and 1 to y-direction
            ents_idx_sort_d_cell (int, int, ...):
                list of indexes of all entities contained within the daughter cell sorted corresponding to part_side 
        
        Returns:
            np.ndarray((float,float)) contianing x & y coordinates of the computed corner for the daughter cell
        """
        coords = np.zeros((2,))
        coords[part_side] = self.LL[part_side] if corner == "LL" else self.all_ents[ents_idx_sort_d_cell[-1]].pos[part_side]
        coords[abs(part_side - 1)] = self.LL[abs(part_side - 1)] if corner == "LL" else self.RH[abs(part_side - 1)]

        return coords
    
    def compute_corner_d_cell_2(self, corner, part_side, ents_idx_sort_d_cell):
        """
        calculates corner coordinates for 2nd daughter cells: right or upper

        Args:
            self (cell):
                cell for which to compute daughter cells
            corner (str: "RH" or "LL"):
                indicating which corner coordinates are being computed
            part_side (int: 0 or 1):
                indicates in which direction to partition mother cell. 0 correspons to x-direction and 1 to y-direction
            ents_idx_sort_d_cell [int, int, ...]:
                list of indexes of all entities contained within the daughter cell sorted corresponding to part_side 
        
        Returns:
            np.ndarray((float,float)) contianing x & y coordinates of the computed corner for the daughter cell
        """
        coords = np.zeros((2,))
        coords[part_side] = nextafter(self.all_ents[ents_idx_sort_d_cell[-1]].pos[part_side], inf) if corner == "LL" else self.RH[part_side] 
        coords[abs(part_side - 1)] = self.LL[abs(part_side - 1)] if corner == "LL" else self.RH[abs(part_side - 1)]

        return coords

    def partition(self):
        """
        Recursive Partition algorithm. Partitions al cell until it contains no more than 6 entities.
        """
        # teilt sobald >= n_entities//2 auf einer Seite sind (also bei x > 6 entities in einer Zelle 
        # geht sie von kleinster koordinate aus und setzt die Grenze genau dort wo die "kleinere" Hälfte endet)
        
        if len(self.ents_idx_sort[0]) <= 6: return # no daughter cells have to be created as we reached 
        
        # else we decide in which direction we will divide
        part_side = 0 if abs(self.LL[0] - self.RH[0]) >= abs(self.LL[1] - self.RH[1]) else 1 # if both sides have same length, cell will divide in x (= 0)
        
        # defining daughter cells
        ents_idx_sort_d_cell_1 =  self.compute_ents_idx_sort_d_cell(part_side, 1)
        ents_idx_sort_d_cell_2 =  self.compute_ents_idx_sort_d_cell(part_side, 2)

        self.d_cells = (cell(LL = self.compute_corner_d_cell_1("LL", part_side, ents_idx_sort_d_cell_1[part_side]),
                             RH = self.compute_corner_d_cell_1("RH", part_side, ents_idx_sort_d_cell_1[part_side]),
                             all_ents = self.all_ents,
                             ents_idx_sort = ents_idx_sort_d_cell_1), 
                        cell(LL = self.compute_corner_d_cell_2("LL", part_side, ents_idx_sort_d_cell_1[part_side]),
                             RH = self.compute_corner_d_cell_2("RH", part_side, ents_idx_sort_d_cell_1[part_side]),
                             all_ents = self.all_ents,
                             ents_idx_sort = ents_idx_sort_d_cell_2)
                             )
        # recursive calls
        self.d_cells[0].partition()
        self.d_cells[1].partition()