# 📄 CHANGELOG

All notable changes to **Nook’iin** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and the project adheres to [Semantic Versioning](https://semver.org/).

---
## [2.0.2] – 2026-02-07
### ✳️ Overview
This release updates the project documentation and citation metadata to reflect the final publication status of Nookiin and to clarify the recommended citation policy for the software.

No changes to the codebase are introduced in this release.

### 🆕 Changes
- **Citation Metadata Update:**  
  The `CITATION.cff` file has been updated to adopt a *software-first* citation policy.  
  Users are now explicitly instructed to cite the Nookiin software via its Zenodo DOI when using the code, while the accompanying journal article is referenced as related work describing the software.

- **README Update:**  
  The *Publications* section has been revised to include the final published reference to the *Computer Physics Communications* article presenting Nookiin, replacing the previous “in preparation” status.

- **Metadata Consistency Improvements:**  
  Naming and bibliographic information have been harmonized across documentation files to ensure consistency between the repository, Zenodo records, and external citation tools.

### 📘 Recommendation
Users citing Nookiin in academic work are encouraged to use the citation information provided in the `CITATION.cff` file.  
For theoretical background and implementation details, the accompanying *Computer Physics Communications* article should be cited as appropriate.

---
## [2.0.1] – 2025-10-19

### ✳️ Overview  
This release introduces an improvement to the guided interface and adds a new example demonstrating the creation of twisted bilayer systems directly from a Python script.  

### 🆕 Changes  
- **Guided Interface Update:**  
  The interactive console interface can now be launched directly using the command:  
  ```bash
  python -m nookiin
  ```  
  once Nookiin is installed. This change simplifies access to the interface and is already documented in the *“Nookiin Usage Modes”* subsection under *Installation*.  
  For detailed guidance, refer to the `Interface_Guide` document included in the repository.  

- **New Example (Example 6):**  
  Added a new example (available in both Spanish and English) that generates two hBN bilayer homostructures with relative twist angles of **21.78°** and **38.22°**.  
  The lattices are loaded directly from a POSCAR file, and the resulting structures share the same Bravais lattice and atom count but differ in stacking configuration.  
  This example runs as a standalone **Python script (.py)**.  

### 📘 Recommendation  
Users are encouraged to review the **Nookiin 2.0.0** release notes to understand the major changes and improvements introduced since version 2.0.0.

---
## [2.0.0] – 2025-10-12

### 🚀 New Features & Improvements

1. **Pip Installation Enabled**
   - Nookiin can now be installed directly with `pip` in virtual environments.
   - Added `pyproject.toml` and `setup.py` for modern Python packaging.
   - The package structure has been reorganized to improve maintainability and usability.

2. **Directory & Module Restructuring**
   - Central Python files reorganized to follow a clear package structure.
   - Many internal functions have been converted to **private** by prefixing them with `_`:
     - **system.py:** `_goesHere`, `_adjust`, `_its_hexagonal_system`, `_analiza_T`
     - **functions.py:** `_leeNumeros`, `_readFile`, `_textLonN`, `_cleanPCell`, `_cleanA`, `_borders`, `_esClon`, `_pts`, `_calcCD`, `_calcPR`, `_megeCut`, `_isitin`
     - **lattice.py:** `_F_hkl`, `_dInfo`
     - **atom.py:** (internal functions updated as needed)
     - **basics.py:** (internal functions updated as needed)

3. **Diffraction Pattern Performance Enhancements**
   - Significant optimizations in functions that compute diffraction patterns:
     - Example: For a lattice with 16,633 atoms evaluated at 19,035 reciprocal space points:
       - **v1.7 (Jan 2025):** ~20–30 minutes  
       - **v1.9 (Aug 2025):** >1 hour (no code changes, likely due to Python/library updates)  
       - **v2.0:** ~131.6 seconds (~2.2 minutes)
   - The diffraction map calculation functions were also improved, reducing execution time by **3–5×** in typical tests.

4. **Other Improvements**
   - Various minor fixes and code refactoring for clarity and maintainability.
   - All changes were tested to ensure backward compatibility with scripts using previous versions.

**Upgrade Instructions:**

```bash
# Recommended: use a virtual environment
python -m venv nookiin_env
source nookiin_env/bin/activate       # Linux/macOS
# Windows PowerShell: .\nookiin_env\Scripts\Activate.ps1

# Install Nookiin via pip
pip install .
```

**Manual usage (optional):**

For users who prefer manual loading without pip, define the environment variable `NOOKIIN_MANUAL_PATH=1` and import:

```python
from src.Nookiin.System import *
```

This ensures that all internal modules are correctly loaded.


**Notes:**
- The v2.0 release focuses on modern Python packaging, internal code refactoring, and **massive performance improvements in diffraction computations**.  
- Users are strongly encouraged to upgrade to v2.0 for better performance and easier installation.

---
## [1.9.1] - 2025-07-28
This release marks the formal update of the program's name in all documentation, from **Nook-iin** to **Nookiin**.

### Changes included:
- All references to `Nook-iin` were replaced in:
  - `README.md`
  - Online documentation
  - Examples and notebooks
  - Auxiliary scripts and module headers
- The project title and internal descriptions have been updated to reflect the new name.
- Links, paths, and textual mentions with hyphens were revised for better compatibility with international tooling and publishing.

### Notes:
- This update **does not affect program functionality**.
- Version 1.9.1 remains fully compatible with previous releases.
- If you're using a local clone of the repository, you can update your remote URL with:
  ```bash
  git remote set-url origin https://github.com/your_username/Nookiin.git

---
## [1.9.0] - 2025-07-14
### Highlights
- New feature: `plot_diffraction_map` — Generates smooth diffraction intensity maps using either Lorentzian or Gaussian peak distributions.
- Supports customizable resolution, width, and output formats.
- Scientific improvement: Better control of reciprocal space resolution and peak broadening. Helps highlight structural features such as Moiré periodicity and stacking contrast.

### Added
- `examples/05_Ejemplo_Mapa_de_difracción.ipynb` (Spanish)
- `examples/05_Example_Diffraction_Map.ipynb` (English)

These demonstrate how to generate and interpret diffraction maps for multilayer systems.

### Internal Changes
- Updated System.py with plot_diffraction_map method.
- Improved internal documentation and consistency of naming in plotting utilities.
- Minor fixes in reciprocal space vector normalization.
---

## [1.7.0] – 2025-06-30
### Added
- Complete refactor of all docstrings across the main modules (`Basics.py`, `Atom.py`, `Lattice.py`, `Functions.py`, `System.py`) following the **PEP 257** documentation standard.
- Two fully documented usage examples in both English and Spanish:
  - `03_Example_Heterostructure.ipynb`: Multilayer heterostructure modeling.
  - `04_Example_Results_AngleInterval.ipynb`: Angular interval search for commensurate primitive cells.
### Changed
- All user-facing messages translated from Spanish to English.
- Significant improvements in code readability and structure across core modules.
### Notes
This version improves usability for international collaborators and serves as the foundation for future releases involving external validation and integration.

---

## [1.5.0] – 2025-04-20
### Added
- Bilingual support through fully translated Jupyter Notebook examples.
- Inclusion of missing or incomplete functionalities from the initial release.
### Changed
- Revised documentation with improved clarity and structure.
- General codebase clean-up to adhere to professional standards.
### Notes
With this release, **Nook’iin** is suitable for citation in academic publications and scientific research projects.

---

## [1.0.0] – 2024-11-01
### Added
- Initial public release of **Nook’iin**, developed as part of a Bachelor's thesis at the Faculty of Sciences, UNAM.
- Functionalities:
  - Calculation of primitive cells for multilayer 2D heterostructures.
  - Graphical representation in reciprocal space.
  - Generation of theoretical diffraction patterns.
- Documentation provided in `Nook_inn_Overview.pdf`.

---

