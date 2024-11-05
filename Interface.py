from src.System import *
import sys

m_Inicial = '''
Elija una opción:
\t0-Instrucciones.
\t1-Cargar redes para el sistema.
\t2-Crear Sistema.
\t3-Salir.
'''
m_Redes ='''
Cargar red.
\t1-Entrada manual.
\t2-Importar archivo.
\t3-Terminar.
'''
m_Sistema = '''
¿Que desea hacer?
\t0-Crear Sistema.
\t1-Mostrar redes en memoria.
\t2-Cargar más redes.
\t3-Salir.
'''
m_Sistema_Crear = '''
¿Que desea hacer a continuación?
\t0-Calcular CP para el sistema.
\t1-Cambiar nombre de la red.
\t2-Mostrar sistema.
\t3-Mostrar patron de difracción.
\t4-Exportar sistema a archivo POSCAR.
\t5-Terminar y cerrar.
'''
m_Sistema_Mat = '''
¿Que desea hacer?
\t0-Usar la MT seleccionada para calcular la CP del sistema.
\t1-Mostrar tabla referente a la MT seleccionada.
\t2-Seleccionar una nueva MT.
\t3-Hacer una nueva busqueda con 'n' y 'epsilon' distintos.
'''
m_Instrucciones='''
x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+
   Ingrese las redes que conforman al sistema, el orden en que son ingresadas debe
ser el mismo en el que están apiladas las redes desde abajo.

   Las redes se pueden agregar manualmente o importandola desde un archivo POSCAR.
Si la red se agrega manualmente, lo primero que se piden son los VPs de esta, los
cuales son dados componente por componente, por ejemplo si a=(2.11,0.2,0.0) las
componentes dadas seran 'a1=2.11, a2=0.2 y a3=0.0'.

   Una vez dados los VPs se continúa con la base atómica. Lo primero es especificar
el número de especies atómicas en la BA, para cada una de estas se pedirá el
simbolo que la representa, el color con el que se representará en pantalla y el
la cantidad de átomos de esta especie que hay. Para cada átomo se debe dar su
posición relativa con respecto a los VPs de la red.

   Una vez dadas las redes, se puede continuar a Crear el sistema. Con el sistema
creado se continua a buscar una celda primitiva para este, para hacerlo se requiere
de las variables 'n' y 'epsilon' que describen el área de busqueda y el error
máximo aceptado respectivamente.

   Con la CP calculada para el sistema se puede mostrar su representacion en los
espacios real y reciproco, así cómo su Patrón de difracción. Si se quiere tambien
se puede expoprtar el resultado a un archivo POSCAR.
x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+
'''
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
        
def newVector(v:str):
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
        print(f'Error en los valores ingresados. Ingrese de nuevo los componentes para el vector {v}')
        return None

def newAtomicBase():
    '''
    Carga la báse atómica para una Red cargando todos los átomos de cada especie atómica
    en la base
    '''
    n = leeNum("¿Cuantas especies atómicas hay en la red? ",
               "**Error. Ingrese un número entero.**")
    atms = []
    if n<1:
        print("Base atómica bacía, no hay átomos en la red")
    i=0
    while i<n:
        i+=1
        clear()
        idAtom = input("¿Cual es el simbolo de la especie atómica? ")
        color = leeColor("Ingrese el color con el que se representarán los átomos: ",
                         "\t**ERROR.Valor no valido.**")
        noa = leeNum(f"¿Cuantos átomos de '{idAtom}' hay en la base? ",
                     "\t**Error. Ingrese un número entero.**")
        for j in range(noa):
            clear()
            print(f"\nIndique la posición relativa del átomo '{idAtom}-{j+1}' con respecto a los VPs de la red.")
            pa = leeNum("Indique la componente correspondiente al VP a: ",
                        "\t**ERROR. Ingrese un número.**",
                        isInt=False)
            pb = leeNum("Indique la componente correspondiente al VP b: ",
                        "\t**ERROR. Ingrese un número.**",
                        isInt=False)
            pc = leeNum("Indique la componente correspondiente al VP c: ",
                        "\t**ERROR. Ingrese un número.**",
                        isInt=False)
            atms.append(Atom((pa,pb),posZ=pc,color=color,sig=idAtom))
    return atms

def menuNewL(l,mem):
    '''
    Maneja y agrega una red 'l' a la lista 'mem'.
    l  -> Red con la que se va a trabajar
    mem-> Lista de redes donde se puede guardar la red
    '''
    while True:
        print("\n¿Que desea hacer?")
        print("\t0-Guardar red creada\n"+
              "\t1-Ver POSCAR de la red creada\n"+
              "\t2-Ver Imagen de la red creada\n"+
              "\t3-Rotar la red\n"
              "\t4-Crear de nuevo la red.")
        k = leeNum('','Entrada invalida')
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
            th = leeNum("¿Cuantos grados se rotará la red?",
                        "Entrada invalida",isInt=False)
            l = l.mRot(th)
        elif k==4:
            return True
        else:
            print('Entrada invalida')
    
def newLattice1(mem):
    '''
    Crea una Red de forma manual paso a paso.
    mem -> Lista de redes donde se guardará la red
    '''
    crear=True
    while crear:
        clear()#-------------------------------------------
        latticeName = input("Indique el nombre de la red: ")
        print("Indique los vectores primitivos de la red.")
        a = b = c = None
        while a is None:
            a = newVector('a')
        while b is None:
            b = newVector('b')
        while c is None:
            c = newVector('c')
        clear()#-------------------------------------------
        print(f"a={a}, b={b}, c={c}\n")
        print("Ingresando Átomos de la base atómica...")
        AB = newAtomicBase()
        clear()#-------------------------------------------
        (a1,a2,a3)=a
        (b1,b2,b3)=b
        (c1,c2,c3)=c
        l = Lattice((a1,a2),(b1,b2),atms=AB,name=latticeName,detachment=c3)
        print("Red creada.")
        crear=menuNewL(l,mem)
    return l

def newLattice2(mem):
    '''
    Crea una Red importandola desde un archivo POSCAR
    mem -> Lista de redes donde se guardará la red
    '''
    crear=True
    while crear:
        clear()#------------------------------------------
        l = None
        while l is None:
            fileName = input('Indique el nombre del archivo VASP que describe la red: ')
            l = importLattice(fileName)
        clear()#------------------------------------------
        print("Red creada.")
        crear=menuNewL(l,mem)
    return l

def muestraRed(red):
    while True:
        e = leeNum("¿Que imagen quiere desplegar?\n"+
                   "\t1-Representación en el espacio Real\n"+
                   "\t2-Representación en el espacio reciproco\n"+
                   "\t0-Salir\n",
                   "Entrada invalida")
        if e==0: break
        elif e==1:
            clear()
            red.showme()
        elif e==2:
            clear()
            red.printReciprocalSpace()
        else:
            print("Entrada invalida")

def cargaRedes(redes):
    '''
    Crea y guarda Redes en una lista.
    redes -> Lista de redes donde se guardará la red
    '''
    while True:
        clear()
        e2 = leeNum(m_Redes,"Entrada invalida. Elija 1, 2 o 3")
        if e2==1: newLattice1(redes)
        elif e2==2: newLattice2(redes)
        elif e2==3: break
        else: print("Entrada invalida. Elija 0, 1, 2 o 3")
    print(f"Hay {len(redes)} redes en memoria.")
    
def buscarCP(S):
    '''
    Busca una CP para un sistema dado
    S -> Sistema con el que se trabajará
    '''
    T = None
    while T is None:
        n = e = -1
        while n<1:
            n = leeNum("Indique el valor de 'n' para delimitar el área de búsqueda: ",
                       "Entrada invalida. Proporcione un número entero mayor a cero.")
            if n<1: print("Entrada invalida. Proporcione un número entero mayor a cero.")
        while e<0:
            e = leeNum("Indique el valor de 'epsilon', el error máximo aceptado.\n"+
                       "Se recomienda un valor menor a 0.05: ",
                       "Entrada invalida. Ingrese un número positivo.",isInt=False)
            if e<0: print("Entrada invalida. Proporcione un número positivo.")
        T = S.ejecuta(n,e)
        if T is None:
            print("No se encontró solución al sistema con los valores 'n' y 'epsilon' dados.\n"+
                  "Procure dar un valor mayor a 'n' o 'epsilon'.")
    clear()
    print("Se propone utilizar la siguiente MT:")
    pmat(T)
    while S.SuperRed is None:
        e1 = leeNum(m_Sistema_Mat,"Entrada invalida")
        if e1==0:
            clear()
            S, d = S.optimize_system(T, prnt=False)
        elif e1==1:
            clear()
            S.leeMT(T)
        elif e1==2:
            clear()
            print("MTs en loMat:")
            S.ShowTMs()
            mt = -1
            while mt<0:
                mt = leeNum("¿Cuál MT de loMat elige? ","Entrada invalida")
                if mt>-1 and mt<len(S.loMat):
                    T = S.loMat[mt]
                else:
                    print("Entrada invalida")
        elif e1==3: return buscarCP(S)
        else: print("Entrada invalida")
    return T

def newSystem(redes):
    '''
    Crea un Sistema a partir de una lista de redes
    '''
    S = System(redes)
    T = None
    print("Se creo el sistema con las redes guardadas.")
    while True:
        e = leeNum(m_Sistema_Crear,"Entrada invalida.")
        if e==0:
            clear()
            T = buscarCP(S)
        elif e==1:
            clear()
            newName = input("Ingrese el nuevo nombre: ")
            S.rename(newName)
        elif e==2:
            clear()
            if T is None: print("Calcule primero la CP del sistema.")
            else:
                muestraRed(S.SuperRed)
        elif e==3:
            clear()
            if T is None: print("Calcule primero la CP del sistema.")
            else: S.diffractionPattern()
        elif e==4:
            clear()
            if T is None: print("Calcule primero la CP del sistema.")
            else:
                name = input("Ingrese el nombre para el archivo POSCAR: ")
                S.SuperRed.exportLattice(name=name)
        elif e==5: return S
        else:
            clear()
            print("Entrada invalida")

def muestraRedes(redes):
    '''
    Imprime en pantalla los nombres de las redes pertenecientes a una lista
    redes -> Lista de redes
    '''
    clear()
    print("Redes en memoria:")
    i=0
    for r in redes:
        print(f'\tL{i}: {r.name}')
        i+=1

def main():
    '''
    Ejecuta una interface para llevar paso a paso la creación y solución de un Sistema.
    '''
    redes=[]
    while True:
        e1 = leeNum(m_Inicial,"Entrada invalida. Elija 0, 1, 2 o 3")
        if e1==1:
            clear()
            cargaRedes(redes)
        elif e1==2: break
        elif e1==3: return 0
        elif e1==0:
            clear()
            print(m_Instrucciones)
        else: print("Entrada invalida. Elija 1, 2 o 3")
    clear()
    S = None
    while S is None:
        e3 = leeNum(m_Sistema,"Entrada invalida. Elija 0, 1, 2 o 3")
        if e3 == 0:
            clear()
            S = newSystem(redes)
        elif e3 == 1:
            clear()
            muestraRedes(redes)
        elif e3 == 2:
            clear()
            cargaRedes(redes)
        elif e3 == 3: return 0
        else: print("Entrada invalida. Elija 0, 1, 2 o 3")
    return 1

if __name__ == '__main__':
    sys.exit(main())