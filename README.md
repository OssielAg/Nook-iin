# **Nookiin**
[![DOI](https://zenodo.org/badge/883646265.svg)](https://doi.org/10.5281/zenodo.14257396)

## English | [Español](#español)
**Primitive cell & commensurate supercell generation for multilayer 2D heterostructures**

---

### 1. Description  
**Nookiin** is a Python-based software designed to construct primitive and commensurate cells for multilayer 2D heterostructures, with support for arbitrary relative orientations and Bravais lattices.

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

To get started with **Nookiin**, follow these instructions:

---

#### Recommended Installation (Modern Approach)

**Nookiin** can be installed directly with pip from the root folder:
```bash
pip install .
```

However, the recommended way to use **Nookiin** is by installing it with `pip` inside a virtual environment:

```bash
python -m venv nookiin_env          # create a virtual environment (optional but recommended)
source nookiin_env/bin/activate     # activate the environment (Linux/macOS)
# For Windows PowerShell: .\nookiin_env\Scripts\Activate.ps1
pip install .
```

This ensures that all dependencies (`numpy`, `matplotlib[gui]`) are installed correctly and isolates Nookiin from other Python packages.

After installation, you can import Nookiin in your scripts:

```python
import nookiin
```

All modules and classes will be available as part of the package.

For more direct usage, it is recommended to import system.py directly:
```python
from nookiin.system import *
```
Once Nookiin is properly installed, you can verify the installation by running the Python file demo.py.
This script will search for a primitive cell of a rotated graphene bilayer and display its representations in reciprocal space (image tabs must be closed to continue execution):
```bash
python3 demo.py
``` 


> ⚠️ Note: **Nookiin automatically configures the matplotlib backend**.  
> On systems with a graphical interface, an interactive backend (`TkAgg`) is used to display plots.  
> On headless servers or systems without a GUI, it falls back to a non-interactive backend (`Agg`) so that figures can still be saved without raising errors.

---

#### Optional Manual Import (Advanced Users)

If you prefer **not to use `pip` or virtual environments** and want to load Nookiin directly from the repository, you can do so manually.  

Set the environment variable `NOOKIIN_MANUAL_PATH` **before running Python** from the root of Nookiin:

- **Linux/macOS:**

```bash
export NOOKIIN_MANUAL_PATH=1
```

- **Windows (cmd):**

```cmd
set NOOKIIN_MANUAL_PATH=1
```

- **Windows (PowerShell):**

```powershell
$env:NOOKIIN_MANUAL_PATH=1
```

Then, in your script, import all modules from `System.py`:

```python
from src.nookiin.system import *
```

> ⚠️ **Warning:** This method is **not recommended** for long-term usage, as it may cause conflicts with installed packages or future versions of Nookiin. Prefer the `pip` installation whenever possible.

---
#### Nookiin Usage Modes

Nookiin can be used in two main ways:

- **Interactive command-line interface:**  
  After installing Nookiin or from the root of the repository, run:
  ```bash
  python -m nookiin
  ```
  This launches the guided step-by-step interface for using Nookiin.
  This option is convenient for users who prefer an interactive workflow, but is limited to the interface guide.

- **Programmatic usage from Python scripts or notebooks:**  
  Import the core module as follows:
  ```python
  from nookiin.system import *
  ```
  This allows access to all classes and functions of Nookiin, suitable for automated workflows, batch processing, or integration into Jupyter notebooks.

---

#### Detailed Usage Guides

For a complete technical overview and usage instructions, refer to:

- [Nook_iin_Overview.pdf](/Nook_iin_Overview.pdf) → Provides detailed technical documentation and methodology.  
- [Interface_Guide.md](/Interface_Guide/Interface_Guide.md) → Step-by-step explanation of the console-guided interface.

These documents provide in-depth guidance on software functionalities and best practices.

---

### 3. Examples  
Explore the examples/ folder for interactive Jupyter Notebooks illustrating Nookiin’s capabilities:
- [Full Workflow Example](/Examples/English/01_Complete_Example.ipynb): Step-by-step guide through a typical Nookiin workflow — from system definition to reciprocal space visualization and diffraction pattern generation. Ideal as an introduction.
- [Twisted Bilayer Graphene](/Examples/English/02_Example_tBLG.ipynb):Generation of primitive cells for bilayer graphene with incommensurate twist angles: 2.54°, 5.63°, 14.21°, 16.18°, and 23.85°.
- [Multilayer Heterostructures](/Examples/English/03_Example_Heterostructure.ipynb): Construction of primitive cells for theoretical multilayer systems (e.g., β-GeSe, CdS, hBN, WS₂, WSe₂, black phosphorene), with strain constraints and diffraction pattern analysis.
- [Angular Interval Search](/Examples/English/04_Example_Results_AngleInterval.ipynb): Search for commensurate primitive cells across a range of twist angles in a bilayer system, with controlled strain. Useful for studying moiré physics, band modulation, and angle-dependent properties.
- [Difraction Map](/Examples/English/05_Example_Diffraction_Map.ipynb): This example demonstrates the capability of **Nookiin** to generate diffraction maps for multilayer systems. Unlike traditional diffraction patterns that only indicate the location of Bragg peaks, diffraction maps represent the continuous intensity distribution across reciprocal space.

---

### 4. Requirements  
- Python ≥3.6  
- Required: `numpy`, `matplotlib`

---
### 5. Citing Nookiin

If you use **Nookiin** in your research, please cite it appropriately to support ongoing development and ensure reproducibility.  

#### 📌 Recommended citation:
```bibtex
@software{Nookiin2025,
  author       = {Aguilar-Spíndola Ossiel and Sánchez‑Ochoa Francisco},
  title        = {{Nookiin}: Software for the construction and analysis of Van der Waals heterostructures and homostructures in 2D multilayer systems},
  version      = {v1.9.0},
  date         = {2025-07-14},
  doi          = {10.5281/zenodo.14257396},
  url          = {https://github.com/OssielAg/Nook-iin},
}
```
Suggested sentence for citation in publications:
“The commensurate primitive cell was generated using the Nookiin code.”

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

This section lists the scientific articles and conference papers directly related to the development, implementation, and capabilities of **Nookiin**.

- [1] Aguilar-Spindola O., Sánchez‑Ochoa F. *Nookiin: Software para la construcción de heteroestructuras 3D multicapa*, *(in preparation)*.
- [[2](https://doi.org/10.1039/D5CP00337G)] Aguilar‑Spíndola O., Rubio‑Ponce A., López‑Urías F., Sánchez‑Ochoa F. *Electronic and optical properties in helical trilayer graphene under compression*, **Phys. Chem. Chem. Phys. 27**, 11541–11550 (2025). DOI: 10.1039/D5CP00337G

## 9. Publications Utilizing Nookiin

Below are peer-reviewed works, theses, or preprints from independent research groups that use **Nookiin** as part of their methodology. If you used Nookiin in your work, feel free to submit a pull request or contact the authors to have your work listed here.

- [[1](https://doi.org/10.1039/D5CP00337G)] Aguilar‑Spíndola O., Rubio‑Ponce A., López‑Urías F., Sánchez‑Ochoa F. *Electronic and optical properties in helical trilayer graphene under compression*, **Phys. Chem. Chem. Phys. 27**, 11541–11550 (2025). DOI: 10.1039/D5CP00337G
---

### Contact  
**Nookiin** was created by **Ossiel Aguilar-Spíndola**.  
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
**Nookiin** es un software en Python para la construcción de celdas primitivas y superceldas conmensurables en heteroestructuras 2D multicapa, permitiendo orientaciones relativas y tipos de red de Bravais arbitrarios.

#### Características principales  
- ✔️ Compatible con sistemas multicapa con o sin torsión  
- ✔️ Algoritmos geométricos con control de deformación  
- ✔️ Representación en espacio recíproco y reducción estructural  
- ✔️ Exportación a POSCAR, cálculo de patrones de difracción y seguimiento reproducible

---

### 2. Instalación

Para comenzar con **Nookiin**, sigue estas instrucciones:

---

#### Instalación Recomendada (Enfoque Moderno)
**Nookiin** puede instalarse directamente con pip desde la carpeta raíz:
```bash
pip install .
```

Sin embargo la forma recomendada de usar **Nookiin** es instalándolo con `pip` en un entorno virtual:

```bash
python -m venv nookiin_env          # crear un entorno virtual (opcional pero recomendado)
source nookiin_env/bin/activate     # activar el entorno (Linux/macOS)
# Para Windows PowerShell: .\nookiin_env\Scripts\Activate.ps1
pip install .
```

Esto asegura que todas las dependencias (`numpy`, `matplotlib[gui]`) se instalen correctamente y aísla Nookiin de otros paquetes de Python.

Después de la instalación, puedes importar Nookiin en tus scripts dentro del entorno virtual:

```python
import nookiin
```

Todos los módulos y clases estarán disponibles como parte del paquete.

Para un uso más directo se recomienda hacer una importación directa de `system.py`:

```python
from nookiin.system import *
```

Una vez instalado correctamente nookiin puede probar si se hizo correctamente ejecutando el archivo de python `demo.py`, este efectuará la búsqueda de una celda primitiva para una bicapa de grafeno rotada mostrando sus representaciones en el espacio reciproco (deben cerarce las pestañas de imagen para continuar la ejecución):
```bash
python3 demo.py
``` 

> ⚠️ Nota: **Nookiin configura automáticamente el backend de matplotlib**.  
> En sistemas con interfaz gráfica, se utiliza un backend interactivo (`TkAgg`) para mostrar gráficos.  
> En servidores sin GUI o sistemas sin interfaz gráfica, se utiliza un backend no interactivo (`Agg`) para que las figuras aún puedan guardarse sin generar errores.

---

#### Importación Manual Opcional (Usuarios Avanzados)

Si prefieres **no usar `pip` o entornos virtuales** y quieres cargar Nookiin directamente desde el repositorio, puedes hacerlo manualmente.  

Define la variable de entorno `NOOKIIN_MANUAL_PATH` **antes de ejecutar Python** desde la raiz de Nookiin:

- **Linux/macOS:**

```bash
export NOOKIIN_MANUAL_PATH=1
```

- **Windows (cmd):**

```cmd
set NOOKIIN_MANUAL_PATH=1
```

- **Windows (PowerShell):**

```powershell
$env:NOOKIIN_MANUAL_PATH=1
```

Luego, en tu script, importa todos los módulos directamente desde `system.py`:

```python
from src.nookiin.system import *
```


> ⚠️ **Advertencia:** Este método **no se recomienda** para uso a largo plazo, ya que puede causar conflictos con paquetes instalados o futuras versiones de Nookiin. Siempre que sea posible, utiliza la instalación con `pip`.

---

#### Modos de uso de Nookiin

Nookiin puede utilizarse de dos maneras principales:

- **Interfaz interactiva en línea de comandos:**  
  Después de instalar Nookiin o desde la raíz del repositorio, ejecute:
  ```bash
  python -m nookiin
  ```
  Esto inicia la interfaz guiada paso a paso para usar Nookiin.  
  Esta opción es conveniente para usuarios que prefieren un flujo de trabajo interactivo, pero está limitado a la guia de la interfaz.

- **Uso programático desde scripts o notebooks de Python:**  
  Importe el módulo principal de la siguiente manera:
  ```python
  from nookiin.system import *
  ```
  Esto permite acceder a todas las clases y funciones de Nookiin, adecuado para flujos de trabajo automatizados, procesamiento por lotes o integración en cuadernos Jupyter.


#### Guías de Uso Detalladas

Para una descripción técnica completa e instrucciones de uso, consulta:

- [Nook_iin_Overview.pdf](/Nook_iin_Overview.pdf) → Proporciona documentación técnica detallada y metodología.  
- [Guia_de_interfaz.md](/Interface_Guide/Guia_de_interfaz.md) → Explicación paso a paso de la interfaz guiada por consola.

Estos documentos ofrecen orientación detallada sobre las funcionalidades del software y las mejores prácticas.


---

### 3. Ejemplos 
Consulta la carpeta examples/ para encontrar notebooks interactivos que muestran las capacidades de Nookiin:
- [Ejemplo Completo de Uso](/Examples/Español/01_Ejemplo_Completo.ipynb): Guía paso a paso que cubre el flujo completo de trabajo: desde la definición del sistema hasta la visualización del espacio recíproco y el patrón de difracción. Ideal como introducción.
- [Grafeno Bicapas Retorcidas](/Examples/Español/02_Ejemplo_tBLG.ipynb): Cálculo de celdas primitivas para grafeno bicapa con ángulos de rotación incomensurables: 2.54°, 5.63°, 14.21°, 16.18° y 23.85°.
- [Heteroestructuras Multicapa](/Examples/Español/03_Ejemplo_Heteroestructura.ipynb): Construcción de celdas primitivas para sistemas teóricos multicapa (ej. β-GeSe, CdS, hBN, WS₂, WSe₂, fosforeno), respetando límites de deformación y mostrando el patrón de difracción.
- [Búsqueda en Intervalo Angular](/Examples/Español/04_Ejemplo_Resultados_IntervaloAngular.ipynb): Exploración de celdas primitivas compatibles para un sistema bicapa dentro de un intervalo de ángulos, manteniendo la deformación bajo un umbral. Útil en el estudio de moiré, diseño de bandas y propiedades angulares.
- [Mapas de difracción](/Examples/Español/05_Ejemplo_Mapa_de_difracción.ipynb): Este ejemplo muestra la capacidad de **Nookiin** para generar mapas de difracción para sistemas multicapa. A diferencia de los patrones de difracción tradicionales que solo marcan la posición de los picos de Bragg, los mapas de difracción representan la distribución continua de intensidad en el espacio recíproco.

---

### 4. Requisitos  
- Python ≥3.8  
- Requiere: `numpy`, `matplotlib`

---
### 5. Citando a Nookiin

Si utilizas **Nookiin** en tu trabajo de investigación, por favor cítalo adecuadamente para apoyar su desarrollo continuo y garantizar la reproducibilidad.  

#### 📌 Citación recomendada:
```bibtex
@software{Nookiin2025,
  author       = {Aguilar-Spíndola Ossiel and Sánchez‑Ochoa Francisco},
  title        = {{Nookiin}: Software for the construction and analysis of Van der Waals heterostructures and homostructures in 2D multilayer systems},
  version      = {v2.0.0},
  date         = {2025-07-14},
  doi          = {10.5281/zenodo.14257396},
  url          = {https://github.com/OssielAg/Nook-iin},
}
```
Frase sugerida para incluir en publicaciones:
“La celda primitiva conmensurable fue generada utilizando el código Nookiin.”

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

Esta sección enumera los artículos científicos y contribuciones que presentan el desarrollo, las funcionalidades y las aplicaciones principales de **Nookiin**.

- [1] Aguilar-Spindola O., Sánchez‑Ochoa F. *Nookiin: Software para la construcción de heteroestructuras 3D multicapa*, *(en preparación)*.
- [[2](https://doi.org/10.1039/D5CP00337G)] Aguilar‑Spíndola O., Rubio‑Ponce A., López‑Urías F., Sánchez‑Ochoa F. *Electronic and optical properties in helical trilayer graphene under compression*, **Phys. Chem. Chem. Phys. 27**, 11541–11550 (2025). DOI: 10.1039/D5CP00337G

### 9. Publicaciones que utilizan Nookiin

A continuación se enlistan trabajos de investigación, tesis o preprints revisados por pares que han empleado **Nookiin** como parte de su metodología. Si usaste Nookiin en tu trabajo, puedes enviar un pull request o contactar a los autores para agregar tu publicación a esta sección.

- [[1](https://doi.org/10.1039/D5CP00337G)] Aguilar‑Spíndola O., Rubio‑Ponce A., López‑Urías F., Sánchez‑Ochoa F. *Electronic and optical properties in helical trilayer graphene under compression*, **Phys. Chem. Chem. Phys. 27**, 11541–11550 (2025). DOI: 10.1039/D5CP00337G
---

### Contacto  
**Nookiin** fue creado por **Ossiel Aguilar-Spíndola**.  
- **Correo de contacto:** OssielAE@ciencias.unam.mx  
- **ORCID:** [0009-0002-8229-8543](https://orcid.org/0009-0002-8229-8543)  

---

### 📚 Créditos  
- Desarrollado bajo la supervisión de Francisco Sánchez  
- Inspirado por herramientas como BandUP, CellMatch y SuperCell  
