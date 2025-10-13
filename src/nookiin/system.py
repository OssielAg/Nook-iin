# ------------------------------------------------------------------------------
# Configure matplotlib backend before importing pyplot anywhere else.
# This ensures that the program can display or save images correctly
# even on systems without a graphical display (e.g., headless servers).
# "TkAgg" provides interactive image windows when possible.
# If Tkinter is not available, it falls back to "Agg", which is non-interactive
# but still supports saving figures as PNG, PDF, etc.
# ------------------------------------------------------------------------------
import matplotlib
try:
    matplotlib.use("TkAgg")   # Try to use an interactive backend (with GUI support)
except ImportError:
    matplotlib.use("Agg")     # Fallback backend for non-GUI environments
import sys, os
from matplotlib.colors import LogNorm

# Optional: add source dir to sys.path for manual usage
if os.environ.get("NOOKIIN_MANUAL_PATH"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)

from .functions import *
print('Load System')
latticeList = List[Lattice]
bereiten()

class System:
    def __init__(self, lol:latticeList, name:str=""):
        '''
        Initializes a 'System' object representing a vertically stacked multilayer structure
        composed of the lattices in the list 'lol'. The system is assigned the given name.
        
        Parameters:
            lol (list): List of Lattice objects forming the system.
            name (str): Optional name of the system.
        '''
        self.redes = lol #Lista de Redes del Sistema
        if name=="":
            self.name = 'System ['+','.join([l.name for l in lol])+']' #System name
            self.poits = []  # List of lattice points common to all layers  
            self.loMat = []  # List of suggested transformation matrices  
            self.MaxNumM = 10  # Maximum number of suggested matrices  
            self.primitive_lattice = None  # Superlattice of the system  
            self.MT = None  # Transformation matrix of the system
            self.DMList = None # List of Deformation Matrices

    
    def _calculateTM(self, min_angle:float = 25):
        '''
        Computes a list of optimal transformation matrices (TMs) for generating
        commensurate supercells, based on the Lattice Points obtained from the
        '_searchLP' method. This method must be executed beforehand.
        
        Parameters:
            min_angle (float): Minimum angular separation (in degrees) to consider between layers.
        '''
        #Ángulo interno minimo aceptado para la super red calculada
        try:
            if self.poits == []:
                errmsg = "There are no common lattice points for the layers."
                errmsg += "\nPlease make sure the function '_searchLP' has been executed beforehand."
                errmsg += "\n*If it has already been executed, try increasing the search range ('rangeOfSearch') or the minimum accepted error ('epsilon')."
                print(errmsg)

                return -1
            self.loMat = []
            if self._its_hexagonal_system():
                for r in self.poits:
                    [m,n]=r[0]
                    M = VtM((m,n),(-n,m-n))
                    self._adjust(M)
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
                            self._adjust(M)
            if self.loMat==[]: return -1
            return 1
        except Exception as e:
            print(f"Error:{str(e)}.")
            return -1
        
    def createSuperLattice(self,T:m2x2):
        '''
        Constructs the supercell corresponding to the given transformation matrix T,
        using the primitive vectors of the substrate layer as the base for transformation.
        (does not modify the lattices that make up the system)

        Parameters:
            T (m2x2): 2x2 transformation matrix for generating the supercell.
        '''
        try:
            a, b = self.redes[0].get_pv()
            sa, sb = transfVs(a, b, T)
            self.primitive_lattice = superMesh(sa,sb,self.redes)
            self.MT = T
            return 1
        except Exception as e:
            print(f"Error:{str(e)}.")
            return 0
    
    def _searchLP(self, rangeOfSearch:int=15, epsilon:float=0.05):
        '''
        Searches for Lattice Points in the substrate layer that match (within a given error)
        with Lattice Points in other layers.

        Parameters:
            rangeOfSearch (int): Extent of the area (in unit cells) to search around the origin.
            epsilon (float): Maximum allowed positional error for matching points.
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
    
    def optimize_system(self, T:m2x2, prnt:bool=True):
        '''
        Constructs a new deformed system where each layer adapts to the transformation matrix T
        to produce a common commensurate supercell.

        Parameters:
            T (m2x2): Transformation matrix.
            prnt (bool): If True, displays summary information on the screen.
        '''
        try:
            s = self.clon()
            if len(s.redes)<2:
                print("The system must have at least 2 layers.")
                return None, []
            V_0 = VtM(s.redes[0].a,s.redes[0].b)
            V_s = m2M(V_0,T)
            deformaciones = []
            for i in range(1,len(s.redes)):
                V_i = VtM(s.redes[i].a,s.redes[i].b)
                T_i = corresponding_points(s.redes[0], s.redes[i], T)
                V_i_Op = m2M(V_s,inv2x2(T_i))
                S_i = m2M(inv2x2(V_i),V_i_Op)
                # Save Deformation Matrix
                deformaciones.append(S_i)
                # Updates the lattice in the layer with the new primitive vectors
                a, b = MtV(V_i_Op)
                s.redes[i].setNewVectors(a,b)
                s.redes[i].name = s.redes[i].name + "'"
            # Create superlattice for the deformed system
            cSR = s.createSuperLattice(T)
            if cSR==1:
                self.primitive_lattice = s.primitive_lattice
                self.MT = s.MT
            if prnt:
                self.show()
                print("***The calculated supercell is optimized. At least one of the system layers was deformed to do so.")
            self.DMList = deformaciones
            return s
        except Exception as e:
            print(f"Error:{str(e)}.")
            return None
       
    def generateSuperCell(self, RoS:int=15, eps:float=0.05, prntRes:bool=True, showTable:bool=False):
        '''
        Performs a complete pipeline to build a commensurate supercell:
        1. Run 'ejecuta'
            1.1- Runs '_searchLP' and '_calculateTM',
            1.2- Selects the best TM,
        2. Applies 'optimize_system',
        3. Displays or saves the final result.

        Parameters:
            RoS (int): Search range for Lattice Points.
            eps (float): Maximum allowed positional error.
            prntRes (bool): If True, prints result summary.
            showTable (bool): If True, displays a comparison table of TMs.
        '''
        T = self.ejecuta(n=RoS,e=eps)
        if T == None:
            return None
        if showTable:
            self.describeTM(T)
        S = self.optimize_system(T,prnt=prntRes)
        return S
    
    def _analiza_T(self,T):
        '''
        Analyzes a specific transformation matrix T by computing its geometric
        and distortion properties.

        Parameters:
            T (m2x2): Matrix to be analyzed.

        Returns:
            list: Metrics associated with the supercell generated by T.
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
    
    def describeTM(self, T,prnt='',shw=True):
        '''
        Displays a detailed table of the geometric and distortion data
        for the supercell associated with transformation matrix T.

        Parameters:
            T (m2x2): Transformation matrix.
            prnt (str): Optional filename to save the table output.
            shw (bool): If True, displays the table on the screen.
        '''
        try:
            dT = self._analiza_T(T)
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
                print(f"The table was saved in: {name}")
            if shw:
                print(tabla)
            return tabla+'\n', dd
        except Exception as e:
                print(f"Error:{str(e)}.")
                return "",0
    
    def ShowTMs(self,shw=True,save=''):
        '''
        Evaluates and compares all candidate TMs stored in loMat.
        If enabled, shows tables for each candidate and recommends the best.

        Parameters:
            shw (bool): If True, displays tables on screen.
            save (str): If provided, saves the tables to a .txt file in the 'Tablas' folder.

        Returns:
            m2x2: Recommended transformation matrix.
        '''
        text=''
        i=0
        ddM = 100
        sugerida = 0
        for T in self.loMat:
            head = f'\n***Option {i+1}: T <- Matrix loMat[{i}]'
            text+=(head+'\n')
            txt,ddi = self.describeTM(T,shw=False)
            text+=txt
            if round(ddi,10)<ddM:
                ddM = round(ddi,10)
                sugerida = i
            i+=1
        text+=f'Recommended transformation matrix: loMat[{sugerida}]'
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
                print(f"The table was saved in: {name}")
            except Exception as e:
                print(f"Error:{str(e)}.")
        return self.loMat[sugerida]
        
    def manualAdjustment(self,ListOfTM):
        '''
        Manually adjusts the primitive vectors of each layer according to
        a given list of transformation matrices to ensure supercell compatibility.

        Parameters:
            ListOfTM (list of m2x2): Transformation matrices for each layer.
        '''
        LoD = []
        if len(self.redes)!=len(ListOfTM):
            print("Invalid input, provide a list of desired MTs for each layer of the system including the substrate layer")
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
            m = '''Effects of layer deformation {}:
        News PVs: a=({:.4f},{:.4f}), b=({:.4f},{:.4f})
        DeltaA:{:+}%\tThetaA:{:.3f}°
        DeltaB:{:+}%\tThetaB:{:.3f}°
        '''.format(i,ax,ay,bx,by,round(d_a,4),t_a,round(d_b,4),t_b)
            print(m)
        return LoD

    def plot_diffraction_map(self,
                             width=None,
                             typ='Lorentzian',
                             border=1.5,
                             resolution=500,
                             minimum_intensity=1e-4,
                             max_intensity=1,
                             prnt=''):
        """
        Draws the diffraction pattern with smooth curves (Gaussian or Lorentzian) of a multilayer system.    
        Parameters:
        - width: Width parameter (sigma or gamma); if None, the user is prompted
        - typ: 'Gaussian' or 'Lorentzian'
        - border: Range in reciprocal space for k_x and k_y (-border to border)
        - resolution: Number of points on each axis for the mesh
        - minimum_intensity: Minimum intensity shown in image
        - prnt: If not '', save the generated image as a <prnt>.png file.
        Returns:
        - Matrix with the intensity values ​​of each point on the calculated map
        """
        if self.primitive_lattice is None:
            print("First calculate the primitive cell of the system")
            return None
        SR=self.primitive_lattice
        if SR.diffractionData is None:
            print("Evaluating Structure Factor at each network point.")
            vl, eq = calcVerticesFBZ(SR.reciprocalVectors)
            xs, ys, S, _ = SR.reciprocalBackgroundMesh(vl,1,border*(2*math.pi),calcS=True,rnd=25)
            SR.diffractionData = np.stack((xs/(2*math.pi), ys/(2*math.pi), S), axis=-1)
        puntos = SR.diffractionData
        
        if width is None:
            width = float(input(f"Enter the value of width ({'σ' if typ=='Gaussian' else 'γ'}): "))
        puntos = puntos[puntos[:, 2] > (minimum_intensity/1e10)]
        # Crear malla de puntos
        kx = np.linspace(-border, border, resolution)
        ky = np.linspace(-border, border, resolution)
        KX, KY = np.meshgrid(kx, ky)
        
        # Inicializar intensidad total
        I_total = np.zeros_like(KX)
        
        # Sumar contribuciones
        i=1
        for kxi, kyi, Ci in puntos:
            print(f'Calculating diffraction pattern....{(i/len(puntos))*100:.2f}%',end="\r")
            i+=1
            dx2 = (KX - kxi)**2
            dy2 = (KY - kyi)**2
            r2 = dx2 + dy2
    
            if typ == 'Gaussian':
                I = (Ci*max_intensity) * np.exp(-r2 / (2 * width**2))
            elif typ == 'Lorentzian':
                I = (Ci*max_intensity) / (1 + r2 / width**2)
            else:
                raise ValueError("The type must be 'Gaussian' or 'Lorentzian'")
            
            I_total += I
        threshold = minimum_intensity*(1e-1)
        I_total[I_total < threshold] = threshold
        # Graficar
        plt.figure(figsize=(6, 5))
        plt.imshow(I_total, extent=(-border, border, -border, border),
                   origin='lower', cmap='inferno', norm=LogNorm(vmax=I_total.max()+1e-1, vmin=minimum_intensity * (I_total.max())))
        plt.colorbar(label='Intensity')
        plt.xlabel(r'$k_x$')
        plt.ylabel(r'$k_y$')
        plt.title(f"Diffraction pattern ({typ}, width = {width})")
        plt.tight_layout()
        if prnt!='':
            #iName=input("Indica el nombre con el que se guardará")
            iName = safe_filename(prnt)
            iName+=f"({typ})"
            Images_path = os.path.join(os.getcwd(), 'Images')
            if not os.path.exists(Images_path):
                os.makedirs(Images_path)
            plt.savefig((Images_path+'/'+iName),dpi=900, bbox_inches='tight')
            print(f"Image address: '{Images_path}/{iName}.png'")
        plt.show()
        return I_total

    
#----------------------------------------------------------------------------------------
    
    def _its_hexagonal_system(self):
        '''
        Returns True if the system is composed exclusively of hexagonal lattices.
        '''
        err = 10**-6
        for r in self.redes:
            if abs(120.0-r.inAngle)>err:
                return False
        return True
    
    def _adjust(self, M):
        '''
        Verifies whether matrix M belongs in the loMat list and inserts it in order.
        
        Parameters:
            M (m2x2): Transformation matrix to be inserted.
        '''
        if det(M)==0:
            return 0
        b, i = self._goesHere(M,0)
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
    
    def _goesHere(self, M: m2x2, i: int):
        '''
        Checks whether matrix M should be placed at position i in loMat.

        Parameters:
            M (m2x2): Transformation matrix.
            i (int): Position index in loMat.
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
            bo, i = self._goesHere(M,i+1)#Verifica en la siguiente posición
            return bo, i
        bo, i = self._goesHere(M,i+1)#Verifica en la siguiente posición
        return bo, i
    
    def clon(self):
        '''
        Creates and returns an identical copy of the system.
        '''
        redes = [copy.copy(r) for r in self.redes]
        s = System(redes)
        s.name = self.name
        s.poits = copy.copy(self.poits)
        s.loMat = copy.copy(self.loMat)
        s.primitive_lattice = copy.copy(self.primitive_lattice)
        s.MT = self.MT
        return s
    
    def sMNoM(self, newMax:int):
        '''
        (set maximum number of matrices)Sets a new maximum size for the list of candidate transformation matrices (loMat).

        Parameters:
            newMax (int): New upper limit for loMat length.
        '''
        self.MaxNumM = newMax
        self._calculateTM()
        
    
    def show(self):
        '''
        Displays basic structural data for the system, including both real space and reciprocal space representations.
        '''
        if self.primitive_lattice is None:
            print('*'*84+"\n  Superlattice not yet computed, use the 'createSuperLattice' function to generate it.  \n"+'*'*84)
        else:
            print("TM:")
            pmat(self.MT)
            print(self.name,"\nUnit cell with {} atoms:".format(self.primitive_lattice.nOAtms()))
            self.primitive_lattice.showme()
            print("Reciprocal Space:")
            self.primitive_lattice.printReciprocalSpace()
            
    def showReciprocalSpace(self,
                            t:float=10,
                            border:float=2.5,
                            prnt:bool=False,
                            zoom:bool=False,
                            colors:list=[]):
        '''
        Generates a visualization of the system in reciprocal space. Each layer's FBZ is shown,
        overlaid with the FBZ of the system’s calculated primitive cell.

        Parameters:
            t (float): Thickness of lines in the figure.
            border (float): Margin around the drawing area.
            prnt (bool): If True, saves the generated figure to file.
            zoom (bool): If True, zooms in around the center.
            colors (list): Optional list of colors for each layer.
        '''
        if self.primitive_lattice is None:
            print('*'*84+"\n  Superlattice not yet computed, use the 'createSuperLattice' function to generate it.  \n"+'*'*84)
        else:
            self.primitive_lattice.printReciprocalSpace(t=t,border=border,prnt=prnt,zoom=zoom,colors=colors)
            
    def showPC(self, iName:str=''):
        '''
        Visualizes the primitive cell of the system, including its primitive vectors.
        If a filename is provided, the image will be saved in the 'Images' folder.

        Parameters:
            iName (str): Optional name for the output image file.
        '''
        if self.primitive_lattice is None:
            print("Primitive Cell not yet computed")
        else:
            self.primitive_lattice.showPC(iName=iName)
    
    def ejecuta(self,n:int=15,e:float=0.05):
        '''
        Executes the full search for the smallest primitive cell of the system,
        based on the given search range and acceptable error.

        Parameters:
            n (int): Search range in unit cells.
            e (float): Maximum allowed error.
        '''
        a = self._searchLP(rangeOfSearch=n, epsilon=e)
        if a<1:
            print("Error:No primitive vector candidates were found, try larger values for the search range(n) or the accepted error bound(e).")
            return None
        a = self._calculateTM()
        if a<0:
            print("Error:No TM candidates were found, try larger values for the search range(n) or the accepted error bound(e).")
            return None
        return self.ShowTMs(shw=False)
    
    def diffractionPattern(self, t=1, border=1.5,prnt=False):
        '''
        Displays the diffraction pattern for the system in reciprocal space.

        Parameters:
            t (float): Thickness of lines.
            border (float): Drawing area border margin.
            prnt (bool): If True, saves the figure to file.
        '''
        if not self.primitive_lattice is None:
            self.primitive_lattice.printLightPoints(t,border,prnt)
            
    def rename(self,newName):
        '''
        Renames the system.

        Parameters:
            newName (str): New name for the system.
        '''
        try:
            self.name=newName
            if self.primitive_lattice!=None:
                self.primitive_lattice.name=f'SuperLattice {newName}'
                return 1
        except Exception as e:
            print(f"Error:{str(e)}.")
            return 0

    def exportPC(self,PCname=''):
        '''
        Exports the system's primitive cell to a POSCAR-formatted .vasp file.

        Parameters:
            PCname (str): Name for the exported file. Default name: PrimitiveCell_of_System
        '''
        if self.primitive_lattice is None:
            print("There is no primitive cell calculated for this system")
            return 0
        if PCname=='':
            PCname = 'Primitive_lattice'
        return self.primitive_lattice.exportLattice(name=PCname)
#---------------------------------------------------------------------------------
'''
    def analiza_Mat(self):
        """
        Analyzes all transformation matrices in the list of candidates,
        saving their geometric and distortion data, and identifies the most suitable one.
        """
        if self.poits==[]:
            self._searchLP()
            self._calculateTM()
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
                # Primitive vectors of layer i
                ai,bi = self.redes[i].get_pv()
                # TM corresponding to layer i
                T_i = corresponding_points(self.redes[0],self.redes[i],T)
                # Superlattice vectors in layer i
                sa_i, sb_i = transfVs(ai,bi,T_i)
                # Matrix with the primitive vectors of layer i
                V_i = VtM(ai,bi)
                # Matrix with the optimized primitive vectors of layer i
                V_i_Op = m2M(VtM(sa,sb),inv2x2(T_i))
                # Strain matrix for layer i
                S_i = m2M(inv2x2(V_i),V_i_Op)
                # Strain in the norm of the primitive vectors of layer i
                d_a, d_b = long(sa_i)/long(sa), long(sb_i)/long(sb)
                # Rotation adjustment in the vectors of layer i
                t_a, t_b = cAng(sa_i,sa), cAng(sb_i,sb)
                # Final error in the primitive vectors of layer i
                e_a, e_b = dist(sa,sa_i)/long(sa), dist(sb,sb_i)/long(sb)
                # Degree of distortion in layer i
                dd = calc_dd(V_i,V_i_Op)
                err += dd
                # All computed values are saved:
                #[Mat Ti, Mat Si, error a, error b,delta_a,delta_b,theta_a,theta_b,dd,#Atms]
                inf_c.append([T_i,S_i,e_a,e_b,d_a,d_b,t_a,t_b,dd,det(T_i)*self.redes[i].nOAtms()])
            info.append([T,(sa,sb),err,inf_c])
            if err<dif:
                dif=err
                mejor = k
            k+=1
        return info,mejor
'''
