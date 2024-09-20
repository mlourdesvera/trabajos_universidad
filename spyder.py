#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:33:07 2024

@author: Estudiante
"""
import pandas as pd
from inline_sql import sql, sql_val

#%%
carpeta = "~/Descargas/tp/"


listaSedes = pd.read_csv(carpeta+"lista-sedes.csv")

listaSecciones = pd.read_csv(carpeta+"lista-secciones.csv")

listaSedesDatos = pd.read_csv(carpeta+"lista-sedes-datos.csv")


#%%
