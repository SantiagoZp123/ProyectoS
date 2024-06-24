from Equipos import Equipos
from Estadios import Estadios
from Partidos import Partidos
from Cliente import Cliente

import requests
import json


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
    print("Hola")
main()