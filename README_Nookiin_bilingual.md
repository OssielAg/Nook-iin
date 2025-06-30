
# 🧩 Nook’iin  
**Primitive cell & commensurate supercell generation for multilayer 2D heterostructures**

---

## 📘 Contents  
1. [Description](#description)  
2. [Installation](#installation)  
3. [Usage](#usage)  
4. [Examples](#examples)  
5. [Requirements](#requirements)  
6. [Contributing](#contributing)  
7. [License](#license)  
8. [Contact](#contact)

---

## 1. Description  
**Nook’iin** is a Python-based software designed to construct primitive and commensurate cells for multilayer 2D heterostructures, with support for arbitrary relative orientations and Bravais lattices.

### Key Features  
- ✔️ Supports *n*-layer twisted or non-twisted structures  
- ✔️ Geometrical and symmetry-based algorithms with strain control  
- ✔️ Reciprocal space representation and primitive cell reduction  
- ✔️ POSCAR export, pattern diffraction module, and reproducibility options

---

## 2. Installation  
Clone the repository and install the required packages:
```bash
git clone https://github.com/OssielAg/Nook-iin.git
cd Nook-iin
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or install directly from PyPI (if available):
```bash
pip install nookiin
```

---

## 3. Usage  
### CLI mode (interactive interface)
```bash
python Interface.py
```

### Programmatic usage (example)
```python
from src.System import System

sys = System(layers=[...])
sys.find_commensurate_cell(max_n=20, tol=1e-2)
sys.export_poscar('Supercell.vasp')
```

---

## 4. Examples  
Some use cases:  
- Twisted bilayer graphene (~3.15°) with reduced supercell size  
- Quasicrystalline tBLG approximation at 30°  
- Moiré pattern modulation by strain  
Explore the `examples/` folder for ready-to-run demos and Jupyter notebooks.

---

## 5. Requirements  
- Python ≥3.6  
- Required: `numpy`, `scipy`, `matplotlib`  
- Optional (recommended): `spglib`, `ase`, `pymatgen`

---

## 6. Contributing  
We welcome your contributions!  
1. Open an issue or discussion.  
2. Fork the repository and create a feature branch.  
3. Submit a pull request with clear explanations.

---

## 7. License  
This project is licensed under the MIT License. See `LICENSE.md` for details.

---

## 8. Contact  
**Main developer**: Ossiel Aguilar  
📧 Email: [your_email@example.com](mailto:your_email@example.com)

---

## 📚 Acknowledgments  
- Developed under supervision of Francisco Sánchez  
- Inspired by tools like BandUP, CellMatch, and SuperCell  

---

# 🧩 Nook’iin  
**Generación de celdas primitivas y superceldas conmensurables para heteroestructuras 2D multicapa**

---

## 📘 Contenido  
1. [Descripción](#descripción)  
2. [Instalación](#instalación)  
3. [Uso](#uso)  
4. [Ejemplos](#ejemplos)  
5. [Requisitos](#requisitos)  
6. [Contribución](#contribución)  
7. [Licencia](#licencia)  
8. [Contacto](#contacto)

---

## 1. Descripción  
**Nook’iin** es un software en Python para la construcción de celdas primitivas y superceldas conmensurables en heteroestructuras 2D multicapa, permitiendo orientaciones relativas y tipos de red de Bravais arbitrarios.

### Características principales  
- ✔️ Compatible con sistemas multicapa con o sin torsión  
- ✔️ Algoritmos geométricos con control de deformación  
- ✔️ Representación en espacio recíproco y reducción estructural  
- ✔️ Exportación a POSCAR, cálculo de patrones de difracción y seguimiento reproducible

---

## 2. Instalación  
Clona el repositorio e instala los paquetes requeridos:
```bash
git clone https://github.com/OssielAg/Nook-iin.git
cd Nook-iin
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

También puedes instalarlo desde PyPI (si se publica):
```bash
pip install nookiin
```

---

## 3. Uso  
### Modo interactivo
```bash
python Interface.py
```

### Uso programático
```python
from src.System import System

sys = System(layers=[...])
sys.find_commensurate_cell(max_n=20, tol=1e-2)
sys.export_poscar('Supercelda.vasp')
```

---

## 4. Ejemplos  
Algunos casos de uso:  
- Bicapa de grafeno rotado (~3.15°) con reducción de tamaño  
- Aproximación cuasicristalina para tBLG a 30°  
- Modulación de moiré mediante tensión  
Consulta la carpeta `examples/` para scripts y notebooks.

---

## 5. Requisitos  
- Python ≥3.6  
- Requiere: `numpy`, `scipy`, `matplotlib`  
- Opcionales (recomendados): `spglib`, `ase`, `pymatgen`

---

## 6. Contribución  
Tu participación es bienvenida:  
1. Abre un _issue_ o discusión.  
2. Crea una rama en tu fork.  
3. Envía un _pull request_ con una descripción clara.

---

## 7. Licencia  
Este proyecto está bajo la licencia MIT. Consulta `LICENSE.md`.

---

## 8. Contacto  
**Desarrollador principal**: Ossiel Aguilar  
📧 Email: [your_email@example.com](mailto:your_email@example.com)

---

## 📚 Créditos  
- Desarrollado bajo la supervisión de Francisco Sánchez  
- Inspirado por herramientas como BandUP, CellMatch y SuperCell  
