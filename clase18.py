#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 09:59:27 2024

@author: Estudiante
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm
#%%

libreta = pd.read_csv("~/Descargas/datos_libreta.txt", delimiter = ' ')
print(libreta)
#%%
x = pd.DataFrame(libreta["RU"])
y = pd.DataFrame(libreta["ID"])

plt.scatter(x, y)
 

model = linear_model.LinearRegression()
model.fit(x,y)

print(model.coef_)   #pendiente de la recta
print(model.intercept_)   #intercept o término constante(valor de y cuando x es 0)


print(model.score(x, y))  #R² (coeficiente de determinacion) mide que tan bien el modelo de regresión se ajusta a los datos obsevados- valor entre 0 y 1

