#pip install bs4
import time as t , peticiones as p, colores as c, os, datos as d, numpy as np, analisis as a,grafico as g
import multiprocessing



lista_contenido = []
lista_html = []
lista_metadata = []
diccionarioResultados = {}

def main():


    while(True):
        os.system("cls")

        print(c.CRED+"""
        =============================
                BIENVENIDO \U0001f44b    
        -----------------------------                         
        1. Obtener Contenido de los Sitios Web \U0001f50d
        -----------------------------
        2. Obtener Metadatos de los Sitios Web \U0001f50d
        -----------------------------
        3. Analizar Metadatos \U0001f52c
        -----------------------------
        4. Ver Datos Obtenidos\U0001f4c4
        -----------------------------
        0. Salir \U0001f6aa
        ============================
        """+c.CEND)


        op = input(c.CYELLOW+"Elija un opcion: "+c.CEND);


        if(op == "1"):
            #Limpia Consola
            os.system("cls")
            global lista_contenido, lista_html

            print(c.CITALIC+c.CRED+"Realizando Peticiones....."+c.CEND)

            #i = t.time()
            #p.obtener_contenido_secuencial(d.sitios_webs)
            #f = t.time()
            #print(c.CGREENBG+"Duración SIN multiprocessing: \u231B "+ str(f-i)+c.CEND )
            
            print(c.CYELLOW+"--------------------------------------------------------"+c.CEND)   

            inicio_mul = t.time()
            lista_contenido = p.contenido_peticion_mp(d.sitios_webs)
            pass
    
            fin_mul = t.time()
            print(c.CGREENBG+"Duración CON multiprocessing: \u231B "+ str(fin_mul-inicio_mul)+c.CEND)
            print(c.CYELLOW+"--------------------------------------------------------"+c.CEND)        

            input(c.CREDBG2+c.CWHITE2+'Presione ENTER para continuar...'+c.CEND)

                   

        elif(op == "2"):
            os.system("cls")
            global lista_metadata

            lista_metadata = a.obtenerMetadata_mp(lista_contenido)
            print("Metadatos de los Sitios Web encontrados correctamente!")
            input(c.CREDBG2+c.CWHITE2+'Presione ENTER para continuar...'+c.CEND)
            pass
        
        elif(op == "3"):
            global diccionarioResultados

            i = t.time()
            diccionarioResultados = a.encontrarPalabrasCategorias(lista_metadata)
            f = t.time()
            
            print(c.CGREENBG+"Duración SIN multiprocessing: \u231B "+ str(f-i)+c.CEND )
            
            print(c.CYELLOW+"--------------------------------------------------------"+c.CEND)       

            print("Analisis de los Metadatos de los Sitios Web realizado correctamente!")
            input(c.CREDBG2+c.CWHITE2+'Presione ENTER para continuar...'+c.CEND)
            

        elif(op == "4"):
            g.generarGrafico(diccionarioResultados)

            

if __name__ == "__main__":
    main()
