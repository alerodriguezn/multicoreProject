#pip install bs4
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
    
    return requests.get(lista_sitios_web)


def contenido_peticion_mp(lista_sitios_web):
    "Funcion que ejecuta una funcion para obtener el contenido de un sitio web utilizando multiprocessing"
    p = Pool()
    resultado = p.map(contenido_peticion,lista_sitios_web)
    p.close
    p.join
    return resultado


def conversionHTML(sitio):
    return BeautifulSoup(sitio.content,"html.parser")


def conversionHTML_mp(lista_contenidos):
    p = Pool()
    resultado = p.map(conversionHTML, lista_contenidos)
    p.close
    p.join
    return resultado


    
    







        



"""
lista_webs=[
requests.get('https://www.netflix.com/us-es/'),
requests.get('https://www.apple.com/la/'),
requests.get('https://www.disneyplus.com/'),
]


lista_contenido = []
#todo el contenido que trae el response hay que convertirlo a HTML con html.parser


for web in lista_webs:
    lista_contenido.append(BeautifulSoup(web.content, "html.parser"))
    
#Aqui se busca el atributo o la etiqueta que se desea
for contenido in lista_contenido:
    #print(contenido.find("h1")) aqui se busca el primero h1(heading/titulo)
    #print(contenido.find_all("h1")) aqui busca todos los h1(heading/titulo)
    print(contenido.find(attrs={'name':'keywords'}))
    print(contenido.find(attrs={'name':'Description'}))

pagina1 = requests.get('https://www.netflix.com/us-es/')
pagina2 = requests.get('https://www.apple.com/la/')
pagina3 = requests.get('https://www.disneyplus.com/')
pagina4 = requests.get('https://www.netflix.com/us-es/')

webpage = pagina1.content
soup = BeautifulSoup(webpage, "html.parser")

print(soup.find(attrs={'name':'keywords'}))
print(soup.find(attrs={'name':'Description'}))

"""
