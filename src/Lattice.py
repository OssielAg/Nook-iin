from Atom import *
import cmath
atomList = List[Atom]
recpVectrs = List[vector2D]
affList = List[Tuple[str, float, float, float,vector2D]]
bgmData = Tuple[np.ndarray, np.ndarray, np.ndarray, mc.LineCollection]
plt.style.use('default')
plt.rcParams['figure.figsize'] = (8,8)

class Lattice:
    '''Class that models a crystal lattice in the system.'''
    def __init__(self,
                 vA:vector2D,
                 vB:vector2D,
                 atms:atomList=[],
                 enls:List[vector2D]=[],
                 name:str='',
                 detachment:float=10.0,
                 prof:int=1):
        '''
        Initializes a Network with the vectors, its rotation, list of Atoms, list
        of its Links, Name and level it occupies in the stacking.
        detachment: Width of the sheet
        name      : Network Name
        vA        : Vector A (with rotation set)
        vB        : Vector B (with rotation set)
        prof      : Position in the stack of lattices if it belongs to a stacked system.
        atms      : List of atoms in the atomic basis
        enls      : List of links in Primitive cell
        '''
        try:
            plt.rcParams['figure.figsize'] = (8,8)
            loas = []
            self.enls=[]
            (a1,a2),(b1,b2) = vA,vB
            rAngle = cRot(vA)
            for a in atms:
                a.clasifica(loas)
            #Width of the sheet
            self.detachment = detachment
            #Primitive Vectors (with rotation)
            self.a = vA
            self.b = vB
            #Primitive Vectors (without rotation)
            self.OriginalA = rota(vA,-rAngle)
            self.OriginalB = rota(vB,-rAngle)
            #Position in the stack of lattices if it belongs to a stacked system.
            self.prof = prof
            #Rotation angle of the lattice with respect to the x-axis
            self.theta = rAngle
            #List of links in Primitive cell
            self.enls = enls
            #Angle between both generating vectors of the Unit cell
            self.inAngle = abs(cAng(vA,vB))
            #List of layers if the Lattice is a heterostructure
            self.layerList = []
            #Reciprocal Vectors
            self.reciprocalVectors = cRecip((a1,a2,0.0),(b1,b2,0.0),(0.0,0.0,detachment))
            #List of atoms in the atomic base classified by family
            self.atms = loas
            #Factores de forma atómica
            self.aff = self.loAtms()
            #Name of Lattice
            if name=='':
                self.name = "Lattice({:.3f}°)".format(self.inAngle)
            else:
                self.name = name
        except Exception as e:
            print(f"Error:{str(e)}.")
    
    def __str__(self):
        return self.showData()
    
    def get_pv(self)->(vector2D,vector2D):
        '''
        Return the primitive vectors of the network
        '''
        return self.a, self.b
    
    def showme(self,
               x:int = 1,
               y:int = 1,
               x0:int = 0,
               y0:int = 0,
               t:int = 10,
               iName:str = '',
               sampling:bool = False,
               scalePosL:bool = True):
        '''
        Displays on the screen the image resulting from repeating the unit cell of the
        Network from 'x0' to 'x' times in its vector 'a' and from 'y0' to 'y' times in
        its vector 'b'. If a iName is given a PNG image with that name will be generated.
        
        x        : Maximum repetition rate with respect to the vector a
        y        : Maximum repetition rate with respect to vector b
        x0       : Initial index for repetitions with respect to the vector a
        y0       : Initial index for repetitions with respect to vector b
        t        : Stroke thickness
        iName    : If it is different from '', an image file with this name will be
                   created inthe 'Images' folder.
        sampling : If it is True, a 3x3 representation of the primitive cell will be
                   drawn on the screen, showing the primitive vectors.
        scalePosL: If True, the scale bar will be displayed on the left; otherwise, it
                   will be on the right.
        '''
        try:
            red=[]
            lx1,ly1 = getLim(self.a,self.b,x,y)
            lx2,ly2 = getLim(self.a,self.b,x,y0)
            lx3,ly3 = getLim(self.a,self.b,x0,y)
            lx4,ly4 = getLim(self.a,self.b,x0,y0)
            lmsx = [min(lx1[0],lx2[0],lx3[0],lx4[0]),max(lx1[1],lx2[1],lx3[1],lx4[1])]
            lmsy = [min(ly1[0],ly2[0],ly3[0],ly4[0]),max(ly1[1],ly2[1],ly3[1],ly4[1])]
            difMax = max((lmsx[1]-lmsx[0]),(lmsy[1]-lmsy[0]))
            plt.style.use('default')
            plt.rcParams['figure.figsize'] = (8,8)
            fig, maxs = plt.subplots()
            
            ats=[]
            col=[]
            tam=[]
            enls=[]
            for i in range(abs(x-x0)):
                a=i+x0
                for j in range(abs(y-y0)):
                    b=j+y0
                    #Carga contornos de celda
                    red.append([m2V(self.a,self.b,(a,b)),m2V(self.a,self.b,(a+1,b))])
                    red.append([m2V(self.a,self.b,(a,b)),m2V(self.a,self.b,(a,b+1))])
                    red.append([m2V(self.a,self.b,(a+1,b)),m2V(self.a,self.b,(a+1,b+1))])
                    red.append([m2V(self.a,self.b,(a,b+1)),m2V(self.a,self.b,(a+1,b+1))])
                    #Carga los atomos
                    for c in self.atms:
                        for at in c:
                            (pu,pv) = at.pos
                            na = m2V(self.a,self.b,(a+pu,b+pv))
                            ats.append(na)
                            col.append(at.color)
                            tam.append(t*(3+(aN(at.sig)/20)))
                    #Carga los enlaces
                    for (ei,ef) in self.enls:
                        (ei1,ei2) = ei
                        (ef1,ef2) = ef
                        o = m2V(self.a,self.b,(a+ei1,b+ei2))
                        f = m2V(self.a,self.b,(a+ef1,b+ef2))
                        enls.append([o,f])
            lis = np.array(ats.copy())
            xs, ys = lis[:,0], lis[:,1]
            #Cargamos los contornos de las celdas en una lista de lineas
            lr = mc.LineCollection(np.array(red), colors='silver', linewidths=(t/30))
            #Cargamos los enlaces en una lista de lineas
            lc = mc.LineCollection(np.array(enls), colors='black', linewidths=(t/20))
            #Dibuja los Enlaces
            maxs.add_collection(lc)
            #Dibuja los contornos de las celdas
            maxs.add_collection(lr)
            #Dibuja los Atomos
            maxs.scatter(xs,ys, color=col,s=tam)
            maxs.axes.xaxis.set_visible(False)
            maxs.axes.yaxis.set_visible(False)
            medX = ((lmsx[0]+lmsx[1])/2)
            medY = ((lmsy[0]+lmsy[1])/2)
            maxs.set(xlim = (medX-(difMax/2),medX+(difMax/2)),
                     ylim = (medY-(difMax/2),medY+(difMax/2)))
            #Dibuja la escala de la imagen
            s=max(10**(round(math.log(difMax/8,10))),1)
            f=s/difMax
            sPosY = medY-(0.98*(difMax/2))
            #Dibuja la referencia de escala en la alineación dada
            if scalePosL:
                hAl = 'left'
                sPosX = medX-(0.9*(difMax/2))
                si = 0.05
                sf = si+f
            else:
                hAl = 'right'
                sPosX = medX+(0.9*(difMax/2))
                sf = 0.95
                si = sf-f
            plt.text(sPosX,
                     (sPosY+(0.06*(difMax/2))),
                     "{} nm".format(s/10),
                     fontsize=12,
                     weight='bold',
                     c='royalblue',
                     horizontalalignment = hAl,
                     backgroundcolor='white')
            plt.axhline(y=sPosY,xmin=si, xmax=sf, c='white',lw=8.0)
            plt.axhline(y=sPosY, xmin=si, xmax=sf, c='royalblue',lw=4.0)
            #Dibuja los Vectores primitivos
            if sampling:
                n=1
                a,b = self.get_pv()
                (ax,ay),(bx,by) = multV(0.9,a),multV(0.9,b)
                (pax,pay) = sumaV(multV(1/3,(ax,ay)),multV(-1/(5-n),(bx,by)))
                (pbx,pby) = sumaV(multV(1/3,(bx,by)),multV(-1/(5-n),(ax,ay)))
                w = (max(long((ax,ay)),long((bx,by))))/50
                plt.arrow(0,0,ax,ay, width = w, color="red")#Dibuja vector a
                plt.arrow(0,0,bx,by, width = w, color="blue")#Dibuja vector b
                plt.text(pax,
                         pay,
                         r"$\vec a$".format(s/10),
                         fontsize=28/(n+1),
                         weight='bold',
                         c='red')#Dibuja leyenda del vector a
                plt.text(pbx,
                         pby,
                         r"$\vec b$".format(s/10),
                         fontsize=28/(n+1),
                         weight='bold',
                         c='blue')#Dibuja leyenda del vector b
            if iName!='':
                Images_path = os.path.join(os.getcwd(), 'Images')
                if not os.path.exists(Images_path):
                    os.makedirs(Images_path)
                plt.savefig((Images_path+'/'+iName),dpi=900, bbox_inches='tight')
                print(f"Image address: '{Images_path}/{iName}.png'")
            plt.show()
        except Exception as e:
            print(f"Error:{str(e)}.")
            
    def showPC(self, iName:str=''):
        '''
        Create an image of the primitive cell by drawing its respective primitive
        vectors. If iName is different from '', an image file with this name will be
        created in the 'Images' folder.
        iName: Name of image file
        '''
        self.showme(sampling=True, iName=iName)
    
    def addAtms(self, loa:atomList):
        '''
        Orderly add a list of Atoms to the Network.
        loa: List of atoms
        '''
        for l in loa:
            for a in l:
                a.clasifica(self.atms)
        self.aff = self.loAtms()
        
    def showData(self):
        '''
        Displays the Lattice on a Text in format POSCAR in fractional coordinates.
        '''
        ang = cAng((1,0),self.a)
        (u1,u2) = self.OriginalA
        (v1,v2) = self.OriginalB
        data=self.name+'''
1.0
        {:.10f}         {:.10f}         0.0000000000
        {:.10f}         {:.10f}         0.0000000000
        0.0000000000         0.0000000000         {:.10f}
'''.format(u1,u2,v1,v2,(self.detachment))
        atms1=""
        atms2=""
        atms3="Direct"
        for i in range(len(self.atms)):
            atms1=atms1+"\t{}".format(self.atms[i][0].sig)
            atms2=atms2+"\t{}".format(len(self.atms[i]))
            for atm in self.atms[i]:
                (x,y) = atm.pos
                z = (atm.posZ + 0.0001)
                esp = '         '
                atms3=atms3+f"\n{esp}{abs(x):.10f}{esp}{abs(y):.10f}{esp}{z:.10f}"
        atms = atms1+"\n"+atms2+"\n"+atms3
        data = data+atms
        return data
    
    def aligned(self):
        '''
        Align the Lattice with the X axis.
        '''
        self.a = self.OriginalA
        self.b = self.OriginalB
        self.theta = 0.0
        
    def rotate(self, th:float):
        '''
        Rotate the Network as it is th degrees.
        th: Rotation angle
        '''
        newTheta = self.theta + th
        self.a = rota(self.OriginalA,newTheta)
        self.b = rota(self.OriginalB,newTheta)
        self.theta = newTheta
    
    def alignedLattice(self):
        '''
        Returns a copy of the Lattice aligned to the X axis.
        ''' 
        na, nb = self.OriginalA, self.OriginalB
        natms, nenls = self.atms.copy(), self.enls.copy()
        nName = self.name+"(aligned)"
        mr = Lattice(na, nb, enls=nenls, name=nName, prof=self.prof)
        mr.atms = natms
        mr.detachment = self.detachment
        return mr
    
    def mRot(self, ang:float):
        '''
        Returns a copy of the Network rotated in "ang" degrees.
        ang: Degrees of given rotation.
        ''' 
        na, nb = rota(self.a,ang), rota(self.b,ang)
        natms, nenls = copy.deepcopy(self.atms), copy.deepcopy(self.enls)
        nName = self.name+"({:.2f}°)".format(ang)
        mr = Lattice(na, nb, enls=nenls, name=nName, prof=self.prof)
        mr.atms = natms
        mr.aff = copy.deepcopy(self.aff)
        mr.detachment = self.detachment
        return mr
    
    def exportLattice(self, name:str=''):
        '''
        Export the network to a POSRCAR file.
        If a name is not given, use the network name.
        name: Name for the file to export the lattice to.
        '''
        try:
            if name=='':
                name=self.name
            VF_path = os.path.join(os.getcwd(), 'VASP_Files')
            if not os.path.exists(VF_path):
                os.makedirs(VF_path)
            name = VF_path+"/" + name.replace('.','_') + ".vasp"
            f = open(name,"w")
            f.write(self.showData())
            f.close()
            print(f"Lattice exported in:'{name}'")
            return 1
        except Exception as e:
            print(f"Error:{str(e)}.")
            return 0
    
    def setNewVectors(self, newA:vector2D, newB:vector2D):
        '''
        Establishes new generating Vectors for the Network.
        newA: New vector a
        newB: New vector b
        '''
        try:
            th = cAng((1,0),newA)
            self.theta = th
            self.a, self.b = newA, newB
            self.OriginalA = rota(newA, -th)
            self.OriginalB = rota(newB, -th)
            self.inAngle = abs(cAng(newA, newB))
            a1,a2 = newA
            b1,b2 = newB
            self.reciprocalVectors = cRecip((a1,a2,0.0),
                                            (b1,b2,0.0),
                                            (0.0,0.0,self.detachment))
        except Exception as e:
            print(f"Error:{str(e)}.")
        
    def getVectors(self)->(vector2D,vector2D):
        '''
        Return the Generating Vectors a,b of the Network (With rotated lattice)
        '''
        return self.a, self.b
    
    def getOV(self)->(vector2D,vector2D):
        '''
        Return the Generating Vectors a,b of the Network (With lattice aligned with
        the abscissa axis).
        '''
        return self.OriginalA, self.OriginalB
    
    def nOAtms(self)->int:
        '''
        Returns the number of atoms in the minimum cell of the lattice
        '''
        noa = 0
        for loa in self.atms:
            noa = noa + len(loa)
        return noa
    
    def loAtms(self)->affList:
        '''
        Generate a list with the data required to calculate the atomic form factor for
        each atom in the atomic basis of the lattice. Each element of the list contains
        the following data for each atom:
          -sig(element identifier)
          -relative position x
          -relative position y
          -relative position z
          -position of the atom in the real plane.
        '''
        nl = []
        for esp in self.atms:
            s = esp[0].sig
            for a in esp:
                (x,y) = a.pos
                v = m2V(self.a,self.b,(x,y))
                nl.append([s,x,y,a.posZ,v])
        return nl

    def F_hkl(self,h:float, k:float, FG:bool=True):
        '''
        Calculate the structure factor of the point [h,k,l].
        h: h position of the calculated point
        k: k position of the calculated point
        l: l position of the calculated point
        FG: If true, the scattering vector is considered; if false, it is not considered.
        '''
        if h==0 and k==0: return 10**(-20)#Da un valor cercano a 0 al punto en el origen
        AB = self.aff
        u,v = self.get_pv()
        rvs = self.reciprocalVectors
        x = to2D(rvs[0])
        y = to2D(rvs[1])
        hk = m2V(x,y,(h,k))
        F = 0
        if FG:
            for atm in AB:
                pa = atm[4]
                s = F_G(atm[0],hk)*cmath.exp(-1j * (pP(to3D(hk),to3D(pa))))
                F+=s
        else:
            for atm in AB:
                pa = m2V(u,v,(atm[1],atm[2]))
                s = aN(atm[0])*cmath.exp(-1j * (pP(to3D(hk),to3D(pa))))
                F+=s
        return abs(F)**2

    def reciprocalBackgroundMesh(self,
                                 vl:recpVectrs,
                                 t:float,
                                 border:float,
                                 calcS:bool=False,
                                 rnd:int=25,
                                 FG=True)->bgmData:
        '''
        Calculate the Network points of the reciprocal network and the network formed
        by their FBZs. Returns 2 lists with the X and Y positions of the points and a
        'collection' of lines used by 'Polygon' to load a polygon on the screen using
        the 'add_patch' function.
        vl    : Vertices of the FBZ associated with the lattice
        t     : Size with which the lines will be painted.
        border: Indicates the size of the area to be drawn  
        calcS : If True, the structure factor of each point is calculated and stored
                in the list S  
        rng   : Determines the number of digits to which the structure factor value of
                each point will be rounded  
        FG    : If True, the scattering vector is considered when calculating the
                structure factor'''
        try:
            b = border
            xs = []
            ys = []
            enls=[]
            S = []
            nPts=0
            maxF = 0.01
            rv = self.reciprocalVectors
            sra, srb = to2D(rv[0]), to2D(rv[1])
            mi = inv2x2(VtM(sra, srb))
            (x1,y1),(x2,y2) = MtV(m2M(mi,[[b,b],[b,-b]]))
            (x3,y3),(x4,y4) = MtV(m2M(mi,[[-b,-b],[b,-b]]))
            x = round(max(abs(x1),abs(x2),abs(x3),abs(x4)))+1
            y = round(max(abs(y1),abs(y2),abs(y3),abs(y4)))+1
            for i in range(-x,x):
                for j in range(-y,y):
                    (px,py) = m2V(sra,srb,(i,j))
                    if abs(px)<b and abs(py)<b:
                        #Calcula el valor F_hkl para este PR
                        if calcS:
                            F = self.F_hkl(i,j,FG=FG)
                            print(f'Calculando Factor de estructura....{nPts} PRs calculados',end="\r")
                            if F>maxF:maxF=F
                            S.append(F)
                            nPts+=1
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
            Sn=[]
            for F in S:
                Sn.append(round(F/maxF,rnd))
            return xs, ys, np.array(Sn), linkList
        except Exception as e:
            print(f"Error, {str(e)}. Check the entries")


    def printReciprocalSpace(self,
                             t:float=10,
                             border:float=2.5,
                             prnt:bool=False,
                             zoom:bool=False,
                             colors:list=[]):
        '''
        Prints on the screen the FBZ of the lattice in reciprocal space. If this
        network belongs to a multilayer system, it also prints the FBZ of each layer.
        t     : Value with which the sizes with which points and lines will be drawn
                will be determined.
        border: Limits of the drawn graph.
        prnt  : If True, save the image in a file with the name of the lattice.
        zoom  : If True, only generate the image in the first quadrant of the space
                with the given border.
        colors: List of colors for the FBZ images of each layer of the system.
        '''
        try:
            lol = self.layerList
            alph = 0.7
            ax = plt.subplot()
            #Dibuja la FBZ de cada capa que forma la red si es que es un sistema multicapa
            if len(lol) > 0:
                if colors==[]:
                    alph = 0.4
                    colors=['#'+''.join([random.choice('123456789') for i in range(6)]) for j in range(len(lol))]
                for i in range(len(lol)):
                    vl, eq = calcVerticesFBZ(lol[i].reciprocalVectors)
                    fbzLayer = Polygon(vl, alpha=alph, color = colors[i], label = lol[i].name)
                    ax.add_patch(fbzLayer)
            #Dibuja la FBZ de la red y el fondo dado por la función 'reciprocalBackgroundMesh'
            vl, eq = calcVerticesFBZ(self.reciprocalVectors)
            xs, ys, S, linkList = self.reciprocalBackgroundMesh(vl,t,border)
            fbzRed = Polygon(vl, alpha=0.7, color = 'gray', label = "Super Red")
            ax.add_patch(fbzRed)
            #Dibuja los enlaces de la red de fondo calculado previamente
            ax.add_collection(linkList)
            #Dibuja los Puntos de la red reciproca calculados previamente 
            ax.scatter(xs,ys, color='black',s=t)
            ax.set(xlim=(-border,border), ylim=(-border,border))
            
            if zoom: ax.set(xlim=(-0.25,border), ylim=(-0.25,border))
            ax.legend(loc = 'upper right',shadow=True)
            plt.xlabel(r'$K_x (^{2\Pi}/_\AA$)') 
            plt.ylabel(r'$K_y (^{2\Pi}/_\AA$)')
            if prnt:
                iName = 'images/RS-'+self.name.replace('.','_')
                plt.savefig(iName,dpi=900, bbox_inches='tight')
                print(f"Dirección de imagen: '{iName}.png'")
            plt.show()
        except Exception as e:
            print(f"Error:{str(e)}.")
    
    def printLightPoints(self, t=20, border=1,prnt=False,rnd=25):
        '''
        '''
        try:
            plt.style.use('dark_background')
            plt.rcParams['figure.figsize'] = (8,8)
            alph = 0.7
            ax = plt.subplot()
            vl, eq = calcVerticesFBZ(self.reciprocalVectors)
            xs, ys, S, linkList = self.reciprocalBackgroundMesh(vl,t,border*(2*math.pi),calcS=True,rnd=rnd)
            xs=xs/(2*math.pi)
            ys=ys/(2*math.pi)
            S =S*(t*100)
            ax.scatter(xs,ys, color='white',s=S)#"Pintamos" los Puntos de la red reciproca calculados previamente 
            ax.set(xlim=(-border,border), ylim=(-border,border))
            ax.spines.left.set_position('zero')
            ax.spines.bottom.set_position('zero')
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines.left.set_color('gray')
            ax.spines.bottom.set_color('gray')
            if prnt:
                plt.savefig(('images/DP-'+self.name.replace('.','_')),dpi=900, bbox_inches='tight')
                print("\nDirección de imagen: '{}.png'".format('/images/DP-'+self.name.replace('.','_')))
            plt.show()
            plt.style.use('default')
            plt.rcParams['figure.figsize'] = (8,8)
            return 1
        except Exception as e:
            print(f"Error:{str(e)}.")
            
    def dInfo(self,D,p=False):
        '''
        Calculate the changes that occur to the lattice vectors when the
        deformation given by the deformation matrix 'D' is applied to it.
        If the flag 'p'=True, then display the result on the screen.
        The result is provided in a list where you have:
            -New vector a
            -New vector b
            -Change in the norm of a
            -Change in the norm of b
            -Change in the direction of a
            -Change in the direction of b
        D : Deformation matrix
        p : Flag to print results
        '''
        a,b = self.get_pv()
        Vo = m2M(VtM(a,b),D)
        (ax,ay),(bx,by) = a_o, b_o = MtV(Vo)
        d_a, d_b = 1-(long(a_o)/long(a)), 1-(long(b_o)/long(b))
        t_a, t_b = cAng(a,a_o), cAng(b,b_o)
        if p:
            m = '''Efectos de la deformación sobre '{}':
        Nuevos PVs: a=({:.4f},{:.4f}), b=({:.4f},{:.4f})
        DeltaA:{:+}%\tThetaA:{:.3f}°
        DeltaB:{:+}%\tThetaB:{:.3f}°
        '''.format(self.name,ax,ay,bx,by,round(d_a*100,4),t_a,round(d_b*100,4),t_b)
            print(m)
        return [a_o,b_o,d_a,d_b,t_a,t_b]
    
    def cloneLattice(self):
        clone = Lattice(self.a,self.b)
        #Position in the stack of lattices if it belongs to a stacked system.
        clone.prof = self.prof
        #Rotation angle of the lattice with respect to the x-axis
        clone.theta = self.theta
        #List of links in Primitive cell
        clone.enls = copy.deepcopy(self.enls)
        #List of layers if the Lattice is a heterostructure
        clone.layerList = copy.deepcopy(self.layerList)
        #Reciprocal Vectors
        clone.reciprocalVectors = copy.deepcopy(self.reciprocalVectors)
        #List of atoms in the atomic base classified by family
        clone.atms = copy.deepcopy(self.atms)
        #Factores de forma atómica
        clone.aff = copy.deepcopy(self.aff)
        clone.name = self.name
        return clone
    
    def deformLattice(self,D):
        '''
        Deform the lattice according to the given deformation matrix.
        D : Deformation matrix to execute
        '''
        inf = self.dInfo(D,p=True)
        a_o, b_o = inf[0], inf[1]
        self.name+="'"
        self.setNewVectors(a_o,b_o)