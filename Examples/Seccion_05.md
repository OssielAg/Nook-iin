# Sección 5

## Español
##### Tricapa de grafeno rotada
Ahora analizaremos una tricapa de grafeno con 10.43° entre la primera y segunda capa y 26.27 entre la primera y tercera capa utilizando el método ejecuta, el cual ejecuta secuancialmente los métodos searchLP y calculateTM regresando la MT sugerida por el programa.

## English
(Translation goes here)


---
## Español
```python
g1=graphen()
g2=graphen()
g3=graphen()
g1.atms[0][0].color=g1.atms[0][1].color='darkgreen'
g2.atms[0][0].color=g2.atms[0][1].color='red'
g3.atms[0][0].color=g3.atms[0][1].color='blue'
```

## English
```python
g1=graphen()
g2=graphen()
g3=graphen()
g1.atms[0][0].color=g1.atms[0][1].color='darkgreen'
g2.atms[0][0].color=g2.atms[0][1].color='red'
g3.atms[0][0].color=g3.atms[0][1].color='blue'
```

---
## Español
```python
s = System([g1,g2.mRot(10.43),g3.mRot(26.27)])
T = s.ejecuta(15,0.03)
s.leeMT(T)
TLG1,d=s.optimize_system(T,prnt=False)
```
**Salida esperada:**
```
Size of the primitive vectors: |a|=23.27612Å, |b|=23.27612Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   1    9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  182   |
|         Grafeno         |  |  -9   10|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  -1   10|  |  | 0.99987  0.00025|  |    +0.0% // -0.01°    |  182   |
|     Grafeno(10.43°)     |  | -10    9|  |  |-0.00025  1.00013|  |    +0.0% // -0.01°    |        |
|                         |               |                       |                       |        |
|                         |  |  -4   11|  |  | 0.98909  0.00019|  |   -1.081% // -0.01°   |  186   |
|     Grafeno(26.27°)     |  | -11    7|  |  |-0.00019  0.98928|  |   -1.081% // -0.01°   |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:550	DD:0.002730

```

## English
```python
s = System([g1,g2.mRot(10.43),g3.mRot(26.27)])
T = s.ejecuta(15,0.03)
s.leeMT(T)
TLG1,d=s.optimize_system(T,prnt=False)
```
**Expected output:**
```
Size of the primitive vectors: |a|=23.27612Å, |b|=23.27612Å
Angle between vectors: 120.000°
+-------------------------+---------------+-----------------------+-----------------------+--------+
|         Lattice         |       T       |      Deformation      |    Distortion:δ//θ    | #Atoms |
+-------------------------+---------------+-----------------------+-----------------------+--------+
|                         |  |   1    9|  |  | 1.00000  0.00000|  |    +0.0% // +0.0°     |  182   |
|         Grafeno         |  |  -9   10|  |  | 0.00000  1.00000|  |    +0.0% // +0.0°     |        |
|                         |               |                       |                       |        |
|                         |  |  -1   10|  |  | 0.99987  0.00025|  |    +0.0% // -0.01°    |  182   |
|     Grafeno(10.43°)     |  | -10    9|  |  |-0.00025  1.00013|  |    +0.0% // -0.01°    |        |
|                         |               |                       |                       |        |
|                         |  |  -4   11|  |  | 0.98909  0.00019|  |   -1.081% // -0.01°   |  186   |
|     Grafeno(26.27°)     |  | -11    7|  |  |-0.00019  0.98928|  |   -1.081% // -0.01°   |        |
|                         |               |                       |                       |        |
+-------------------------+---------------+-----------------------+-----------------------+--------+
		Total atoms:550	DD:0.002730

```

---
## Español
 Generamos las imagenes de la CP encontrada para el sistema, una supercelda 2x2 de esta (guardando la imagen) y su representación en el espacio reciproco.

## English
(Translation goes here)


---
## Español
```python
TLG1.showPC()
TLG1.SuperRed.showme(x=2,y=2,t=1,iName="TLG(1_43,26_27)")
TLG1.SuperRed.printReciprocalSpace()
```
**Salida esperada:**
```
Dirección de imagen: '/images/TLG(1_43,26_27).png'

```

## English
```python
TLG1.showPC()
TLG1.SuperRed.showme(x=2,y=2,t=1,iName="TLG(1_43,26_27)")
TLG1.SuperRed.printReciprocalSpace()
```
**Expected output:**
```
Dirección de imagen: '/images/TLG(1_43,26_27).png'

```

---
