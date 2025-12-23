from typing import List, Tuple, Dict

# Ejercicio 1
def verificar_transacciones(s: str) -> int:
    saldo_actual: int = 0
    saldo_anterior: int = 0
    for elem in s:
        saldo_anterior = saldo_actual
        if elem == "r":
            saldo_actual += 350
        elif elem == "v":
            saldo_actual -= 56
        elif elem == "x":
            return saldo_actual
        if saldo_actual < 0:
            return saldo_anterior
    return saldo_anterior
# print(verificar_transacciones("ssrvvrrvvsvvsxrvvv"))

# Ejercicio 2
def valor_minimo(s: List[Tuple[float, float]]) -> float:
    lista_vacia = []
    for tupla in s:
        for elem in tupla:
            lista_vacia.append(elem)
    minimo = el_minimo(lista_vacia)
    return minimo

def el_minimo(lista: List[float]) -> float:
    minimo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo

# print(valor_minimo([(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)]))

# Ejercicio 3
def valores_extremos(cotizaciones_diarias: Dict[str, List[Tuple[int,float]]]) -> Dict[str, Tuple[float,float]]:
    res: dict[str, Tuple[float,float]] = {}
    for empresas in cotizaciones_diarias.keys():
        res[empresas] = ()                      #Inicializa el valor correspondiente a la clave empresas en el diccionario res como una tupla vacía.
        valores_empresa = []
        for tuplas in cotizaciones_diarias[empresas] :
            valores_empresa.append(tuplas[1])
            res[empresas] = (el_minimo(valores_empresa),el_maximo(valores_empresa))
    return res 

def el_maximo(lista: List[float]) -> float:
    maximo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

# print(valores_extremos( {"YPF" :[(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}))

# Ejercicio 4
def es_sudoku_valido(m: List[List[int]]) -> bool:
    res: bool = True
    for fila in m: 
       for elem in fila:
            if elem != 0 and cant_apariciones(elem,fila) > 1:
                res = False
    for elem in [1,2,3,4,5,6,7,8,9]:
       for i in range(0,9):
           if cant_apariciones_en_posicion(elem,i,m) > 1:
               res = False 
    return res



def cant_apariciones (e:int,s:list[int]) -> int:
    contador: int = 0
    for elem in s:
        if elem == e:
            contador +=1
    return contador

def cant_apariciones_en_posicion(e:int, pos:int, s:list[list[int]])->int:
    contador : int = 0
    for fila in s:
        for i in range (len(fila)):
            if fila[i] == e and i == pos:
                contador += 1
    return contador

# print(es_sudoku_valido( [
# [1, 2, 3, 4, 5, 6, 7, 8, 9],
# [9, 8, 7, 6, 4, 5, 3, 2, 1],
# [0, 0, 0, 0, 0, 0, 1, 0, 0],
# [0, 0, 0, 0, 0, 4, 0, 0, 0],
# [0, 0, 0, 0, 6, 0, 0, 0, 0],
# [0, 0, 0, 5, 0, 0, 0, 0, 0],
# [0, 0, 4, 0, 0, 0, 0, 0, 0],
# [0, 3, 0, 0, 0, 0, 0, 0, 0], 
# [2, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
# ))