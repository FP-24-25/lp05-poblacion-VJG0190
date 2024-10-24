from poblacion import *
def test_lee_poblaciones(lista_poblaciones):
     print("Lista de poblaciones")
     print(f"Se han censado {len(lista_poblaciones)}")
     lista = list(lista_poblaciones)
     print(f"Las dos primeras son{lista[:2]}")
     print(f"Las dos ultimas  son{lista[-2:]}")
def test_calcula_paises(poblaciones):
     print(f'Se han censado {len(poblaciones)}')
     lista = list(poblaciones)
     print(f"Las dos primeras son{lista[:2]}")
     print(f"Las dos ultimas  son{lista[-2:]}")
def test_filtra_por_pais(poblaciones):
     print("Los datos del pais elegido son: ")
     print(poblaciones)
def test_filtra_por_paises_y_anyo(poblaciones):
     print("Los datos del pais elegido para el año anterior al elegido son: ")
     print(poblaciones)


if __name__ == '__main__':
    var ='data/population.csv'
    #print(test_lee_poblaciones(lee_poblaciones(var)))
    #print(test_calcula_paises(calcula_paises(var)))
    print(test_filtra_por_pais(filtra_por_pais(var,"Panama")))
    #print (test_filtra_por_pais(filtra_por_pais(var,"PAN"))) #Deberia salir lo mismo que en el de arriba
    #print(test_filtra_por_paises_y_anyo(filtra_por_paises_y_anyo(var,1982,"Panama")))
    