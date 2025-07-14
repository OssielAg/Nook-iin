from Lattice import *
#print('Load Functions')

# Métodos derivados

def isitin(r:Lattice, cent:vector2D, sr:Lattice, slvl:float):
    '''
    Determines which atoms from the cell of lattice 'r' positioned at 'cent'
    fall within the primitive cell (PC) of the lattice 'sr'.

    Parameters:
    r     : Lattice being evaluated
    cent  : Position of the origin of the evaluated cell
    sr    : Heterostructure lattice
    slvl  : Layer level of the evaluated lattice

    Atoms from 'r' that fall inside the PC of 'sr' are added to the atomic basis
    of 'sr', assigning them to the specified layer level.
    '''
    try:
        er = 1/(10**3) #Error de calculo aceptable en la frontera de la CP de sr
        (u1,u2) = r.a
        (v1,v2) = r.b
        (p1,p2) = sr.a
        (q1,q2) = sr.b
        eq0 = (p2*q1)-(p1*q2)
        eq1 = (q1*u2)-(q2*u1)
        eq2 = (q1*v2)-(q2*v1)
        eq3 = (p2*u1)-(p1*u2)
        eq4 = (p2*v1)-(p1*v2)
        for c in r.atms:# Iteramos en cada lista de Átomos de la Red r
            nc=[]
            for a in c:# Iteramos en cada átomo de la lista c
                (x,y) = sumaV(cent,a.pos)
                # Calculamos la posición del átomo relativas a los VPs de sr
                nx = (eq1*x+eq2*y)/eq0 
                ny = (eq3*x+eq4*y)/eq0
                # Evaluamos si se encuentra dentro de la Celda mínima de sr
                if (nx<(1+er) and nx>(0-er)) and (ny<(1+er) and ny>(0-er)):
                    aPosZ = ((a.posZ*r.detachment)+slvl)/sr.detachment
                    nAtm = Atom((nx,ny),posZ = aPosZ ,color=a.color,sig=a.sig,lvl=slvl)
                    #print("Agregado átomo",nAtm)
                    nAtm.clasifica(sr.atms)
        for e in r.enls:
            (x1,y1) = sumaV(cent,e[0])
            (x2,y2) = sumaV(cent,e[1])
            (ox,oy) = ((eq1*x1+eq2*y1)/eq0,(eq3*x1+eq4*y1)/eq0)
            (fx,fy) = ((eq1*x2+eq2*y2)/eq0,(eq3*x2+eq4*y2)/eq0)
            if (ox<1+er and ox>0-er) and (oy<1+er and oy>0-er):
                sr.enls.append([(ox,oy),(fx,fy)])
        return 1
    except Exception as e:
        print(f"Error:{str(e)}.")

def megeCut(r:Lattice, sr:Lattice, lvl:int=0):
    '''
    Auxiliary method used in the construction of supercells.

    Parameters:
    r   : Lattice being evaluated
    sr  : Heterostructure lattice
    lvl : Layer level of the evaluated lattice

    Determines the unit cells of lattice 'r' that contribute atoms
    to the primitive cell of the composite system and integrates them.
    '''
    try:
        (u1,u2), (v1,v2) = r.getVectors()
        (p1,p2), (q1,q2) = sr.getVectors()
        np1 = ((p2*v1)-(p1*v2))/((u2*v1)-(u1*v2))
        np2 = ((p1*u2)-(p2*u1))/((u2*v1)-(u1*v2))
        nq1 = ((q2*v1)-(q1*v2))/((u2*v1)-(u1*v2))
        nq2 = ((q1*u2)-(q2*u1))/((u2*v1)-(u1*v2))
        npq1 = np1+nq1
        npq2 = np2+nq2
        lu = [round(min(np1,nq1,npq1,0)-1),round(max(np1,nq1,npq1,0)+1)]
        lv = [round(min(np2,nq2,npq2,0)-1),round(max(np2,nq2,npq2,0)+1)]
        for i in range(lu[1]-lu[0]):
            a = i+lu[0]
            for j in range(lv[1]-lv[0]):
                b = j+lv[0]
                isitin(r,(a,b),sr,lvl)
        return 1
    except Exception as e:
        print(f"Error:{str(e)}.")

def cleanA(r:Lattice, err:float=0.001):
    '''
    Removes duplicate atoms from the atomic basis of a lattice.

    Parameters:
    r   : Lattice whose atomic basis will be cleaned
    err : Threshold distance to consider atoms as duplicates

    Returns:
    List of atoms that were removed due to redundancy.
    '''
    try:
        atms=r.atms
        newAtms=[]
        cont=0
        for loa in atms:
            lc=loa.copy()
            for i in range(len(loa)):
                l2 = loa[i+1:]
                for a in l2:
                    if a.posZ == loa[i].posZ:
                        (x1,y1) = loa[i].pos
                        (x2,y2) = a.pos
                        if checkP(x1,x2,err):
                            if checkP(y1,y2,err):
                                cont+=1
                                lc.remove(loa[i])
                                break
            newAtms.append(lc)
        r.atms=newAtms
        return 1
    except Exception as e:
        print(f"Error:{str(e)}.")

def superMesh(sa:vector2D, sb:vector2D, layerList:list):
    '''
    Constructs the superlattice resulting from stacking multiple layers.

    Parameters:
    sa        : Superlattice primitive vector a
    sb        : Superlattice primitive vector b
    layerList : List of Lattice objects forming the heterostructure

    Returns:
    A Lattice object representing the full heterostructure using vectors sa and sb.
    '''
    try:
        sR = Lattice(sa,sb)
        sR.enls = []
        detachment = 0
        for l in layerList:
            detachment = detachment + l.detachment
        sR.detachment = detachment
        sR.prof=0
        newName="SuperLattice"
        i=0
        for m in layerList:
            megeCut(m, sR, lvl=i)
            sR.prof=sR.prof+m.prof
            newName=newName+" ["+m.name+"]"
            i = i + m.detachment
        elim = cleanPCell(sR)
        sR.name = newName
        sR.layerList = layerList
        sR.aff = sR.loAtms()
        return sR
    except Exception as e:
        print(f"Error:{str(e)}.")

def pts(layer:Lattice, max_it:int=15):
    '''
    Generates a list of lattice points within a defined region.

    Parameters:
    layer  : Lattice whose points will be generated
    max_it : Maximum number of unit cell repetitions in each direction

    Returns:
    List of points corresponding to repeated cells within the given bounds.
    '''
    try:
        res = []
        a,b = layer.getVectors()
        for k in range(1,(max_it*2)-1):
            for i in range(min(max_it,k+1)):
                j=k-i
                if j<max_it:
                    res.append([[[i,-j],m2V(a,b,(i,-j))],0.0])
                    if j!=0:
                        res.append([[[i,j],m2V(a,b,(i,j))],0.0])
        return res
    except Exception as e:
        print(f"Error:{str(e)}.")

def calcCD(substrate:Lattice, layer:Lattice, ab:list):
    '''
    Approximates a lattice point from one lattice in another lattice's coordinate system.

    Parameters:
    substrate : Reference lattice
    layer     : Lattice to be approximated
    ab        : Tuple (a, b) representing a lattice point in 'substrate'

    Returns:
    Tuple (c, d) such that the point (c, d) in 'layer' is closest to (a, b) in 'substrate'.
    '''
    try:
        (a,b) = ab
        (u_1,u_2), (v_1,v_2) = substrate.getVectors()
        (p_1,p_2), (q_1,q_2) = layer.getVectors()
        eq0 = (p_2*q_1)-(p_1*q_2)
        eq1 = (q_1*u_2)-(q_2*u_1)
        eq2 = (q_1*v_2)-(q_2*v_1)
        eq3 = (p_2*u_1)-(p_1*u_2)
        eq4 = (p_2*v_1)-(p_1*v_2)
        c = ((eq1*a)+(eq2*b))/(eq0)
        d = ((eq3*a)+(eq4*b))/(eq0)
        return (round(c),round(d))
    except Exception as e:
        print(f"Error:{str(e)}.")
    
def calcPR(pts:list, substrate:Lattice, layer:Lattice, eps:float=0.05):
    '''
    Filters a list of lattice points, keeping only those that match between two lattices.

    Parameters:
    pts       : List of candidate lattice points
    substrate : Reference lattice
    layer     : Lattice to compare
    eps       : Tolerance for matching in projected coordinates

    Returns:
    Filtered list of points that exist in both lattices within the allowed error.
    '''
    try:
        (u,v), (p,q) = substrate.getVectors(), layer.getVectors()
        (u_1,u_2), (v_1,v_2) = u, v
        (p_1,p_2), (q_1,q_2) = p, q
        res = []
        eq0 = (p_2*q_1)-(p_1*q_2)
        eq1 = (q_1*u_2)-(q_2*u_1)
        eq2 = (q_1*v_2)-(q_2*v_1)
        eq3 = (p_2*u_1)-(p_1*u_2)
        eq4 = (p_2*v_1)-(p_1*v_2)
        for pt in pts:
            [a,b] = pt[0][0]
            c = ((eq1*a)+(eq2*b))/(eq0)
            d = ((eq3*a)+(eq4*b))/(eq0)
            #Vector esperado
            r1 = pt[0][1]
            #Vector aproximado
            r2 = m2V(p,q,(round(c),round(d)))
            err = dist(r1,r2)/(long(r1))
            #err = math.sqrt((dist(r1,r2)**2)/(3*long(r1)))
            if err<=eps:
                newErr = pt[1]+err
                res = acomoda(pt[0],newErr,res,len(pts))
        return res
    except Exception as e:
        print(f"Error:{str(e)}.")
    
def commonVs(redes:list, max_val:int=15, eps:float=0.05):
    '''
    Finds common lattice points across all lattices in a multilayer system.

    Parameters:
    redes    : List of Lattices forming the heterostructure
    max_val  : Search area bound in lattice units
    eps      : Error tolerance for matching projections

    Returns:
    List of common lattice points shared across all lattices.
    '''
    try:
        if len(redes)>1:
            sustrato = redes[0]
            #Calcula todos los Puntos de Red de la capa 0 para el rango indicado por max_val
            puntos = pts(sustrato, max_it=max_val)
            #En cada capa actualiza la lista de Puntos de red dejando los puntos que coinciden, con
            #un error inferor a eps, con algún punto de red para la red en la capa actual 
            for i in range(1,len(redes)):
                puntos = calcPR(puntos, sustrato, redes[i], eps=eps)
            pr = [[p[0][0],p[1]/(len(redes)-1)] for p in puntos]
            return sorted(pr, key=lambda op : op[1])
        return []
    except Exception as e:
        print(f"Error:{str(e)}.")

def corresponding_points(l1:Lattice, l2:Lattice, M1:m2x2):
    '''
    Computes the matrix that maps lattice points from 'l1' to corresponding points in 'l2'.

    Parameters:
    l1 : First lattice
    l2 : Second lattice
    M1 : Matrix defining a cell in lattice 'l1'

    Returns:
    Matrix representing the corresponding cell in 'l2'.
    '''
    a1, b1 = MtV(M1)
    a2, b2 = (calcCD(l1,l2,a1),calcCD(l1,l2,b1))
    return VtM(a2,b2)
    
def calc_dd(V_i:m2x2, V_o:m2x2):
    '''
    Computes the degree of distortion between two lattice cells.

    Parameters:
    V_i : Initial 2x2 matrix of primitive vectors
    V_o : Final 2x2 matrix of primitive vectors (after deformation)

    Returns:
    Degree of distortion (as scalar or matrix, depending on implementation).
    '''
    try:
        dd = 0.0
        t = 10
        a_i, b_i = MtV(V_i)
        a_o, b_o = MtV(V_o)
        c = 0
        for i in range(t):
            for j in range(t):
                c += 1
                r1 = m2V(a_i,b_i,(i/t,j/t))
                r2 = m2V(a_o,b_o,(i/t,j/t))
                d = long(r1)
                div = 10**(-10) if d == 0.0 else d
                err = dist(r1,r2)/(2*div)
                dd+=err
        return dd/c
    except Exception as e:
        print(f"Error:{str(e)}.")
        
#--------------Funciones Auxilares para quitar átomos repetidos de una red---------------
def esClon(Atms: list, atm: Atom, eps: float):
    '''
    Determine whether the atom `atm` is a duplicate (clone) of any atom in `Atms`.

    Parameters:
    Atms : list
        List of existing Atom instances to compare against.
    atm : Atom
        Atom to be evaluated as a potential duplicate.
    eps : float
        Maximum allowed difference in distance and z-position to consider atoms as equivalent.

    Returns:
    bool
        True if the atom is considered a clone; False otherwise.
    '''
    for a in Atms:
        if abs(a.posZ-atm.posZ)<eps:
            d = abs(1-dist(atm.pos,a.pos))
            #print(f'\t{a.pos}:{d:.8f}')
            if d<eps:
                #print('****Es Clon****')
                return True
    return False

def borders(Atms: list):
    '''
    Identify atoms positioned on the boundary of the unit cell.

    Parameters:
    Atms : list
        List of Atom instances positioned relative to a unit cell.

    Returns:
    list
        List of Atom instances located at the boundaries (x ≈ 0 or y ≈ 0).
    '''
    orilla=[]
    for a in Atms:
        x, y = a.pos
        if x<0.001 or y<0.001:
            orilla.append(a)
    return orilla

def cleanA(Atms: list, eps: float):
    '''
    Remove atoms considered redundant due to overlap at the boundaries of a unit cell.

    Parameters:
    Atms : list
        List of Atom instances located in a primitive cell.
    eps : float
        Tolerance value for determining redundancy based on position and height (z-axis).

    Returns:
    list
        List of Atom instances that were removed as duplicates.
    '''
    repetidos=[]
    orilla = borders(Atms)
    #print(f'{len(orilla)} átomos en frontera')
    for a in Atms:
        x, y = a.pos
        if abs(1-x)<0.01 or abs(1-y)<0.01:
            #print(f'\nAnalizando {a}')
            if esClon(orilla,a,eps):
                repetidos.append(a)
                #print(f'***Se elimina {a}')
    for a in repetidos:
        Atms.remove(a)
    return repetidos

def cleanPCell(L: Lattice, acc: int = 6):
    '''
    Clean a lattice by removing duplicate atoms from its atomic basis.

    Parameters:
    L : Lattice
        The Lattice instance whose atomic basis will be filtered.
    acc : int, optional
        Precision parameter used to determine the tolerance for duplication (default is 6).

    Returns:
    list
        List of Atom instances that were removed.
    '''
    removidos=[]
    a,b = L.get_pv()
    t = max(long(a),long(b))
    for esp in L.atms:
        rep=cleanA(esp,1/(t*10**acc))
        removidos+=rep
    return removidos

#-------------------Funciones auxiliares para mostrar datos de una MT-------------------
def textLonN(t:str,n:int,al:str='c'):
    '''
    Format a string to a fixed width using alignment and padding.

    Parameters:
    t : str
        Input string to format.
    n : int
        Desired fixed length of the resulting string.
    al : str, optional
        Text alignment: 'c' for center, 'l' for left, 'r' for right (default is 'c').

    Returns:
    str
        Formatted string of exact length `n`.
    '''
    m = len(t)
    nt = ""
    resto = n-m
    if al == 'l':
        nt+=t[:min(m,n)]
        nt+=' '*resto
        return nt
    elif al == 'c':
        ri = int(resto/2)
        rd = resto-ri
        nt = ' '*ri
        nt +=t[:min(m,n)]
        nt += ' '*rd
        return nt
    elif al == 'r':
        nt = ' '*resto
        nt += t[:min(m,n)]
        return nt
    return t

def header():
    '''
    Generate a formatted header for a deformation/distortion summary table.

    Returns:
    str
        String representation of the table header including column names and borders.
    '''
    delta=u'\u03B4'
    theta=u'\u03B8'
    encabezados=["Lattice","T","Deformation","Distortion:"+delta+"//"+theta,"#Atoms"]
    linea = '+'+'-'*25+'+'+'-'*15+'+'+'-'*23+'+'+'-'*23+'+'+'-'*8+'+'+'\n'
    head = linea + '|'
    head += textLonN(encabezados[0],25)+ '|'
    head += textLonN(encabezados[1],15)+ '|'
    head += textLonN(encabezados[2],23)+ '|'
    head += textLonN(encabezados[3],23)+ '|'
    head += textLonN(encabezados[4],8)+'|\n'
    head += linea
    return head

def infLayer(L: Lattice, data: list):
    '''
    Format and display a line of lattice data in tabular form.

    Parameters:
    L : Lattice
        Lattice layer for which the data is being displayed.
    data : list
        List containing the transformation matrix, deformation matrix,
        deformation ratios, and angles.

    Returns:
    tuple
        Formatted string (row in the table) and number of atoms in the transformed cell.
    '''
    lin='|'+' '*25+'|'+' '*15+'|'+' '*23+'|'+' '*23+'|'+' '*8+'|'+'\n'
    T,dM,da,db,ta,tb = data
    name = L.name
    nA = int(det(T))*int(L.nOAtms())
    fila=''
    fila += '|' + ' '*25 + '|'
    fila += '  |'+textLonN(str(T[0][0]),4,al='r')+textLonN(str(T[0][1]),5,al='r')+'|  |'
    fila += '  |'+textLonN(f'{dM[0][0]:.5f}',8,al='r')+textLonN(f'{dM[0][1]:.5f}',9,al='r')+'|  |'
    fila += textLonN(f"{round((da-1)*100,3):+}% // {round(ta,2):+}°",23)+'|'
    fila += textLonN(str(nA),8)+'|\n'
    fila += '|' + textLonN(name,25) + '|'
    fila += '  |'+textLonN(str(T[1][0]),4,al='r')+textLonN(str(T[1][1]),5,al='r')+'|  |'
    fila += '  |'+textLonN(f'{dM[1][0]:.5f}',8,al='r')+textLonN(f'{dM[1][1]:.5f}',9,al='r')+'|  |'
    fila += textLonN(f"{round((db-1)*100,3):+}% // {round(tb,2):+}°",23)+'|'
    fila += textLonN(' ',8)+'|\n'
    fila += lin
    return fila, nA

#--------------Funciones Auxiliares para la función "importLattice(File)"--------------
def readFile(name: str):
    '''
    Read the contents of a file and return its lines as a list of strings.

    Parameters:
    name : str
        Name of the file to read (without extension).

    Returns:
    list
        Lines of the file as string elements.
    '''
    try:
        file = open(name, 'r')
        count = 0
        lines = []
        while True:
            count+=1
            line = file.readline()
            if not line:
                break
            lines.append(format(line))
        file.close()
        return lines
    except Exception as e:
        print(f"Error:{str(e)}.")
        return None
        
def leeNumeros(line: str):
    '''
    Extract all numerical values from a given string.

    Parameters:
    line : str
        Input string containing numeric values.

    Returns:
    list
        List of float numbers found in the string.
    '''
    s = []
    s = [float(l) for l in re.findall(r'-?\d+\.?\d*', line)]
    return s
#----------------------------------------------------------------------------    
def importLattice(name: str, prnt: bool = True):
    '''
    Import lattice data from a VASP POSCAR file and create a Lattice object.

    Parameters:
    name : str
        Base name of the POSCAR file (without '.vasp' extension).
    prnt : bool, optional
        If True, display status messages during import (default is True).

    Returns:
    Lattice
        Lattice object containing the structure described in the file.

    Raises:
    ValueError
        If the file is not found or the format is unsupported.
    '''
    errormsg = '''The file does not exist or is not in the format supported by the program.
    - You must provide the name of a VASP file (not including the '.vasp').
    - The format must be a POSCAR format of type 'DIRECT'.
    - POSCAR files of type 'Cartesian' are not recognized.'''
    xyz = []
    try:
        # cargamos el nombre de la Red
        if prnt: print("File '{}' will be read".format(name+".vasp"))
        lines = readFile(name+".vasp")
        nameRed = re.sub(r'[^a-zA-Z0-9_() ]','',lines[0].replace('.','_').strip())
        #Cargamos los vectores primitivos de la Red
        vA = leeNumeros(lines[2])
        vB = leeNumeros(lines[3])
        vC = leeNumeros(lines[4])
        if (round(vA[2],5)!=0.0 or round(vB[2],5)!=0.0 or round(vC[0],5)!=0.0 or round(vC[1],5)!=0.0):
            msg = '''
            Initial vectors that are not supported as is will be modified to look like this:
                a = (a1,a2,0), b = (b1,b2,0), c = (0,0,c3)
            Their functionality is at your discretion.
            '''
            print(msg,errormsg)
        #Cargamos una lista con los tipos de Átomos en la Red y una con el numero de átomos de ese tipo
        aTipos = lines[5].split()
        aCant = leeNumeros(lines[6])
        if len(aTipos)!=len(aCant):
            print("Error: Number of Atom Types does not match")
            raise SyntaxError('Document not supported')
        atomos = []
        ind = 8
        for i in range(len(aTipos)):
            col = '#'+''.join([random.choice('123456789ABCD') for i in range(6)])
            for j in range(round(aCant[i])):
                pA = leeNumeros(lines[ind+j])
                at = Atom((pA[0], pA[1]), posZ=pA[2], color=col, sig=aTipos[i])
                atomos.append(at)
            ind = ind+round(aCant[i])
        leido = Lattice((vA[0],vA[1]),(vB[0],vB[1]),atms=atomos,name=nameRed,detachment=vC[2])
        if prnt: print("--Lattice created successfully from file '{}'--".format(name+".vasp"))
        return leido
    except:
        print(errormsg)
        return None


#----------------------Redes prediseñadas------------------------------
def ejemplos():
    texto ='''
    Predefined lattices are available, as follows:

hexa6(p, atms, name) -> Generates a hexagonal lattice with lattice constant 'p' and atoms specified in the 'atms' list.
    If 'atms' is not provided, it will contain two atoms in its basis, resulting in a hexagonal lattice with 6-fold radial symmetry.

hexa3(p, atms, name) -> Generates a hexagonal lattice with lattice constant 'p' and atoms specified in the 'atms' list.
    If this is not provided, it will contain two atoms, one inside its basis and another on a vertex, resulting in a hexagonal lattice with 3-fold radial symmetry.

rectMesh(p1, p2, atms, name) -> Generates a rectangular lattice with lattice constants p1 and p2 and atoms specified in the 'atms' list.
    If not provided, it will generate a lattice with a single atom at the center of the basis.

grafeno() -> Generates a Graphene lattice with a lattice constant of 2.44 Å and atoms arranged in the hexa6 format.

grafeno3() -> Generates a Graphene lattice with a lattice constant of 2.44 Å and atoms arranged in the hexa3 format.

blackPhospho() -> Generates a Black Phosphorene lattice with lattice constants 3.3061099052 and 4.552418232.
'''
    print(texto)
    
def hexa6(p,atms=[['C','C'],['sienna','sienna']],name=''):
    '''
    Generates a hexagonal lattice with a lattice constant p, using the atomic configuration provided in the atms list.
    If atms is not specified, a default configuration with two atoms in the basis is used, producing a lattice with 6-fold rotational symmetry.
    '''
    u,v=(p,0.0),(-p/2,math.sqrt(3)*(p/2))
    p1,p2,p3,p4 = (1/3,2/3),(2/3,1/3),(1/3,-1/3),(4/3,2/3)
    ats = [Atom(p1, sig = atms[0][0], color=atms[1][0]),Atom(p2, sig = atms[0][1], color=atms[1][1])]
    return Lattice(u,v,atms=ats,name=name,enls=[(p1,p2),(p2,p3),(p2,p4)])

def hexa3(p,atms=[['C','C'],['sienna','sienna']],name=''):
    '''
    Creates a hexagonal lattice with lattice constant p, using the atoms defined in the atms list.
    If not provided, the function uses a default basis with two atoms: one at the center and one at a vertex, resulting in a structure with 3-fold rotational symmetry.
    '''
    u,v=(p,0.0),(-p/2,math.sqrt(3)*(p/2))
    p1,p2,p3,p4 = (0.0,0.0),(1/3,2/3),(0,1),(1,1)
    ats = [Atom(p1, sig = atms[0][0], color=atms[1][0]),Atom(p2, sig = atms[0][1], color=atms[1][1])]
    return Lattice(u,v,atms=ats,name=name,enls=[(p1,p2),(p2,p3),(p2,p4)])

def rectLattice(p1,p2,atms='C',name=''):
    '''
    Generates a rectangular lattice with lattice constants p1 and p2, and the atoms specified in the atms list.
    If no atom list is provided, a single atom is placed at the center of the primitive cell.
    '''
    u,v = (p1,0.0),(0.0,p2)
    p1,p2,p3 = (1/2,1/2),(3/2,1/2),(1/2,3/2)
    ats = [Atom(p1,sig = atms)]
    return Lattice(u,v,atms=ats,name=name,enls=[(p1,p2),(p1,p3)])
    
def graphene():
    '''
    Returns a standard hexagonal graphene lattice with a lattice constant of 2.44 Å, using a 6-fold symmetric atomic arrangement as defined in hexa6.
    '''
    return hexa6(2.44, name='Graphene')
    
def grapheneC3():
    '''
    Returns a variant of the graphene lattice with a lattice constant of 2.44 Å, configured with a 3-fold symmetric basis as described in hexa3.
    '''
    return hexa3(2.44, name='Graphene(s3)')

def blackPhosphorene():
    '''
    Generates a lattice model of black phosphorene using its experimentally derived lattice parameters: 3.2601301670 Å and 4.3470306396 Å.
    The atomic positions and out-of-plane displacements are configured to match the layered anisotropic structure of black phosphorus.
    '''
    a,b=(3.2601301670,0.0), (0.0,4.3470306396)
    p1,p2=(0.000000000,0.913483083),(0.500000000,0.579813302)
    p3,p4=(0.000000000,0.079836130),(0.500000000,0.413437814)
    ats = [Atom(p1,sig='P',color='orchid',posZ=0.0161670960),
           Atom(p2,sig='P',color='orchid',posZ=0.0161669898),
           Atom(p3,sig='P',color='orchid',posZ=0.2266394472),
           Atom(p4,sig='P',color='orchid',posZ=0.2266392330)]
    enl = [(p1,p2),(p3,p4),(p2,p4),(p2,sumaV(p1,(1.0,0.0))),(p4,sumaV(p3,(1.0,0.0))),(p1,sumaV(p3,(0.0,1.0)))]
    return Lattice(a,b,atms=ats,name='Black-Phosphorene',enls=enl)

def h_BN():
    '''
    Creates a lattice representing the hexagonal face of layered boron nitride (h-BN).
    The atoms and bonds are positioned to reflect the characteristic honeycomb geometry and layer separation of this material.
    '''
    a = (2.512,0.0)
    b = rota(a,120)
    Tc= 7.707/2
    P1, P2 = (1/3,2/3), (2/3,1/3)
    bAt = [Atom(P1,color='green',sig='B'),
           Atom(P2,color='silver',sig='N')]
    enl = [(P1,P2),(sumaV(P1,(1,0)),P2),(sumaV(P1,(0,-1)),P2)]
    return Lattice(a,b,detachment=Tc,atms=bAt,enls=enl,name="h-BN")
