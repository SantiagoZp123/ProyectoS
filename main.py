from Equipos import Equipos
from Estadios import Estadios
from Partidos import Partidos
from Cliente import Cliente

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

def crearEstadio(nombre, ubicacion, estadio, estadios_objeto):
    nuevo_estadio = Estadios(nombre, ubicacion, estadio)
    estadios_objeto.append(nuevo_estadio)

def crear_mapa(filas,columnas):
    '''
    
    Funcion que genera el mapa de los puestos Vip y General.
    
    '''
    mapa=[]
    for y in range(filas):
        aux=[]
        for x in range(columnas):
            aux.append(False)
        mapa.append(aux)
    return mapa

def codigoAleatorio(item):
    identificador = format(id(item), 'x')
    return identificador

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

def mapa(fila,columna):
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

def main():
    equipos_objeto = []
    equipos = []
    estadios_objeto = []
    estadios = []
    partidos_objeto = []
    partidos = []
    codigos =[]
    producto =[]
    clientes =[]
    monto_tickets_vip =0
    cedulas_vip=[]
    
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
                    [1] » Buscar constructor por país
                    [2] » Buscar pilotos por constructor
                    [3] » Buscar las carreras por país del circuito
                    [4] » Buscar las carreras que ocurran en un mes
                    [5] » Finalizar Carrera
                    [6] » Finalizar Temporada
                    [7] » Regresar """)

                    if busqueda.isnumeric()== False or int(busqueda)>8:
                        print ("Ingresa una opción válida: ")
                    else:
                        busqueda = int(busqueda)
                        if busqueda==1:
                            print("Hola")
                        elif busqueda ==2:
                            print("Hola")
                        elif busqueda ==3:
                            print("Hola")
                        elif busqueda ==4:
                            print("Hola")
                        elif busqueda ==5:
                            break
            elif gestion ==2:
                print("░░░░░░░░░░░░░░░░░░░░░ Seccion de venta de entradas ░░░░░░░░░░░░░░░░░░░░░")
                opcion = input("""Usted desea realizar una compra
                [1] » Si 
                [2] » No""")
                if opcion.isnumeric() == False or int(opcion)>2:
                    print("Por favor ingrese una opción válida")
                else: 
                    opcion = int(opcion)
                    if opcion == 1:
                        lista_generales = []
                        lista_vip =[]
                        for x in datos_estadios:
                            nombre = x["name"]  
                            for x2,y in x.items():
                                if x2 == "capacity":
                                    general =y[0]
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
                        """buscarCarreras(carreras_objeto)"""
                        cantidad_entradas = input("Ingrese la cantidad de entradas a comprar: ")
                        while not cantidad_entradas.isnumeric():
                            cantidad_entradas = input("Ingrese una cantidad de entradas válida:")
                        for x in carreras_objeto:
                            print(x.mostrar_carrera())
                        tipo_entrada = input("""Ingrese el tipo de entrada que desea adquirir: 
[1] » General
[2] » Vip """)
                        if tipo_entrada == "1":
                            asientos_c=[]
                            precio_general = 150.00
                            option = int(input("Ingrese el numero de la carrera que desea comprar: "))
                            print("--------------------------------------------------------------------------------------------------------------")
                            print(f"A continuación se muestra la lista de entradas disponible de la forma [Fila,Columna] --> {lista_vip[option]} ")
                            print("--------------------------------------------------------------------------------------------------------------")
                            i=lista_vip[option][0]
                            j=lista_vip[option][1]
                            """print(i)
                            print(j)"""
                            mapa = crear_mapa(i,j)
                            print(f"                                 ╔ Mapa Carrera {option} ╗                                                   ")
                            print(mapa)
                            print("--------------------------------------------------------------------------------------------------------------")
                            
                            for i in range(int(cantidad_entradas)):    
                                while True:
                                    try:
                                        mapa

                                        fila = input("Seleccione la fila:")
                                        while fila==False:
                                            fila =input("Seleccione otro asiento, ya que el seleccionado no se encuentra disponible: ")
                                        columna = input("Seleccione la columna")
                                        while columna==False:
                                            columna =input("Seleccione otro asiento, ya que el seleccionado no se encuentra disponible: ")
                                        mapa[int(fila)-1][int(columna)-1] = True

                                        print("\n Aviso: Los puestos ocupados contienen True, por favor selecciona los que no estan ocupados\n")
                                        print(mapa)

                                        asiento = (f"F{fila}C{columna} ")
                                        asientos_c.append(asiento)
                                        break
                                    except:
                                        print("33")
                                        
                            codigo_ticket = codigoAleatorio(nombre)
                            iva =0.16
                            monto = float(cantidad_entradas)*precio_general
                            
                            if numeroOndulado(cedula) == True:
                                ("Su cedula es un numero ondulado, por ende obtiene un descuento en la compra de sus entradas")
                                monto_descuento = monto*0.50
                                monto_d = monto - monto_descuento
                                monto_con_iva= monto_d * 0.16
                                monto_total = float(monto_d) + float(monto_con_iva) 
                            else:
                                monto_con_iva = float(monto)*0.16
                                monto_descuento = "No"
                                print("Su cedula no es un numero ondulado, por ende no hay descuento")
                                monto_total = float(monto) + float(monto_con_iva)
                            print(f"""Detalles compra:
                            Asientos: {asientos_c} 
                            Código: {codigo_ticket}
                            Subtotal: {monto}
                            Descuento: {monto_descuento}
                            Iva: {iva}
                            Total: {monto_total}
                            
                            """)
                            compra = input("Desea proceder a comprar la entrada \n[1] » Si \[2] » No")
                            if compra.isnumeric()==False:
                                compra = input("Desea proceder a comprar la entrada \n[1] » Si \[2] » No")
                            else: 
                                compra = int(compra)
                                if compra ==1:
                                    print("Compra exitosa")
                                    codigos.append(codigo_ticket)
                                    entrada = "general"
                                    cliente = Cliente(nombre,cedula,edad,entrada, codigo_ticket,asientos_c)
                                    clientes.append(cliente)
                                    print(cliente.mostrar_cliente())
                                else:
                                    break 

                        elif tipo_entrada == "2":
                            asientos_c =[]
                            entrada = "vip"
                            precio_vip = 340.00
                            #print(lista_vip)
                            option = int(input("Ingrese la ronda de la carrera a comprar: "))
                            print("--------------------------------------------------------------------------------------------------------------")
                            print(f"A continuación se muestra la lista de entradas disponible de la forma [Fila,Columna] --> {lista_vip[option]} ")
                            print("--------------------------------------------------------------------------------------------------------------")
                            i=lista_vip[option][0]
                            j=lista_vip[option][1]
                            """print(i)
                            print(j)"""
                            mapa = crear_mapa(i,j)
                            print(f"                                 ╔ Mapa Carrera {option} ╗                                                   ")
                            print(mapa)
                            print("--------------------------------------------------------------------------------------------------------------")
                            
                            for i in range(int(cantidad_entradas)):
                                while True:
                                    try:
                                        mapa

                                        fila = input("Seleccione la fila:")
                                        while fila==False:
                                            fila =input("Seleccione otro asiento, ya que el seleccionado no se encuentra disponible: ")
                                        columna = input("Seleccione la columna")
                                        while columna==False:
                                            columna =input("Seleccione otro asiento, ya que el seleccionado no se encuentra disponible: ")
                                        
                                        mapa[int(fila)-1][int(columna)-1] = True

                                        print("\n Aviso: Los puestos ocupados contienen True, por favor selecciona los que no estan ocupados\n")
                                        print(mapa)

                                        asiento = (f"F{fila}C{columna} ")
                                        asientos_c.append(asiento)
                                        break
                                    except:
                                        print("33")

                            #montos_tickets_vip += monto_total_vip
                            #while i in range(cantidad_entradas) lo itero la cantidad de veces que compra la entrada 
                            codigo_ticket = codigoAleatorio(nombre)
                            iva =0.16
                            monto = float(cantidad_entradas)*precio_vip
                           
                            if numeroOndulado(cedula) == True:
                                print("Su cedula es un numero ondulado, por ende obtiene un descuento en la compra de sus entradas")
                                monto_descuento = monto *0.50
                                monto_d = monto-monto_descuento
                                monto_con_iva = float(monto_d)*0.16
                                monto_total_vip = float(monto) + float(monto_con_iva)-monto_descuento
                            else: 
                                print("Su cedula no es un numero ondulado, por ende no hay descuento")
                                monto_descuento = "No"
                                monto_con_iva = float(monto)*0.16
                                monto_total_vip = float(monto) + float(monto_con_iva)
                            print(f"""Detalles compra:
                            Asientos: {asientos_c} 
                            Código: {codigo_ticket}
                            Subtotal: {monto}
                            Descuento: {monto_descuento}
                            Iva: {iva}
                            Total: {monto_total_vip}
                            
                            """)
                            compra = input("Desea proceder a comprar la entrada \n[1] » Si \[2] » No")
                            if compra.isnumeric()==False:
                                compra = input("Desea proceder a comprar la entrada \n[1] » Si \[2] » No")
                            else: 
                                compra = int(compra)
                                if compra ==1:
                                    print("Compra exitosa")
                                    codigos.append(codigo_ticket)
                                    cedulas_vip.append(cedula)
                                    cliente = Cliente(nombre,cedula,edad,entrada, codigo_ticket,asientos_c)
                                    clientes.append(cliente)
                                    print(cliente.mostrar_cliente())
                                else:
                                    break 
                            with open("clientesvip.txt", "w") as f:
                                f.write(nombre,cedula,edad,entrada,codigo_ticket,asientos_c)
            elif opcion == 2:
                print ("Gracias por su visita")
                break

main()