# Sección 4

## Español
Tras analizar los resultados resaltan 2 de ellos, el primero es el sugerido por el programa al ser el de menor distorsion en la capa del grafeno, el segundo es el que genera la PC de menor tamaño.

##### Resultado sugerido
|$$\text{Lattice}$$|$$\text{T}$$|$$\text{M.Deformation}$$|$$\text{delta//theta}$$|$$\text{\#Atoms}$$|
|-------|-|-------------|------------|--------|
|FePS3|$$\begin{matrix}9&5\\-5&14\end{matrix}$$|$$\begin{matrix}1&0\\0&1\end{matrix}$$|$$\begin{matrix}0.000\%\text{ }//\text{ }0.0^o\\0.000\%\text{ }//\text{ }0.0°\end{matrix}$$|1510|
|Graphene(24.07°)|$$\begin{matrix}-9&24\\-24&33\end{matrix}$$|$$\begin{matrix}0.99988&-0.00003\\0.00003&0.99985\end{matrix}$$|$$\begin{matrix}-0.013\%\text{ }//\text{ }0.0^o\\-0.013\%\text{ }//\text{ }0.0^o\end{matrix}$$|1746|

###### Resultado más pequeño
|$$\text{Lattice}$$|$$\text{T}$$|$$\text{M.Deformation}$$|$$\text{delta//theta}$$|$$\text{\#Atoms}$$|
|-------|-|-------------|------------|--------|
|FePS3|$$\begin{matrix}6&-9\\9&-3\end{matrix}$$|$$\begin{matrix}1&0\\0&1\end{matrix}$$|$$\begin{matrix}0.000\%\text{ }//\text{ }0.0^o\\0.000\%\text{ }//\text{ }0.0°\end{matrix}$$|630|
|Graphene(24.07°)|$$\begin{matrix}20&-18\\18&2\end{matrix}$$|$$\begin{matrix}1.00265&-0.00494\\0.00494&1.00265\end{matrix}$$|$$\begin{matrix}0.018\%\text{ }//\text{ }+0.25^o\\0.018\%\text{ }//\text{ }+0.25^o\end{matrix}$$|728|

Con el primer resultado el número de átomos es igual a $3256$ con una disminución en la longitud de los VPs de la segunda capa del 0.013%, mientras que el segundo, a coste de una reducción del $0.18\%$ y correción en el ángulo de $0.26°$ en sus VPs reduce este número hasta $1374$.

 A continuación crearán sistemas con ambos resultados para ser mostrados comenzando con el resultado sugerido.

## English
(Translation goes here)


---
## Español
```python
sOp,_ = sr.optimize_system(sr.loMat[2],prnt=False)
sr.leeMT(sr.loMat[2])
sOp.SuperRed.showme(t=2)
```
**Salida esperada:**
```
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

```

## English
```python
sOp,_ = sr.optimize_system(sr.loMat[2],prnt=False)
sr.leeMT(sr.loMat[2])
sOp.SuperRed.showme(t=2)
```
**Expected output:**
```
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

```

---
## Español
 Ahora el resultado más pequeño.

## English
(Translation goes here)


---
## Español
```python
sMi,_ = sr.optimize_system(sr.loMat[0],prnt=False)
sr.leeMT(sr.loMat[0])
sMi.SuperRed.showme(t=2)
```
**Salida esperada:**
```
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

```

## English
```python
sMi,_ = sr.optimize_system(sr.loMat[0],prnt=False)
sr.leeMT(sr.loMat[0])
sMi.SuperRed.showme(t=2)
```
**Expected output:**
```
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

```

---
## Español
 Cómo observación se hace uso del método optimize\_system para generar nuevos sistemas con cada MT para no modificar el sistema original.

 A continuación veremos las representaciones de ambos modelos en el espacio Real con la función 'showme', guardando a su vez las imagenes resultantes en archivos png

## English
(Translation goes here)


---
## Español
```python
sOp.SuperRed.showme(t=1,iName="ModeloOptimo")
sMi.SuperRed.showme(t=1,iName="ModeloMinimo")
```
**Salida esperada:**
```
Dirección de imagen: '/images/ModeloOptimo.png'
Dirección de imagen: '/images/ModeloMinimo.png'

```

## English
```python
sOp.SuperRed.showme(t=1,iName="ModeloOptimo")
sMi.SuperRed.showme(t=1,iName="ModeloMinimo")
```
**Expected output:**
```
Dirección de imagen: '/images/ModeloOptimo.png'
Dirección de imagen: '/images/ModeloMinimo.png'

```

---
## Español
 Ahora usando la función 'exportLattice()' guardamos en la carpeta VASP\_Files las CPs calculadas en archivos POSCAR

## English
(Translation goes here)


---
## Español
```python
sOp.SuperRed.exportLattice(name="Sistema_Sugerido")
sMi.SuperRed.exportLattice(name="Sistema_Minimo")
```

## English
```python
sOp.SuperRed.exportLattice(name="Sistema_Sugerido")
sMi.SuperRed.exportLattice(name="Sistema_Minimo")
```

---
## Español
 Continuamos generando las imagenes en elespacio reciproco para ambos resultados.

## English
(Translation goes here)


---
## Español
```python
sOp.SuperRed.printReciprocalSpace(t=3,zoom=True)
sMi.SuperRed.printReciprocalSpace(t=3,zoom=True)
```

## English
```python
sOp.SuperRed.printReciprocalSpace(t=3,zoom=True)
sMi.SuperRed.printReciprocalSpace(t=3,zoom=True)
```

---
## Español
 Finalmente generamos sus patrones de difracción, estos deben ser muy parecidos dado que ambos sistemas aproximan al mismo.
 
 Este es el método más tardado, especialmente en el caso del primer sistema dado que el tamaño de este es mucho mayor al segundo.

## English
(Translation goes here)


---
## Español
```python
sOp.SuperRed.name="Sistema_Sugerido"
sMi.SuperRed.name="Sistema_Minimo"
sOp.diffractionPattern(border=1.2,prnt=True)
sMi.diffractionPattern(border=1.2,prnt=True)
```
**Salida esperada:**
```
Calculando Factor de estructura....26494 PRs calculados
Dirección de imagen: '/images/DP-Sistema_Sugerido.png'
Calculando Factor de estructura....11040 PRs calculados
Dirección de imagen: '/images/DP-Sistema_Minimo.png'

```

## English
```python
sOp.SuperRed.name="Sistema_Sugerido"
sMi.SuperRed.name="Sistema_Minimo"
sOp.diffractionPattern(border=1.2,prnt=True)
sMi.diffractionPattern(border=1.2,prnt=True)
```
**Expected output:**
```
Calculando Factor de estructura....26494 PRs calculados
Dirección de imagen: '/images/DP-Sistema_Sugerido.png'
Calculando Factor de estructura....11040 PRs calculados
Dirección de imagen: '/images/DP-Sistema_Minimo.png'

```

---
