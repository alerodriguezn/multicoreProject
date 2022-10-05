#pip install bs4
import time as t , peticiones as p, colores as c, os, datos as d, numpy as np, analisis as a
import multiprocessing



lista_contenido = []
lista_html = []
lista_metadata = []

def main():


    while(True):
        os.system("clear")

        print(c.CRED+"""
        =============================
                BIENVENIDO \U0001f44b    
        -----------------------------                         
        1. Obtener Contenido de los Sitios Web \U0001f50d
        -----------------------------
        2. Obtener Metadatos de los Sitios Web \U0001f50d
        -----------------------------
        4. Analizar Metadatos \U0001f52c
        -----------------------------
        5. Ver Datos Obtenidos\U0001f4c4
        -----------------------------
        6. Salir \U0001f6aa
        ============================
        """+c.CEND)


        op = input(c.CYELLOW+"Elija un opcion: "+c.CEND);


        if(op == "1"):
            #Limpia Consola
            os.system("clear")
            global lista_contenido, lista_html

            print(c.CITALIC+c.CRED+"Realizando Peticiones....."+c.CEND)

            i = t.time()
            p.obtener_contenido_secuencial(d.sitios_webs)
            f = t.time()
            print(c.CGREENBG+"Duración SIN multiprocessing: \u231B "+ str(f-i)+c.CEND )
            
            print(c.CYELLOW+"--------------------------------------------------------"+c.CEND)   

            inicio_mul = t.time()
            lista_contenido = p.contenido_peticion_mp(d.sitios_webs)
            pass
    
            fin_mul = t.time()
            print(c.CGREENBG+"Duración CON multiprocessing: \u231B "+ str(fin_mul-inicio_mul)+c.CEND)
            print(c.CYELLOW+"--------------------------------------------------------"+c.CEND)        

            input(c.CREDBG2+c.CWHITE2+'Presione ENTER para continuar...'+c.CEND)

                   

        elif(op == "2"):
            os.system("clear")
            global lista_metadata

            lista_metadata = a.obtenerMetadata_mp(lista_contenido)
            pass
        
        elif(op == "3"):
            break;


    

if __name__ == "__main__":
    main()
