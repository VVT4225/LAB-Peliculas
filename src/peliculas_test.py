from peliculas import *

if __name__ == "__main__":
    datos = lee_peliculas("data/peliculas.csv")
    #print(datos)
    print(pelicula_mas_ganancias(datos,"Drama"))