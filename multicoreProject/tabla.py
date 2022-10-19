import csv

import pandas as pd

# open the file in the write mode
def generarTabla(resultados):
    with open('multicoreProject/datos.csv', 'w', newline='') as file:
        file.writelines("URL"+"," +"Cateogria"+","+"Palabras Encontradas"+"\n")
        for r in resultados:
            file.writelines(r[0]+"," +r[1]+","+r[2]+"\n")
         

def imprimirTabla():
    df = pd.read_csv('multicoreProject/datos.csv')
    print(df.to_string()) 
    
        
