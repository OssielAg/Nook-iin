# **Nook'iin**  

## Español | [English](#english)  

**Nook'iin** es un software libre desarrollado como parte del trabajo de titulación para la Licenciatura en Ciencias de la Computación en la Facultad de Ciencias de la UNAM. Su objetivo es facilitar el análisis y la construcción teórica de heteroestructuras bidimensionales complejas mediante el uso de herramientas geométricas, con un enfoque particular en sistemas como las heteroestructuras de van der Waals.  

### **Funcionalidades principales**  
- **Cálculo de celdas primitivas:** Identifica las celdas primitivas más pequeñas para estructuras bidimensionales multicapa.  
- **Espacio recíproco:** Genera representaciones en el espacio recíproco y patrones de difracción teóricos para los sistemas analizados.  
- **Compatibilidad y flexibilidad:** Diseñado para trabajar con configuraciones geométricas complejas en sistemas multicapa con distintas redes de Bravais, constantes de red, orientación y número de capas. Resultados compatibles con programas de cristalografía capaces de interpretar archivos en formato POSCAR.

### Primeros pasos

Para comenzar a utilizar **Nook'inn**, sigue estas instrucciones:

#### Importar el software en Python
Para utilizar **Nook'inn** en un script de Python, importa todos los componentes desde el archivo `Nook-iin/src/System.py`.
Si estás creando el script de Python en la raíz del proyecto *Nook'inn*, debes escribir la siguiente línea:

```python
from src.System import *
```
Esto cargará todos los módulos esenciales para la construcción y análisis de sistemas multicapa 2D.

#### Guías de uso detalladas.
Para obtener una explicación más completa sobre la metodología y el funcionamiento del software, consulta los siguientes documentos incluidos en este repositorio:
- [Nook_iin_Overview.pdf](/Nook_iin_Overview.pdf) → Contiene documentación técnica detallada y metodología.
- [Guia_de_interfaz.md](/Interface_Guide/Guia_de_interfaz.md) → Explica paso a paso el uso de la interfaz guiada por consola.

Estos documentos proporcionan orientación detallada sobre las funcionalidades del software y mejores prácticas de uso.

### **Licencia**  
Este software es distribuido bajo la **Licencia Pública General GNU (GNU GPL)**, lo que permite su uso, modificación y distribución bajo las mismas condiciones de licencia. Para más información, consulta el archivo [`LICENSE`](LICENSE) en este repositorio.  

### **Autoría**  
**Nook'iin** fue creado por **Ossiel Aguilar-Spíndola** como parte de su tesis de licenciatura.  
- **Correo de contacto:** OssielAE@ciencias.unam.mx  
- **ORCID:** [0009-0002-8229-8543](https://orcid.org/0009-0002-8229-8543)  

---

## English  

**Nook'iin** is a free software developed as part of the undergraduate thesis for the **Bachelor's Degree in Computer Science** at the **Faculty of Sciences, UNAM**. Its goal is to facilitate the analysis and theoretical construction of complex two-dimensional heterostructures using **geometrical tools**, with a particular focus on van der Waals heterostructures.  

### **Main Features**  
- **Primitive Cell Calculation:** Identifies the smallest primitive cells for multilayer two-dimensional structures.  
- **Reciprocal Space:** Generates reciprocal space representations and theoretical diffraction patterns for the analyzed systems.  
- **Compatibility and Flexibility:** Designed to work with complex geometrical configurations in multilayer systems with different Bravais lattices, lattice constants, orientations, and number of layers. Results are compatible with crystallography software that supports POSCAR format files.  

### **Getting Started**

To get started with **Nook'inn**, follow these instructions:

### Importing the software in Python

To use **Nook'inn** in a Python script, import all components from the `Nook-iin/src/System.py` file.

If you are creating your Python script in the root directory of the *Nook'inn* project, you should use the following line:

```python
from src.System import *
```
This will load all essential modules needed to construct and analyze 2D multilayer systems.

### Detailed Usage Guides
For a complete technical overview and usage instructions, refer to the following files included in this repository:
- [Nook_iin_Overview.pdf](/Nook_iin_Overview.pdf) → Provides detailed technical documentation and methodology.
- [Interface_Guide.md](/Interface_Guide/Interface_Guide.md) → Offers a step-by-step explanation of the console-guided interface.

These documents provide in-depth guidance on software functionalities and best practices.

### **License**  
This software is distributed under the **GNU General Public License (GNU GPL)**, allowing use, modification, and distribution under the same licensing terms. For more information, see the `LICENSE` file in this repository.  

### **Authorship**  
**Nook'iin** was created by **Ossiel Aguilar-Spíndola** as part of his undergraduate thesis.  
- **Contact email:** OssielAE@ciencias.unam.mx  
- **ORCID:** [0009-0002-8229-8543](https://orcid.org/0009-0002-8229-8543)  
