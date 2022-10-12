from exceptiongroup import catch
import requests
import datos as d
from bs4 import BeautifulSoup
from multiprocessing import Pool
import colores as c
import main as m
import time as t
 

# Variables y listas globales
lista_contenido = []

def obtener_contenido_secuencial(lista_sitios_web):
    "Funcion que obtiene el contenido de los sitios webs de forma secuencial"
    global lista_contenido
    for ws in lista_sitios_web:
        lista_contenido.append(requests.get(ws))
    return lista_contenido

def contenido_peticion(lista_sitios_web):
    """
    Realiza una peticion a un sitio web y retorna el contenido
    """
    try:
        return requests.get(lista_sitios_web,verify=False, allow_redirects=False, stream=True,timeout=10)
    except:
        return "error"

      

def contenido_peticion_mp(lista_sitios_web,pc):
    "Funcion que ejecuta una funcion para obtener el contenido de un sitio web utilizando multiprocessing"
    p = Pool(processes=pc)
    resultado = p.map(contenido_peticion,lista_sitios_web)
    p.close
    p.join
    return resultado