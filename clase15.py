# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
from inline_sql import sql, sql_val

#%%
carpeta = "~/Descargas/Clase 15/"

Titanic = pd.read_csv(carpeta + "titanic_training.csv")



#%%

primera_clase = sql ^"""
                SELECT Count(*) AS PrimeraClase
                FROM Titanic
                WHERE pclass == 1
                """

segunda_clase = sql ^"""
                SELECT Count(*) AS SegundaClase
                FROM Titanic
                WHERE pclass == 2
                """
                
tercera_clase = sql ^"""
                SELECT Count(*) AS TerceraClase
                FROM Titanic
                WHERE pclass == 3
              """        
                
cantidad_niños  = sql ^"""
                SELECT Count(*) AS CantidadNiños
                FROM Titanic
                WHERE Age <= 18
               """    
proporcionNiños = 139/891
#print(proporcionNiños)               
#falta sacar proporcion niños

mujeres = sql ^"""
                SELECT Count(*) AS mujeres_sobrevivientes
                FROM Titanic
                WHERE Sex = 'female'
               """  
sobrevivientes  = sql ^"""
                SELECT *
                FROM Titanic
                WHERE Survived == 1
                """    
mujeres_sobrevivientes = sql ^"""
                SELECT Count(*) AS mujeres_sobrevivientes
                FROM sobrevivientes
                WHERE Sex = 'female'
               """  
proporcion_mujeres_sobrevivientes = 233/314
print(proporcion_mujeres_sobrevivientes)               
                

primera_clase_sobrevivientes = sql ^"""
                SELECT Count(*) AS primera_clase_sobrevivientes
                FROM sobrevivientes
                WHERE pclass == 1
               """
proporcion_primera_clase_sobrevivientes = 136/216
print(proporcion_primera_clase_sobrevivientes)               
#%%                
mujeres_clase1= Titanic[(Titanic['Sex'] == 'female')&(Titanic['Pclass'] == 1)]
mujeres_clase1_sobrevivieron = Titanic[(Titanic['Sex'] == 'female')&(Titanic['Pclass'] == 1)&(Titanic['Survived'] == 1)]
cantidad_total = mujeres_clase1.shape[0]
cantidad = mujeres_clase1_sobrevivieron.shape[0]
proporcion = cantidad / cantidad_total
print(proporcion)

#%%

TitanicCompetencia = pd.read_csv(carpeta + "titanic_competencia.csv")


def clasificador_titanic(x):
    vive = False
    if x.Sex == "female":
        vive = True
    elif x.Age < 5 or x.Pclass == 1 :
        vive = True
    return vive
#revisarlo
#x.competencia.iloc[0]
#%%


