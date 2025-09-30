from .basics import *

#print('Load Atom')
class Atom:
    """
    Class that defines an atom in the system, including its position, element type,
    drawing color, and layer level in a possible heterostructure.
    """
    def __init__(self, pos:tuple, posZ:float=0.0, color:str='black', sig:str='C', lvl:int=1):
        """
        Initializes an Atom object with spatial, visual, and descriptive properties.
    
        Parameters:
            pos (tuple): Relative 2D position of the atom in the lattice plane (x, y).
            posZ (float): Position along the c-axis (vertical stacking) of the lattice.
            color (str): Color used to draw the atom in visualizations.
            sig (str): Chemical symbol or element identifier for the atom.
            lvl (int): Layer level if the atom belongs to a multilayer system.
        """
        self.pos = pos
        self.posZ = posZ
        self.color = color
        self.sig = sig
        self.lvl = lvl
    
    def __str__(self):
        """
        Returns a string representation of the atom using its element symbol and position.
    
        Returns:
            str: A formatted string like 'C(x, y, z)'.
        """
        (x,y) = self.pos
        return self.sig + f'({x},{y},{self.posZ})'

    def setData(self, color:str='Silver', sig:str='C'):
        """
        Updates the atom's drawing color and/or element symbol.
    
        Parameters:
            color (str): New color for drawing the atom.
            sig (str): New chemical symbol for the atom.
        """
        self.color = color
        self.sig = sig
    
    def getPos(self):
        """
        Returns the 2D relative position of the atom in the lattice plane.
    
        Returns:
            tuple: Atom position as (x, y).
        """
        return self.pos
        
    def clasifica(self, loa:list):
        """
        Classifies the atom into a grouped list based on its chemical symbol.
    
        Parameters:
            loa (list): List of lists, where each sublist groups atoms of the same type.
    
        Returns:
            int: 1 if the atom was added to an existing group,
                 0 if a new group was created for it.
        """
        if len(loa)==0:
            loa.append([self])
            return 0
        for l in loa:
            if len(l)==0:
                l.append(self)
                return 1
            else:
                if l[0].sig==self.sig:
                    l.append(self)
                    return 1
        loa.append([self])
        return 0