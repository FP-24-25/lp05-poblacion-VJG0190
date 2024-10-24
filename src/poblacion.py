from collections import namedtuple
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
        if f[0] == nombre_o_codigo or f[1] == nombre_o_codigo:
            datos_pais.append([f[2],f[3]])
    return datos_pais

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    datos_pais=list()
    for f in poblaciones:
        if f[0] == paises and f[2] == (anyo - 1):
            datos_pais.append([f[0],f[3]])
            
    return datos_pais