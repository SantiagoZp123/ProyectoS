import requests
import json
import os
from Equipos import Equipos
from Estadios import Estadios
from Partidos import Partidos
from Cliente import Cliente


from Alimento import Alimento 
from Bebida import Bebida
from Alcoholica import Alcoholica
from NoAlcoholica import NoAlcoholica
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

def crear_mapa(columnas):
    '''
    Genera un mapa de puestos Vip y General.
    Divide el mapa en sublistas de 10 columnas cada una y coloca cada sublista una debajo de la otra.
    '''
    if columnas < 10:
        columnas = 10

    mapa = []
    fila = []

    for i in range(columnas):
        fila.append(False)
        if len(fila) == 10:
            mapa.append(fila)
            fila = []

    if fila:  # Si hay columnas restantes que no completan una fila de 10, se agregan al mapa
        mapa.append(fila)

    return mapa


def codigoAleatorio(item):
    """
    Genera un identificador aleatorio en formato hexadecimal basado en el ID del objeto.

    Parameters:
    item (object): Objeto del cual se generará el identificador.

    Returns:
    str: Identificador aleatorio en formato hexadecimal.
    """
    identificador = format(id(item), 'x')
    return identificador

def esNumeroVampiro(num):
    '''
    Determina si un número es un número vampiro.
    Un número vampiro es un número que puede ser formado por la multiplicación de dos números de la mitad de sus dígitos,
    manteniendo el mismo orden de los dígitos originales.

    Parameters:
    num (int): Número a evaluar.

    Returns:
    bool: True si el número es vampiro, False en caso contrario.
    '''
    num_str = str(num)
    n = len(num_str)
    
    # Un número vampiro debe tener un número par de dígitos
    if n % 2 != 0:
        return False
    
    # Generar todos los pares posibles de "colmillos"
    mitad = n // 2
    
    # Crear una lista para almacenar los colmillos
    colmillos = []
    
    # Crear los colmillos manualmente
    for i in range(1, 10**mitad):
        for j in range(1, 10**mitad):
            if sorted(str(i) + str(j)) == sorted(num_str) and i * j == num:
                colmillos.append((i, j))
    
    # Verificar si algún par de colmillos cumple la condición
    for colmillo1, colmillo2 in colmillos:
        if colmillo1 * colmillo2 == num:
            return True
    
    return False

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

def guardar_estado_asientos(filename, estado_asientos):
    with open(filename, 'w') as file:
        json.dump(estado_asientos, file)

# Función para cargar el estado de los asientos desde un archivo
def cargar_estado_asientos(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def seleccionar_asiento(mapa, cantidad_entradas):
    asientos_seleccionados = []
    for i in range(cantidad_entradas):
        while True:
            try:
                fila = int(input("Seleccione la fila: ")) - 1
                columna = int(input("Seleccione la columna: ")) - 1

                if fila < 0 or fila >= len(mapa) or columna < 0 or columna >= len(mapa[0]):
                    print("Fila o columna fuera de rango. Intente de nuevo.")
                    continue

                if mapa[fila][columna]:
                    print("Asiento ya ocupado. Seleccione otro asiento.")
                else:
                    mapa[fila][columna] = True
                    asiento = f"F{fila + 1}C{columna + 1}"
                    asientos_seleccionados.append(asiento)
                    break
            except ValueError:
                print("Entrada no válida. Por favor ingrese números válidos.")
            except Exception as e:
                print(f"Ocurrió un error: {e}")

        print("\nAviso: Los puestos ocupados contienen True, por favor selecciona los que no están ocupados\n")
        print(mapa)
    return asientos_seleccionados

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
    asientos_general = cargar_estado_asientos('asientos_general.json')
    asientos_vip = cargar_estado_asientos('asientos_vip.json')
    

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
    

    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ Bienvenido a la Euro 2024 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
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
                print("░░░░░░░░░░░░░░░░░░░░░ Seccion de venta de entradas ░░░░░░░░░░░░░░░░░░░░░")

                opcion = input("""Usted desea realizar una compra:
[1] » Si 
[2] » No """)
                if opcion.isnumeric()==False or int(opcion)>2:
                    print ("Ingrese una opción válida: ")
                else: 
                    opcion = int(opcion)
                    if opcion ==1:
                        lista_generales = []
                        lista_vip = []
                        for x in datos_estadios:
                            nombre = x["name"]
                            for x2,y in x.items():
                                if x2 =="capacity":
                                    general = y[0]
                                    vip = y[1]

                                    lista_generales.append(general)
                                    lista_vip.append(vip)

                        nombre = input("Ingrese su nombre: ")
                        while not nombre.isalpha():
                            nombre = (input("Ingrese un nombre valido: "))
                        cedula = input("Ingrese su cedula: ")
                        while not cedula.isnumeric():
                            cedula = input("Ingrese una cedula validad: ")
                        
                        edad = input("Ingrese su edad: ")
                        while not edad.isnumeric():
                            edad = input ("Introduzca una edad valida:")
                            if int(edad) > 0 and int(edad) < 100:
                                continue
                            else: 
                                edad = input("Ingrese una edad válida: ")
                        """buscarEstadios(partidoss_objeto)"""
                        cantidad_entradas = input("Ingrese la cantidad de entradas a comprar: ")
                        while not cantidad_entradas.isdigit():
                            cantidad_entradas = input("Ingrese una cantidad de entradas válida: ")

                        cantidad_entradas = int(cantidad_entradas)
                        for i, x in enumerate(estadios_objeto, start=1):
                            print(f"{i}. {x.mostrar_estadio()}")
                        tipo_entrada = input("""Ingrese el tipo de entrada que desea adquirir: 
[1] » General           
[2] » Vip """)
                        if tipo_entrada == "1":
                            asientos_general = []
                            precio_general = 35.00
                            option = int(input("Ingrese el número del partido que desea comprar: ")) - 1
                            print("--------------------------------------------------------------------------------------------------------------")
                            print(f"A continuación se muestra la lista de entradas disponible de la forma [Fila,Columna] --> {lista_generales[option]}")
                            print("--------------------------------------------------------------------------------------------------------------")
                            i = lista_generales[option]
                            mapa = crear_mapa(i)
                            print(f"                                 ╔ Mapa Carrera {option} ╗                                                   ")
                            print(mapa)
                            print("--------------------------------------------------------------------------------------------------------------")

                            asientos_general = seleccionar_asiento(mapa, cantidad_entradas)

                            codigo_ticket = codigoAleatorio(nombre)
                            iva = 0.16
                            monto = float(len(asientos_general)) * precio_general

                            if esNumeroVampiro(cedula):
                                print("Su cédula es un número ondulado, por ende obtiene un descuento en la compra de sus entradas")
                                monto_descuento = monto * 0.50
                                monto_d = monto - monto_descuento
                                monto_con_iva = monto_d * iva
                                monto_total = monto_d + monto_con_iva
                            else:
                                monto_con_iva = monto * iva
                                monto_descuento = "No"
                                print("Su cédula no es un número ondulado, por ende no hay descuento")
                                monto_total = monto + monto_con_iva

                            print(f"""Detalles compra:
                        Asientos: {asientos_general}
                        Código: {codigo_ticket}
                        Subtotal: {monto}
                        Descuento: {monto_descuento}
                        Iva: {monto_con_iva}
                        Total: {monto_total}
                        """)

                            compra = input("¿Desea proceder a comprar la entrada?\n[1] » Sí\n[2] » No\n")
                            while compra not in ['1', '2']:
                                compra = input("Entrada no válida. ¿Desea proceder a comprar la entrada?\n[1] » Sí\n[2] » No\n")

                            compra = int(compra)
                            if compra == 1:
                                print("Compra exitosa")
                                codigos.append(codigo_ticket)
                                entrada = "general"
                                cliente = Cliente(nombre, cedula, edad, entrada, codigo_ticket, asientos_general)
                                clientes.append(cliente)
                                print(cliente.mostrar_cliente())
                                # Guardar el estado de los asientos generales
                                guardar_estado_asientos('asientos_general.json', asientos_general)
                            else:
                                print("Compra cancelada")

                        elif tipo_entrada == "2":
                            asientos_vip = []
                            entrada = "vip"
                            precio_vip = 75.00
                            option = int(input("Ingrese el número del partido que desea comprar: ")) - 1
                            print("--------------------------------------------------------------------------------------------------------------")
                            print(f"A continuación se muestra la lista de entradas disponible de la forma [Fila,Columna] --> {lista_vip[option]}")
                            print("--------------------------------------------------------------------------------------------------------------")
                            i = lista_vip[option]
                            mapa = crear_mapa(i)
                            print(f"                                 ╔ Mapa Carrera {option} ╗                                                   ")
                            print(mapa)
                            print("--------------------------------------------------------------------------------------------------------------")

                            asientos_vip = seleccionar_asiento(mapa, cantidad_entradas)

                            codigo_ticket = codigoAleatorio(nombre)
                            iva = 0.16
                            monto = float(len(asientos_vip)) * precio_vip

                            if esNumeroVampiro(cedula):
                                print("Su cédula es un número vampiro, por ende obtiene un descuento en la compra de sus entradas")
                                monto_descuento = monto * 0.50
                                monto_d = monto - monto_descuento
                                monto_con_iva = monto_d * iva
                                monto_total_vip = monto_d + monto_con_iva
                            else:
                                print("Su cédula no es un número vampiro, por ende no hay descuento")
                                monto_descuento = 0
                                monto_con_iva = monto * iva
                                monto_total_vip = monto + monto_con_iva

                            print(f"""Detalles compra:
                        Asientos: {asientos_vip}
                        Código: {codigo_ticket}
                        Subtotal: {monto}
                        Descuento: {monto_descuento}
                        Iva: {monto_con_iva}
                        Total: {monto_total_vip}
                        """)

                            compra = input("Desea proceder a comprar la entrada \n[1] » Si \n[2] » No\n")
                            while compra not in ['1', '2']:
                                compra = input("Entrada no válida. Desea proceder a comprar la entrada \n[1] » Si \n[2] » No\n")

                            compra = int(compra)
                            if compra == 1:
                                print("Compra exitosa")
                                codigos.append(codigo_ticket)
                                cedulas_vip.append(cedula)
                                cliente = Cliente(nombre, cedula, edad, entrada, codigo_ticket, asientos_vip)
                                clientes.append(cliente)
                                print(cliente.mostrar_cliente())
                                # Guardar el estado de los asientos VIP
                                guardar_estado_asientos('asientos_vip.json', asientos_vip)
                            else:
                                print("Compra cancelada")
                            #with open("clientesvip.txt", "w") as f:
                                #f.write(nombre,cedula,edad,entrada,codigo_ticket,asientos_c)
            elif gestion == 3:
                print("Gestión de asitencia a partidos")
                aux = 0
                aux1 = 0

                while True:
                    try:
                        codigo = input("Ingrese el codigo numerico de su boleto: ")
                        break
                    except:
                        print("Error")

                for x in codigos:
                    if codigo == x:
                        aux += 1

                for x in codigos_usados:
                    if codigo == x:
                        aux1 += 1
                
                if aux1 > 0:
                    print("Este codigo ya ha sido utilizado")
                elif aux == 0:
                    print("Error, boleto no encontrado")
                else:
                    codigos_usados.append(codigo)
                    print("Disfrute del partido")
            elif gestion == 4:
                print("Gestión de restaurantes")
                for x in datos_estadios:
                    for x2,y in x.items():
                        if x2 == "restaurants":
                            inventarioind = []
                            for x3 in y:
                                nombre_restaurante = x3["name"]
                                for x4,y2 in x3.items():
                                    if x4 == "products":
                                        for x5 in y2:
                                            nombre_producto = x5["name"]
                                            tipo_producto = x5["adicional"]
                                            if tipo_producto == "alcoholic":
                                                precio_producto = x5["price"]  
                                                cantidad =x5["quantity"] 
                                                stock =x5["stock"]
                                                precio_con_iva = float(precio_producto) * 0.16
                                                precio_total = float(precio_producto) + float(precio_con_iva)
                                                precio_final = round(precio_total,2)
                                                tipo = "bebida"
                                                #print(nombre_restaurante,nombre_producto,tipo_producto,precio_producto,precio_con_iva,precio_total,precio_final)
                                                alcoholic = Alcoholica(nombre_producto, cantidad,precio_final,stock,tipo_producto, tipo)
                                                bebidas_alcholicas_objeto.append(alcoholic)
                                                total_productos.append(alcoholic)
                                                #print(alcoholic.mostrar_bebida_alcoholica())

                
                for x in datos_estadios:
                    for x2,y in x.items():
                        if x2 == "restaurants":
                            inventarioind = []
                            for x3 in y:
                                nombre_restaurante = x3["name"]
                                for x4,y2 in x3.items():
                                    if x4 == "products":
                                        for x5 in y2:
                                            nombre_producto = x5["name"]
                                            tipo_producto = x5["adicional"]
                                            if tipo_producto == "non-alcoholic":
                                                precio_producto = x5["price"]
                                                cantidad = x5["quantity"]
                                                stock =x5["stock"]
                                                precio_con_iva = float(precio_producto) * 0.16
                                                precio_total = float(precio_producto) + float(precio_con_iva) 
                                                precio_final = round(precio_total,2)
                                                tipo = "bebida"
                                                #print(nombre_restaurante,nombre_producto,tipo_producto,precio_producto,precio_con_iva,precio_total,precio_final)"""
                                                noalcoholic = NoAlcoholica(nombre_producto,cantidad,precio_final, stock,tipo_producto, tipo)
                                                bebidas_noalcoholicas_objeto.append(noalcoholic)
                                                total_productos.append(noalcoholic)

                                                #print(noalcoholic.mostrar_bebida_noalcoholica())"""
                for x in datos_estadios:
                    for x2,y in x.items():
                        if x2 == "restaurants":
                            inventarioind = []
                            for x3 in y:
                                nombre_restaurante = x3["name"]
                                for x4,y2 in x3.items():
                                    if x4 == "products":
                                        for x5 in y2:
                                            nombre_producto = x5["name"]
                                            tipo_producto = x5["adicional"]
                                            if tipo_producto == "plate":
                                                precio_producto = x5["price"] 
                                                cantidad = x5["quantity"]
                                                stock =x5["stock"]
                                                precio_con_iva = float(precio_producto) * 0.16
                                                precio_total = float(precio_producto) + float(precio_con_iva)
                                                precio_final = round(precio_total,2)  
                                                tipo = "alimento"
                                                #print(nombre_restaurante,nombre_producto,tipo_producto,precio_producto,precio_con_iva,precio_total,precio_final)
                                                plates = Plate(nombre_producto,cantidad,precio_final,stock, tipo_producto, tipo)
                                                alimentos_plate_objeto.append(plates)
                                                total_productos.append(plates)
                                                #print(preparado.mostrar_preparacion())

                for x in datos_estadios:
                    for x2,y in x.items():
                        if x2 == "restaurants":
                            inventarioind = []
                            for x3 in y:
                                nombre_restaurante = x3["name"]
                                for x4,y2 in x3.items():
                                    if x4 == "products":
                                        for x5 in y2:
                                            nombre_producto = x5["name"]
                                            tipo_producto = x5["adicional"]
                                            if tipo_producto == "package":
                                                precio_producto = x5["price"] 
                                                cantidad = x5["quantity"]
                                                stock =x5["stock"]  
                                                precio_con_iva = float(precio_producto) * 0.16
                                                precio_total = float(precio_producto) + float(precio_con_iva)
                                                precio_final = round(precio_total,2)
                                                tipo = "alimento"
                                                #print(nombre_restaurante,nombre_producto,tipo_producto,precio_producto,precio_con_iva,precio_total,precio_final)
                                                packagee = Package(nombre_producto,cantidad, precio_final, stock,tipo_producto,tipo)
                                                alimentos_package_objeto.append(packagee)
                                                total_productos.append(packagee)
                                                #print(empacado.mostrar_empaque())

                option = input("""Desea buscar productos por: 
[1] » Nombre 
[2] » Tipo
[3] » Rango de Precio """)
                if option.isnumeric() == False:
                    option = input(""""Desea buscar productos por:
[1] » Nombre 
[2] » Tipo
[3] » Rango de Precio""")
                else:
                    option = int(option)
                    if option ==1:
                        for x in total_productos:
                            print(x.mostrar_producto())
                        contador = 0
                        while True:
                            try:
                                nombre = input("Ingrese el nombre del producto que desea buscar: ")
                                break
                            except:
                                print("Error")
                        
                        for x in total_productos:
                            if x.nombre == nombre:
                                contador += 1
                                print(x.mostrar_producto())
                                print("\nProducto encontrado con exito!! \n")
                        
                        if contador == 0:
                            print("No se encontro el producto")

                    elif option ==2:
                        for x in total_productos:
                            print(x.mostrar_producto())
                        contador = 0
                        while True:
                            try:
                                tipe = input("Ingrese el tipo del producto que desea buscar: ")
                                break
                            except:
                                print("Error")
                        
                        for x in total_productos:
                            if x.tipo == tipe:
                                contador += 1
                                print(x.mostrar_producto())
                                print("\nTipo de producto encontrado con exito!! \n")
                    elif option ==3:
                        # Muestra todos los productos
                        for x in total_productos:
                            print(x.mostrar_producto())

                        contador = 0

                        # Obtén el precio mínimo
                        while True:
                            try:
                                price1 = float(input("Ingrese el precio mínimo: "))
                                break
                            except ValueError:
                                print("Error: Por favor, ingrese un número válido para el precio mínimo.")

                        # Obtén el precio máximo
                        while True:
                            try:
                                price2 = float(input("Ingrese el precio máximo: "))
                                if price2 < price1:
                                    raise ValueError("El precio máximo no puede ser menor que el precio mínimo.")
                                break
                            except ValueError as e:
                                print(f"Error: {e}")

                        # Filtra y muestra los productos dentro del rango de precios
                        for x in total_productos:
                            try:
                                precio = float(x.precio)
                                if price1 <= precio <= price2:
                                    contador += 1
                                    print(x.mostrar_producto())
                            except ValueError:
                                print(f"Error: El precio del producto '{x.nombre}' no es válido.")
                                print("\nRango de precio de productos encontrado con exito!! \n")

            elif gestion == 5:
                print("Gestión de venta de restaurantes")
                cedula = input("Ingrese su cedula")
                cont = 0
                cont1 = 0
                for x in clientes:
                    if x.cedula == cedula:
                        cont+=1
                        if x.tipo_entrada == "vip":
                            cont1 +=1
                            name = x.nombre
                            cedu=x.cedula
                            ed= x.edad
                            entrad = x.tipo_entrada
                            codticket = x.codigoticket
                            asien = x.asientos
                            print(name,cedu,ed,entrad,codticket,asien)
                    else:
                        cont = cont
                        cont1 = cont1
                if cont ==0:
                    print("No se encontro el cliente")
                elif cont1 ==0:
                    print("Su ticket no es vip, y por ende no es posible acceder al restaurante")
                else:
                    print("╠══════════════════════════Bienvenido al restaurante para clientes vip══════════════════════════╣")
                    precio = 0
                    carrito = []
                    total_restaurante_vip =0
                    print (total_productos)
                    while True:
                        try:
                            i = 1
                            for x in total_productos:
                                print(i)
                                print(x.mostrar_producto())
                                i += 1
                            prod = int(input("Ingrese el numero del producto que desee comprar: "))
                            quit = total_productos[prod-1]
                            print(quit.mostrar_producto())
                            carrito.append(quit)
                            precio += int(quit.precio)
                            total_productos.pop(prod-1)

                            opcion = input("""Desea ordenar otro producto?
                            1. Si
                            2. No
                            """)
                            if opcion == "2":
                                break
                        except:
                            print("Error")
                    for x in carrito:
                        print(x.mostrar_producto())
                    compra = input("Desea proceder con la compra \n[1] » Si \[2] » No")
                    if compra.isnumeric()==False:
                        compra = input("Desea proceder con la compra \n[1] » Si \[2] » No")
                    else: 
                        compra = int(compra)
                        if compra ==1:
                            cedula = int(cedula)
                            if es_numero_perfecto(cedula) == True:
                                print("Su cedula es un numero perfecto, por ende obtiene un descuento de 15%")
                                descuento = True
                                monto_total = precio * 0.15
                            else: 
                                print("Su cedula no es un numero perfecto, por ende no hay descuento")
                                monto_total = precio
                                descuento = False
                            print("Compra exitosa")
                            print(precio)
                            print(f"""Detalles Compra: 
                            Subtotal: {precio}
                            Descuento: {descuento}
                            Total: {monto_total}
                            """)
                            total_restaurante_vip+=int(monto_total)
                        else:
                            break 
            elif gestion ==6:
                print("Indicadores de gestión")
                estadistica = input("""Ingrese la gestión a la que desea acceder
        [1] » ¿Cuál es el promedio de gasto de un cliente VIP en un partido ticket +restaurante?
        [2] » Mostrar tabla con la asistencia a los partidos de mejor a peor, mostrando el  nombre del partido nombre de los equipos, estadio en donde se juega, boletos vendidos, personas que asistieron y la relación asistencia/venta
        [3] » ¿Cuál fue el partido con mayor asistencia?                
        [4] » ¿Cuál fue el partido con mayor boletos vendidos?
        [5] » Top 3 productos más vendidos en el restaurante.
        [6] » Top 3 de clientes (clientes que más compraron boletos) """)
                if estadistica ==1:
                    promedio_gasto_vip= (monto_tickets_vip + total_restaurante_vip)/2
                    print(f"{promedio_gasto_vip}")
                elif estadistica ==2:
                    partidos.sort(key=lambda x: x.codigos_usados, reverse=True)
                    for x in partidos:
                        print(x.show_partido())
                elif estadistica ==3:
                    partidos.sort(key=lambda x: x.codigos_usados, reverse=True)
                    print(partidos[0].show_partido())
                elif estadistica ==4:
                    partidos.sort(key=lambda x: x.precio_total, reverse=True)
                    print(partidos[0].show_partido())
                elif estadistica ==5: 
                    total_productos.sort(key=lambda x: x.cantidad, reverse=True)
                    for x in total_productos:
                        print(x.mostrar_producto())
                elif estadistica ==6:
                    clientes.sort(key=lambda x: x.tipo_entrada, reverse=True)
                    for x in clientes:
                        print(x.mostrar_cliente()) 
                else: 
                    break
            else: 
                break 

main()