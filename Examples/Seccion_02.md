# Sección 2

## Español
#### Crear redes
Las redes (Lattices) son los cristales que forman las estructuras modeladas por los sistemas creados, tenemos dos formas para crear redes:

La primera es crear manualmente la red indicando los vectores primitivos (PV) de esta, la lista de átomos en su base atómica (esta debe ser una lista de objetos de clase Atom con sus posiciones relativas segun los PVs de la red).
Tambien se puede hacer uso de las instrucciones hexa3(),hexa6() y rectLattice para crear redes hexagonales (con simetrias S3 o S6) y rectangulares, donde sólo indicaremos el tamaño de el/los periodos. Igualmente se cuenta con redes precreadas que se pueden usar (grafeno y fosforeno negro).

A continuación se creará una Lattice para beta-GeSe de forma manual.

## English
(Translation goes here)


---
## Español
```python
# Base atómica de la red.
pos1,pos2,pos3,pos4=(0.750000000,0.367782116),(0.250000000,0.868400931),(0.750000000,0.846623361),(0.250000000,0.346943438)
atomos=[Atom(pos1,posZ=0.160547823,color='purple',sig='Ge'),
        Atom(pos2,posZ=0.063394181,color='purple',sig='Ge'),
        Atom(pos3,posZ=0.160837263,color='green',sig='Se'),
        Atom(pos4,posZ=0.063084550,color='green',sig='Se')]
# Enlaces de los átomos en la base (opcional)
enlaces=[(pos1,pos3),(pos1,pos4),(pos1,sumaV(pos4,(1,0))),(pos1,sumaV(pos3,(0,-1))),
         (pos2,pos4),(pos2,pos3),(pos2,sumaV(pos3,(-1,0))),(pos2,sumaV(pos4,(0,1)))]
# Vectores primitivos de la red
vA, vB = (3.8261001110,0.0000000000), (0.0000000000,5.8088998795)
# Inicialización de la Red
bGeSe = Lattice(vA,vB,atms=atomos,enls=enlaces,detachment=18.0892009735,name='b-GeSe')
#Muestra en pantalla de los resultados
print("+-"*40+"\n"+bGeSe.showData()+"\n"+"+-"*40)
bGeSe.showme(x=3,y=3)
```
**Salida esperada:**
```
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
b-GeSe
1.0
        3.8261001110         0.0000000000         0.0000000000
        0.0000000000         5.8088998795         0.0000000000
        0.0000000000         0.0000000000         18.0892009735
	Ge	Se
	2	2
Direct
         0.7500000000         0.3677821160         0.1606478230
         0.2500000000         0.8684009310         0.0634941810
         0.7500000000         0.8466233610         0.1609372630
         0.2500000000         0.3469434380         0.0631845500
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

```

## English
```python
# Base atómica de la red.
pos1,pos2,pos3,pos4=(0.750000000,0.367782116),(0.250000000,0.868400931),(0.750000000,0.846623361),(0.250000000,0.346943438)
atomos=[Atom(pos1,posZ=0.160547823,color='purple',sig='Ge'),
        Atom(pos2,posZ=0.063394181,color='purple',sig='Ge'),
        Atom(pos3,posZ=0.160837263,color='green',sig='Se'),
        Atom(pos4,posZ=0.063084550,color='green',sig='Se')]
# Enlaces de los átomos en la base (opcional)
enlaces=[(pos1,pos3),(pos1,pos4),(pos1,sumaV(pos4,(1,0))),(pos1,sumaV(pos3,(0,-1))),
         (pos2,pos4),(pos2,pos3),(pos2,sumaV(pos3,(-1,0))),(pos2,sumaV(pos4,(0,1)))]
# Vectores primitivos de la red
vA, vB = (3.8261001110,0.0000000000), (0.0000000000,5.8088998795)
# Inicialización de la Red
bGeSe = Lattice(vA,vB,atms=atomos,enls=enlaces,detachment=18.0892009735,name='b-GeSe')
#Muestra en pantalla de los resultados
print("+-"*40+"\n"+bGeSe.showData()+"\n"+"+-"*40)
bGeSe.showme(x=3,y=3)
```
**Expected output:**
```
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
b-GeSe
1.0
        3.8261001110         0.0000000000         0.0000000000
        0.0000000000         5.8088998795         0.0000000000
        0.0000000000         0.0000000000         18.0892009735
	Ge	Se
	2	2
Direct
         0.7500000000         0.3677821160         0.1606478230
         0.2500000000         0.8684009310         0.0634941810
         0.7500000000         0.8466233610         0.1609372630
         0.2500000000         0.3469434380         0.0631845500
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

```

---
## Español
La segunda forma es mediante el comando importLattice(), en este caso se carga un archivo POSCAR guardado en la raiz del programa.

**En este caso, a menos que se agreguen manualmente, los enlaces atómicos no se imprimen dado que no se calculan automaticamente.*

## English
(Translation goes here)


---
## Español
```python
# Importamos los archivos POSCAR de FePS3 y Graphene dados
l1=importLattice("VASP_Files/FePS3")
l2=importLattice("VASP_Files/graphene")

# Renombramos para tener los nombres correctos
l1.name="FePS3"
l2.name="Graphene"

#Muestra en pantalla de los resultados
print("+-"*40+"\n"+l1.showData()+"\n"+"+-"*40)
l1.showme(x=3,y=3)
print("+-"*40+"\n"+l2.showData()+"\n"+"+-"*40)
l2.showme(x=3,y=3)
```
**Salida esperada:**
```
Se leerá el archivo VASP_Files/FePS3.vasp
--Red creada a partir del archivo 'VASP_Files/FePS3.vasp'--
Se leerá el archivo VASP_Files/graphene.vasp
--Red creada a partir del archivo 'VASP_Files/graphene.vasp'--
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
FePS3
1.0
        5.9314999580         0.0000000000         0.0000000000
        -2.9657499790         5.1368296462         0.0000000000
        0.0000000000         0.0000000000         20.0000000000
	Fe	P	S
	2	2	6
Direct
         0.0000000000         0.0000000000         0.5001000000
         0.6666666870         0.3333333430         0.5001000000
         0.3333333430         0.6666666870         0.4451491070
         0.3333333430         0.6666666870         0.5550508930
         0.3333333430         0.3302960990         0.4212900530
         0.3333333430         0.0030372400         0.5789099770
         0.9969627860         0.6666666870         0.4212900530
         0.9969627860         0.3302960990         0.5789099770
         0.6697039010         0.6666666870         0.5789099770
         0.6697039010         0.0030372400         0.4212900530
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
Graphene
1.0
        2.4672000408         0.0000000000         0.0000000000
        -1.2336000204         2.1366579116         0.0000000000
        0.0000000000         0.0000000000         5.0000000000
	C
	2
Direct
         0.3333333430         0.6666666870         0.1001000000
         0.6666666870         0.3333333430         0.1001000000
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

```

## English
```python
# Importamos los archivos POSCAR de FePS3 y Graphene dados
l1=importLattice("VASP_Files/FePS3")
l2=importLattice("VASP_Files/graphene")

# Renombramos para tener los nombres correctos
l1.name="FePS3"
l2.name="Graphene"

#Muestra en pantalla de los resultados
print("+-"*40+"\n"+l1.showData()+"\n"+"+-"*40)
l1.showme(x=3,y=3)
print("+-"*40+"\n"+l2.showData()+"\n"+"+-"*40)
l2.showme(x=3,y=3)
```
**Expected output:**
```
Se leerá el archivo VASP_Files/FePS3.vasp
--Red creada a partir del archivo 'VASP_Files/FePS3.vasp'--
Se leerá el archivo VASP_Files/graphene.vasp
--Red creada a partir del archivo 'VASP_Files/graphene.vasp'--
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
FePS3
1.0
        5.9314999580         0.0000000000         0.0000000000
        -2.9657499790         5.1368296462         0.0000000000
        0.0000000000         0.0000000000         20.0000000000
	Fe	P	S
	2	2	6
Direct
         0.0000000000         0.0000000000         0.5001000000
         0.6666666870         0.3333333430         0.5001000000
         0.3333333430         0.6666666870         0.4451491070
         0.3333333430         0.6666666870         0.5550508930
         0.3333333430         0.3302960990         0.4212900530
         0.3333333430         0.0030372400         0.5789099770
         0.9969627860         0.6666666870         0.4212900530
         0.9969627860         0.3302960990         0.5789099770
         0.6697039010         0.6666666870         0.5789099770
         0.6697039010         0.0030372400         0.4212900530
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
Graphene
1.0
        2.4672000408         0.0000000000         0.0000000000
        -1.2336000204         2.1366579116         0.0000000000
        0.0000000000         0.0000000000         5.0000000000
	C
	2
Direct
         0.3333333430         0.6666666870         0.1001000000
         0.6666666870         0.3333333430         0.1001000000
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

```

---
