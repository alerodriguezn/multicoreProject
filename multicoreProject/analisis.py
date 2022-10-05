
from curses import meta
from multiprocessing import Pool

from bs4 import BeautifulSoup


def obtenerMetadata(sitio):
    
    lista = []
    metadata = ""
    url = sitio.url
    lista.append(url)
    contenido = BeautifulSoup(sitio.content,"html.parser")

    keywords = str(contenido.find(attrs={'name':'keywords'}))
    if (keywords != None):
        metadata = keywords
    descrip_name = str(contenido.find(attrs={'name':'Description'}))
    if (keywords != None):
        metadata += " "+descrip_name
    descrip_prop = str(contenido.find(attrs={'property':'og:description'}))
    if (keywords != None):
        metadata += " "+descrip_prop

    lista.append(metadata)

    return lista


def obtenerMetadata_mp(lista_contenido):
    "Funcion que ejecuta una funcion para obtener el contenido de un sitio web utilizando multiprocessing"
    m = Pool()
    resultado = m.map(obtenerMetadata,lista_contenido)
    m.close
    m.join
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
