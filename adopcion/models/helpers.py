# -*- coding: utf-8 -*-
"""
Created on 10 aug 2026

@author: JCOD
"""

#from models.mascota import *

def buscar_mascota(nombre, lista_mascotas):
    for mascota in lista_mascotas:
        if mascota.nombre == nombre:
            return mascota
    return "No se encontró ninguna mascota con ese nombre."