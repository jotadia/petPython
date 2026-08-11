# -*- coding: utf-8 -*-
"""
Created on 10 aug 2026

@author: JCOD
"""

import mascota as m

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."  

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"
    
class Adoptante(Persona):
    
    mascotas_adoptadas = []
    
    def adoptar(self, mascota):
        self.mascotas_adoptadas.append(mascota)
    
    def __init__(self, nombre, edad, direccion):
        super().__init__(nombre, edad)
        self.direccion = direccion
        
    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y vivo en {self.direccion}."
    
    def __str__(self):
        return f"{self.nombre} ({self.edad} años, vive en {self.direccion})"