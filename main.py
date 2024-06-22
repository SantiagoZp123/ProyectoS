from Equipos import Equipos
from Estadios import Estadios
from Partidos import Partidos

import requests
import json

def crearEquipo(nombre_pais, codigo_fifa, grupo, equipos_objeto, equipos):
    nuevo_equipo = Equipos(nombre_pais, codigo_fifa, grupo)
    equipos_objeto.append(nuevo_equipo)
    equipos.append(nuevo_equipo.mostrar_equipo())


def crearEstadio(nombre, ubicacion, estadios_objeto, estadios):
    nuevo_estadio = Estadios(nombre, ubicacion)
    estadios_objeto.append(nuevo_estadio)
    estadios.append(nuevo_estadio.mostrar_estadio())

def crearPartido(equipo_local, equipo_visitante, fecha_hora, estadio, partidos_objeto, partidos):
    nuevo_partido = Partidos(equipo_local, equipo_visitante, fecha_hora, estadio)
    partidos_objeto.append(nuevo_partido)
    partidos.append(nuevo_partido.mostrar_partido())

def emparejar_partidos(equipos, estadios, partidos):
    equipos_dict = {equipo["id"]: Equipos(equipo["id"], equipo["code"], equipo["name"], equipo["group"]) for equipo in equipos}
    estadios_dict = {estadio["id"]: Estadios(estadio["id"], estadio["name"], estadio["city"], estadio["capacity"], estadio["restaurants"]) for estadio in estadios}
    
    partidos_objeto = []
    partidos_lista = []

    for partido in partidos:
        equipo_local = equipos_dict.get(partido["home"]["id"])
        equipo_visitante = equipos_dict.get(partido["away"]["id"])
        estadio = estadios_dict.get(partido["id"])
        
        if equipo_local and equipo_visitante and estadio:
            nuevo_partido = Partidos(partido["id"], partido["number"], equipo_local, equipo_visitante, partido["date"], partido["group"], estadio)
            partidos_objeto.append(nuevo_partido)
            partidos_lista.append(nuevo_partido.mostrar_partido())
    
    return partidos_objeto, partidos_lista

def main():

    equipos_objeto= []
    equipos =[]
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

    archivo_equipos = open('equipos.json')
    datos_equipos = json.load(archivo_equipos)

    for i in range (0,len(datos_equipos)):
       nombre = datos_equipos[i]["name"]
       codigoFifa = datos_equipos[i]["code"]
       grupo = datos_equipos[i]["group"]
       crearEquipo(nombre, codigoFifa, grupo, equipos_objeto, equipos)
       info_equipos.close()

    print (equipos)

main()