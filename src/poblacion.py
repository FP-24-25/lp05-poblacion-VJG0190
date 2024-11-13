from collections import namedtuple
import matplotlib.pyplot as plt
from random import random
import csv
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')
def lee_poblaciones(ruta_poblaciones:str)->list[RegistroPoblacion]:
    """Pasar los datos del archivo csv a una lista de tuplas

    :param ruta_poblaciones: Ruta del archivo csv con los datos de poblacion
    :type ruta_poblaciones: str
    :return:    Lista de tuplas con los datos de poblacion
    :rtype: list[RegistroPoblacion]
    """
    lista_registro_poblaciones= set()
    with open(ruta_poblaciones,encoding='utf-8') as f:
        lectorcsv = csv.reader(f)
        for l in lectorcsv:
            pais= l[0].strip() #En el documento csv, en el primer elemento hay veces que hay espacios que no dejan funcionar al codigo de normal.
            codigo = l[1]
            año = int(l[2])
            censo = int(l[3])
            regPoblacion = RegistroPoblacion(pais,codigo,año,censo)
            lista_registro_poblaciones.add(regPoblacion)
    return lista_registro_poblaciones

def calcula_paises(poblaciones):
    poblaciones = lee_poblaciones(poblaciones)
    paises= set()
    for f in poblaciones:
        pais= f[0]
        paises.add(pais)
    return sorted(paises)     


def filtra_por_pais(poblaciones,nombre_o_codigo):
    poblaciones = lee_poblaciones(poblaciones)
    datos_pais=list()
    for f in poblaciones:
        if f[0]  or f[1] == nombre_o_codigo:
            datos_pais.append([f[2],f[3]])
    return datos_pais

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    poblaciones = lee_poblaciones(poblaciones)
    datos_pais=list()
    for f in poblaciones:
        if f[0] == paises and f[2] == (anyo - 1):
            datos_pais.append([f[0],f[3]])
            
    return datos_pais

def muestra_evolucion_poblacion(poblaciones,nombre_o_codigo):
    poblaciones = lee_poblaciones(poblaciones)
    lista_años = list()
    lista_habitantes=list()
    for f in poblaciones:
        if  f[0] == nombre_o_codigo or f[1] == nombre_o_codigo:
            lista_años.append(f[2])
            lista_habitantes.append(f[3])
    if lista_años and lista_habitantes:
        plt.title(f"Evolución de la población: {nombre_o_codigo}")
        plt.plot(lista_años, lista_habitantes,)
        plt.show()
    else:
        print(f"No se encontraron datos para {nombre_o_codigo}.")        
           
def aux_lista_paises_azar():
    poblaciones = lee_poblaciones(poblaciones)
    paises=calcula_paises(poblaciones)
    return   random.sample(paises, 5)

def muestra_comparativa_paises_anyo(poblaciones,paises,anyo):
    poblaciones = lee_poblaciones(poblaciones)
    paises= sorted(set(paises))
    poblacion_por_pais = dict()
    #Voy a crear un diccionario para que el pais y los habitantes vayan en el mismo orden y les doy el valor 0 antes de añadir los habitantes desde poblaciones
    for pais in paises:                 
        poblacion_por_pais[pais] = 0 
    for f in poblaciones:
        if f[2] == anyo and f[0] in poblacion_por_pais:
            poblacion_por_pais[f[0]] = f[3]
    lista_habitantes = []
    for pais in paises:
        lista_habitantes.append(poblacion_por_pais[pais])
    
    plt.title("Grafica")
    plt.bar(paises, lista_habitantes)
    plt.show() 

            