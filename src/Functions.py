from Lattice import *

# Métodos derivados

def isitin(r,cent, sr, slvl):
    '''
    r   : Lattice evaluated
    sr  : Heterostructure lattice
    cent: Position of the origin of the evaluated cell
    slvl: Level of the layer where the evaluated lattice is

    Verify which atoms belonging to the cell of the 'r' lattice positioned at 'cent'
    fall within the area corresponding to the primitive cell (PC) of the 'sr' lattice.
    The atoms that meet this condition are added to the atomic basis of 'sr'.'''
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

def megeCut(r, sr, lvl=0):
    '''
    r  : Lattice evaluated
    sr : Heterostructure lattice
    lvl: Level of the layer where the evaluated lattice is
    
    Auxiliary method for superMesh. Calculate the cells of the lattice that coincide
    with the primitive cell calculated for the system to determine its atomic basis.'''
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

def cleanA(r, err=0.001):
    '''
    r: Lattice
    err: Minimum maximum error

    Cleans the list of atoms in a Lattice by eliminating repeated ones.'''
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

def superMesh(sa,sb,layerList):
    '''
    sa       : Primitive vector 'a' calculated for the system
    sb       : Primitive vector 'b' calculated for the system
    layerList: List of Lattices that make up the system.

    Creates the Lattice that will represent the System formed by stacking the Lattices in "layerList", using the given primitive vectors.'''
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

def pts(layer, max_it=15):
    '''
    layer : Lattice corresponding to the layer being evaluated
    max_it: Maximum number of repetitions of the cell in any of the directions of its primitive vectors

    Generates a list of all 'Lattice Points' within the designated search area.'''
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

def calcCD(substrate, layer, ab):
    '''
    substrate: Lattice substrate.
    layer    : Lattice to approximate
    ab       : Pair of integers that define the vector we want to approximate
    
    Given 2 lattices, 'substrate' and 'layer', calculate the integers 'c' and 'd' such
    that the projection of the Lattice point (c, d) of the 'layer' is the closest to
    the projection from the Lattice Point (a, b) of 'substrate'.'''
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
    
def calcPR(pts, substrate, layer, eps=0.05):
    '''
    pts      : List of Lattice Points in which we will search for matches.
    substrate: Lattice substrate
    layer    : Lattice to approximate
    eps      : Maximum distance allowed between point projection

    Checks a list of Lattice Points for 'Substrate' leaving only those corresponding
    with Lattice Points for 'layer' with a maximum difference in their projections on
    the plane given by 'eps'.'''
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
    
def commonVs(redes, max_val=15, eps=0.05):
    '''
    redes    :List of Lattices that make up the multilayer system
    max_value: Limit of the search area
    eps      : Maximum accepted error.

    Using the lattice in position 0 of the 'lattices' list as the 'substrate', it
    sequentially executes the 'calcPR' method with each of the other lattices in the
    list, using the result of the 'pts(substrate, max_val)' method as the initial pts
    list. The final result is a list containing only the Lattice Points (PR) that have
    a corresponding PR in each layer of the system with an error smaller than 'eps'.'''
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

def corresponding_points(l1, l2, M1):
    '''
    l1: Lattice 1
    l2: Lattice 2
    M1: Translation Matrix
    Indicate the 2x2 matrix that refers to the lattice point for l2 corresponding to
    the lattice point of l1 referenced by m1.'''
    a1, b1 = MtV(M1)
    a2, b2 = (calcCD(l1,l2,a1),calcCD(l1,l2,b1))
    return VtM(a2,b2)
    
def calc_dd(V_i,V_o):
    '''
    V_i: Matrix composed of the original primitive vectors of the Lattice.
    V_0: Matrix composed of the deformed primitive vectors of the Lattice.
    
    Calculate the "Degree of distortion" corresponding to a cell by transforming its
    primitive vectors from those expressed in matrix V_i to those expressed in
    matrix V_o.'''
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
def esClon(Atms,atm,eps):
    '''
    Atms -> List with atoms to compare
    atm -> Atom to be compared
    eps -> Threshold for accepted error    
    Determine if the atom 'atm' is equivalent to any in the list 'Atms' with an error
    bounded by eps.'''
    for a in Atms:
        if abs(a.posZ-atm.posZ)<eps:
            d = abs(1-dist(atm.pos,a.pos))
            #print(f'\t{a.pos}:{d:.8f}')
            if d<eps:
                #print('****Es Clon****')
                return True
    return False

def borders(Atms):
    '''
    Atms -> List of atoms in a lattice
    Calculates the atoms from the Atms list that belong to the boundary of the primitive
    cell and returns them in a list.'''
    orilla=[]
    for a in Atms:
        x, y = a.pos
        if x<0.001 or y<0.001:
            orilla.append(a)
    return orilla

def cleanA(Atms,eps):
    '''
    Atoms -> List of atoms
    eps -> Accepted error threshold
    Remove repeated atoms from a list of atoms placed at positions relative to a
    primitive cell.'''
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


    
def cleanPCell(L,acc=6):
    '''
    acc -> Maximum accepted error precision

    Remove all repeated atoms from the atomic basis of the lattice.
    '''
    removidos=[]
    a,b = L.get_pv()
    t = max(long(a),long(b))
    #print('Presición:{}'.format(1/(t*10**acc)))
    for esp in L.atms:
        rep=cleanA(esp,1/(t*10**acc))
        removidos+=rep
    return removidos

#-------------------Funciones auxiliares para mostrar datos de una MT-------------------
def textLonN(t:str,n:int,al:str='c'):
    '''
    t -> Original text
    n -> Exact length
    al -> Alignment of the resulting text
    Return a String of size 'n' by cutting or adding spaces to the given text 't'.
    If 'n' is greater than the size of 't', the result will have an alignment according
    to the value of 'al':
        c -> Centered
        l -> Left
        r -> Right'''
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
    '''Defines a text used as a header for the table to be created'''
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

def infLayer(L,data):
    '''
    L -> Lattice belonging to a System
    data -> List with information about network 'L'

    Print in a specific format to display in a table the data indicated by data.'''
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
def readFile(name):
    '''
    name: Imported file name
    Reads the designated File and transforms it into an array of Strings
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

def leeNumeros(line):
    '''
    line: String to read
    Auxiliary function. It reads a string and returns a list with the numbers in it.
    '''
    s = []
    s = [float(l) for l in re.findall(r'-?\d+\.?\d*', line)]
    return s
#----------------------------------------------------------------------------    
def importLattice(name,prnt=True):
    '''
    name: Imported file name
    Generates a Lattice from a VASP file with the name indicated in 'name'.
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
    Se cuenta con redes predefinidas, estas son:
hexa6(p,atms,name) -> Genera una Red hexagonal con constante de red 'p' y con los átomos de la lista atms.
    Si atms no se dá, entonces tendrá 2 átomos dentro de su base, generando una red hexagonal con 6 simetrías radiales.

hexa3(p,atms,name) -> Genera una Red hexagonal con constante de red 'p' y con los átomos de la lista atms.
    Si esta no se da entonces tendrá 2 átomos, uno dentro de su base y otro en un vértice, generando una red hexagonal con 3 simetrías radiales.

rectMesh(p1,p2,atms,name) -> Genera una Red rectangular con las constantes de red p1, p2 y los átomos señalados en la lista atms.
    Si esta no se dá, se generará con un solo átomo en el centro de su base.

grafeno() -> Genera una red de Grafeno, con constante de red 2.44 A y con sus átomos acomodados en el formato de hexa6

grafeno3() -> Genera una red de Grafeno, con constante de red 2.44 A y con sus átomos acomodados en el formato de hexa3

blackPhospho() -> Genera una Red de Fosforeno Negro con las constantes de red 3.3061099052 y 4.552418232.
'''
    print(texto)
    
def hexa6(p,atms=[['C','C'],['sienna','sienna']],name=''):
    '''
    Genera una Red hexagonal con constante de red 'p' y con los átomos de la lista atms.
    Si esta no es dada entonces tendrá 2 átomos dentro de su base, generando una red hexagonal con 6 simetrías radiales.
    '''
    u,v=(p,0.0),(-p/2,math.sqrt(3)*(p/2))
    p1,p2,p3,p4 = (1/3,2/3),(2/3,1/3),(1/3,-1/3),(4/3,2/3)
    ats = [Atom(p1, sig = atms[0][0], color=atms[1][0]),Atom(p2, sig = atms[0][1], color=atms[1][1])]
    return Lattice(u,v,atms=ats,name=name,enls=[(p1,p2),(p2,p3),(p2,p4)])

def hexa3(p,atms=[['C','C'],['sienna','sienna']],name=''):
    '''
    Genera una Red hexagonal con constante de red 'p' y con los átomos de la lista atms.
    Si esta no se da entonces tendrá 2 átomos, uno dentro de su base y otro en un vértice, generando una red hexagonal con 3 simetrías radiales.'''
    u,v=(p,0.0),(-p/2,math.sqrt(3)*(p/2))
    p1,p2,p3,p4 = (0.0,0.0),(1/3,2/3),(0,1),(1,1)
    ats = [Atom(p1, sig = atms[0][0], color=atms[1][0]),Atom(p2, sig = atms[0][1], color=atms[1][1])]
    return Lattice(u,v,atms=ats,name=name,enls=[(p1,p2),(p2,p3),(p2,p4)])

def rectLattice(p1,p2,atms='C',name=''):
    '''
    Genera una Red rectangular con las constantes de red p1, p2 y los átomos señalados en la lista atms.
    Si esta no se da, se generará con un solo átomo en el centro de su base.'''
    u,v = (p1,0.0),(0.0,p2)
    p1,p2,p3 = (1/2,1/2),(3/2,1/2),(1/2,3/2)
    ats = [Atom(p1,sig = atms)]
    return Lattice(u,v,atms=ats,name=name,enls=[(p1,p2),(p1,p3)])
    
def graphene():
    '''
    Genera una red de Grafeno, con constante de red 2.44 A y con sus átomos dentro de su base,
    generando una red hexagonal con 6 simetrías radiales.
    '''
    return hexa6(2.44, name='Grafeno')
    
def grapheneC3():
    '''
    Genera una red de Grafeno, con constante de red 2.44 A y con uno de sus átomos dentro de su base y otro en un vértice,
    generando una red hexagonal con 3 simetrías radiales.
    '''
    return hexa3(2.44, name='Grafeno(s3)')

def blackPhosphorene():
    '''
    Genera una Red de Fosforeno Negro con las constantes de red 3.2601301670 y 4.3470306396.
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
    Genera una Red que describe la face hexagonal del Nitruro de Boro laminar. 
    '''
    a = (2.512,0.0)
    b = rota(a,120)
    Tc= 7.707/2
    P1, P2 = (1/3,2/3), (2/3,1/3)
    bAt = [Atom(P1,color='green',sig='B'),
           Atom(P2,color='silver',sig='N')]
    enl = [(P1,P2),(sumaV(P1,(1,0)),P2),(sumaV(P1,(0,-1)),P2)]
    return Lattice(a,b,detachment=Tc,atms=bAt,enls=enl,name="h-BN")
