# -*- coding: utf-8 -*-
"""
Created on 10 aug 2026

@author: JCOD
"""

# DEBO REVBISAR ESTA CLASE, YA QUE NO SE SI ESTA BIEN IMPLEMENTADA, YA QUE NO SE SI LA LISTA DE MASCOTAS SE ESTA INICIALIZANDO CORRECTAMENTE.

import mascota as m

class Refugio():
    def __init__(self):
        self.__mascotas = m.Mascota
        
    def registrar_mascota(self, mascota):
        self.__mascotas.append(mascota)
    
    def listado_mascotas(self):
        if not self.__mascotas:
            return "No hay mascotas registradas."
        elif any(mascota.adoptado for mascota in self.__mascotas):
            return [str(mascota) for mascota in self.__mascotas if mascota.adoptado]
        #return self.__mascotas
    
    def asignar_adopcion(self, adoptante, mascota):
        if mascota in self.__mascotas and not mascota.adoptado:
            adoptante.adoptar(mascota)
            mascota.adoptado = True
            return f"{adoptante.nombre} ha adoptado a {mascota.nombre}."
        else:
            return "La mascota no está disponible para adopción."
    
    
   
    
   