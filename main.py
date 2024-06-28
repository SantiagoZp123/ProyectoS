import requests
import json
from Equipos import Equipos
from Estadios import Estadios
from Partidos import Partidos
from Cliente import Cliente

from Bebida import Bebida
from Alcoholica import Alcoholica
from NoAlcoholica import NoAlcoholica
from Alimento import Alimento
from Plate import Plate
from Package import Package

def crearEquipo(nombre, codigoFifa, grupo, equipo_id, equipos_objeto, equipos):
    """
    Crea un nuevo equipo y lo añade tanto al objeto de equipos como a la lista de equipos.

    Parameters:
    nombre (str): Nombre del equipo.
    codigoFifa (str): Código FIFA del equipo.
    grupo (str): Grupo al que pertenece el equipo.
    equipo_id (str): Identificador único del equipo.
    equipos_objeto (list): Lista de objetos de tipo Equipos donde se almacenará el nuevo equipo.
    equipos (list): Lista de equipos donde se mostrará el nuevo equipo.

    Returns:
    None
    """
    nuevo_equipo = Equipos(nombre, codigoFifa, grupo, equipo_id)
    equipos_objeto.append(nuevo_equipo)
    equipos.append(nuevo_equipo.mostrar_equipo())

def crearEstadio(name, city, capacity, estadio_id, estadios_objeto, estadios):
    """
    Crea un nuevo estadio y lo añade tanto al objeto de estadios como a la lista de estadios.

    Parameters:
    name (str): Nombre del estadio.
    city (str): Ciudad donde se encuentra el estadio.
    capacity (int): Capacidad del estadio.
    estadio_id (str): Identificador único del estadio.
    estadios_objeto (list): Lista de objetos de tipo Estadios donde se almacenará el nuevo estadio.
    estadios (list): Lista de estadios donde se mostrará el nuevo estadio.

    Returns:
    None
    """
    nuevo_estadio = Estadios(name, city, capacity, estadio_id)
    estadios_objeto.append(nuevo_estadio)
    estadios.append(nuevo_estadio.mostrar_estadio())

def buscarPartidosPorPais(partidos):
    '''
    Función que muestra los partidos según el país seleccionado.
    Muestra una lista de países disponibles y permite al usuario seleccionar uno para mostrar los partidos correspondientes.
    '''
    ciudades = set()
    for partido in partidos:
        ciudades.add(partido.estadio.city)

    ciudades = list(ciudades)
    print("Ciudades disponibles:")
    for i, ciudad in enumerate(ciudades):
        print(f"{i + 1} -- {ciudad}")

    opcion = input("Ingrese el número de la ciudad que desea buscar: ")

    if opcion.isnumeric() and 1 <= int(opcion) <= len(ciudades):
        ciudad_seleccionada = ciudades[int(opcion) - 1]
        print(f"Partidos en {ciudad_seleccionada}:")
        for partido in partidos:
            if partido.estadio.city == ciudad_seleccionada:
                print(partido.show_partido())
    else:
        print("Opción inválida")

def buscarPartidosEquipos(partidos):
    '''
    Función que muestra los partidos según el país seleccionado.
    Muestra una lista de países disponibles y permite al usuario seleccionar uno para mostrar los partidos correspondientes.
    '''
    paises = set()
    for partido in partidos:
        paises.add(partido.equipo_local)
        paises.add(partido.equipo_visitante)

    paises = list(paises)
    print("Países disponibles:")
    for i, pais in enumerate(paises):
        print(f"{i + 1} -- {pais}")

    opcion = input("Ingrese el número del país que desea buscar: ")

    if opcion.isnumeric() and 1 <= int(opcion) <= len(paises):
        pais_seleccionado = paises[int(opcion) - 1]
        print(f"Partidos de {pais_seleccionado}:")
        for partido in partidos:
            if partido.equipo_local == pais_seleccionado or partido.equipo_visitante == pais_seleccionado:
                print(partido.show_partido())
    else:
        print("Opción inválida")

def buscarPartidosPorFecha(partidos):
    '''
    Función que muestra los partidos según la fecha seleccionada.
    Muestra una lista de fechas disponibles y permite al usuario seleccionar una para mostrar los partidos correspondientes.
    '''
    fechas = set()
    for partido in partidos:
        fechas.add(partido.fecha)

    fechas = list(fechas)
    print("Fechas disponibles:")
    for i, fecha in enumerate(fechas):
        print(f"{i + 1} -- {fecha}")

    opcion = input("Ingrese el número de la fecha que desea buscar (en formato yyyy-mm-dd): ")

    found = False
    for partido in partidos:
        if partido.fecha == opcion:
            print(partido.show_partido())
            found = True

    if not found:
        print(f"No se encontraron partidos en la fecha {opcion}.")

def mapa(fila, columna):
    """
    Marca una posición específica en un mapa bidimensional.

    Parameters:
    fila (int): Número de fila.
    columna (int): Número de columna.

    Returns:
    list: Mapa actualizado con la posición marcada como True.
    """
    fila = input("Seleccione la fila:")
    columna = input("Seleccione la columna")

    mapa[int(fila)-1][int(columna)-1] = True
    return mapa

def codigoAleatorio(item):
    identificador = format(id(item), 'x')
    return identificador


def es_numero_perfecto(var):
    '''
    
    Funcion que revisa si un numero es perfecto, para aplicar el descuento.
    
    '''
    divisores = []
    for i in range(1, var):
        if var % i == 0:
            divisores.append(i)
    if sum(divisores) == var:
        return True
    else:
        return False
    
def numeroOndulado(num):
    '''
    
    Funcion que revisa si la cedula es un numero ondulado, para aplicar el descuento.
    
    '''
    num_str = str(num)
    n = len(num_str)
    for i in range(1, n):
        if i%2 == 0 and num_str[i] >= num_str[i-1]:
            return False
        elif i%2 == 1 and num_str[i] <= num_str[i-1]:
            return False
    return True

def main():
    equipos = []
    equipos_objeto = []
    estadios = []
    estadios_objeto = []
    partidos = []
    codigos =[]
    clientes = []
    cedulas_vip =[]
    codigos =[]
    codigos_usados =[]

    bebidas_alcholicas_objeto =[]
    bebidas_noalcoholicas_objeto =[]
    alimentos_plate_objeto =[]
    alimentos_package_objeto =[]
    total_productos =[]
    monto_tickets_vip =[]

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

    archivo_equipos = open('equipos.json')
    datos_equipos = json.load(archivo_equipos)
    for i in range(len(datos_equipos)):
        nombre = datos_equipos[i]["name"]
        codigoFifa = datos_equipos[i]["code"]
        grupo = datos_equipos[i]["group"]
        equipo_id = datos_equipos[i]["id"]
        crearEquipo(nombre, codigoFifa, grupo, equipo_id, equipos_objeto, equipos)
    archivo_equipos.close()

    try:
        with open('estadios.json', 'r', encoding='utf-8') as archivo_estadios:
            datos_estadios = json.load(archivo_estadios)
    except FileNotFoundError:
        print("El archivo 'estadios.json' no fue encontrado.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Asegúrese de que el archivo contiene un JSON válido.")
    except UnicodeDecodeError:
        print("Error al decodificar el archivo. Asegúrese de que el archivo está codificado en UTF-8.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    if 'datos_estadios' in locals():
        for estadio in datos_estadios:
            name = estadio["name"]
            city = estadio["city"]
            capacity = estadio["capacity"]
            estadio_id = estadio["id"]
            crearEstadio(name, city, capacity, estadio_id, estadios_objeto, estadios)

    # Cargar los partidos
    requests_partidos = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json')
    contenido_partidos = requests_partidos.content
    info_partidos = open('partidos.json', 'wb')
    info_partidos.write(contenido_partidos)
    info_partidos.close()

    archivo_partidos = open('partidos.json')
    datos_partidos = json.load(archivo_partidos)

    for partido in datos_partidos:
        home_team_id = partido["home"]["id"]
        away_team_id = partido["away"]["id"]
        hora = partido["date"]
        estadio_id = partido["stadium_id"]
        

        home_team = next((equipo for equipo in equipos_objeto if equipo.equipo_id == home_team_id), None)
        away_team = next((equipo for equipo in equipos_objeto if equipo.equipo_id == away_team_id), None)
        estadio = next((estadio for estadio in estadios_objeto if estadio.estadio_id == estadio_id), None)

        if home_team and away_team and estadio:
            nuevo_partido = Partidos(home_team, away_team, hora,estadio )
            partidos.append(nuevo_partido)
    
    archivo_partidos.close()

    #for partido in partidos:
    #print(partido.show_partido())
    

    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ Bienvenido a la Euro 2024 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    while True: 
        gestion = input("""Ingrese la gestión a la que desea acceder
        [1] » Gestion de partidos y estadios
        [2] » Gestion de venta de entradas
        [3] » Gestion de asitencia a partidos                
        [4] » Gestion de restaurantes 
        [5] » Gestion de venta de restaurantes 
        [6] » Undicadores de gestión """)
        if gestion.isnumeric() == False or int(gestion)>7:
            print("Por favor ingrese una opción válida")
        else:
            gestion = int(gestion)
            if gestion == 1:
                print("░░░░░░░░░░░░░░░░░░░░░ Bienvenido a la seccion de busqueda ░░░░░░░░░░░░░░░░░░░░░")
                while True: 
                    busqueda = input("""Ingrese la opcion a la que desea acceder
                    [1] » Buscar todos los partidos de un país
                    [2] » Buscar todos los partidos que se jugarán en un estadio específico
                    [3] » Buscar todos los partidos que se jugarán en una fecha determinada
                    [4] » Finalizar """)

                    if busqueda.isnumeric()== False or int(busqueda)>8:
                        print ("Ingresa una opción válida: ")
                    else:
                        busqueda = int(busqueda)
                        if busqueda==1:
                            buscarPartidosEquipos(partidos)
                        elif busqueda ==2:
                            buscarPartidosPorPais(partidos)
                        elif busqueda ==3:
                            buscarPartidosPorFecha(partidos)
                        elif busqueda ==4:
                            break
            elif gestion ==2:
                
            elif opcion == 2:
                print ("Gracias por su visita")
                break

main()