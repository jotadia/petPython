# adopcion/__init__.py

# Variables del paquete

VERSION = "1.0.0"
AUTOR = "JCOD"

from .models.mascota import Mascota
from .models.persona import Persona, Adoptante
from .models.refugio import Refugio
from .models.helpers import buscar_mascota
