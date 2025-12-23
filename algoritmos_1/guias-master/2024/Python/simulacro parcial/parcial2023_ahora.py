# Ejercicio 1

def ind_nesima_aparicion(s: list, n: int, elem: int) -> int:
    i:int = 0
    contador:int = 0
    res: int = -1           #inclyo aca el caso de si esta menos de n veces
    if cantidad_de_apariciones(elem,s) >= n:
        while (i < len(s)) and  (n > contador):
            if s[i] == elem:
                contador += 1
                if contador == n :
                    res = i
            i += 1
    return res 

def cantidad_de_apariciones(elem:int,s:list[int])->int:
    contador:int = 0
    for i in range(len(s)):
        if elem == s[i]:
            contador += 1
    return contador
#print(ind_nesima_aparicion([-1, 1, 1, 5, -7, 1, 3],2,1))

# Ejercicio 2
def mezclar(s1: list, s2: list) -> list:
    lista_vacia:list = []
    for i in range(len(s1)):
        lista_vacia.append(s1[i])
        lista_vacia.append(s2[i])
    return lista_vacia
# print(mezclar([1, 3, 0, 1],[4, 0, 2, 3]))




# Ejercicio 3

def frecuencia_posiciones_por_caballo(caballos: list, carreras: dict) -> dict:
    nuevo_diccionario: dict[str,list[int]] = {}
    for caballo in caballos:
        lista_ceros = [0] * len(caballos)
        for carrera in carreras.values():
            posicion = 0
            while posicion < len(carrera): 
                if carrera[posicion] == caballo:
                    lista_ceros[posicion] +=1
                posicion += 1                    
        nuevo_diccionario[caballo] =lista_ceros
    return nuevo_diccionario

#print(frecuencia_posiciones_por_caballo(["linda", "petisa", "mister", "luck" ],{"carrera1":["linda", "petisa", "mister", "luck"],"carrera2":["petisa", "mister", "linda", "luck"]}))

# Ejercicio 4
def matriz_capicua(m: list) -> bool:
    for i in range(len(m)):
        if es_capicua(m[i]) == False:
            return False
    return True  


def es_capicua(s:list[int]) -> bool:
    longitud: int = len(s)
    res: bool = True
    if longitud == 1:
        res = True
    else:
        for i in range(longitud//2):
            if (s[i]!=s[(longitud-1)-i]):
                return False
    return res 


# print(matriz_capicua([[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]))