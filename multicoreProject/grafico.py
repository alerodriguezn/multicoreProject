from matplotlib import pyplot as plt 
import numpy as np 



data= []
res = [0,0,0,0,0,0]
  
def generarGrafico(resultados):
    
    for valor in resultados:
        data.append(valor[1])

    for dato in data:
        if dato == "comercio_electronico":
            res[0]+= 1
        elif dato =="plataforma_peliculas":
            res[1]+= 1
        elif dato =="tienda_ropa":
            res[2]+= 1
        elif dato =="redes_comunicacion":
            res[3]+= 1
        elif dato =="books":
            res[4]+= 1
        elif dato =="Otros":
            res[5]+= 1

    categorias = ["Comercio","Streaming","Ropa","Redes","Libros","No relevantes"] 
    #fig = plt.figure(figsize =(10, 7)) 
    #plt.pie(res, labels = categorias) 
    #plt.show()

    explode = (0.15, 0.12, 0.16,0.12,0.15,0.12) 
  
    colors = ( "orange", "cyan", "brown", 
              "grey", "indigo", "beige") 
    
    wp = { 'linewidth' : 1, 'edgecolor' : "green" } 
    
    def func(pct, allvalues): 
        absolute = int(pct / 100.*np.sum(allvalues)) 
        return "{:.1f}%\n({:d} sitios)".format(pct, absolute) 
    
    fig, ax = plt.subplots(figsize =(10, 7)) 
    wedges, texts, autotexts = ax.pie(res,  
    autopct = lambda pct: func(pct, res), 
    explode = explode,  
    labels = categorias, 
    shadow = False, 
    colors = colors, 
    startangle = 70, 
    wedgeprops = wp, 
    textprops = dict(color ="magenta")) 
    
    ax.legend(wedges, categorias, 
              title ="Categorias", 
              loc ="center right", 
              bbox_to_anchor =(1, 0, 0.5, 1)) 
    plt.setp(autotexts, size = 7, weight ="bold") 
    ax.set_title("Categorias") 
    
    plt.show()  



  


  





