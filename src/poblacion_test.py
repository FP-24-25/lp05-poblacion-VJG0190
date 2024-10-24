from poblacion import *
def test_lee_poblaciones(lista_poblaciones):
     print("Lista de poblaciones")
     print(lista_poblaciones)
def test_calcula_paises(poblaciones):
     print('Los paises censados son: ')
     print(poblaciones)



if __name__ == '__main__':
    var ='data/population.csv'
    #print(test_lee_poblaciones(lee_poblaciones(var)))
    print(test_calcula_paises(calcula_paises(var)))
     

    