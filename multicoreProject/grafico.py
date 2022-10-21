from re import L
from matplotlib import pyplot as plt 
import numpy as np 

  
def generarGrafico(resultados):

    data= []
    res = [0,0,0,0,0,0,0,0]

    for valor in resultados:
        data.append(valor[1])

    for dato in data:
        if dato == "comercio_electronico":
            res[0]+= 1
        elif dato =="plataforma_peliculas":
            res[1]+= 1
        elif dato =="tienda_ropa":
            res[2]+= 1
        elif dato =="redes_sociales":
            res[3]+= 1
        elif dato =="tecnologia":
            res[4]+= 1
        elif dato =="books":
            res[5]+= 1
        elif dato =="Otros":
            res[6]+= 1
        elif dato =="sitios_no_visitados":
            res[7]+= 1

    categorias = ["Comercio Electronico","Streaming/Peliculas/Series","Ropa","Redes Sociales", "Tecnologia" ,"Libros","No relevantes","Sitio No visitado(error)"] 
    #fig = plt.figure(figsize =(10, 7)) 
    #plt.pie(res, labels = categorias) 
    #plt.show()
    pass
    explode = (0.16, 0.12, 0.14,0.11,0.13,0.11,0.11, 0.12) 
  
    colors = ( "#f16d7b", "#71c1e6", "#a47bb3", 
              "#f9cf59", "#57e2b1", "#019fb9","#71c1e6", "#57e2b1") 
    
    wp = { 'linewidth' : 1, 'edgecolor' : "#e6e6e6" }
    
    def func(pct, allvalues): 
        absolute = int(pct / 100.*np.sum(allvalues)) 
        return "{:.1f}%\n({:d} sitios)".format(pct, absolute) 
    
    fig, ax = plt.subplots(figsize =(10, 7)) 
    wedges, texts, autotexts = ax.pie(res,  
    autopct = lambda pct: func(pct, res), 
    explode = explode,  
    labels = categorias, 
    labeldistance=1.05,
    shadow = False, 
    colors = colors, 
    startangle = 70, 
    wedgeprops = wp, 
    textprops = dict(color ="black")) 

    ax.legend(wedges, categorias, 
              title ="Categorias", 
              loc ="center right", 
              bbox_to_anchor =(1, 0, 0.5, 1)) 
    plt.setp(autotexts, size = 7, weight ="bold") 
    ax.set_title("Categorias") 
    
    plt.show()  

 
    


    





  


  





