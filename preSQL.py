# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

empleado01 = [[20222333, 33456234, 45432345],[45, 40, 41],[2, 0, 1],[20000, 25000, 10000]]

def superanSalarioActividad01(matriz,umbral):
    res =[]
    for i in range(len(matriz[0])):
        salario = matriz[3][i]
        if salario > umbral:
            empleado = [matriz[0][i], matriz[1][i], matriz[2][i], matriz[3][i]]
            res.append(empleado)
    return res
print(superanSalarioActividad01(empleado01, 15000))


empleado02 = [[20222333, 33456234, 45432345, 43967304, 42236276],[45, 40, 41, 37, 36],[2, 0, 1, 0, 0],[20000, 25000, 10000, 12000, 18000]]
print(superanSalarioActividad01(empleado02, 15000))


empleado03 = [[20222333, 33456234, 45432345, 43967304, 42236276],[20000, 25000, 10000, 12000, 18000],[45, 40, 41, 37, 36],[2, 0, 1, 0, 0]]
def superanSalarioActividad03(matriz,umbral):
    res =[]
    for i in range(len(matriz[0])):
        salario = matriz[1][i]
        if salario > umbral:
            empleado = [matriz[0][i], matriz[1][i], matriz[2][i], matriz[3][i]]
            res.append(empleado)
    return res
print(superanSalarioActividad03(empleado03, 15000))   


empleado04 = [[20222333, 20000, 45, 2],[33456234, 25000, 40, 0],[45432345, 10000, 41, 1],[43967304, 12000, 37, 0],[42236276, 18000, 36, 0]]
def superanSalarioActividad04(matriz,umbral):
    res =[]
    for i in range(len(matriz[0])+1):
        salario = matriz[i][1]
        if salario > umbral:
            empleado = matriz[i]
            res.append(empleado)
    return res
print(superanSalarioActividad04(empleado04, 15000))   


# 1 tuve que cambiar la mayoria de las funciones
#a. no me cambio tanto
#b. tuve que cambiar los indices de mi funcion
##2. tuve que cambiar bastante la funcion
#3. poder modificarla mas facilmente