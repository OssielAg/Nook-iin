# Sección 6

## Español
###### Más pruebas

Regresamos al sistema de $FePS\_3-Grafeno$, pero ahora con un ángulo de rotación de 13.9, que acepta un modelo más pequeño que el ángulo ya visto.

## English
(Translation goes here)


---
## Español
```python
sr2 = System([l1,l2.mRot(13.9)])
sr2.searchLP(rangeOfSearch=10,epsilon=0.008)
sr2.calculateTM()
sr2.ShowTMs()
```
**Salida esperada:**
```

***Option 1: T <- Matrix loMat[0]
Size of the primitive vectors: |a|=17.79450Å, |b|=17.79450Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   0    3|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |   90   |
|          FePS3          |  |  -3    3|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  -2    8|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  104   |
|    Graphene(13.90°)     |  |  -8    6|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:194	DD:0.000093

***Option 2: T <- Matrix loMat[1]
Size of the primitive vectors: |a|=30.82098Å, |b|=30.82098Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   3   -6|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  270   |
|          FePS3          |  |   6   -3|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  10  -14|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  312   |
|    Graphene(13.90°)     |  |  14   -4|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:582	DD:0.000093

***Option 3: T <- Matrix loMat[2]
Size of the primitive vectors: |a|=35.58900Å, |b|=35.58900Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   0    6|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  360   |
|          FePS3          |  |  -6    6|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  -4   16|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  416   |
|    Graphene(13.90°)     |  | -16   12|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:776	DD:0.000093

***Option 4: T <- Matrix loMat[3]
Size of the primitive vectors: |a|=47.07982Å, |b|=47.07982Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   3   -9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  630   |
|          FePS3          |  |   9   -6|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  12  -22|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  728   |
|    Graphene(13.90°)     |  |  22  -10|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:1358	DD:0.000093

***Option 5: T <- Matrix loMat[4]
Size of the primitive vectors: |a|=53.38350Å, |b|=53.38350Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   0    9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  810   |
|          FePS3          |  |  -9    9|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  -6   24|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  936   |
|    Graphene(13.90°)     |  | -24   18|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:1746	DD:0.000093

***Option 6: T <- Matrix loMat[5]
Size of the primitive vectors: |a|=61.64196Å, |b|=61.64196Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   6    6|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  1080  |
|          FePS3          |  |  -6   12|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |   8   20|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  1248  |
|    Graphene(13.90°)     |  | -20   28|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:2328	DD:0.000093

***Option 7: T <- Matrix loMat[6]
Size of the primitive vectors: |a|=64.15898Å, |b|=64.15898Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   3    9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  1170  |
|          FePS3          |  |  -9   12|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |   0   26|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  1352  |
|    Graphene(13.90°)     |  | -26   26|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:2522	DD:0.000093

***Option 8: T <- Matrix loMat[7]
Size of the primitive vectors: |a|=77.56443Å, |b|=77.56443Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   6    9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  1710  |
|          FePS3          |  |  -9   15|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |   6   28|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  1976  |
|    Graphene(13.90°)     |  | -28   34|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:3686	DD:0.000093

***Option 9: T <- Matrix loMat[8]
Size of the primitive vectors: |a|=92.46293Å, |b|=92.46293Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   9    9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  2430  |
|          FePS3          |  |  -9   18|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  12   30|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  2808  |
|    Graphene(13.90°)     |  | -30   42|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:5238	DD:0.000093
Matriz sugerida: loMat[0]

```

## English
```python
sr2 = System([l1,l2.mRot(13.9)])
sr2.searchLP(rangeOfSearch=10,epsilon=0.008)
sr2.calculateTM()
sr2.ShowTMs()
```
**Expected output:**
```

***Option 1: T <- Matrix loMat[0]
Size of the primitive vectors: |a|=17.79450Å, |b|=17.79450Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   0    3|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |   90   |
|          FePS3          |  |  -3    3|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  -2    8|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  104   |
|    Graphene(13.90°)     |  |  -8    6|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:194	DD:0.000093

***Option 2: T <- Matrix loMat[1]
Size of the primitive vectors: |a|=30.82098Å, |b|=30.82098Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   3   -6|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  270   |
|          FePS3          |  |   6   -3|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  10  -14|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  312   |
|    Graphene(13.90°)     |  |  14   -4|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:582	DD:0.000093

***Option 3: T <- Matrix loMat[2]
Size of the primitive vectors: |a|=35.58900Å, |b|=35.58900Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   0    6|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  360   |
|          FePS3          |  |  -6    6|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  -4   16|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  416   |
|    Graphene(13.90°)     |  | -16   12|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:776	DD:0.000093

***Option 4: T <- Matrix loMat[3]
Size of the primitive vectors: |a|=47.07982Å, |b|=47.07982Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   3   -9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  630   |
|          FePS3          |  |   9   -6|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  12  -22|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  728   |
|    Graphene(13.90°)     |  |  22  -10|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:1358	DD:0.000093

***Option 5: T <- Matrix loMat[4]
Size of the primitive vectors: |a|=53.38350Å, |b|=53.38350Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   0    9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  810   |
|          FePS3          |  |  -9    9|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  -6   24|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  936   |
|    Graphene(13.90°)     |  | -24   18|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:1746	DD:0.000093

***Option 6: T <- Matrix loMat[5]
Size of the primitive vectors: |a|=61.64196Å, |b|=61.64196Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   6    6|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  1080  |
|          FePS3          |  |  -6   12|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |   8   20|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  1248  |
|    Graphene(13.90°)     |  | -20   28|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:2328	DD:0.000093

***Option 7: T <- Matrix loMat[6]
Size of the primitive vectors: |a|=64.15898Å, |b|=64.15898Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   3    9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  1170  |
|          FePS3          |  |  -9   12|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |   0   26|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  1352  |
|    Graphene(13.90°)     |  | -26   26|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:2522	DD:0.000093

***Option 8: T <- Matrix loMat[7]
Size of the primitive vectors: |a|=77.56443Å, |b|=77.56443Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   6    9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  1710  |
|          FePS3          |  |  -9   15|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |   6   28|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  1976  |
|    Graphene(13.90°)     |  | -28   34|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:3686	DD:0.000093

***Option 9: T <- Matrix loMat[8]
Size of the primitive vectors: |a|=92.46293Å, |b|=92.46293Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   9    9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  2430  |
|          FePS3          |  |  -9   18|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  12   30|  |  | 1.00016  0.00004|  |   +0.018% // -0.0°    |  2808  |
|    Graphene(13.90°)     |  | -30   42|  |  |-0.00004  1.00020|  |   +0.018% // -0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:5238	DD:0.000093
Matriz sugerida: loMat[0]

```

---
## Español
```python
sr2_1,d3=sr2.optimize_system(sr2.loMat[0])
sr2_2,d3=sr2.optimize_system(sr2.loMat[1])
```
**Salida esperada:**
```
Matriz de trasformación:
	0	3
	-3	3

Sistema [FePS3,Graphene(13.90°)] 
Celda unitaria con 194 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.
Matriz de trasformación:
	3	-6
	6	-3

Sistema [FePS3,Graphene(13.90°)] 
Celda unitaria con 582 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.

```

## English
```python
sr2_1,d3=sr2.optimize_system(sr2.loMat[0])
sr2_2,d3=sr2.optimize_system(sr2.loMat[1])
```
**Expected output:**
```
Matriz de trasformación:
	0	3
	-3	3

Sistema [FePS3,Graphene(13.90°)] 
Celda unitaria con 194 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.
Matriz de trasformación:
	3	-6
	6	-3

Sistema [FePS3,Graphene(13.90°)] 
Celda unitaria con 582 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.

```

---
## Español
Dos tBLG con una rotación de $24.8^o$, en la primera ambas capas tienen 6 simetrias radiales; en la segunda,su capa sustrato tiene sólo 3 simetreias radiales, generando 2 sistemas distintos, el primero con empalmes de tipo AA en las esquinas de su CP y el segundo con empalmes de tipo AB. 

## English
(Translation goes here)


---
## Español
```python
g2i=graphenC3()
g2i.atms[0][0].color=g2i.atms[0][1].color='red'
g1.detachment=2
g2.detachment=g2i.detachment=7
sa=System([g1,g2.mRot(24.8)])
sb=System([g1,g2i.mRot(24.8)])
t=[[2, 7], [-7, 9]]
sa,d=sa.optimize_system(t)
sb,d=sb.optimize_system(t)
sa.SuperRed.showme(3,3,t=1)
sb.SuperRed.showme(3,3,t=1)
```
**Salida esperada:**
```
Matriz de trasformación:
	2	7
	-7	9

Sistema [Grafeno,Grafeno(24.80°)] 
Celda unitaria con 268 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.
Matriz de trasformación:
	2	7
	-7	9

Sistema [Grafeno,Grafeno(s3)(24.80°)] 
Celda unitaria con 268 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.

```

## English
```python
g2i=graphenC3()
g2i.atms[0][0].color=g2i.atms[0][1].color='red'
g1.detachment=2
g2.detachment=g2i.detachment=7
sa=System([g1,g2.mRot(24.8)])
sb=System([g1,g2i.mRot(24.8)])
t=[[2, 7], [-7, 9]]
sa,d=sa.optimize_system(t)
sb,d=sb.optimize_system(t)
sa.SuperRed.showme(3,3,t=1)
sb.SuperRed.showme(3,3,t=1)
```
**Expected output:**
```
Matriz de trasformación:
	2	7
	-7	9

Sistema [Grafeno,Grafeno(24.80°)] 
Celda unitaria con 268 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.
Matriz de trasformación:
	2	7
	-7	9

Sistema [Grafeno,Grafeno(s3)(24.80°)] 
Celda unitaria con 268 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.

```

---
## Español
```python
sa.SuperRed.name="tBLG(24.8)AA"
sb.SuperRed.name="tBLG(24.8)AB"
sa.diffractionPattern(border=1.72,prnt=True,t=3)
sb.diffractionPattern(border=1.72,prnt=True,t=3)
```
**Salida esperada:**
```
Calculando Factor de estructura....4094 PRs calculados
Dirección de imagen: '/images/DP-tBLG(24_8)AA.png'
Calculando Factor de estructura....4094 PRs calculados
Dirección de imagen: '/images/DP-tBLG(24_8)AB.png'

```

## English
```python
sa.SuperRed.name="tBLG(24.8)AA"
sb.SuperRed.name="tBLG(24.8)AB"
sa.diffractionPattern(border=1.72,prnt=True,t=3)
sb.diffractionPattern(border=1.72,prnt=True,t=3)
```
**Expected output:**
```
Calculando Factor de estructura....4094 PRs calculados
Dirección de imagen: '/images/DP-tBLG(24_8)AA.png'
Calculando Factor de estructura....4094 PRs calculados
Dirección de imagen: '/images/DP-tBLG(24_8)AB.png'

```

---
## Español
Al analizar el patrón de difracción de cada sistema podemos ver que es el mismo, por lo que ambos sistemas son iguales y simplemente uno es el otro con una traslación, por lo que sus CPs parecen distintas.

## English
(Translation goes here)


---
## Español
 Más ejemplos

## English
(Translation goes here)


---
## Español
```python
s1=System([g1,g2.mRot(3.15)])
s2=System([g1,g2i.mRot(3.15)])
t=[[11, 10], [-10, 21]]
s1,d=s1.optimize_system(t)
s2,d=s2.optimize_system(t)
```
**Salida esperada:**
```
Matriz de trasformación:
	11	10
	-10	21

Sistema [Grafeno,Grafeno(3.15°)] 
Celda unitaria con 1324 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.
Matriz de trasformación:
	11	10
	-10	21

Sistema [Grafeno,Grafeno(s3)(3.15°)] 
Celda unitaria con 1324 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.

```

## English
```python
s1=System([g1,g2.mRot(3.15)])
s2=System([g1,g2i.mRot(3.15)])
t=[[11, 10], [-10, 21]]
s1,d=s1.optimize_system(t)
s2,d=s2.optimize_system(t)
```
**Expected output:**
```
Matriz de trasformación:
	11	10
	-10	21

Sistema [Grafeno,Grafeno(3.15°)] 
Celda unitaria con 1324 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.
Matriz de trasformación:
	11	10
	-10	21

Sistema [Grafeno,Grafeno(s3)(3.15°)] 
Celda unitaria con 1324 átomos:
Espacio Reciproco:
***La supercelda calculada está optimizada
Se deformó al menos una de las capas del sistema para hacerlo.

```

---
## Español
```python
s1.SuperRed.showme(3,3,t=0.5)
s2.SuperRed.showme(3,3,t=0.5)
```

## English
```python
s1.SuperRed.showme(3,3,t=0.5)
s2.SuperRed.showme(3,3,t=0.5)
```

---
## Español
```python
s1.SuperRed.name="tBLG(3.15)AA"
s2.SuperRed.name="tBLG(3.15)AB"
s1.diffractionPattern(border=1.2,prnt=True,t=3)
s2.diffractionPattern(border=1.2,prnt=True,t=3)
```
**Salida esperada:**
```
Calculando Factor de estructura....9832 PRs calculados
Dirección de imagen: '/images/DP-tBLG(3_15)AA.png'
Calculando Factor de estructura....9832 PRs calculados
Dirección de imagen: '/images/DP-tBLG(3_15)AB.png'

```

## English
```python
s1.SuperRed.name="tBLG(3.15)AA"
s2.SuperRed.name="tBLG(3.15)AB"
s1.diffractionPattern(border=1.2,prnt=True,t=3)
s2.diffractionPattern(border=1.2,prnt=True,t=3)
```
**Expected output:**
```
Calculando Factor de estructura....9832 PRs calculados
Dirección de imagen: '/images/DP-tBLG(3_15)AA.png'
Calculando Factor de estructura....9832 PRs calculados
Dirección de imagen: '/images/DP-tBLG(3_15)AB.png'

```

---
## Español
```python
g2.detachment=g2i.detachment=3
g3i=graphenC3()
g3i.atms[0][0].color=g3i.atms[0][1].color='blue'
t = 13.282
S3_1=System([g1,g2.mRot(t),g3.mRot(2*t)])
S3_2=System([g1,g2.mRot(t),g3i.mRot(2*t)])
S3_3=System([g1,g2i.mRot(t),g3i.mRot(2*t)])
S3_4=System([g1,g2i.mRot(t),g3.mRot(2*t)])
T=S3_1.ejecuta(20,0.02)
_=S3_1.leeMT(T)
```
**Salida esperada:**
```
Size of the primitive vectors: |a|=36.84319Å, |b|=36.84319Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |  14  -16|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  456   |
|         Grafeno         |  |  16   -2|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  16  -14|  |  | 0.99891  0.00219|  |    +0.0% // -0.11°    |  456   |
|     Grafeno(13.28°)     |  |  14    2|  |  |-0.00219  1.00109|  |    +0.0% // -0.11°    |        |
|                         |               |                       |                       |        |
|                         |  |  17  -11|  |  | 1.01505 -0.00785|  |   +1.115% // +0.39°   |  446   |
|     Grafeno(26.56°)     |  |  11    6|  |  | 0.00785  1.00720|  |   +1.115% // +0.39°   |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:1358	DD:0.003696

```

## English
```python
g2.detachment=g2i.detachment=3
g3i=graphenC3()
g3i.atms[0][0].color=g3i.atms[0][1].color='blue'
t = 13.282
S3_1=System([g1,g2.mRot(t),g3.mRot(2*t)])
S3_2=System([g1,g2.mRot(t),g3i.mRot(2*t)])
S3_3=System([g1,g2i.mRot(t),g3i.mRot(2*t)])
S3_4=System([g1,g2i.mRot(t),g3.mRot(2*t)])
T=S3_1.ejecuta(20,0.02)
_=S3_1.leeMT(T)
```
**Expected output:**
```
Size of the primitive vectors: |a|=36.84319Å, |b|=36.84319Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |  14  -16|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  456   |
|         Grafeno         |  |  16   -2|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  16  -14|  |  | 0.99891  0.00219|  |    +0.0% // -0.11°    |  456   |
|     Grafeno(13.28°)     |  |  14    2|  |  |-0.00219  1.00109|  |    +0.0% // -0.11°    |        |
|                         |               |                       |                       |        |
|                         |  |  17  -11|  |  | 1.01505 -0.00785|  |   +1.115% // +0.39°   |  446   |
|     Grafeno(26.56°)     |  |  11    6|  |  | 0.00785  1.00720|  |   +1.115% // +0.39°   |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:1358	DD:0.003696

```

---
## Español
```python
SAAA,d1 = S3_1.optimize_system(T,prnt=False)
SAAB,d2 = S3_2.optimize_system(T,prnt=False)
SABB,d3 = S3_3.optimize_system(T,prnt=False)
SABA,d4 = S3_4.optimize_system(T,prnt=False)
Sistemas=[SAAA,SAAB,SABB,SABA]
Nombres=['SAAA','SAAB','SABB','SABA']
i=0
for s in Sistemas:
    s.SuperRed.showme(3,3,t=0.5,iName=f"{Nombres[i]}_SuperCelda3x3")
    s.SuperRed.name=Nombres[i]
    i+=1
```
**Salida esperada:**
```
Dirección de imagen: '/images/SAAA_SuperCelda3x3.png'
Dirección de imagen: '/images/SAAB_SuperCelda3x3.png'
Dirección de imagen: '/images/SABB_SuperCelda3x3.png'
Dirección de imagen: '/images/SABA_SuperCelda3x3.png'

```

## English
```python
SAAA,d1 = S3_1.optimize_system(T,prnt=False)
SAAB,d2 = S3_2.optimize_system(T,prnt=False)
SABB,d3 = S3_3.optimize_system(T,prnt=False)
SABA,d4 = S3_4.optimize_system(T,prnt=False)
Sistemas=[SAAA,SAAB,SABB,SABA]
Nombres=['SAAA','SAAB','SABB','SABA']
i=0
for s in Sistemas:
    s.SuperRed.showme(3,3,t=0.5,iName=f"{Nombres[i]}_SuperCelda3x3")
    s.SuperRed.name=Nombres[i]
    i+=1
```
**Expected output:**
```
Dirección de imagen: '/images/SAAA_SuperCelda3x3.png'
Dirección de imagen: '/images/SAAB_SuperCelda3x3.png'
Dirección de imagen: '/images/SABB_SuperCelda3x3.png'
Dirección de imagen: '/images/SABA_SuperCelda3x3.png'

```

---
## Español
```python
for s in Sistemas:
    s.diffractionPattern(border=2.1,t=1.7,prnt=True)
```
**Salida esperada:**
```
Calculando Factor de estructura....20766 PRs calculados
Dirección de imagen: '/images/DP-SAAA.png'
Calculando Factor de estructura....20766 PRs calculados
Dirección de imagen: '/images/DP-SAAB.png'
Calculando Factor de estructura....20766 PRs calculados
Dirección de imagen: '/images/DP-SABB.png'
Calculando Factor de estructura....20766 PRs calculados
Dirección de imagen: '/images/DP-SABA.png'

```

## English
```python
for s in Sistemas:
    s.diffractionPattern(border=2.1,t=1.7,prnt=True)
```
**Expected output:**
```
Calculando Factor de estructura....20766 PRs calculados
Dirección de imagen: '/images/DP-SAAA.png'
Calculando Factor de estructura....20766 PRs calculados
Dirección de imagen: '/images/DP-SAAB.png'
Calculando Factor de estructura....20766 PRs calculados
Dirección de imagen: '/images/DP-SABB.png'
Calculando Factor de estructura....20766 PRs calculados
Dirección de imagen: '/images/DP-SABA.png'

```

---
## Español
```python
redes=[g1,g2.mRot(t),g2i.mRot(t),g3.mRot(2*t),g3i.mRot(2*t)]
for l in redes:
    l.showme(5,5,t=3)
    l.printLightPoints(border=2.1,t=1.7,prnt=True)
```
**Salida esperada:**
```
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno.png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(13_28°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(s3)(13_28°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(26_56°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(s3)(26_56°).png'

```

## English
```python
redes=[g1,g2.mRot(t),g2i.mRot(t),g3.mRot(2*t),g3i.mRot(2*t)]
for l in redes:
    l.showme(5,5,t=3)
    l.printLightPoints(border=2.1,t=1.7,prnt=True)
```
**Expected output:**
```
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno.png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(13_28°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(s3)(13_28°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(26_56°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(s3)(26_56°).png'

```

---
## Español
```python
S3_1.diffractionPattern(border=2.1,t=1.7,prnt=True)
```
**Salida esperada:**
```
Calculando Factor de estructura....20766 PRs calculados
Dirección de imagen: '/images/DP-SAAA.png'

```

## English
```python
S3_1.diffractionPattern(border=2.1,t=1.7,prnt=True)
```
**Expected output:**
```
Calculando Factor de estructura....20766 PRs calculados
Dirección de imagen: '/images/DP-SAAA.png'

```

---
## Español
```python
for i in range(144):
    lc=graphen().mRot(0.4167*i)
    le=graphenC3().mRot(0.4167*i)
    lc.printLightPoints(border=2.1,t=1.7,prnt=True)
    #le.printLightPoints(border=2.1,t=1.7,prnt=True)
    
```
**Salida esperada:**
```
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(0_00°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(0_42°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(0_83°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(1_25°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(1_67°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(2_08°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(2_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(2_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(3_33°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(3_75°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(4_17°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(4_58°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(5_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(5_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(5_83°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(6_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(6_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(7_08°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(7_50°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(7_92°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(8_33°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(8_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(9_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(9_58°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(10_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(10_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(10_83°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(11_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(11_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(12_08°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(12_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(12_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(13_33°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(13_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(14_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(14_58°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(15_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(15_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(15_83°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(16_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(16_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(17_08°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(17_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(17_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(18_33°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(18_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(19_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(19_58°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(20_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(20_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(20_84°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(21_25°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(21_67°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(22_09°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(22_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(22_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(23_34°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(23_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(24_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(24_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(25_00°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(25_42°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(25_84°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(26_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(26_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(27_09°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(27_50°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(27_92°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(28_34°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(28_75°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(29_17°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(29_59°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(30_00°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(30_42°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(30_84°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(31_25°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(31_67°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(32_09°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(32_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(32_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(33_34°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(33_75°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(34_17°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(34_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(35_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(35_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(35_84°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(36_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(36_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(37_09°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(37_50°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(37_92°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(38_34°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(38_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(39_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(39_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(40_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(40_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(40_84°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(41_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(41_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(42_09°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(42_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(42_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(43_34°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(43_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(44_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(44_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(45_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(45_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(45_84°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(46_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(46_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(47_09°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(47_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(47_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(48_34°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(48_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(49_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(49_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(50_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(50_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(50_84°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(51_25°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(51_67°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(52_09°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(52_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(52_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(53_34°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(53_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(54_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(54_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(55_00°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(55_42°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(55_84°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(56_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(56_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(57_09°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(57_50°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(57_92°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(58_34°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(58_75°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(59_17°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(59_59°).png'

```

## English
```python
for i in range(144):
    lc=graphen().mRot(0.4167*i)
    le=graphenC3().mRot(0.4167*i)
    lc.printLightPoints(border=2.1,t=1.7,prnt=True)
    #le.printLightPoints(border=2.1,t=1.7,prnt=True)
    
```
**Expected output:**
```
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(0_00°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(0_42°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(0_83°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(1_25°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(1_67°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(2_08°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(2_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(2_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(3_33°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(3_75°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(4_17°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(4_58°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(5_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(5_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(5_83°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(6_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(6_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(7_08°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(7_50°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(7_92°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(8_33°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(8_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(9_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(9_58°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(10_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(10_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(10_83°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(11_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(11_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(12_08°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(12_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(12_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(13_33°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(13_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(14_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(14_58°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(15_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(15_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(15_83°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(16_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(16_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(17_08°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(17_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(17_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(18_33°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(18_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(19_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(19_58°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(20_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(20_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(20_84°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(21_25°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(21_67°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(22_09°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(22_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(22_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(23_34°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(23_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(24_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(24_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(25_00°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(25_42°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(25_84°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(26_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(26_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(27_09°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(27_50°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(27_92°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(28_34°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(28_75°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(29_17°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(29_59°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(30_00°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(30_42°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(30_84°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(31_25°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(31_67°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(32_09°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(32_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(32_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(33_34°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(33_75°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(34_17°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(34_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(35_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(35_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(35_84°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(36_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(36_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(37_09°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(37_50°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(37_92°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(38_34°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(38_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(39_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(39_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(40_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(40_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(40_84°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(41_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(41_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(42_09°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(42_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(42_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(43_34°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(43_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(44_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(44_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(45_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(45_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(45_84°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(46_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(46_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(47_09°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(47_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(47_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(48_34°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(48_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(49_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(49_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(50_00°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(50_42°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(50_84°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(51_25°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(51_67°).png'
Calculando Factor de estructura....88 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(52_09°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(52_50°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(52_92°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(53_34°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(53_75°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(54_17°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(54_59°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(55_00°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(55_42°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(55_84°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(56_25°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(56_67°).png'
Calculando Factor de estructura....90 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(57_09°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(57_50°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(57_92°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(58_34°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(58_75°).png'
Calculando Factor de estructura....94 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(59_17°).png'
Calculando Factor de estructura....92 PRs calculados
Dirección de imagen: '/images/DP-Grafeno(59_59°).png'

```

---
## Español
```python
144*.4167
```

## English
```python
144*.4167
```

---
## Español
```python

```

## English
```python

```

---
