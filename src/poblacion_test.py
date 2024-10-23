from poblacion import *
def test_lee_poblaciones(ruta_poblaciones):
    lista_poblaciones =lee_poblaciones(ruta_poblaciones)
    print("Lista de poblaciones")
    print(lista_poblaciones)



if __name__ == '__main__':
    print(test_lee_poblaciones('data/population.csv'))
    