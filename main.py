from Equipos import Equipos
from Estadios import Estadios
from Partidos import Partidos

import requests
import json

def crearEquipo(nombre, codigoFifa, grupo, equipos_objeto, equipos):
    nuevo_equipo = Equipos(nombre, codigoFifa, grupo)
    equipos_objeto.append(nuevo_equipo)
    equipos.append(nuevo_equipo)

def emparejar_equipos_partidos(equipos):
    equipos1_2 = []
    for i in equipos:
        if getattr(i, 'partido') == 'partido':
            equipos1_2.append(i.show_nombre_num())
    return equipos1_2

def crearPartido(equipo_local, equipo_visitante, fecha, estadio, equipos, partidos_objeto, partidos):
    equipos1_2 = emparejar_equipos_partidos(equipos)
    nuevo_partido = Partidos(equipo_local, equipo_visitante, fecha, estadio, fecha)
    partidos_objeto.append(nuevo_partido)
    partidos.append(nuevo_partido.mostrar_partido())

def mostrarPartidos(partidos):
    paises = []
    for partido in partidos:
        paises.append(partido.equipo_local)  # Corregido para usar equipo_local
    paises = list(set(paises))
    for i, pais in enumerate(paises):
        print(f"{i+1}. {pais}")
    option = input("Seleccione el pais que desea ver: ")

    for partido in partidos:
        if partido.equipo_local == paises[int(option)-1]:  # Corregido para usar equipo_local
            print(partido.mostrar_partido())

def crearEstadio(nombre, ubicacion, estadio, estadios_objeto, estadios):
    nuevo_estadio = Estadios(nombre, ubicacion, estadio)
    estadios_objeto.append(nuevo_estadio)

def main():
    equipos_objeto = []
    equipos = []
    estadios_objeto = []
    estadios = []
    partidos_objeto = []
    partidos = []

    requests_equipos = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json')
    contenido_equipos = requests_equipos.content
    info_equipos = open('equipos.json', 'wb')
    info_equipos.write(contenido_equipos)
    info_equipos.close()

    requests_estadios = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json')
    contenido_estadios = requests_estadios.content
    info_estadios = open('estadios.json', 'wb')
    info_estadios.write(contenido_estadios)
    info_estadios.close()

    requests_partidos = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json')
    contenido_partidos = requests_partidos.content
    info_partidos = open('partidos.json', 'wb')
    info_partidos.write(contenido_partidos)
    info_partidos.close()

    archivo_partidos = open('partidos.json')
    datos_partidos = json.load(archivo_partidos)
    for i in range(len(datos_partidos)):
        equipo_local = datos_partidos[i]["home"]
        equipo_visitante = datos_partidos[i]["away"]
        fecha = datos_partidos[i]["date"]
        estadio = datos_partidos[i]["stadium_id"]
        crearPartido(equipo_local, equipo_visitante, fecha, estadio, equipos, partidos_objeto, partidos)
    archivo_partidos.close()
    
    archivo_equipos = open('equipos.json')
    datos_equipos = json.load(archivo_equipos)
    for i in range(len(datos_equipos)):
        nombre = datos_equipos[i]["name"]
        codigoFifa = datos_equipos[i]["code"]
        grupo = datos_equipos[i]["group"]
        crearEquipo(nombre, codigoFifa, grupo, equipos_objeto, equipos)
    archivo_equipos.close()

    archivo_estadios = open('estadios.json')
    datos_estadios = json.load(archivo_estadios)
    for i in range(len(datos_estadios)):
        nombre = datos_estadios[i]["name"]
        ubicacion = datos_estadios[i]["city"]
        estadio = datos_estadios[i]["id"]
        crearEstadio(nombre, ubicacion, estadio, estadios_objeto, estadios)
    archivo_estadios.close()

    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ Bienvenido a la Euro 2024 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    mostrarPartidos(partidos_objeto)

main()