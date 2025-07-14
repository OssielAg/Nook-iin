# 📄 CHANGELOG

All notable changes to **Nook’iin** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and the project adheres to [Semantic Versioning](https://semver.org/).

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

