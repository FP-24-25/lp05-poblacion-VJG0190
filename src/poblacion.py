from collections import namedtuple
import csv
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')
def lee_poblaciones(ruta_poblaciones):
    lista_registro_poblaciones= []
    with open(ruta_poblaciones,encoding='utf-8') as f:
        lectorcsv = csv.reader(f)
        for l in lectorcsv:
            pais= l[0].strip() #En el documento csv, en el primer elemento hay veces que hay espacios que no dejan funcionar al codigo de normal.
            codigo = l[1]
            año = int(l[2])
            censo = int(l[3])
            regPoblacion = RegistroPoblacion(pais,codigo,año,censo)
            lista_registro_poblaciones.append(regPoblacion)
    return lista_registro_poblaciones

def calcula_paises(poblaciones):
    poblaciones = lee_poblaciones(poblaciones)
    paises=list()
    for f in poblaciones:
        pais= f[0]
        paises.append(pais)
    return sorted(paises)     

