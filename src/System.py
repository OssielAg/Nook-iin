import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from Functions import *

bereiten()

class System:
    def __init__(self, lol, name=""):
        '''
        Initialize the 'System' corresponding to the structure formed by vertically
        stacking all the materials from the list of Lattices described in 'lol'
        giving it the name 'name.'
        lol -> List of networks forming the system
        name -> Name of the system.'''
        self.redes = lol #Lista de Redes del Sistema
        if name=="":
            self.name = 'Sistema ['+','.join([l.name for l in lol])+']' #Nombre del Sistema
        self.poits = []#Lista de Puntos de red comunes para todas las capas
        self.loMat = []  #Lista de Matrices de transformación sugeridas
        self.MaxNumM = 10 #Número maximo de Matrices sugeridas
        self.SuperRed = None  #Super-Red del Sistema
        self.MT = None
    
    def calculateTM(self, min_angle = 25):
        '''
        Generate a list of optimal transformation matrices of smaller size based on
        the Lattice Points belonging to the 'results' list of the System. Therefore,
        it is required to execute the "searchLP" function first before running this.'''
        #Ángulo interno minimo aceptado para la super red calculada
        try:
            if self.poits == []:
                errmsg = "No hay puntos de red en común para las capas."
                errmsg +="\nEjecute la función searchLP previamente."
                errmsg +="\n*En caso de ya haberlo hecho aumente el rango de búsqueda (rangeOfSearch) o el error mínimo aceptado (epsilon)"
                print(errmsg)
                return -1
            self.loMat = []
            if self.its_hexagonal_system():
                #print("Sistema Hexagonal")
                for r in self.poits:
                    [m,n]=r[0]
                    M = VtM((m,n),(-n,m-n))
                    self.adjust(M)
                return 0
            for i in range(len(self.poits)):
                for j in range(i+1,len(self.poits)):
                    [a1,a2] = self.poits[i][0]
                    [b1,b2] = self.poits[j][0]
                    M = VtM((a1,a2),(b1,b2))
                    if det(M)<0:
                        M = VtM((b1,b2),(a1,a2))
                    a,b = transfVs(self.redes[0].a,self.redes[0].b,M)
                    if cAng(a,b) >= min_angle:
                        if 180-cAng(a,b) >= min_angle:
                            self.adjust(M)
            if self.loMat==[]: return -1
            return 1
        except Exception as e:
            print(f"Error:{str(e)}.")
            return -1
        
    def createSuperLattice(self,M):
        '''
        Create the supercell representing a primitive cell of the system from the
        given transformation matrix.
        The primitive vectors of this lattice are obtained by transforming the
        primitive vectors of the lattice in the first layer (substrate layer) with
        the given transformation matrix M.
        M -> Transformation matrix for primitive vectors'''
        try:
            a, b = self.redes[0].get_pv()
            sa, sb = transfVs(a, b, M)
            self.SuperRed = superMesh(sa,sb,self.redes)
            self.MT = M
            return 1
        except Exception as e:
            print(f"Error:{str(e)}.")
            return 0
    
    def searchLP(self, rangeOfSearch=15, epsilon=0.05):
        '''
        Search for the Lattice Points of the substrate layer that match with an error
        smaller than the given epsilon with any LP from the other layers of the system.
        rangeOfSearch -> Determines the range of the search area for the Lattice
                         Points of the substrate layer.
        epsilon -> Maximum allowed error between the positions of the Lattice Points of
                   the substrate layer and those of the other layers.
        '''
        try:
            lor = commonVs(self.redes, max_val=rangeOfSearch, eps=epsilon)
            self.poits = lor
            if lor==[]:
                msg = '''
                No se encontraron soluciones en el rango de búsqueda={} y con epsilon={}
                Aumente el rango de búsqueda o el epsilon para tener resultados
                '''.format(rangeOfSearch,epsilon)
                p:print(msg)
                return 0
            return 1
        except Exception as e:
            print(f"Error:{str(e)}.")
            return 0
    
    def optimize_system(self, T, prnt=True):
        '''
        Generate a new system based on the original, with the required deformations in
        each layer so that the given transformation matrix generates a commensurate
        supercell for all layers of this system. Calculate the primitive cell for this
        new system corresponding to the given matrix.
        '''
        try:
            s = self.clon()
            if len(s.redes)<2:
                print("El sistema debe tener al menos 2 capas.")
                return None, []
            V_0 = VtM(s.redes[0].a,s.redes[0].b)
            V_s = m2M(V_0,T)
            deformaciones = []
            for i in range(1,len(s.redes)):
                V_i = VtM(s.redes[i].a,s.redes[i].b)
                T_i = corresponding_points(s.redes[0], s.redes[i], T)
                V_i_Op = m2M(V_s,inv2x2(T_i))
                S_i = m2M(inv2x2(V_i),V_i_Op)
                #Guarda la matríz de deformación
                deformaciones.append(S_i)
                #Actualiza la red en la capa con los nuevos vectores primitivos
                a, b = MtV(V_i_Op)
                s.redes[i].setNewVectors(a,b)
                s.redes[i].name = s.redes[i].name + "'"
            #Creando super Red para el sistema deformado
            cSR = s.createSuperLattice(T)
            if cSR==1:
                self.SuperRed = s.SuperRed
                self.MT = s.MT
            if prnt:
                self.show()
                print("***La supercelda calculada está optimizada\nSe deformó al menos una de las capas del sistema para hacerlo.")
            return s, deformaciones
        except Exception as e:
            print(f"Error:{str(e)}.")
            return None, []
       
    def generateSuperCell(self, RoS=15, eps=0.05, sd=False):
        '''
        Execute sequentially the 'searchLP' and 'calculateTM' functions. Subsequently,
        with the recommended matrix from the loMat list, execute 'optimize_system' to
        create a new system in which its layers have undergone a deformation that
        allows it to have a commensurate result in all its layers. Finally, display
        the result on the screen with the 'show' function for the newly created system.
        RoS -> Determines the range of the search area for the Lattice Points of the
               substrate layer.
        eps -> Maximum allowed error in the calculation of the Lattice Points used to
               generate the results.'''
        self.searchLP(rangeOfSearch=RoS, epsilon=eps)
        if self.poits == []:
            print("No se encontraron puntos de red comunes en todas las capas, intente cambiando los valores 'RoS' o 'eps'")
            return -1
        self.calculateTM()
        #print("Posibles Matrices de trasformación calculadas:{}\nOpción recomendada:".format(len(self.loMat)))
        if self.loMat == []:
            return -2
        T = self.ShowTMs(shw=sd)
        S, d = self.optimize_system(T)
        return S
    
    def analiza_Mat(self):
        '''
        Analyze the possible transformation matrices of smaller size for the system, saving their characteristics in a list and proposing the best option.
        '''
        if self.poits==[]:
            self.searchLP()
            self.calculateTM()
        m0 = [[1.0,0.0],[0.0,1.0]]
        dif = 100.0
        info = []
        mejor = 0
        k=0
        a,b = self.redes[0].get_pv()
        for T in self.loMat:
            sa, sb = transfVs(a,b,T)#Vectores de la super-red en capa 0
            err = 0.0
            inf_c = []
            for i in range(1, len(self.redes)):
                #Vectores primitivos de la capa i
                ai,bi = self.redes[i].get_pv()
                #TM correspondiente a la capa i
                T_i = corresponding_points(self.redes[0],self.redes[i],T)
                #Vectores de la super-red en capa i
                sa_i, sb_i = transfVs(ai,bi,T_i)
                #Matriz con los vectores primitivos de la capa i
                V_i = VtM(ai,bi)
                #Matriz con los vectores primitivos optimizados de la capa i
                V_i_Op = m2M(VtM(sa,sb),inv2x2(T_i))
                #Matriz de deformación para la capa i
                S_i = m2M(inv2x2(V_i),V_i_Op)
                #Deformación en la norma de los vectores primitivos de la capa i
                d_a, d_b = long(sa_i)/long(sa), long(sb_i)/long(sb)
                #Ajuste de rotación en los vectores de la capa i
                t_a, t_b = cAng(sa_i,sa), cAng(sb_i,sb)
                #Error final en los vectores primitivos de la capa i
                e_a, e_b = dist(sa,sa_i)/long(sa), dist(sb,sb_i)/long(sb)
                #Grado de distorción en la capa i
                dd = calc_dd(V_i,V_i_Op)
                err += dd
                #Se guardan todos los valores calculados:
                #[Mat Ti, Mat Si, error a, error b,delta_a,delta_b,theta_a,theta_b,dd,#Atms]
                inf_c.append([T_i,S_i,e_a,e_b,d_a,d_b,t_a,t_b,dd,det(T_i)*self.redes[i].nOAtms()])
            info.append([T,(sa,sb),err,inf_c])
            if err<dif:
                dif=err
                mejor = k
            k+=1
        return info,mejor
    
    def analiza_T(self,T):
        '''
        t -> TM to be examined
        Calculate the data of the cell generated from the TM 'T', returning them in a list.
        '''
        m0 = [[1.0,0.0],[0.0,1.0]]
        dif = 100.0
        k=0
        a,b = self.redes[0].get_pv()
        sa, sb = transfVs(a,b,T)#Vectores de la super-red en capa 0
        inf_c = []
        for i in range(1, len(self.redes)):
            ai,bi = self.redes[i].get_pv()
            T_i = corresponding_points(self.redes[0],self.redes[i],T) #TM para capa i
            sa_i, sb_i = transfVs(ai,bi,T_i) #Super vectores para capa i
            V_i = VtM(ai,bi) #Matriz con PV de Capa i
            V_i_Op = m2M(VtM(sa,sb),inv2x2(T_i)) #Matriz PV optimizados de capa i
            ai_o, bi_o = MtV(V_i_Op) # PV optimizados de la capa i
            S_i = m2M(inv2x2(V_i),V_i_Op) #Matriz de deformacion para la capa i
            #Deformación en la norma de los vectores primitivos de la capa i
            d_a = long(ai_o)/long(ai)
            d_b = long(bi_o)/long(bi)
            #Ajuste de rotación en los vectores de la capa i
            t_a, t_b = cAng(ai,ai_o), cAng(bi,bi_o)
            #Error final en los vectores primitivos de la capa i
            e_a, e_b = dist(sa,sa_i)/long(sa), dist(sb,sb_i)/long(sb)
            #Grado de distorción en la capa i
            dd = calc_dd(V_i,V_i_Op)#(abs(t_a)+abs(t_b)+abs((d_a-1)*100)+abs((d_b-1)*100))/2
            #Se guardan todos los valores calculados:
            #[Mat Ti, Mat Si, error a, error b,delta_a,delta_b,theta_a,theta_b,dd,#Atms]
            inf_c.append([T_i,S_i,e_a,e_b,d_a,d_b,t_a,t_b,dd,det(T_i)*self.redes[i].nOAtms()])
        return [T,(sa,sb),0,inf_c]
    
    def leeMT(self, T,prnt='',shw=True):
        '''
        T -> TM used to generate a Cell for the system

        Print on screen a Table with the data of the Cell generated from the TM 'T'.
        If you want to save the result in a txt file, a value must be given to the
        entry 'prnt', this will be the name of the created file.
        '''
        try:
            dT = self.analiza_T(T)
            tAt = 0
            sa,sb = dT[1]
            inAng = cAng(sa,sb)
            mA = long(sa)
            mB = long(sb)
            dd = 0.0
            ddd = max(len(self.redes)-1,10**(-8))
            DDm = 0.0
            tabla = f'Size of the primitive vectors: |a|={mA:.5f}Å, |b|={mB:.5f}Å\nAngle between vectors: {inAng:.3f}°\n'
            lin='+'+'-'*25+'+'+'-'*15+'+'+'-'*23+'+'+'-'*23+'+'+'-'*8+'+'
            tabla += header()
            data = (dT[0],[[1.0,0.0],[0.0,1.0]],1.0,1.0,0.0,0.0)
            fila, nA = infLayer(self.redes[0],data)
            tabla += fila
            tAt += nA
            for i in range(1,len(self.redes)):
                dC = dT[3][i-1]
                data = (dC[0],dC[1],dC[4],dC[5],dC[6],dC[7])
                fila, nA = infLayer(self.redes[i],data)
                dd += dC[8]
                tabla += fila
                tAt += nA
                DDm = max(DDm,dC[8])
            tabla += lin
            dd=dd/ddd
            if ddd>2:
                tabla += f'\n\t\tTotal atoms:{tAt}\tDD prom:{dd:.6f}\tDD max:{DDm:.6f}'
            else:
                tabla += f'\n\t\tTotal atoms:{tAt}\tDD:{dd:.6f}'
            if prnt!='':
                name = "VASP_Files/" + prnt + ".txt"
                f = open(name,"w",encoding="utf-8")
                f.write(tabla)
                f.close()
                print(f"Se guardó la tabla en: {name}")
            if shw:
                print(tabla)
            return tabla+'\n', dd
        except Exception as e:
                print(f"Error:{str(e)}.")
                return "",0
    
    def ShowTMs(self,shw=True,save=''):
        text=''
        i=0
        ddM = 100
        sugerida = 0
        for T in self.loMat:
            head = f'\n***Option {i+1}: T <- Matrix loMat[{i}]'
            text+=(head+'\n')
            txt,ddi = self.leeMT(T,shw=False)
            text+=txt
            if round(ddi,10)<ddM:
                ddM = round(ddi,10)
                sugerida = i
            i+=1
        text+=f'Matriz sugerida: loMat[{sugerida}]'
        if shw:
            print(text)
        if save!='':
            try:
                name = "Tablas/" + save + ".txt"
                if not os.path.exists('./Tablas'):
                    os.mkdir('./Tablas')
                f = open(name,"w",encoding="utf-8")
                f.write(text)
                f.close()
                print(f"Se guardó la tabla en: {name}")
            except Exception as e:
                print(f"Error:{str(e)}.")
        return self.loMat[sugerida]
    
    #def muestra(self,shw=True):
    #    return self.ShowTMs(shw=shw)    
        
    def manualAdjustment(self,ListOfTM):
        '''
        Adjust the PVs of each layer so that they match in a common Super lattice given the provided TMs.
        ListOfTM -> List with the desired TMs.
        '''
        LoD = []
        if len(self.redes)!=len(ListOfTM):
            print("Entrada invalida, proporcione una lista con las MT deseadas para cada capa del sistema incluyendo la capa sustrato")
            return LoD
        a_s, b_s = self.redes[0].get_pv()
        S = m2M(VtM(a_s,b_s),ListOfTM[0])
        for i in range(1,len(ListOfTM)):
            a_i, b_i = self.redes[i].get_pv()
            Vi = VtM(a_i,b_i)
            Vo = m2M(S,inv2x2(ListOfTM[i]))
            D = m2M(inv2x2(Vi),Vo)
            (ax,ay),(bx,by) = a_o, b_o = MtV(Vo)
            LoD.append(D)
            self.redes[i].setNewVectors(a_o,b_o)
            if D!=[[1.0,0.0],[0.0,1.0]]:
                self.redes[i].name+="'"
            d_a, d_b = ((long(a_o)/long(a_i))-1)*100, ((long(b_o)/long(b_i))-1)*100
            t_a, t_b = cAng(a_i,a_o), cAng(b_i,b_o)
            m = '''Efectos de la deformación en capa {}:
        Nuevos PVs: a=({:.4f},{:.4f}), b=({:.4f},{:.4f})
        DeltaA:{:+}%\tThetaA:{:.3f}°
        DeltaB:{:+}%\tThetaB:{:.3f}°
        '''.format(i,ax,ay,bx,by,round(d_a,4),t_a,round(d_b,4),t_b)
            print(m)
        return LoD
    
#----------------------------------------------------------------------------------------
    
    def its_hexagonal_system(self):
        '''
        Señala si el sistema está conformado sólo por redes hexagonales.
        '''
        err = 10**-6
        for r in self.redes:
            if abs(120.0-r.inAngle)>err:
                return False
        return True
    
    def adjust(self, M):
        '''
        Verifica si una matriz de trasformación M entra a la lista loMat y la coloca manteniendo el orden
            M -> Matriz a examinar
        '''
        if det(M)==0:
            #print("---Matriz invalida--")
            return 0
        b, i = self.goesHere(M,0)
        if b:
            if len(self.loMat)<self.MaxNumM:
                if i<len(self.loMat):
                    self.loMat.insert(i,M)
                else:
                    self.loMat.append(M)
            else:
                self.loMat.insert(i,M)
                del self.loMat[-1]
        #print("---Matriz rechazada--")
        return 1
    
    def goesHere(self, M, i):
        '''
        Determina si una Matriz de transformacion M entra o no en la posición i de la lista loMat
        M -> Matriz a examinar
        i -> posición que examinamos
        '''
        if i>=len(self.loMat):#Si el indice sobrepasa los validos
            if len(self.loMat)<self.MaxNumM:#Verifica si aaun hay espacio en loMat
                return True,i
            #print("\t--Matriz descartada")
            return False, -1 #La matriz M es peor que las de loMat
        dM = det(M)
        d = det(self.loMat[i])
        if dM < d:# M es mejor opción que la que está actualmente en i
            #print("\t--Nueva mejor en {}".format(i))
            return True, i
        if dM == d:
            #return False, -1
            a,b = transfVs(self.redes[0].a,self.redes[0].b,M)
            c,d = transfVs(self.redes[0].a,self.redes[0].b,self.loMat[i])
            if esRotacion(a,b,c,d):#Si el resultado es rotación del que ya tenemos lo descarta
                #print("\t--Matriz rotada existente")
                return False, -1
            bo, i = self.goesHere(M,i+1)#Verifica en la siguiente posición
            return bo, i
        bo, i = self.goesHere(M,i+1)#Verifica en la siguiente posición
        return bo, i
    
    def clon(self):
        '''
        Clona el sistema regresando una copia identica
        '''
        redes = [copy.copy(r) for r in self.redes]
        s = System(redes)
        s.name = self.name
        s.poits = copy.copy(self.poits)
        s.loMat = copy.copy(self.loMat)
        s.SuperRed = copy.copy(self.SuperRed)
        s.MT = self.MT
        return s
    
    def set_maximum_number_of_matrices(self, newMax):
        self.MaxNumM = newMax
        self.calculateTM()
        
    
    def show(self):
        if self.SuperRed is None:
            print('*'*84+"\n  Super Red no calculada aún, utilice la función 'createSuperLattice' para hacerlo  \n"+'*'*84)
        else:
            print("Matriz de trasformación:")
            pmat(self.MT)
            print(self.name,"\nCelda unitaria con {} átomos:".format(self.SuperRed.nOAtms()))
            self.SuperRed.showme()
            print("Espacio Reciproco:")
            self.SuperRed.printReciprocalSpace()
            
    def showReciprocalSpace(self,
                            t:float=10,
                            border:float=2.5,
                            prnt:bool=False,
                            zoom:bool=False,
                            colors:list=[]):
        if self.SuperRed is None:
            print('*'*84+"\n  Super Red no calculada aún, utilice la función 'createSuperLattice' para hacerlo  \n"+'*'*84)
        else:
            self.SuperRed.printReciprocalSpace(t=t,border=border,prnt=prnt,zoom=zoom,colors=colors)
            
    def showPC(self, iName:str=''):
        '''
        Create an image of the primitive cell by drawing its respective primitive
        vectors. If iName is different from '', an image file with this name will be
        created in the 'Images' folder.
        iName: Name of image file
        '''
        if self.SuperRed is None:
            print("No se ha calculado la CP para este sistema")
        else:
            self.SuperRed.showPC(iName=iName)
    
    def ejecuta(self,n,e):
        a = self.searchLP(rangeOfSearch=n, epsilon=e)
        if a<1: return None
        a = self.calculateTM()
        if a<0: return None
        return self.ShowTMs(shw=False)
    
    def diffractionPattern(self, t=1, border=1.5,prnt=False):
        if not self.SuperRed is None:
            self.SuperRed.printLightPoints(t,border,prnt)
            
    def rename(self,newName):
        try:
            self.name=newName
            if self.SuperRed!=None:
                self.SuperRed.name=f'SuperLattice {newName}'
                return 1
        except Exception as e:
            print(f"Error:{str(e)}.")
            return 0

    def exportPC(self,PCname=''):
        if self.SuperRed is None:
            print("There is no primitive cell calculated for this system")
            return 0
        if PCname=='':
            PCname=self.name
        return self.SuperRed.exportLattice(name=PCname)
#---------------------------------------------------------------------------------
'''
    def analyze(self, angle_range=(0.0,180.0), rangeOfSearch=15, precision=2, maxErr=0.05):
        
        Functional only in bilayer systems, it searches for the rotation angles between
        the layers of the system that can yield results with minimal deformation.
        angle_range -> Search range for the angle specified by the pair
                              (initial angle, final angle)
        rangeOfSearch -> Determines the range of the search area for the Lattice Points
                         of the substrate layer.
        precision -> Search precision given by the number of digits after the decimal 
                     point (1=tenths of a degree, 2=hundredths of a degree, ...)
        maxErr -> Maximum tolerable error to be accepted
        if len(self.redes)==2:
            return analiza(self.redes[0],self.redes[1],roAng=angle_range,erMax=maxErr,mor=rangeOfSearch,accuracy=precision)
        print("Este método sólo funcional en Sistemas binarios")
'''