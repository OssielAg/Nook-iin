from src.System import *
import sys

def select_language():
    print("Seleccione un idioma / Select a language")
    print("1 - Español")
    print("2 - English")

    while True:
        choice = input("Opción / Option: ").strip()
        if choice == '1':
            import menu_texts.texts_es as texts
            return texts
        elif choice == '2':
            import menu_texts.texts_en as texts
            return texts
        else:
            print("Entrada inválida / Invalid input. Intente de nuevo / Try again.")

def clear():
    '''
    Limpia la consola
    '''
    print('x+'*20)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print()
        
def leeColor(msg,ermsg):
    '''
    Espera una entrada correspondiente a un Color
    smg  -> Mensaje de petición
    ermsg-> Mensaje de error si la entrada no es correcta
    '''
    while True:
        color = input(msg)
        try:
            lL = mc.LineCollection(np.array([[(0,0),(1,0)]]), colors=color)
            return color
        except:
            print(ermsg)
        
def leeNum(msg:str,ermsg:str,isInt:bool=True):
    '''
    Espera una entrada correspondiente a un Número, si isInt=True entonces se espera
    un número entero, de lo contrario un flotante.
    smg  -> Mensaje de petición
    ermsg-> Mensaje de error si la entrada no es correcta
    isInt-> Indica si el número esperado es entero
    '''
    n = 0
    while True:
        try:
            if isInt:
                n = int(input(msg))
                break
            else:
                n = float(input(msg))
                break
        except ValueError:
            print(ermsg)
    return n

def newVector(v:str,texts):
    '''
    Crea un vector 3D pidiendo componente a componente.
    v -> Nombre del vector
    '''
    try:
        print(f"Vector {v}:")
        a1=float(input(f'\t{v}1:'))
        a2=float(input(f'\t{v}2:'))
        a3=float(input(f'\t{v}3:'))
        a=(a1,a2,a3)
        print(f'Verctor {v}={a}')
        return a
    except ValueError:
        print(texts.m_newVector_err)
        return None

def newAtomicBase(texts):
    '''
    Carga la báse atómica para una Red cargando todos los átomos de cada especie atómica
    en la base
    '''
    n = leeNum(texts.m_newAtomicBase_1,
               texts.m_newAtomicBase_2)
    atms = []
    if n<1:
        print(texts.m_newAtomicBase_3)
    i=0
    while i<n:
        i+=1
        clear()
        idAtom = input(texts.m_newAtomicBase_4)
        color = leeColor(texts.m_newAtomicBase_5,
                         texts.m_newAtomicBase_6)
        noa = leeNum(texts.m_newAtomicBase_7_1+f"'{idAtom}'"+texts.m_newAtomicBase_7_2,
                     texts.m_newAtomicBase_8)
        for j in range(noa):
            clear()
            print(texts.m_newAtomicBase_9_1+f"'{idAtom}-{j+1}'"+texts.m_newAtomicBase_9_2)
            pa = leeNum(texts.m_newAtomicBase_10,
                        textsm_newAtomicBase_13,
                        isInt=False)
            pb = leeNum(texts.m_newAtomicBase_11,
                        textsm_newAtomicBase_13,
                        isInt=False)
            pc = leeNum(texts.m_newAtomicBase_12,
                        textsm_newAtomicBase_13,
                        isInt=False)
            atms.append(Atom((pa,pb),posZ=pc,color=color,sig=idAtom))
    return atms


def menuNewL(l,mem,texts):
    '''
    Maneja y agrega una red 'l' a la lista 'mem'.
    l  -> Red con la que se va a trabajar
    mem-> Lista de redes donde se puede guardar la red
    '''
    while True:
        print(texts.m_menuNewL_1)
        k = leeNum('',texts.m_menuNewL_2)
        if k==0:
            mem.append(l)
            return False
        elif k==1:
            clear()
            print(l)
        elif k==2:
            clear()
            l.showPC()
        elif k==3:
            th = leeNum(texts.m_menuNewL_3,
                        texts.m_menuNewL_4,isInt=False)
            l = l.mRot(th)
        elif k==4:
            return True
        else:
            print(texts.m_menuNewL_4)

def newLattice1(mem,texts):
    '''
    Crea una Red de forma manual paso a paso.
    mem -> Lista de redes donde se guardará la red
    '''
    crear=True
    while crear:
        clear()#-------------------------------------------
        latticeName = input(texts.m_newLattice1_1)
        print(texts.m_newLattice1_2)
        a = b = c = None
        while a is None:
            a = newVector('a',texts)
        while b is None:
            b = newVector('b',texts)
        while c is None:
            c = newVector('c',texts)
        clear()#-------------------------------------------
        print(f"a={a}, b={b}, c={c}\n")
        print(texts.m_newLattice1_3)
        AB = newAtomicBase(texts)
        clear()#-------------------------------------------
        (a1,a2,a3)=a
        (b1,b2,b3)=b
        (c1,c2,c3)=c
        l = Lattice((a1,a2),(b1,b2),atms=AB,name=latticeName,detachment=c3)
        print(texts.m_newLattice1_4)
        crear=menuNewL(l,mem,texts)
    return l

def newLattice2(mem,texts):
    '''
    Crea una Red importandola desde un archivo POSCAR
    mem -> Lista de redes donde se guardará la red
    '''
    crear=True
    while crear:
        clear()#------------------------------------------
        l = None
        while l is None:
            fileName = input(texts.m_newLattice2_1)
            l = importLattice(fileName)
        clear()#------------------------------------------
        print(texts.m_newLattice2_2)
        crear=menuNewL(l,mem,texts)
    return l

def show_Lattice(red,texts):
    while True:
        e = leeNum(texts.m_show_Lattice_1,
                   texts.m_show_Lattice_2)
        if e==0: break
        elif e==1:
            clear()
            red.showme()
        elif e==2:
            clear()
            red.printReciprocalSpace()
        else:
            print(texts.m_show_Lattice_2)

def loadLattices(redes,texts):
    '''
    Crea y guarda Redes en una lista.
    redes -> Lista de redes donde se guardará la red
    '''
    while True:
        clear()
        e2 = leeNum(texts.m_Lattices,texts.m_loadLattices_1)
        if e2==1: newLattice1(redes,texts)
        elif e2==2: newLattice2(redes,texts)
        elif e2==3: break
        else: print(texts.m_loadLattices_1)
    print(texts.m_loadLattices_2_1+f"{len(redes)}"+texts.m_loadLattices_2_2)

def calcPC(S,texts):
    '''
    Busca una CP para un sistema dado
    S -> Sistema con el que se trabajará
    '''
    T = None
    while T is None:
        n = e = -1
        while n<1:
            n = leeNum(texts.m_calcPC_1,
                       texts.m_calcPC_2)
            if n<1: print(texts.m_calcPC_2)
        while e<0:
            e = leeNum(texts.m_calcPC_3,
                       texts.m_calcPC_4,isInt=False)
            if e<0: print(texts.m_calcPC_5)
        T = S.ejecuta(n,e)
        if T is None:
            print(texts.m_calcPC_6)
    clear()
    print(texts.m_calcPC_7)
    pmat(T)
    while S.SuperRed is None:
        e1 = leeNum(texts.m_System_Mat,texts.m_calcPC_8)
        if e1==0:
            clear()
            S, d = S.optimize_system(T, prnt=False)
        elif e1==1:
            clear()
            S.describeTM(T)
        elif e1==2:
            clear()
            print(texts.m_calcPC_9)
            S.ShowTMs()
            mt = -1
            while mt<0:
                mt = leeNum(texts.m_calcPC_10,texts.m_calcPC_8)
                if mt>-1 and mt<len(S.loMat):
                    T = S.loMat[mt]
                else:
                    print(texts.m_calcPC_8)
        elif e1==3: return calcPC(S,texts)
        else: print(texts.m_calcPC_8)
    return T

def newSystem(redes,texts):
    '''
    Crea un Sistema a partir de una lista de redes
    '''
    S = System(redes)
    T = None
    print(texts.m_newSystem_1)
    while True:
        e = leeNum(texts.m_System_Create,texts.m_newSystem_0)
        if e==0:
            clear()
            T = calcPC(S,texts)
        elif e==1:
            clear()
            newName = input(texts.m_newSystem_2)
            S.rename(newName)
        elif e==2:
            clear()
            if T is None: print(texts.m_newSystem_3)
            else:
                show_Lattice(S.SuperRed,texts)
        elif e==3:
            clear()
            if T is None: print(texts.m_newSystem_3)
            else: S.diffractionPattern()
        elif e==4:
            clear()
            if T is None: print(texts.m_newSystem_3)
            else:
                name = input(texts.m_newSystem_4)
                S.SuperRed.exportLattice(name=name)
        elif e==5: return S
        else:
            clear()
            print(texts.m_newSystem_0)

def printLatticeNames(redes,texts):
    '''
    Imprime en pantalla los nombres de las redes pertenecientes a una lista
    redes -> Lista de redes
    '''
    clear()
    print(texts.m_printLatticeNames_1)
    i=0
    for r in redes:
        print(f'\tL{i}: {r.name}')
        i+=1

def main():
    '''
    Ejecuta una interface para llevar paso a paso la creación y solución de un Sistema.
    '''
    texts = select_language()
    redes=[]
    while True:
        e1 = leeNum(texts.m_Initial,texts.m_main_0)
        if e1==1:
            clear()
            loadLattices(redes,texts)
        elif e1==2: break
        elif e1==3: return 0
        elif e1==0:
            clear()
            print(texts.m_Instructions)
        else: print(texts.m_main_0)
    clear()
    S = None
    while S is None:
        e3 = leeNum(texts.m_System,texts.m_main_0)
        if e3 == 0:
            clear()
            S = newSystem(redes,texts)
        elif e3 == 1:
            clear()
            printLatticeNames(redes,texts)
        elif e3 == 2:
            clear()
            loadLattices(redes,texts)
        elif e3 == 3: return 0
        else: print(texts.m_main_0)
    return 1

if __name__ == '__main__':
    sys.exit(main())