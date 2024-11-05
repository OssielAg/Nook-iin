from .basics import *
class Atom:
    '''Class that defines an atom in the system'''
    def __init__(self, pos:tuple, posZ:float=0.0, color:str='black', sig:str='C', lvl:int=1):
        '''
        Initializes the Atom object giving its characteristics.
        pos   : Relative position of the atom projected on the plane
        posZ  : Position of the atom on the c axis of the lattice.
        color : Color with which the atom will be drawn
        sig   : Atom element identifier
        lvl   : Heterostructure layer level'''
        self.pos = pos
        self.posZ = posZ
        self.color = color
        self.sig = sig
        self.lvl = lvl
    
    def __str__(self):
        '''
        Returns a string that points to the atom using its variables 'sig' and 'pos'
        '''
        (x,y) = self.pos
        return self.sig + f'({x},{y},{self.posZ})'

    def setData(self, color:str='Silver', sig:str='C'):
        '''
        Change the color and/or sign data of the Atom.
        color: New color
        sig  : New sig'''
        self.color = color
        self.sig = sig
    
    def getPos(self):
        '''
        Return the position of the atom.'''
        return self.pos
        
    def clasifica(self, loa:list):
        '''
        Classify the Atom in a list of atoms distinguished by their sign "sig"
        loa: Ordered list of atoms.'''
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