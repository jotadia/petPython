# -*- coding: utf-8 -*-
"""
Created on 10 aug 2026

@author: JCOD
"""
from adopcion import *
'''
from models.persona import *
from models.mascota import *
from models.refugio import *
from models.helpers import buscar_mascota
'''

persona = Persona("Julio Cesar", 47)
print(persona.presentarse())  # Salida: Hola, mi nombre es Juan y tengo 30 años.
print(persona)  # Salida: Juan (30 años)

mascota = []
mascota.append(Mascota("Firulais", 3, "Perro"))
mascota.append(Mascota("Michi", 2, "Gato"))
mascota.append(Mascota("otto", 1, "Loro"))
#print(mascota[0])  # Salida: Firulais (Perro, False, 3 años)
#print(mascota[1])  # Salida: Michi (Gato, False, 2 años)

#mascota_buscada = buscar_mascota("otto", mascota)
#print(mascota_buscada)  # Salida: Firulais (Perro, False, 3 años)


opcion = input("Selecciona una opción: \n1. Listar mascotas disponibles.\n2. Adoptar una mascota por nombre.\n3. Ver las mascotas adoptadas.\n4. Salir.\n")

while opcion != "4":
    refugio = Refugio()
    for m in mascota:
        refugio.registrar_mascota(m)
    if opcion == "1":
        '''refugio = Refugio()
        for m in mascota:
            refugio.registrar_mascota(m)'''
        print(f"Mascotas disponibles: {', '.join(refugio.listado_mascotas())}")
    elif opcion == "2":
        nombre_mascota = input("Ingrese el nombre de la mascota que desea adoptar: ")
        mascota_a_adoptar = buscar_mascota(nombre_mascota, mascota)
        if isinstance(mascota_a_adoptar, Mascota):
            adoptante = Adoptante("Julio Cesar", 47, "Calle 123")
            resultado_adopcion = refugio.asignar_adopcion(adoptante, mascota_a_adoptar)
            print(resultado_adopcion)
        else:
            print(mascota_a_adoptar)  # Mensaje de error si no se encuentra la mascota
    elif opcion == "3":
        adoptante = Adoptante("Julio Cesar", 47, "Calle 123")
        if not adoptante.mascotas_adoptadas:
            print(f"{adoptante.nombre} no ha adoptado ninguna mascota.")
        else:
            for adoptada in adoptante.mascotas_adoptadas:
                print(f"Mascota adoptada por {adoptante.nombre}: {adoptada.nombre} ({adoptada.especie}, {adoptada.edad} años)")
        #print(adoptante.mascotas_adoptadas[0].nombre)  # Salida: Firulais
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.\n1. Listar mascotas disponibles.\n2. Adoptar una mascota por nombre.\n3. Ver las mascotas adoptadas.\n4. Salir.\n")
    
    opcion = input("Selecciona una opción: \n1. Listar mascotas disponibles.\n2. Adoptar una mascota por nombre.\n3. Ver las mascotas adoptadas.\n4. Salir.\n")