#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:15:11 2024

@author: Estudiante
"""


#%%
import pandas as pd
archivo = '../Estudiante/Documentos/Lourdes/arbolado-en-espacios-verdes.csv'   #descargarlo de nuevo
df = pd.read_csv(archivo, index_col = 2)

#%% dataframe que contenga las filas de Jacarandás y Palos borracho


df_jacaranda = df[df['nombre_com'] == 'Jacarandá']
df_palo_borracho = df[df['nombre_com'] == 'Palo borracho']

#%%Cantidad de árboles, altura máxima, mínima y promedio, diámetro máximo, mínimo y promedio.

cantidad_jacaranda = (df_jacaranda['nombre_com']=='Jacarandá').sum()
cantidad_palo_borracho = (df_palo_borracho['nombre_com']=='Palo borracho').sum()

df_jacaranda.shape  #me dice (filas, columnas)

df['nombre_com'].value_counts() #me cuenta de todos los tipos de arboles cuantos hay

altura_max_jacaranda = df_jacaranda['altura_tot'].max()
altura_max_palo_borracho = df_palo_borracho['altura_tot'].max()

altura_min_jacaranda = df_jacaranda['altura_tot'].min()
altura_min_palo_borracho = df_palo_borracho['altura_tot'].min()

promedio_altura_jacaranda = (df_jacaranda['altura_tot'].sum())/cantidad_jacaranda
promedio_altura_palo_borracho = (df_palo_borracho['altura_tot'].sum())/cantidad_palo_borracho


diametro_max_jacaranda = df_jacaranda['diametro'].max()
diametro_max_palo_borracho = df_palo_borracho['diametro'].max()

diametro_min_jacaranda = df_jacaranda['diametro'].min()
diametro_min_palo_borracho = df_palo_borracho['diametro'].min()

promedio_diametro_jacaranda = (df_jacaranda['diametro'].sum())/cantidad_jacaranda
promedio_diametro_palo_borracho = (df_palo_borracho['diametro'].sum())/cantidad_palo_borracho

#%% Definir una función cantidad_arboles(parque) que, dado el nombre de un parque, calcule la cantidad de árboles que tiene


#%%Definir una función cantidad_nativos (parque) que calcule la cantidad de árboles nativos.

