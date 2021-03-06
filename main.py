from src.Acceso_a_datos.conexion_bd import conexion_bd
from src.Acceso_a_datos.extraccion_datos import extraccion_datos
from src.Logica_python.conversion import conversion_md
from src.Logica_python.filter import high_filter, low_filter, medium_filter
from src.Logica_python.lanzar_hugo import iniciar_hugo


def main():
    ##### CONEXIÓN CON LA BBDD #####

    # Defino una variable a la que le asigno la funcion que devuelve la coleccion de la BBDD.
    coleccion = conexion_bd()
    # Defino una variable a la que le asigno la funcion que devuelve una lista de diccionarios.
    lista = extraccion_datos(coleccion)

    ##### FILTRO POR VALORACIÓN #####

    # Devuelve la lista principal filtrada por valoracion.
    bajo = low_filter(lista)
    medio = medium_filter(lista)
    alto = high_filter(lista)

    ##### CONVERSION A MD #####

    # Les pasa las listas filtradas para que las convierta a 3 MARKDOWNS diferentes.
    conversion_md(bajo, "baja")
    conversion_md(medio, "media")
    conversion_md(alto, "alta")
    iniciar_hugo() #Inicia el servidor y habre el la pagina en el  navegador predeterminado.

if __name__ == '__main__':
    main()