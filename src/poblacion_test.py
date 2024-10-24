from poblacion import *
def test_lee_poblaciones(lista_poblaciones):
     print("Lista de poblaciones")
     print(lista_poblaciones)
def test_calcula_paises(poblaciones):
     print('Los paises censados son: ')
     print(poblaciones)
def test_filtra_por_pais(poblaciones):
     print("Los datos del pais elegido son: ")
     print(poblaciones)


if __name__ == '__main__':
    var ='data/population.csv'
    #print(test_lee_poblaciones(lee_poblaciones(var)))
    #print(test_calcula_paises(calcula_paises(var)))
    #print(test_filtra_por_pais(filtra_por_pais(var,"Panama")))
    #print (test_filtra_por_pais(filtra_por_pais(var,"PAN"))) #Deberia salir lo mismo que en el de arriba

    