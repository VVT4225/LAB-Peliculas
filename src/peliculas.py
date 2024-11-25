import csv
from collections import namedtuple
from datetime import *

Pelicula = namedtuple("Pelicula","fecha_estreno,titulo,director,generos,duracion,presupuesto,recaudacion,reparto")

def parse_fecha(fecha):
    return datetime.strptime(fecha,"%d/%m/%Y")

def parse_lista(lista):
    partes = lista.split(",")
    return [i.strip() for i in partes]

def lee_peliculas(fichero):
    res = []
    with open(fichero,encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for fecha_estreno,titulo,director,generos,duracion,presupuesto,recaudacion,reparto in lector:
            res.append(Pelicula(parse_fecha(fecha_estreno),titulo,director,parse_lista(generos),int(duracion),int(presupuesto),int(recaudacion),parse_lista(reparto)))
    return res

def pelicula_mas_ganancias(datos,genero="None"):
    max_ganancia = 0
    max_titulo = ""
    if genero == "None":
        for i in datos:
            if i.recaudacion >= max_ganancia:
                max_ganancia = i.recaudacion
                max_titulo = i.titulo
    else:
        for i in datos:
            if genero in i.generos:
                if i.recaudacion >= max_ganancia:
                    max_ganancia = i.recaudacion
                    max_titulo = i.titulo
    return((max_titulo,max_ganancia))
    