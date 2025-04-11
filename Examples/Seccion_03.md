# Sección 3

## Español
#### Creación y funciones para el sistema

Se modela la estructura mediante la creación de un *Sistema* señalando en una lista las redes que lo conforman, entonces podemos buscar una celda primitiva(PC) para este. Puede hacerce sitematicamente ejecutando las funciones searchLP() y calculateTM(), es en la primera donde se dan los parametros de la busqueda, rangeOfSearch y epsilon, que determinan respectivamente el alcance de la búsqueda y el error máximo aceptado. Teniendo esos resultados se puede ejecutar la función muestra(), esta desplegará tablas con la descripción de las PCs generadas por las matrices de transformación calculadas.

Puede ejecutarse sólamente la función muestra(), en ese caso el cálculo se hará con los parametros por default ( n=15
 y 𝜖=0.05
 ).

A continuación crearemos y evaluaremos posibles PCs para un sistema de 𝐹𝑒𝑃𝑆3
 y Grafeno con un ángulo entre sus capas de 24.07°
 (esta es una de las opciones dadas por la función analyze()).

## English
(Translation goes here)


---
## Español
```python
#Inicializa el Sistema
sr=System([l1,l2.mRot(24.07)])

# Buscan posibles vectores primitivos en un alcance de busqueda de maximo 20 y error maximo de 0.005
sr.searchLP(rangeOfSearch=10,
            epsilon=0.005)

# Calcula matrices de transformación
sr.calculateTM()

# Desgloza los resultados
sr.ShowTMs()
```
**Salida esperada:**
```

***Option 1: T <- Matrix loMat[0]
Size of the primitive vectors: |a|=47.07982Å, |b|=47.07982Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   6   -9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  630   |
|          FePS3          |  |   9   -3|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  20  -18|  |  | 1.00265 -0.00494|  |   +0.018% // +0.25°   |  728   |
|    Graphene(24.07°)     |  |  18    2|  |  | 0.00494  0.99770|  |   +0.018% // +0.25°   |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:1358	DD:0.002122

***Option 2: T <- Matrix loMat[1]
Size of the primitive vectors: |a|=47.45200Å, |b|=47.45200Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   0    8|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  640   |
|          FePS3          |  |  -8    8|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  -9   22|  |  | 1.00333  0.00127|  |   +0.396% // -0.06°   |  734   |
|    Graphene(24.07°)     |  | -22   13|  |  |-0.00127  1.00459|  |   +0.396% // -0.06°   |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:1374	DD:0.002034

***Option 3: T <- Matrix loMat[2]
Size of the primitive vectors: |a|=72.88749Å, |b|=72.88749Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   9    5|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  1510  |
|          FePS3          |  |  -5   14|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |   9   24|  |  | 0.99988 -0.00003|  |   -0.013% // +0.0°    |  1746  |
|    Graphene(24.07°)     |  | -24   33|  |  | 0.00003  0.99985|  |   -0.013% // +0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:3256	DD:0.000068

***Option 4: T <- Matrix loMat[3]
Size of the primitive vectors: |a|=82.18927Å, |b|=82.18927Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   8    8|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  1920  |
|          FePS3          |  |  -8   16|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |   4   31|  |  | 1.00333  0.00127|  |   +0.396% // -0.06°   |  2202  |
|    Graphene(24.07°)     |  | -31   35|  |  |-0.00127  1.00459|  |   +0.396% // -0.06°   |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:4122	DD:0.002034
Matriz sugerida: loMat[2]

```

## English
```python
#Inicializa el Sistema
sr=System([l1,l2.mRot(24.07)])

# Buscan posibles vectores primitivos en un alcance de busqueda de maximo 20 y error maximo de 0.005
sr.searchLP(rangeOfSearch=10,
            epsilon=0.005)

# Calcula matrices de transformación
sr.calculateTM()

# Desgloza los resultados
sr.ShowTMs()
```
**Expected output:**
```

***Option 1: T <- Matrix loMat[0]
Size of the primitive vectors: |a|=47.07982Å, |b|=47.07982Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   6   -9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  630   |
|          FePS3          |  |   9   -3|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  20  -18|  |  | 1.00265 -0.00494|  |   +0.018% // +0.25°   |  728   |
|    Graphene(24.07°)     |  |  18    2|  |  | 0.00494  0.99770|  |   +0.018% // +0.25°   |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:1358	DD:0.002122

***Option 2: T <- Matrix loMat[1]
Size of the primitive vectors: |a|=47.45200Å, |b|=47.45200Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   0    8|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  640   |
|          FePS3          |  |  -8    8|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  -9   22|  |  | 1.00333  0.00127|  |   +0.396% // -0.06°   |  734   |
|    Graphene(24.07°)     |  | -22   13|  |  |-0.00127  1.00459|  |   +0.396% // -0.06°   |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:1374	DD:0.002034

***Option 3: T <- Matrix loMat[2]
Size of the primitive vectors: |a|=72.88749Å, |b|=72.88749Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   9    5|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  1510  |
|          FePS3          |  |  -5   14|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |   9   24|  |  | 0.99988 -0.00003|  |   -0.013% // +0.0°    |  1746  |
|    Graphene(24.07°)     |  | -24   33|  |  | 0.00003  0.99985|  |   -0.013% // +0.0°    |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:3256	DD:0.000068

***Option 4: T <- Matrix loMat[3]
Size of the primitive vectors: |a|=82.18927Å, |b|=82.18927Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   8    8|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  1920  |
|          FePS3          |  |  -8   16|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |   4   31|  |  | 1.00333  0.00127|  |   +0.396% // -0.06°   |  2202  |
|    Graphene(24.07°)     |  | -31   35|  |  |-0.00127  1.00459|  |   +0.396% // -0.06°   |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:4122	DD:0.002034
Matriz sugerida: loMat[2]

```

---
