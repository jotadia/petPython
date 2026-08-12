# -*- coding: utf-8 -*-
"""
Created on 10 aug 2026

@author: JCOD
"""

# DEBO REVBISAR ESTA CLASE, YA QUE NO SE SI ESTA BIEN IMPLEMENTADA, YA QUE NO SE SI LA LISTA DE MASCOTAS SE ESTA INICIALIZANDO CORRECTAMENTE.

#from models.mascota import *

class Refugio():
    
    
    
    def __init__(self):
        self.__mascotas = []
        
    def registrar_mascota(self, mascota):
        self.__mascotas.append(mascota)
    
    def listado_mascotas(self):
        if not self.__mascotas:
            return "No hay mascotas registradas."
        else:
            __mascotas_disponibles = []
            j = 0
            for i in range(len(self.__mascotas)):
                if not self.__mascotas[i].adoptado:
                    __mascotas_disponibles.append(self.__mascotas[i].nombre)
                    j += 1
                    #return f"{self.__mascotas[i].nombre} ({self.__mascotas[i].especie}, {self.__mascotas[i].edad} años)"
                elif j == 0:
                    return "No hay mascotas disponibles."
            return __mascotas_disponibles
            #return [str(mascota.nombre) for mascota in self.__mascotas if mascota.adoptado]
        #return self.__mascotas
    
    def asignar_adopcion(self, adoptante, mascota):
        if mascota in self.__mascotas and not mascota.adoptado:
            adoptante.adoptar(mascota)
            mascota.adoptado = True
            return f"{adoptante.nombre} ha adoptado a {mascota.nombre}."
        else:
            return "La mascota no está disponible para adopción."
    
    
   
    
   