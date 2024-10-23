from collections import namedtuple
import csv
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')
def lee_poblaciones(ruta_poblaciones):
    lista_registro_poblaciones= []
    with open(ruta_poblaciones,encoding='utf-8'):
        lectorcsv = csv.reader(ruta_poblaciones)
        for l in lectorcsv:
            pais= l[0]
            codigo = l[1]
            año = int(l[2])
            censo = int(l[3])
            regPoblacion = RegistroPoblacion(pais,codigo,año,censo)
            lista_registro_poblaciones.append(regPoblacion)
    return lista_registro_poblaciones
