import time as t , analisis as a, colores as c, os, datos as d, numpy as np
import multiprocessing


lista_contenido = []
lista_html = []

def main():


    while(True):
        os.system("clear")

        print(c.CRED+"""
        =============================
                BIENVENIDO \U0001f44b    
        -----------------------------                         
        1. Analizar Sitios Webs \U0001f50d
        -----------------------------
        2. Ver Datos \U0001f4c4
        -----------------------------
        3. Salir \U0001f6aa
        ============================
        """+c.CEND)


        op = input(c.CYELLOW+"Elija un opcion: "+c.CEND);


        if(op == "1"):
            #Limpia Consola
            os.system("clear")
            global lista_contenido, lista_html

            print(c.CITALIC+c.CRED+"Realizando Peticiones....."+c.CEND)

            inicio_mul = t.time()
            lista_contenido = a.contenido_peticion_mp(d.sitios_webs)
            fin_mul = t.time()
            print(c.CGREENBG+"Duración CON multiprocessing: \u231B "+ str(fin_mul-inicio_mul)+c.CEND)
            print(c.CYELLOW+"--------------------------------------------------------"+c.CEND)

            i = t.time()
            a.obtener_contenido_secuencial(d.sitios_webs)
            f = t.time()
            print(c.CGREENBG+"Duración SIN multiprocessing: \u231B "+ str(f-i)+c.CEND )
            
            print(c.CYELLOW+"--------------------------------------------------------"+c.CEND)           

            input(c.CREDBG2+c.CWHITE2+'Presione ENTER para continuar...'+c.CEND)

                   

        elif(op == "2"):
            os.system("clear")
        
        elif(op == "3"):
            break;


    

if __name__ == "__main__":
    main()
