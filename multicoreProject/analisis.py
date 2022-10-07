
from curses import meta
from multiprocessing import Pool
import keywords as k
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
    if (descrip_name != None):
        metadata += " "+descrip_name
    descrip_prop = str(contenido.find(attrs={'property':'og:description'}))
    if (descrip_prop != None):
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


# Palabras Claves (tupla) Tupla con las palabras a validar en nuestras categorias existentes.
def encontrarPalabrasCategorias(lista_metadata_sitio):
    lista_resultados = []
    
    for metadata_sitio in lista_metadata_sitio:
        # Este diccionario contiene las categorias y la cantidad de palabras que se encuentran de ellas.
        diccionarioCategoria = {"comercio_electronico":0, "servicios_streaming":0, "tienda_ropa":0}

        # Contamos la cantidad palabras encontradas en cada categoria
        for key ,value in k.palabras_claves.items():
            for i in value:
                if i in metadata_sitio[1]:
                    diccionarioCategoria[key]+=1

        # Recorremos el resultado y retornamos la categoria dominante segun la cantidad de palabras
        mayor = 0
        categoriaDominante = "Otros"
        for key, value in diccionarioCategoria.items():
            if value > mayor:
                categoriaDominante = key
                mayor = value
        #print([metadata_sitio[0],categoriaDominante])
        res = []
        res.append(metadata_sitio[0])
        res.append(categoriaDominante)
        lista_resultados.append(res)
    return lista_resultados

# print("La categoria dominante es: "+encontrarPalabrasCategorias(("ropa","shoes","camisas","juegos","series","novela","pantalones")))
# print("Resultados (Diccionario): ")
# print(diccionarioCategoria)

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
