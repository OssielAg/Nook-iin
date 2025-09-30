# src/nookiin/__init__.py

# Importar y exponer todo de basics
from .basics import *

# Importar y exponer Atom
from .atom import *

# Importar y exponer Lattice
from .lattice import *

# Importar y exponer todo de functions
from .functions import *

# Importar y exponer System
from .system import *

# Interface no se carga por defecto (se importa manualmente si el usuario lo necesita)
#from . import interface

# Definir qué queda expuesto globalmente
__all__ = []
__all__ += basics.__all__ if "__all__" in dir(basics) else []
__all__ += atom.__all__ if "__all__" in dir(atom) else ["Atom"]
__all__ += lattice.__all__ if "__all__" in dir(lattice) else ["Lattice"]
__all__ += functions.__all__ if "__all__" in dir(functions) else []
__all__ += system.__all__ if "__all__" in dir(system) else ["System"]
