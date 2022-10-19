#pip install bs4
import time as t , peticiones as p, colores as c, os, datos as d, numpy as np, analisis as a,grafico as g, tabla as tb,gui as gui
import multiprocessing


lista_contenido = []
lista_html = []
lista_metadata = []
diccionarioResultados = {}
procesos = 0

def limpiarDatos():
    global lista_contenido,lista_metadata,lista_html, diccionarioResultados
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
        5. Ver Tabla con los Datos Obtenidos\U0001f4c3
        -----------------------------
        0. Salir \U0001f6aa
        ============================
        """+c.CEND)


        op = input(c.CYELLOW+"Elija un opcion: "+c.CEND);


        if(op == "1"):
            #Limpia Consola
            global procesos
            limpiarDatos()
            os.system("cls")
            global lista_contenido, lista_html

            procesos = int(input(c.CYELLOW+"Cantidad de Procesos \U0001f477:  "+c.CEND))

            if(procesos<24):

                print(c.CITALIC+c.CRED+"Realizando Peticiones....."+c.CEND)

                #i = t.time()
                #p.obtener_contenido_secuencial(d.sitios_webs)
                #f = t.time()
                #print(c.CGREENBG+"Duración SIN multiprocessing: \u231B "+ str(f-i)+c.CEND )
                
                print(c.CYELLOW+"--------------------------------------------------------"+c.CEND)   

                inicio_mul = t.time()
                lista_contenido = p.contenido_peticion_mp(d.sitios_webs,procesos)
                pass
        
                fin_mul = t.time()
                print(c.CGREENBG+"Duración CON multiprocessing: \u231B "+ str(fin_mul-inicio_mul)+c.CEND)
                print(c.CYELLOW+"--------------------------------------------------------"+c.CEND)        

                input(c.CREDBG2+c.CWHITE2+'Presione ENTER para continuar...'+c.CEND)
            else:
                print(c.CREDBG2+c.CWHITE2+'Cantidad de procesos No Validos'+c.CEND)
                print(c.CYELLOW+"-------------------------------------------------"+c.CEND)        
                input(c.CREDBG2+c.CWHITE2+'Presione ENTER para continuar...'+c.CEND)


        elif(op == "2"):
            os.system("cls")
            global lista_metadata

            lista_metadata = [] #Se asegura de que antes este limpia
            lista_metadata = a.obtenerMetadata_mp(lista_contenido)
            print("Metadatos de los Sitios Web encontrados correctamente! \u2705")
            input(c.CREDBG2+c.CWHITE2+'Presione ENTER para continuar...'+c.CEND)
            pass
        
        elif(op == "3"):
            global diccionarioResultados
            i = t.time()
            diccionarioResultados = {} #Se asegura de que antes este limpia
            diccionarioResultados = a.encontrarPalabrasCategorias(lista_metadata)
            f = t.time()
            
            print(c.CGREENBG+"Duración: \u231B "+ str(f-i)+c.CEND )
            
            print(c.CYELLOW+"--------------------------------------------------------"+c.CEND)       

            print("Analisis de los Metadatos de los Sitios Web realizado correctamente! \u2705")
            input(c.CREDBG2+c.CWHITE2+'Presione ENTER para continuar...'+c.CEND)
            

        elif(op == "4"):
            g.generarGrafico(diccionarioResultados)

        elif(op =="5"):
            tb.generarTabla(diccionarioResultados)
            gui.desplegarGUI()
            input(c.CREDBG2+c.CWHITE2+'Presione ENTER para continuar...'+c.CEND)

            

if __name__ == "__main__":
    main()
