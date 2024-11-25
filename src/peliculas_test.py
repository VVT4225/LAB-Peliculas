from peliculas import *

if __name__ == "__main__":
    datos = lee_peliculas("data/peliculas.csv")
    #print(datos)
    #print(pelicula_mas_ganancias(datos,"Drama"))
    #print(media_presupuesto_por_genero(datos))
    #print(peliculas_por_actor(datos, 2015, 2024))
    print(actores_mas_frecuentes(datos,3,2015,2024))