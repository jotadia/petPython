# -*- coding: utf-8 -*-
"""
Created on 10 aug 2026

@author: JCOD
"""


class Mascota:
    def __init__(self, nombre, edad, especie, adoptado=False):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.adoptado = adoptado

    def __str__(self):
        return f"{self.nombre} ({self.especie}, {self.adoptado}, {self.edad} años)"