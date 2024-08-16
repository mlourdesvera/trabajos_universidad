with open('datame.txt','rt') as file:
    data = file.read()

data_nuevo = '2024 seguimos con DATAME\n\n' + data
data_nuevo = data_nuevo + 'Dirección de Carrera LCD'

datame = open("datame_2024.txt", "w")    #write mode
datame.write(data_nuevo)
datame.close()


nombre_archivo = 'cronograma_sugerido.csv'
with open(nombre_archivo,'rt') as file:
    for line in file:
        datos_linea = line.split(',')
        #print(datos_linea[1])

#lista = list()
#for elem in datos_linea:        
 #   lista.append(elem)
#    print(lista)
#no me da

import csv
nombre_del_archivo = 'cronograma_sugerido.csv'
f = open(nombre_del_archivo)
filas =csv.reader(f)
#for fila in filas:
 #   print(fila)

import pandas as pd
d={'nombre':['Antonio','Brenda','Camilo','David'],'apellido':['Restrepo','Sanez','Torres','Urondo'],'lu':['78/23','449/22','111/24','1/21']}
df = pd.DataFrame(data=d)
df.set_index('lu',inplace=True)
#print(df)


fname = 'cronograma_sugerido.csv'
df = pd.read_csv(fname)
df = pd.read_csv(fname,index_col = 0)
df = pd.read_csv(fname, header = 0)
print(df)