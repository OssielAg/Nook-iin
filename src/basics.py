import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections  as mc
from matplotlib.patches import Polygon
from typing import *
import copy
import math
import random
import re
import os
plt.style.use('default')
plt.rcParams['figure.figsize'] = (8,8)
vector2D = Tuple[float, float]
vector3D = Tuple[float, float, float]
m2x2 = List
#print('Load Basics')
#Funciones Básicas
#---------------------------Funciones para Vectores---------------------------#
def sumaV(x:vector2D, y:vector2D)->vector2D:
    """
    Computes the vector sum of two 2D vectors.

    Parameters:
        x (vector2D): First 2D vector.
        y (vector2D): Second 2D vector.

    Returns:
        vector2D: The resulting 2D vector from the sum x + y.
    """
    try:
        a,b = x
        c,d = y
        return (a+c,b+d)
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")
    

def multV(n:float,a:vector2D)->vector2D:
    """
    Multiplies a 2D vector by a scalar.

    Parameters:
        n (float): Scalar multiplier.
        a (vector2D): 2D vector to be scaled.

    Returns:
        vector2D: The scaled 2D vector.
    """
    try:
        a1,a2 = a
        return (a1*n,a2*n)
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def m2V(a:vector2D,b:vector2D,s:tuple)->vector2D:
    """
    Computes the linear combination m*a + n*b for two 2D vectors.

    Parameters:
        a (vector2D): First vector.
        b (vector2D): Second vector.
        s (tuple): Tuple of scalars (m, n).

    Returns:
        vector2D: Resulting vector from the linear combination.
    """
    try:
        m,n = s
        return sumaV(multV(m,a),multV(n,b))
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def rota(vect:vector2D, theta:float)->vector2D:
    """
    Rotates a 2D vector counterclockwise by a given angle.

    Parameters:
        vect (vector2D): The vector to rotate.
        theta (float): Angle in degrees.

    Returns:
        vector2D: The rotated vector.
    """
    try:
        ang = math.radians(theta)
        (x,y) = vect
        c,s = math.cos(ang),math.sin(ang)
        vr = ((c*x)-(s*y), (s*x)+(c*y))
        return vr
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def dist(a:vector2D, b:vector2D)->float:
    """
    Calculates the Euclidean distance between two points in 2D.

    Parameters:
        a (vector2D): First point.
        b (vector2D): Second point.

    Returns:
        float: Distance between points a and b.
    """
    try:
        a1, a2 = a
        b1, b2 = b
        return math.sqrt(((b1-a1)**2)+((b2-a2)**2))
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def long(v:vector2D)->float:
    """
    Computes the magnitude (length) of a 2D vector.

    Parameters:
        v (vector2D): The vector whose magnitude is calculated.

    Returns:
        float: Magnitude of the vector.
    """
    try:
        return dist((0,0),v)
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def cAng(u:vector2D, v:vector2D)->float:
    """
    Calculates the angle in degrees between two 2D vectors.

    Parameters:
        u (vector2D): First vector.
        v (vector2D): Second vector.

    Returns:
        float: Signed angle in degrees from u to v.
    """
    try:
        (u1,u2),(v1,v2) = u, v
        x = ((u1*v1)+(u2*v2))/(long(u)*long(v))
        th = math.degrees(math.acos(round(x,10)))
        if (u1*v2-u2*v1)<0: th=-th
        return th
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def cRot(v:vector2D)->float:
    """
    Calculates the angle between a 2D vector and the positive x-axis.

    Parameters:
        v (vector2D): The vector.

    Returns:
        float: Signed angle in degrees from the x-axis to the vector.
    """
    try:
        return cAng((1,0),v)
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def pC(a:vector3D, b:vector3D)->vector3D:
    """
    Computes the cross product of two 3D vectors.

    Parameters:
        a (vector3D): First vector.
        b (vector3D): Second vector.

    Returns:
        vector3D: The resulting vector from the cross product a × b.
    """
    try:
        a1,a2,a3 = a
        b1,b2,b3 = b
        return ((a2*b3-a3*b2),(a3*b1-a1*b3),(a1*b2-a2*b1))
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def pP(a:vector3D, b:vector3D)->float:
    """
    Computes the dot product of two 3D vectors.

    Parameters:
        a (vector3D): First vector.
        b (vector3D): Second vector.

    Returns:
        float: The scalar dot product of the vectors.
    """
    try:
        a1,a2,a3 = a
        b1,b2,b3 = b
        return a1*b1+a2*b2+a3*b3
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def to2D(v:vector3D)->vector2D:
    """
    Projects a 3D vector onto the 2D plane (xy-plane).

    Parameters:
        v (vector3D): The 3D vector.

    Returns:
        vector2D: The 2D projection (x, y).
    """
    x,y,z=v
    return (x,y)
    
def to3D(v:vector2D)->vector3D:
    """
    Converts a 2D vector into a 3D vector with z = 0.

    Parameters:
        v (vector2D): The 2D vector.

    Returns:
        vector3D: The corresponding 3D vector.
    """
    (a,b)=v
    return (a,b,0.0)
#---------------------------Funciones para matrices---------------------------#
def sumaM(A:m2x2,B:m2x2)->m2x2:
    """
    Computes the element-wise sum of two 2x2 matrices.

    Parameters:
        A (m2x2): First matrix.
        B (m2x2): Second matrix.

    Returns:
        m2x2: Resulting matrix from A + B.
    """
    try:
        C = np.array(A)+np.array(B)
        return C.tolist()
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def multM(c:float,M:m2x2)->m2x2:
    """
    Multiplies a 2x2 matrix by a scalar.

    Parameters:
        c (float): Scalar multiplier.
        M (m2x2): Matrix to scale.

    Returns:
        m2x2: Scaled matrix.
    """
    try:
        cM=c*np.array(M)
        return cM.tolist()
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

    
def VtM(v1:vector2D, v2:vector2D)->m2x2:
    """
    Constructs a 2x2 matrix from two 2D column vectors.

    Parameters:
        v1 (vector2D): First column vector.
        v2 (vector2D): Second column vector.

    Returns:
        m2x2: 2x2 matrix with v1 and v2 as columns.
    """
    try:
        (a1,a2), (b1,b2) = v1, v2
        return [[a1,b1],[a2,b2]]
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def MtV(m:m2x2)->(vector2D, vector2D):
    """
    Extracts the column vectors from a 2x2 matrix.

    Parameters:
        m (m2x2): 2x2 matrix.

    Returns:
        tuple: Two 2D vectors corresponding to the matrix columns.
    """
    try:
        [[a1,b1],[a2,b2]] = m
        return (a1,a2), (b1,b2)
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")
    
def det(m:m2x2)->float:
    """
    Computes the determinant of a 2x2 matrix.

    Parameters:
        m (m2x2): 2x2 matrix.

    Returns:
        float: Determinant of the matrix.
    """
    try:
        return (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def inv2x2(m:m2x2)->m2x2:
    """
    Calculates the inverse of a 2x2 matrix.

    Parameters:
        m (m2x2): 2x2 matrix to invert.

    Returns:
        m2x2: Inverse of the matrix.
    """
    try:
        [[a,b],[c,d]] = m
        dm = det(m)
        return [[d/dm, -b/dm], [-c/dm, a/dm]]
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def m2M(m1:m2x2, m2:m2x2)->m2x2:
    """
    Computes the matrix product of two 2x2 matrices.

    Parameters:
        m1 (m2x2): First matrix.
        m2 (m2x2): Second matrix.

    Returns:
        m2x2: Resulting matrix from m1 × m2.
    """
    try:
        [[a,b],[c,d]] = m1
        [[x,y],[z,w]] = m2
        return [[(a*x+b*z),(a*y+b*w)],[(c*x+d*z),(c*y+d*w)]]
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def transfVs(u:vector2D,v:vector2D,t:m2x2)->(vector2D,vector2D):
    """
    Applies a linear transformation represented by a matrix to two 2D vectors.

    Parameters:
        u (vector2D): First vector.
        v (vector2D): Second vector.
        t (m2x2): Transformation matrix.

    Returns:
        tuple: Transformed vectors (T(u), T(v)).
    """
    try:
        [[m,p],[n,q]] = t
        return m2V(u,v,(m,n)), m2V(u,v,(p,q))
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")


#---------------------------Funciones misceláneas-----------------------------#
def getLim(u:vector2D, v:vector2D, m:float, n:float)->(list,list):
    """
    Calculates the x and y limits of the rhombus defined by m*u and n*v.

    Parameters:
        u (vector2D): First 2D vector.
        v (vector2D): Second 2D vector.
        m (float): Scalar for vector u.
        n (float): Scalar for vector v.

    Returns:
        tuple: Lists with x and y range limits, respectively.
    """
    try:
        (a1,a2) = multV(m,u)
        (b1,b2) = multV(n,v)
        (c1,c2) = m2V(u,v,(m,n))
        xma = max(a1,b1,c1,0)
        xmi = min(a1,b1,c1,0)
        yma = max(a2,b2,c2,0)
        ymi = min(a2,b2,c2,0)
        return [xmi-1, xma+1], [ymi-1, yma+1]
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def esRotacion(a:vector2D, b:vector2D, c:vector2D, d:vector2D, eps:float=0.001):
    """
    Checks if the pair (a, b) is a rotation of the pair (c, d) within a given tolerance.

    Parameters:
        a (vector2D): First vector of the first pair.
        b (vector2D): Second vector of the first pair.
        c (vector2D): First vector of the second pair.
        d (vector2D): Second vector of the second pair.
        eps (float): Maximum allowed angle difference in degrees.

    Returns:
        bool: True if rotation match is found, False otherwise.
    """
    try:
        if abs(cAng(a,c)-cAng(b,d))<eps:
            return True
        if abs(cAng(a,d)-cAng(b,c))<eps:
            return True
        return False
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def acomoda(x, valor, lis, tamMax):
    """
    Inserts element 'x' into ordered list 'lis' by its value, maintaining order and respecting max size.

    Parameters:
        x: Element to insert.
        valor: Associated value used for ordering.
        lis (list): Target ordered list.
        tamMax (int): Maximum allowed length of list.

    Returns:
        list: Updated ordered list.
    """
    try:
        if len(lis)<tamMax:
            lis.append([x,valor])
            return lis
        for i in range(len(lis)):
            if valor<lis[i][1]:
                lis.insert(i,[x,valor])
                if len(lis)>tamMax:
                    trash=lis.pop()
                return lis
        return lis
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

#---------------Funciones auxiliares para el espacio reciproco-----------------#
def aN(a:str)->float:
    """
    Returns the atomic number of a given chemical element symbol.

    Parameters:
        a (str): Element symbol (e.g., "C", "O", "Fe").

    Returns:
        float: Atomic number, or 0.5 if not found.
    """
    elements=['H','He','Li','Be','B','C','N','O','F','Ne',
              'Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca',
              'Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn',
              'Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr',
              'Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn',
              'Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd',
              'Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb',
              'Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg',
              'Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th',
              'Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm',
              'Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds',
              'Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']
    if a in elements:
        return elements.index(a)+1
    return 0.5

def cRecip(a:vector3D, b:vector3D, c:vector3D):
    """
    Calculates the reciprocal lattice vectors for a 3D lattice.

    Parameters:
        a (vector3D): First primitive vector.
        b (vector3D): Second primitive vector.
        c (vector3D): Third primitive vector.

    Returns:
        list: List of reciprocal lattice vectors (u, v, w).
    """
    try:
        (a1,a2,a3) = a
        (b1,b2,b3) = b
        (c1,c2,c3) = c
        e = (math.pi*2)/(pP(a,pC(b,c))) #1/(pP(a,pC(b,c)))
        (x,y,z) = pC(b,c)
        u = (x*e, y*e, z*e)
        e = (math.pi*2)/(pP(b,pC(c,a))) #1/(pP(b,pC(c,a)))
        (x,y,z) = pC(c,a)
        v = (x*e, y*e, z*e)
        e = (math.pi*2)/(pP(c,pC(a,b))) #1/(pP(c,pC(a,b))) 
        (x,y,z) = pC(a,b)
        w = (x*e, y*e, z*e)
        return [u,v,w]
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def buscaEsquina(m:list, j:int, e1:int, e2:int):
    """
    Finds the row index for pivot selection in matrix operations.

    Parameters:
        m (list): Matrix to analyze.
        j (int): Current column index.
        e1 (int): First fixed row.
        e2 (int): Second fixed row.

    Returns:
        int: Row index with the optimal pivot value.
    """
    try:
        ind = -1
        val = (10.0)**300
        for i in range(8):
            if not(i==e1 or i==e2):
                if (m[i][j]>0):
                    c = m[i][10]/m[i][j]
                    if c < val:
                        val = c
                        ind = i
        return ind
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")

def opera(m:list, e:int, s:int):
    """
    Performs Gauss-Jordan-like elimination to pivot a matrix column.

    Parameters:
        m (list): Matrix to operate on.
        e (int): Pivot column index.
        s (int): Pivot row index.

    Returns:
        None
    """
    try:
        m[s] = m[s]/(m[s][e])
        for i in range(8):
            if i!=s:
                piv=m[i][e]
                m[i] = m[i]-(m[s]*piv)
    except Exception as e:
        print(f"Error {str(e)}. Check the entries")


def pmat(m):
    """
    Prints a matrix to the console with rounded formatting.

    Parameters:
        m (list): Matrix to print.

    Returns:
        None
    """
    for i in range(len(m)):
        lin = ""
        for j in range(len(m[0])):
            lin = lin+"\t"+str(round(m[i][j],2))
        print(lin)
    print("")
    
def checkP(x,y,err=0.001):
    """
    Checks whether two numbers are approximately congruent modulo 1.

    Parameters:
        x (float): First value.
        y (float): Second value.
        err (float): Tolerance for difference.

    Returns:
        bool: True if difference mod 1 is less than error.
    """
    d = abs((x%1)-(y%1))
    if d<err:
        return True
    return False
    
def dameVecinos(rv):
    """
    Returns the 8 nearest non-origin lattice vectors in reciprocal space.

    Parameters:
        rv (list): List of reciprocal lattice vectors (3D).

    Returns:
        list: List of 2D vectors nearest to the origin.
    """
    try:
        b1, b2 = to2D(rv[0]), to2D(rv[1])
        d1 = long(m2V(b1,b2,(1,1)))
        d2 = long(m2V(b1,b2,(-1,1)))
        if d1<d2:
            n = round(d2/d1)
        else:
            n = round(d1/d2)
        vec = []
        for i in range(-(2*n),(2*n)+1):
            for j in range(-(2*n),(2*n)+1):
                if (i,j)!=(0,0):
                    v = m2V(b1,b2,(i,j))
                    vec.append([v,long(v),(i,j)])
        vec=sorted(vec, key=lambda op : op[1])
        vecinos=[]
        vC=[]
        ind=0
        while len(vecinos)<8 and ind<len(vec):
            if califica(vec[ind][2],vC):
                vecinos.append(vec[ind][0])
                vC.append(vec[ind][2])
            ind+=1
        return vecinos
    except Exception as e:
        print(f"Error, {str(e)}. Check the entries")

def califica(pos, lista):
    """
    Evaluates whether a given position is visible from origin without being occluded by others.

    Parameters:
        pos (tuple): Current position to evaluate.
        lista (list): List of previously selected positions.

    Returns:
        bool: True if position is not blocked, False otherwise.
    """
    try:
        for i in range(len(lista)):
            (px,py) = pos
            (lx,ly) = lista[i]
            if px!=0:
                k=lx/px
                if k>0:
                    if ly==k*py:
                        #print("({},{}) es tapado por ({},{})".format(px,py,lx,ly))
                        return False
            elif py!=0:
                k=ly/py
                if k>0:
                    if lx==k*px:
                        #print("({},{}) es {} veces ({},{})".format(px,py,k,lx,ly))
                        return False
        return True
    except Exception as e:
        print(f"Error, {str(e)}. Check the entries")
    
def calcVerticesFBZ(rv,pnt=False):
    """
    Calculates the vertices of the First Brillouin Zone (FBZ) from a 2D projection of reciprocal lattice.

    Parameters:
        rv (list): List of 3D reciprocal lattice vectors.
        pnt (bool): Whether to print matrix operations step-by-step.

    Returns:
        tuple: List of FBZ vertex coordinates and the working matrix.
    """
    
    try:
        pts = []
        vecinos = dameVecinos(rv)
        '''[m2V(b1,b2,( 1, 0)),m2V(b1,b2,( 1, 1)),
                 m2V(b1,b2,( 0, 1)),m2V(b1,b2,(-1, 1)),
                 m2V(b1,b2,(-1, 0)),m2V(b1,b2,(-1,-1)),
                 m2V(b1,b2,( 0,-1)),m2V(b1,b2,( 1,-1))]'''
        # Creamos el espacio para la matriz en que operaremos
        v = np.array(vecinos)
        eq = np.zeros((8,11))
        et = ["V1","V2","V3","V4","V5","V6","V7","V8"]
        xy = [10,10]
        cruce = [-1,-1]
        # Damos los valores correspondientes
        for i in range(8):
            eq[i][i] = 1
            eq[i][8] = 2*v[i][0]
            eq[i][9] = 2*v[i][1]
            eq[i][10] = (v[i][0]**2) + (v[i][1]**2)
        if(pnt):pmat(eq) #---Imprime la matriz para hacer seguimiento
        # Entra valor de X
        ind = buscaEsquina(eq,8,xy[0],xy[1])
        xy[0]=ind
        cruce[0]=ind
        opera(eq,8,ind)
        if(pnt):pmat(eq) #---Imprime la matriz para hacer seguimiento
        # Entra valor de Y
        ind = buscaEsquina(eq,9,xy[0],xy[1])
        xy[1]=ind
        cruce[1]=ind
        opera(eq,9,ind)
        p = (round(eq[xy[0]][10],10),round(eq[xy[1]][10],10))
        pts.append(p)
        if(pnt):pmat(eq) #---Imprime la matriz para hacer seguimiento
        cont=0
        while True:
            cont+=1
            e = cruce[0]
            s = buscaEsquina(eq,e,xy[0],xy[1])
            opera(eq,e,s)
            if(pnt):pmat(eq) #---Imprime la matriz para hacer seguimiento
            cruce[0] = cruce[1]
            cruce[1] = s
            p2 = (round(eq[xy[0]][10],10),round(eq[xy[1]][10],10))
            if p2!=p:
                if p2==pts[0]:
                    break
                p=p2
                pts.append(p)
            if cont>10:
                break

        return pts, eq
    except Exception as e:
        print(f"Error, {str(e)}. Check the entries")
        return pts, eq
    
def F_G(e:str, G):
    """
    Computes the atomic form factor f(G) for a given element and scattering vector G.
    
    Parameters:
        e (str): Atomic symbol (e.g., "C", "Fe", "O").
        G (array): Scattering vector.
    
    Returns:
        float: Atomic form factor f(G).
    """
    elemList=['H','H1-','He','Li','Li1+','Be','Be2+','B','C','Cval','N',
              'O','O1-','F','F1-','Ne','Na','Na1+','Mg','Mg2+','Al','Al3+',
              'Siv','Sival','Si4+','P','S','Cl','Cl1-','Ar','K','K1+','Ca',
              'Ca2+','Sc','Sc3+','Ti','Ti2+','Ti3+','Ti4+','V','V2+','V3+',
              'V5+','Cr','Cr2+','Cr3+','Mn','Mn2+','Mn3+','Mn4+','Fe',
              'Fe2+','Fe3+','Co','Co2+','Co3+','Ni','Ni2+','Ni3+','Cu',
              'Cu1+','Cu2+','Zn','Zn2+','Ga','Ga3+','Ge','Ge4+','As','Se',
              'Br','Br1-','Kr','Rb','Rb1+','Sr','Sr2+','Y','Y3+','Zr','Zr4+',
              'Nb','Nb3+','Nb5+','Mo','Mo3+','Mo5+','Mo6+','Tc','Ru','Ru3+',
              'Ru4+','Rh','Rh3+','Rh4+','Pd','Pd2+','Pd4+','Ag','Ag1+',
              'Ag2+','Cd','Cd2+','In','In3+','Sn','Sn2+','Sn4+','Sb','Sb3+',
              'Sb5+','Te','I','I1-','Xe','Cs','Cs1+','Ba','Ba2+','La','La3+',
              'Ce','Ce3+','Ce4+','Pr','Pr3+','Pr4+','Nd','Nd3+','Pm','Pm3+',
              'Sm','Sm3+','Eu','Eu2+','Eu3+','Gd','Gd3+','Tb','Tb3+','Dy',
              'Dy3+','Ho','Ho3+','Er','Er3+','Tm','Tm3+','Yb','Yb2+','Yb3+',
              'Lu','Lu3+','Hf','Hf4+','Ta','Ta5+','W','W6+','Re','Os','Os4+',
              'Ir','Ir3+','Ir4+','Pt','Pt2+','Pt4+','Au','Au1+','Au3+','Hg',
              'Hg1+','Hg2+','Tl','Tl1+','Tl3+','Pb','Pb2+','Pb4+','Bi',
              'Bi3+','Bi5+','Po','At','Rn','Fr','Ra','Ra2+','Ac','Ac3+','Th',
              'Th4+','Pa','U','U3+','U4+','U6+','Np','Np3+','Np4+','Np6+',
              'Pu','Pu3+','Pu4+','Pu6+','Am','Cm','Bk','Cf']
    elemVals = [[0.489918,20.6593,0.262003,7.74039,0.196767,49.5519,0.049879,2.20159,0.001305],
                [0.897661,53.1368,0.565616,15.187,0.415815,186.576,0.116973,3.56709,0.002389],
                [0.8734,9.1037,0.6309,3.3568,0.3112,22.9276,0.178,0.9821,0.0064],
                [1.1282,3.9546,0.7508,1.0524,0.6175,85.3905,0.4653,168.261,0.0377],
                [0.6968,4.6237,0.7888,1.9557,0.3414,0.6316,0.1563,10.0953,0.0167],
                [1.5919,43.6427,1.1278,1.8623,0.5391,103.483,0.7029,0.542,0.0385],
                [6.2603,0.0027,0.8849,0.8313,0.7993,2.2758,0.1647,5.1146,-6.1092],
                [2.0545,23.2185,1.3326,1.021,1.0979,60.3498,0.7068,0.1403,-0.1932],
                [2.31,20.8439,1.02,10.2075,1.5886,0.5687,0.865,51.6512,0.2156],
                [2.26069,22.6907,1.56165,0.656665,1.05075,9.75618,0.839259,55.5949,0.286977],
                [12.2126,0.0057,3.1322,9.8933,2.0125,28.9975,1.1663,0.5826,-11.529],
                [3.0485,13.2771,2.2868,5.7011,1.5463,0.3239,0.867,32.9089,0.2508],
                [4.1916,12.8573,1.63969,4.17236,1.52673,47.0179,-20.307,-0.01404,21.9412],
                [3.5392,10.2825,2.6412,4.2944,1.517,0.2615,1.0243,26.1476,0.2776],
                [3.6322,5.27756,3.51057,14.7353,1.26064,0.442258,0.940706,47.3437,0.653396],
                [3.9553,8.4042,3.1125,3.4262,1.4546,0.2306,1.1251,21.7184,0.3515],
                [4.7626,3.285,3.1736,8.8422,1.2674,0.3136,1.1128,129.424,0.676],
                [3.2565,2.6671,3.9362,6.1153,1.3998,0.2001,1.0032,14.039,0.404],
                [5.4204,2.8275,2.1735,79.2611,1.2269,0.3808,2.3073,7.1937,0.8584],
                [3.4988,2.1676,3.8378,4.7542,1.3284,0.185,0.8497,10.1411,0.4853],
                [6.4202,3.0387,1.9002,0.7426,1.5936,31.5472,1.9646,85.0886,1.1151],
                [4.17448,1.93816,3.3876,4.14553,1.20296,0.228753,0.528137,8.28524,0.706786],
                [6.2915,2.4386,3.0353,32.3337,1.9891,0.6785,1.541,81.6937,1.1407],
                [5.66269,2.6652,3.07164,38.6634,2.62446,0.916946,1.3932,93.5458,1.24707],
                [4.43918,1.64167,3.20345,3.43757,1.19453,0.2149,0.41653,6.65365,0.746297],
                [6.4345,1.9067,4.1791,27.157,1.78,0.526,1.4908,68.1645,1.1149],
                [6.9053,1.4679,5.2034,22.2151,1.4379,0.2536,1.5863,56.172,0.8669],
                [11.4604,0.0104,7.1964,1.1662,6.2556,18.5194,1.6455,47.7784,-9.5574],
                [18.2915,0.0066,7.2084,1.1717,6.5337,19.5424,2.3386,60.4486,-16.378],
                [7.4845,0.9072,6.7723,14.8407,0.6539,43.8983,1.6442,33.3929,1.4445],
                [8.2186,12.7949,7.4398,0.7748,1.0519,213.187,0.8659,41.6841,1.4228],
                [7.9578,12.6331,7.4917,0.7674,6.359,-0.002,1.1915,31.9128,-4.9978],
                [8.6266,10.4421,7.3873,0.6599,1.5899,85.7484,1.0211,178.437,1.3751],
                [15.6348,-0.0074,7.9518,0.6089,8.4372,10.3116,0.8537,25.9905,-14.875],
                [9.189,9.0213,7.3679,0.5729,1.6409,136.108,1.468,51.3531,1.3329],
                [13.4008,0.29854,8.0273,7.9629,1.65943,-0.28604,1.57936,16.0662,-6.6667],
                [9.7595,7.8508,7.3558,0.5,1.6991,35.6338,1.9021,116.105,1.2807],
                [9.11423,7.5243,7.62174,0.457585,2.2793,19.5361,0.087899,61.6558,0.897155],
                [17.7344,0.22061,8.73816,7.04716,5.25691,-0.15762,1.92134,15.9768,-14.652],
                [19.5114,0.178847,8.23473,6.67018,2.01341,-0.29263,1.5208,12.9464,-13.28],
                [10.2971,6.8657,7.3511,0.4385,2.0703,26.8938,2.0571,102.478,1.2199],
                [10.106,6.8818,7.3541,0.4409,2.2884,20.3004,0.0223,115.122,1.2298],
                [9.43141,6.39535,7.7419,0.383349,2.15343,15.1908,0.016865,63.969,0.656565],
                [15.6887,0.679003,8.14208,5.40135,2.03081,9.97278,-9.576,0.940464,1.7143],
                [10.6406,6.1038,7.3537,0.392,3.324,20.2626,1.4922,98.7399,1.1832],
                [9.54034,5.66078,7.7509,0.344261,3.58274,13.3075,0.509107,32.4224,0.616898],
                [9.6809,5.59463,7.81136,0.334393,2.87603,12.8288,0.113575,32.8761,0.518275],
                [11.2819,5.3409,7.3573,0.3432,3.0193,17.8674,2.2441,83.7543,1.0896],
                [10.8061,5.2796,7.362,0.3435,3.5268,14.343,0.2184,41.3235,1.0874],
                [9.84521,4.91797,7.87194,0.294393,3.56531,10.8171,0.323613,24.1281,0.393974],
                [9.96253,4.8485,7.97057,0.283303,2.76067,10.4852,0.054447,27.573,0.251877],
                [11.7695,4.7611,7.3573,0.3072,3.5222,15.3535,2.3045,76.8805,1.0369],
                [11.0424,4.6538,7.374,0.3053,4.1346,12.0546,0.4399,31.2809,1.0097],
                [11.1764,4.6147,7.3863,0.3005,3.3948,11.6729,0.0724,38.5566,0.9707],
                [12.2841,4.2791,7.3409,0.2784,4.0034,13.5359,2.3488,71.1692,1.0118],
                [11.2296,4.1231,7.3883,0.2726,4.7393,10.2443,0.7108,25.6466,0.9324],
                [10.338,3.90969,7.88173,0.238668,4.76795,8.35583,0.725591,18.3491,0.286667],
                [12.8376,3.8785,7.292,0.2565,4.4438,12.1763,2.38,66.3421,1.0341],
                [11.4166,3.6766,7.4005,0.2449,5.3442,8.873,0.9773,22.1626,0.8614],
                [10.7806,3.5477,7.75868,0.22314,5.22746,7.64468,0.847114,16.9673,0.386044],
                [13.338,3.5828,7.1676,0.247,5.6158,11.3966,1.6735,64.8126,1.191],
                [11.9475,3.3669,7.3573,0.2274,6.2455,8.6625,1.5578,25.8487,0.89],
                [11.8168,3.37484,7.11181,0.244078,5.78135,7.9876,1.14523,19.897,1.14431],
                [14.0743,3.2655,7.0318,0.2333,5.1652,10.3163,2.41,58.7097,1.3041],
                [11.9719,2.9946,7.3862,0.2031,6.4668,7.0826,1.394,18.0995,0.7807],
                [15.2354,3.0669,6.7006,0.2412,4.3591,10.7805,2.9623,61.4135,1.7189],
                [12.692,2.81262,6.69883,0.22789,6.06692,6.36441,1.0066,14.4122,1.53545],
                [16.0816,2.8509,6.3747,0.2516,3.7068,11.4468,3.683,54.7625,2.1313],
                [12.9172,2.53718,6.70003,0.205855,6.06791,5.47913,0.859041,11.603,1.45572],
                [16.6723,2.6345,6.0701,0.2647,3.4313,12.9479,4.2779,47.7972,2.531],
                [17.0006,2.4098,5.8196,0.2726,3.9731,15.2372,4.3543,43.8163,2.8409],
                [17.1789,2.1723,5.2358,16.5796,5.6377,0.2609,3.9851,41.4328,2.9557],
                [17.1718,2.2059,6.3338,19.3345,5.5754,0.2871,3.7272,58.1535,3.1776],
                [17.3555,1.9384,6.7286,16.5623,5.5493,0.2261,3.5375,39.3972,2.825],
                [17.1784,1.7888,9.6435,17.3151,5.1399,0.2748,1.5292,164.934,3.4873],
                [17.5816,1.7139,7.6598,14.7957,5.8981,0.1603,2.7817,31.2087,2.0782],
                [17.5663,1.5564,9.8184,14.0988,5.422,0.1664,2.6694,132.376,2.5064],
                [18.0874,1.4907,8.1373,12.6963,2.5654,24.5651,-34.193,-0.0138,41.4025],
                [17.776,1.4029,10.2946,12.8006,5.72629,0.125599,3.26588,104.354,1.91213],
                [17.9268,1.35417,9.1531,11.2145,1.76795,22.6599,-33.108,-0.01319,40.2602],
                [17.8765,1.27618,10.948,11.916,5.41732,0.117622,3.65721,87.6627,2.06929],
                [18.1668,1.2148,10.0562,10.1483,1.01118,21.6054,-2.6479,-0.10276,9.41454],
                [17.6142,1.18865,12.0144,11.766,4.04183,0.204785,3.53346,69.7957,3.75591],
                [19.8812,0.019175,18.0653,1.13305,11.0177,10.1621,1.94715,28.3389,-12.912],
                [17.9163,1.12446,13.3417,0.028781,10.799,9.28206,0.337905,25.7228,-6.3934],
                [3.7025,0.2772,17.2356,1.0958,12.8876,11.004,3.7429,61.6584,4.3875],
                [21.1664,0.014734,18.2017,1.03031,11.7423,9.53659,2.30951,26.6307,-14.421],
                [21.0149,0.014345,18.0992,1.02238,11.4632,8.78809,0.740625,23.3452,-14.316],
                [17.8871,1.03649,11.175,8.48061,6.57891,0.058881,0,0,0.344941],
                [19.1301,0.864132,11.0948,8.14487,4.64901,21.5707,2.71263,86.8472,5.40428],
                [19.2674,0.80852,12.9182,8.43467,4.86337,24.7997,1.56756,94.2928,5.37874],
                [18.5638,0.847329,13.2885,8.37164,9.32602,0.017662,3.00964,22.887,-3.1892],
                [18.5003,0.844582,13.1787,8.12534,4.71304,0.36495,2.18535,20.8504,1.42357],
                [19.2957,0.751536,14.3501,8.21758,4.73425,25.8749,1.28918,98.6062,5.328],
                [18.8785,0.764252,14.1259,7.84438,3.32515,21.2487,-6.1989,-0.01036,11.8678],
                [18.8545,0.760825,13.9806,7.62436,2.53464,19.3317,-5.6526,-0.0102,11.2835],
                [19.3319,0.698655,15.5017,7.98929,5.29537,25.2052,0.605844,76.8986,5.26593],
                [19.1701,0.696219,15.2096,7.55573,4.32234,22.5057,0,0,5.2916],
                [19.2493,0.683839,14.79,7.14833,2.89289,17.9144,-7.9492,0.005127,13.0174],
                [19.2808,0.6446,16.6885,7.4726,4.8045,24.6605,1.0463,99.8156,5.179],
                [19.1812,0.646179,15.9719,7.19123,5.27475,21.7326,0.357534,66.1147,5.21572],
                [19.1643,0.645643,16.2456,7.18544,4.3709,21.4072,0,0,5.21404],
                [19.2214,0.5946,17.6444,6.9089,4.461,24.7008,1.6029,87.4825,5.0694],
                [19.1514,0.597922,17.2535,6.80639,4.47128,20.2521,0,0,5.11937],
                [19.1624,0.5476,18.5596,6.3776,4.2948,25.8499,2.0396,92.8029,4.9391],
                [19.1045,0.551522,18.1108,6.3247,3.78897,17.3595,0,0,4.99635],
                [19.1889,5.8303,19.1005,0.5031,4.4585,26.8909,2.4663,83.9571,4.7821],
                [19.1094,0.5036,19.0548,5.8378,4.5648,23.3752,0.487,62.2061,4.7861],
                [18.9333,5.764,19.7131,0.4655,3.4182,14.0049,0.0193,-0.7583,3.9182],
                [19.6418,5.3034,19.0455,0.4607,5.0371,27.9074,2.6827,75.2825,4.5909],
                [18.9755,0.467196,18.933,5.22126,5.10789,19.5902,0.288753,55.5113,4.69626],
                [19.8685,5.44853,19.0302,0.467973,2.41253,14.1259,0,0,4.69263],
                [19.9644,4.81742,19.0138,0.420885,6.14487,28.5284,2.5239,70.8403,4.352],
                [20.1472,4.347,18.9949,0.3814,7.5138,27.766,2.2735,66.8776,4.0712],
                [20.2332,4.3579,18.997,0.3815,7.8069,29.5259,2.8868,84.9304,4.0714],
                [20.2933,3.9282,19.0298,0.344,8.9767,26.4659,1.99,64.2658,3.7118],
                [20.3892,3.569,19.1062,0.3107,10.662,24.3879,1.4953,213.904,3.3352],
                [20.3524,3.552,19.1278,0.3086,10.2821,23.7128,0.9615,59.4565,3.2791],
                [20.3361,3.216,19.297,0.2756,10.888,20.2073,2.6959,167.202,2.7731],
                [20.1807,3.21367,19.1136,0.28331,10.9054,20.0558,0.77634,51.746,3.02902],
                [20.578,2.94817,19.599,0.244475,11.3727,18.7726,3.28719,133.124,2.14678],
                [20.2489,2.9207,19.3763,0.250698,11.6323,17.8211,0.336048,54.9453,2.4086],
                [21.1671,2.81219,19.7695,0.226836,11.8513,17.6083,3.33049,127.113,1.86264],
                [20.8036,2.77691,19.559,0.23154,11.9369,16.5408,0.612376,43.1692,2.09013],
                [20.3235,2.65941,19.8186,0.21885,12.1233,15.7992,0.144583,62.2355,1.5918],
                [22.044,2.77393,19.6697,0.222087,12.3856,16.7669,2.82428,143.644,2.0583],
                [21.3727,2.6452,19.7491,0.214299,12.1329,15.323,0.97518,36.4065,1.77132],
                [20.9413,2.54467,20.0539,0.202481,12.4668,14.8137,0.296689,45.4643,1.24285],
                [22.6845,2.66248,19.6847,0.210628,12.774,15.885,2.85137,137.903,1.98486],
                [21.961,2.52722,19.9339,0.199237,12.12,14.1783,1.51031,30.8717,1.47588],
                [23.3405,2.5627,19.6095,0.202088,13.1235,15.1009,2.87516,132.721,2.02876],
                [22.5527,2.4174,20.1108,0.185769,12.0671,13.1275,2.07492,27.4491,1.19499],
                [24.0042,2.47274,19.4258,0.196451,13.4396,14.3996,2.89604,128.007,2.20963],
                [23.1504,2.31641,20.2599,0.174081,11.9202,12.1571,2.71488,24.8242,0.954586],
                [24.6274,2.3879,19.0886,0.1942,13.7603,13.7546,2.9227,123.174,2.5745],
                [24.0063,2.27783,19.9504,0.17353,11.8034,11.6096,3.87243,26.5156,1.36389],
                [23.7497,2.22258,20.3745,0.16394,11.8509,11.311,3.26503,22.9966,0.759344],
                [25.0709,2.25341,19.0798,0.181951,13.8518,12.9331,3.54545,101.398,2.4196],
                [24.3466,2.13553,20.4208,0.155525,11.8708,10.5782,3.7149,21.7029,0.645089],
                [25.8976,2.24256,18.2185,0.196143,14.3167,12.6648,2.95354,115.362,3.58324],
                [24.9559,2.05601,20.3271,0.149525,12.2471,10.0499,3.773,21.2773,0.691967],
                [26.507,2.1802,17.6383,0.202172,14.5596,12.1899,2.96577,111.874,4.29728],
                [25.5395,1.9804,20.2861,0.143384,11.9812,9.34972,4.50073,19.581,0.68969],
                [26.9049,2.07051,17.294,0.19794,14.5583,11.4407,3.63837,92.6566,4.56796],
                [26.1296,1.91072,20.0994,0.139358,11.9788,8.80018,4.93676,18.5908,0.852795],
                [27.6563,2.07356,16.4285,0.223545,14.9779,11.3604,2.98233,105.703,5.92046],
                [26.722,1.84659,19.7748,0.13729,12.1506,8.36225,5.17379,17.8974,1.17613],
                [28.1819,2.02859,15.8851,0.238849,15.1542,10.9975,2.98706,102.961,6.75621],
                [27.3083,1.78711,19.332,0.136974,12.3339,7.96778,5.38348,17.2922,1.63929],
                [28.6641,1.9889,15.4345,0.257119,15.3087,10.6647,2.98963,100.417,7.56672],
                [28.1209,1.78503,17.6817,0.15997,13.3335,8.18304,5.14657,20.39,3.70983],
                [27.8917,1.73272,18.7614,0.13879,12.6072,7.64412,5.47647,16.8153,2.26001],
                [28.9476,1.90182,15.2208,9.98519,15.1,0.261033,3.71601,84.3298,7.97628],
                [28.4628,1.68216,18.121,0.142292,12.8429,7.33727,5.59415,16.3535,2.97573],
                [29.144,1.83262,15.1726,9.5999,14.7586,0.275116,4.30013,72.029,8.58154],
                [28.8131,1.59136,18.4601,0.128903,12.7285,6.76232,5.59927,14.0366,2.39699],
                [29.2024,1.77333,15.2293,9.37046,14.5135,0.295977,4.76492,63.3644,9.24354],
                [29.1587,1.50711,18.8407,0.116741,12.8268,6.31524,5.38695,12.4244,1.78555],
                [29.0818,1.72029,15.43,9.2259,14.4327,0.321703,5.11982,57.056,9.8875],
                [29.4936,1.42755,19.3763,0.104621,13.0544,5.93667,5.06412,11.1972,1.01074],
                [28.7621,1.67191,15.7189,9.09227,14.5564,0.3505,5.44174,52.0861,10.472],
                [28.1894,1.62903,16.155,8.97948,14.9305,0.382661,5.67589,48.1647,11.0005],
                [30.419,1.37113,15.2637,6.84706,14.7458,0.165191,5.06795,18.003,6.49804],
                [27.3049,1.59279,16.7296,8.86553,15.6115,0.417916,5.83377,45.0011,11.4722],
                [30.4156,1.34323,15.862,7.10909,13.6145,0.204633,5.82008,20.3254,8.27903],
                [30.7058,1.30923,15.5512,6.71983,14.2326,0.167252,5.53672,17.4911,6.96824],
                [27.0059,1.51293,17.7639,8.81174,15.7131,0.424593,5.7837,38.6103,11.6883],
                [29.8429,1.32927,16.7224,7.38979,13.2153,0.263297,6.35234,22.9426,9.85329],
                [30.9612,1.24813,15.9829,6.60834,13.7348,0.16864,5.92034,16.9392,7.39534],
                [16.8819,0.4611,18.5913,8.6216,25.5582,1.4826,5.86,36.3956,12.0658],
                [28.0109,1.35321,17.8204,7.7395,14.3359,0.356752,6.58077,26.4043,11.2299],
                [30.6886,1.2199,16.9029,6.82872,12.7801,0.212867,6.52354,18.659,9.0968],
                [20.6809,0.545,19.0417,8.4484,21.6575,1.5729,5.9676,38.3246,12.6089],
                [25.0853,1.39507,18.4973,7.65105,16.8883,0.443378,6.48216,28.2262,12.0205],
                [29.5641,1.21152,18.06,7.05639,12.8374,0.284738,6.89912,20.7482,10.6268],
                [27.5446,0.65515,19.1584,8.70751,15.538,1.96347,5.52593,45.8149,13.1746],
                [21.3985,1.4711,20.4723,0.517394,18.7478,7.43463,6.82847,28.8482,12.5258],
                [30.8695,1.1008,18.3481,6.53852,11.9328,0.219074,7.00574,17.2114,9.8027],
                [31.0617,0.6902,13.0637,2.3576,18.442,8.618,5.9696,47.2579,13.4118],
                [21.7886,1.3366,19.5682,0.488383,19.1406,6.7727,7.01107,23.8132,12.4734],
                [32.1244,1.00566,18.8003,6.10926,12.0175,0.147041,6.96886,14.714,8.08428],
                [33.3689,0.704,12.951,2.9238,16.5877,8.7937,6.4692,48.0093,13.5782],
                [21.8053,1.2356,19.5026,6.24149,19.1053,0.469999,7.10295,20.3185,12.4711],
                [33.5364,0.91654,25.0946,0.39042,19.2497,5.71414,6.91555,12.8285,-6.7994],
                [34.6726,0.700999,15.4733,3.55078,13.1138,9.55642,7.02588,47.0045,13.677],
                [35.3163,0.68587,19.0211,3.97458,9.49887,11.3824,7.42518,45.4715,13.7108],
                [35.5631,0.6631,21.2816,4.0691,8.0037,14.0422,7.4433,44.2473,13.6905],
                [35.9299,0.646453,23.0547,4.17619,12.1439,23.1052,2.11253,150.645,13.7247],
                [35.763,0.616341,22.9064,3.87135,12.4739,19.9887,3.21097,142.325,13.6211],
                [35.215,0.604909,21.67,3.5767,7.91342,12.601,7.65078,29.8436,13.5431],
                [35.6597,0.589092,23.1032,3.65155,12.5977,18.599,4.08655,117.02,13.5266],
                [35.1736,0.579689,22.1112,3.41437,8.19216,12.9187,7.05545,25.9443,13.4637],
                [35.5645,0.563359,23.4219,3.46204,12.7473,17.8309,4.80703,99.1722,13.4314],
                [35.1007,0.555054,22.4418,3.24498,9.78554,13.4661,5.29444,23.9533,13.376],
                [35.8847,0.547751,23.2948,3.41519,14.1891,16.9235,4.17287,105.251,13.4287],
                [36.0228,0.5293,23.4128,3.3253,14.9491,16.0927,4.188,100.613,13.3966],
                [35.5747,0.52048,22.5259,3.12293,12.2165,12.7148,5.37073,26.3394,13.3092],
                [35.3715,0.516598,22.5326,3.05053,12.0291,12.5723,4.7984,23.4582,13.2671],
                [34.8509,0.507079,22.7584,2.8903,14.0099,13.1767,1.21457,25.2017,13.1665],
                [36.1874,0.511929,23.5964,3.25396,15.6402,15.3622,4.1855,97.4908,13.3573],
                [35.7074,0.502322,22.613,3.03807,12.9898,12.1449,5.43227,25.4928,13.2544],
                [35.5103,0.498626,22.5787,2.96627,12.7766,11.9484,4.92159,22.7502,13.2116],
                [35.0136,0.48981,22.7286,2.81099,14.3884,12.33,1.75669,22.6581,13.113],
                [36.5254,0.499384,23.8083,3.26371,16.7707,14.9455,3.47947,105.98,13.3812],
                [35.84,0.484938,22.7169,2.96118,13.5807,11.5331,5.66016,24.3992,13.1991],
                [35.6493,0.481422,22.646,2.8902,13.3595,11.316,5.18831,21.8301,13.1555],
                [35.1736,0.473204,22.7181,2.73848,14.7635,11.553,2.28678,20.9303,13.0582],
                [36.6706,0.483629,24.0992,3.20647,17.3415,14.3136,3.49331,102.273,13.3592],
                [36.6488,0.465154,24.4096,3.08997,17.399,13.4346,4.21665,88.4834,13.2887],
                [36.7881,0.451018,24.7736,3.04619,17.8919,12.8946,4.23284,86.003,13.2754],
                [36.9185,0.437533,25.1995,3.00775,18.3317,12.4044,4.24391,83.7881,13.2674]]
    if e in elemList:
        ev = elemVals[elemList.index(e)]
    else:
        ev = elemVals[0]
    nG = ((np.linalg.norm(G)/(math.pi*2))/4*math.pi)**2
    if nG==0:
        return 0.01
    a = [ev[0],ev[2],ev[4],ev[6]]
    b = [ev[1],ev[3],ev[5],ev[7]]
    c = ev[8]
    f = 0
    for i in range(4):
        f+=(a[i]*math.exp(-b[i]*((nG))))
    return f+c

def reciprocalBackgroundMesh_original(rv,vl,t,b):
    """
    Constructs a mesh of reciprocal lattice points and their FBZ boundaries for plotting.

    Parameters:
        rv (list): Reciprocal lattice basis vectors.
        vl (list): FBZ vertex list.
        t (float): Line width scaling factor.
        b: Parameter defining plotting range or density.

    Returns:
        tuple: Arrays of x, y coordinates and a LineCollection object.
    """
    try:
        xs = []
        ys = []
        enls=[]
        sra, srb = to2D(rv[0]), to2D(rv[1])
        mi=inv2x2(VtM(sra, srb))
        (x1,y1),(x2,y2) = MtV(m2M(mi,[[b,b],[b,-b]]))
        (x3,y3),(x4,y4) = MtV(m2M(mi,[[-b,-b],[b,-b]]))
        x = round(max(abs(x1),abs(x2),abs(x3),abs(x4)))+1
        y = round(max(abs(y1),abs(y2),abs(y3),abs(y4)))+1
        for i in range(-x,x):
            for j in range(-y,y):
                (px,py) = m2V(sra,srb,(i,j))
                #Calcula la posición de cada centro
                xs.append(px)
                ys.append(py)
                o = sumaV((px,py),vl[len(vl)-1])
                for p in vl:#calcula las aristas de la FBZ de cada centro
                    f = sumaV((px,py), p)
                    enls.append([o, f])
                    o = f
        xs = np.array(xs)
        ys = np.array(ys)
        linkList = mc.LineCollection(np.array(enls), colors='silver', linewidths=(t/10))
        return xs, ys, linkList
    except Exception as e:
        print(f"Error, {str(e)}. Check the entries")

def bereiten():
    """
    Prepares Matplotlib with default style and figure settings for Nookiin.
    
    Returns:
    None
    """
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (8,8)
    print("Nookiin Ready-to-work")