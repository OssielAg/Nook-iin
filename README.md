# **Nook'iin**
[![DOI](https://zenodo.org/badge/883646265.svg)](https://doi.org/10.5281/zenodo.14257396)

## English | [Español](#español)
**Primitive cell & commensurate supercell generation for multilayer 2D heterostructures**

---

### 1. Description  
**Nook’iin** is a Python-based software designed to construct primitive and commensurate cells for multilayer 2D heterostructures, with support for arbitrary relative orientations and Bravais lattices.

#### **Main Features**  
- **Primitive Cell Calculation:** Identifies the smallest primitive cells for multilayer two-dimensional structures.  
- **Reciprocal Space:** Generates reciprocal space representations and theoretical diffraction patterns for the analyzed systems.  
- **Compatibility and Flexibility:** Designed to work with complex geometrical configurations in multilayer systems with different Bravais lattices, lattice constants, orientations, and number of layers. Results are compatible with crystallography software that supports POSCAR format files.  


#### Key Features  
- ✔️ Supports *n*-layer twisted or non-twisted structures  
- ✔️ Geometrical and symmetry-based algorithms with strain control  
- ✔️ Reciprocal space representation and primitive cell reduction  
- ✔️ POSCAR export, pattern diffraction module, and reproducibility options

---

### 2. Installation  
To get started with **Nook'inn**, follow these instructions:

#### Importing the software in Python

To use **Nook'inn** in a Python script, import all components from the `Nook-iin/src/System.py` file.

If you are creating your Python script in the root directory of the *Nook'inn* project, you should use the following line:

```python
from src.System import *
```
This will load all essential modules needed to construct and analyze 2D multilayer systems.

#### Detailed Usage Guides
For a complete technical overview and usage instructions, refer to the following files included in this repository:
- [Nook_iin_Overview.pdf](/Nook_iin_Overview.pdf) → Provides detailed technical documentation and methodology.
- [Interface_Guide.md](/Interface_Guide/Interface_Guide.md) → Offers a step-by-step explanation of the console-guided interface.

These documents provide in-depth guidance on software functionalities and best practices.

---

### 3. Examples  
Explore the examples/ folder for interactive Jupyter Notebooks illustrating Nook’iin’s capabilities:
- [Full Workflow Example](/Examples/English/01_Complete_Example.ipynb): Step-by-step guide through a typical Nook’iin workflow — from system definition to reciprocal space visualization and diffraction pattern generation. Ideal as an introduction.
- [Twisted Bilayer Graphene](/Examples/English/02_Example_tBLG.ipynb):Generation of primitive cells for bilayer graphene with incommensurate twist angles: 2.54°, 5.63°, 14.21°, 16.18°, and 23.85°.
- [Multilayer Heterostructures](/Examples/English/03_Example_Heterostructure.ipynb): Construction of primitive cells for theoretical multilayer systems (e.g., β-GeSe, CdS, hBN, WS₂, WSe₂, black phosphorene), with strain constraints and diffraction pattern analysis.
- [Angular Interval Search](/Examples/English/04_Example_Results_AngleInterval.ipynb): Search for commensurate primitive cells across a range of twist angles in a bilayer system, with controlled strain. Useful for studying moiré physics, band modulation, and angle-dependent properties.
- [Difraction Map](/Examples/English/05_Example_Diffraction_Map.ipynb): This example demonstrates the capability of **Nook’iin** to generate diffraction maps for multilayer systems. Unlike traditional diffraction patterns that only indicate the location of Bragg peaks, diffraction maps represent the continuous intensity distribution across reciprocal space.

---

### 4. Requirements  
- Python ≥3.6  
- Required: `numpy`, `matplotlib`

---
### 5. Citing Nook’iin

If you use **Nook’iin** in your research, please cite it appropriately to support ongoing development and ensure reproducibility.  

#### 📌 Recommended citation:
```bibtex
@software{Nookiin2025,
  author       = {Aguilar-Spíndola Ossiel and Sánchez‑Ochoa Francisco},
  title        = {{Nook’iin}: Software for the construction and analysis of Van der Waals heterostructures and homostructures in 2D multilayer systems},
  version      = {v1.9.0},
  date         = {2025-07-14},
  doi          = {10.5281/zenodo.14257396},
  url          = {https://github.com/OssielAg/Nook-iin},
}
```
Suggested sentence for citation in publications:
“The commensurate primitive cell was generated using the Nook’iin code.”

For further citation metadata, see the [CITATION file](/CITATION.cff).

---

### 6. Contributing  
We welcome your contributions!  
1. Open an issue or discussion.  
2. Fork the repository and create a feature branch.  
3. Submit a pull request with clear explanations.

---

### 7. License  
This software is distributed under the **GNU General Public License (GNU GPL)**, allowing use, modification, and distribution under the same licensing terms. For more information, see the `LICENSE` file in this repository.  

---

### 8. Publications

This section lists the scientific articles and conference papers directly related to the development, implementation, and capabilities of **Nook’iin**.

- [1] Aguilar-Spindola O., Sánchez‑Ochoa F. *Nook’iin: Software para la construcción de heteroestructuras 3D multicapa*, *(in preparation)*.
- [[2](https://doi.org/10.1039/D5CP00337G)] Aguilar‑Spíndola O., Rubio‑Ponce A., López‑Urías F., Sánchez‑Ochoa F. *Electronic and optical properties in helical trilayer graphene under compression*, **Phys. Chem. Chem. Phys. 27**, 11541–11550 (2025). DOI: 10.1039/D5CP00337G

## 9. Publications Utilizing Nook’iin

Below are peer-reviewed works, theses, or preprints from independent research groups that use **Nook’iin** as part of their methodology. If you used Nook’iin in your work, feel free to submit a pull request or contact the authors to have your work listed here.

- [[1](https://doi.org/10.1039/D5CP00337G)] Aguilar‑Spíndola O., Rubio‑Ponce A., López‑Urías F., Sánchez‑Ochoa F. *Electronic and optical properties in helical trilayer graphene under compression*, **Phys. Chem. Chem. Phys. 27**, 11541–11550 (2025). DOI: 10.1039/D5CP00337G
---

### Contact  
**Nook'iin** was created by **Ossiel Aguilar-Spíndola**.  
- **Contact email:** OssielAE@ciencias.unam.mx  
- **ORCID:** [0009-0002-8229-8543](https://orcid.org/0009-0002-8229-8543)  
---

### 📚 Acknowledgments  
- Developed under supervision of Francisco Sánchez  
- Inspired by tools like BandUP, CellMatch, and SuperCell  

---
---

## Español
---

### 1. Descripción  
**Nook’iin** es un software en Python para la construcción de celdas primitivas y superceldas conmensurables en heteroestructuras 2D multicapa, permitiendo orientaciones relativas y tipos de red de Bravais arbitrarios.

#### Características principales  
- ✔️ Compatible con sistemas multicapa con o sin torsión  
- ✔️ Algoritmos geométricos con control de deformación  
- ✔️ Representación en espacio recíproco y reducción estructural  
- ✔️ Exportación a POSCAR, cálculo de patrones de difracción y seguimiento reproducible

---

### 2. Instalación  
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

---

### 3. Ejemplos 
Consulta la carpeta examples/ para encontrar notebooks interactivos que muestran las capacidades de Nook’iin:
- [Ejemplo Completo de Uso](/Examples/Español/01_Ejemplo_Completo.ipynb): Guía paso a paso que cubre el flujo completo de trabajo: desde la definición del sistema hasta la visualización del espacio recíproco y el patrón de difracción. Ideal como introducción.
- [Grafeno Bicapas Retorcidas](/Examples/Español/02_Ejemplo_tBLG.ipynb): Cálculo de celdas primitivas para grafeno bicapa con ángulos de rotación incomensurables: 2.54°, 5.63°, 14.21°, 16.18° y 23.85°.
- [Heteroestructuras Multicapa](/Examples/Español/03_Ejemplo_Heteroestructura.ipynb): Construcción de celdas primitivas para sistemas teóricos multicapa (ej. β-GeSe, CdS, hBN, WS₂, WSe₂, fosforeno), respetando límites de deformación y mostrando el patrón de difracción.
- [Búsqueda en Intervalo Angular](/Examples/Español/04_Ejemplo_Resultados_IntervaloAngular.ipynb): Exploración de celdas primitivas compatibles para un sistema bicapa dentro de un intervalo de ángulos, manteniendo la deformación bajo un umbral. Útil en el estudio de moiré, diseño de bandas y propiedades angulares.
- [Mapas de difracción](/Examples/Español/05_Ejemplo_Mapa_de_difracción.ipynb): Este ejemplo muestra la capacidad de **Nook’iin** para generar mapas de difracción para sistemas multicapa. A diferencia de los patrones de difracción tradicionales que solo marcan la posición de los picos de Bragg, los mapas de difracción representan la distribución continua de intensidad en el espacio recíproco.

---

### 4. Requisitos  
- Python ≥3.6  
- Requiere: `numpy`, `matplotlib`

---
### 5. Citando a Nook'iin

Si utilizas **Nook'iin** en tu trabajo de investigación, por favor cítalo adecuadamente para apoyar su desarrollo continuo y garantizar la reproducibilidad.  

#### 📌 Citación recomendada:
```bibtex
@software{Nookiin2025,
  author       = {Aguilar-Spíndola Ossiel and Sánchez‑Ochoa Francisco},
  title        = {{Nook’iin}: Software for the construction and analysis of Van der Waals heterostructures and homostructures in 2D multilayer systems},
  version      = {v1.9.0},
  date         = {2025-07-14},
  doi          = {10.5281/zenodo.14257396},
  url          = {https://github.com/OssielAg/Nook-iin},
}
```
Frase sugerida para incluir en publicaciones:
“La celda primitiva conmensurable fue generada utilizando el código Nook’iin.”

Para más información sobre la citación, consulta el archivo [CITATION](/CITATION.cff).

---

### 6. Contribución  
Tu participación es bienvenida:  
1. Abre un _issue_ o discusión.  
2. Crea una rama en tu fork.  
3. Envía un _pull request_ con una descripción clara.

---

### 7. Licencia  
Este software es distribuido bajo la **Licencia Pública General GNU (GNU GPL)**, lo que permite su uso, modificación y distribución bajo las mismas condiciones de licencia. Para más información, consulta el archivo [`LICENSE`](LICENSE) en este repositorio.

---

### 8. Publicaciones

Esta sección enumera los artículos científicos y contribuciones que presentan el desarrollo, las funcionalidades y las aplicaciones principales de **Nook’iin**.

- [1] Aguilar-Spindola O., Sánchez‑Ochoa F. *Nook’iin: Software para la construcción de heteroestructuras 3D multicapa*, *(en preparación)*.
- [[2](https://doi.org/10.1039/D5CP00337G)] Aguilar‑Spíndola O., Rubio‑Ponce A., López‑Urías F., Sánchez‑Ochoa F. *Electronic and optical properties in helical trilayer graphene under compression*, **Phys. Chem. Chem. Phys. 27**, 11541–11550 (2025). DOI: 10.1039/D5CP00337G

### 9. Publicaciones que utilizan Nook’iin

A continuación se enlistan trabajos de investigación, tesis o preprints revisados por pares que han empleado **Nook’iin** como parte de su metodología. Si usaste Nook’iin en tu trabajo, puedes enviar un pull request o contactar a los autores para agregar tu publicación a esta sección.

- [[1](https://doi.org/10.1039/D5CP00337G)] Aguilar‑Spíndola O., Rubio‑Ponce A., López‑Urías F., Sánchez‑Ochoa F. *Electronic and optical properties in helical trilayer graphene under compression*, **Phys. Chem. Chem. Phys. 27**, 11541–11550 (2025). DOI: 10.1039/D5CP00337G
---

### Contacto  
**Nook'iin** fue creado por **Ossiel Aguilar-Spíndola**.  
- **Correo de contacto:** OssielAE@ciencias.unam.mx  
- **ORCID:** [0009-0002-8229-8543](https://orcid.org/0009-0002-8229-8543)  

---

### 📚 Créditos  
- Desarrollado bajo la supervisión de Francisco Sánchez  
- Inspirado por herramientas como BandUP, CellMatch y SuperCell  
