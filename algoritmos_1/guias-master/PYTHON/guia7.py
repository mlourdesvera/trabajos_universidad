#EJERCICIO 1
#PRIMERA PARTE
#1.1
def pertenece (s:[int],e:int) -> bool :
    longitud : int = len(s)
    indice_actual : int = 0
    pertenece: bool = False 
    while indice_actual < longitud :
        if e == s[indice_actual]:
            pertenece = True
        indice_actual += 1
    return pertenece

def pertenece_for (s:[int],e:int) -> bool :
    longitud : int = len(s)
    pertenece: bool = False 
    for i in range (0,longitud):
        if e == s[i]:
            pertenece = True
    return pertenece

def pertenece_for_ret (s:[int],e:int) -> bool :
    longitud : int = len(s)
    for i in range (0,longitud):
        if e == s[i]:
            return True
    return False 

def pertenece_generico(s:[],e) -> bool :
    longitud : int = len(s)
    for elem in s:
        if elem == e:
            return  True
    return False 


#1.2
def divide_a_todos (s:[int],e:int) -> bool :
    longitud : int = len(s)
    for i in s:
        if i % e == 0:
            return True
    return False    

#1.3
def suma_total (s:[int]) -> int :
    total: int = 0
    longitud:int = len(s)
    indice_actual: int = 0
    while indice_actual < longitud :
        total += s[indice_actual] #equivalente total = total + indice atual
        indice_actual += 1
    return total  

#1.4
def ordenados (s:[int]) -> bool :
    elem_anterior: int = s[0] 
    s = s [1::]
    for i in s :
        if elem_anterior > i:
            return False 
        else: 
            elem_anterior = i 
    return True

#1.5
def palabra_mayor_a_7(s:[str]) ->bool:
    for i in range (0,len(s)):
        if (len(s[i])>7):
            return True
    return False     

#1.6
def es_palindromo(texto:str) -> bool:
    longitud : int = len (texto)
    for i in range (0,longitud//2):
        if (texto[i] != texto [(longitud-1)-i]):
          return False
    return True
 
#1.7
def fortaleza_contrasena (contrasena : str) -> str:
    longitud_mayor_a_8 : bool = len(contrasena) > 8 #verifico longitud mayor a 8    
    longitud_menor_a_5 : bool = len(contrasena) < 5 #verifico longitud menor a 5

    #verifico tiene una mayuscula
    tiene_una_mayuscula : bool = False 
    indice_actual : int = 0
    while indice_actual < len(contrasena):
        if contrasena[indice_actual]>= 'A' and contrasena[indice_actual] <= 'Z':
            tiene_una_mayuscula = True 
        indice_actual += 1 

    #verifico tiene una minuscula   
    tiene_una_minuscula : bool = False 
    indice_actual : int = 0
    while indice_actual < len(contrasena):
        if contrasena[indice_actual]>= 'a' and contrasena[indice_actual] <= 'z':
            tiene_una_minuscula = True 
        indice_actual += 1 

    #verifico tiene un digito numerico
    tiene_un_numero : bool = False
    indice_actual = 0
    while indice_actual < len(contrasena) and not (contrasena[indice_actual] >= '0' and contrasena[indice_actual] <= '9'):
        indice_actual += 1
    tiene_un_numero = indice_actual < len (contrasena)  

    #devuelvo color segun condiciones
    if longitud_mayor_a_8 and tiene_un_numero and tiene_una_mayuscula and tiene_una_minuscula:
        return "VERDE"
    elif longitud_menor_a_5: #else if
        return "ROJA"
    else:
        return "AMARILLA"    


#1.8
def saldo_actual(operaciones:[(str,float)]) -> float :
    saldo:int = 0
    longitud : int = len (operaciones)
    for i in range (0,longitud):
        if (operaciones [i][0] == "I"):
            saldo += operaciones[i][1]
        elif (operaciones [i][0] == "R"):
            saldo -= operaciones[i][1]
    return saldo
#print(saldo_actual([("I",2000),("R",20),("R",1000),("I",300)]))

#1.9
def vocales_distintas(palabra:str)-> bool:
    contador_vocales_distintas: int = 0
    longitud: int = len(palabra)
    if (pertenece_generico (palabra, "a") or pertenece_generico (palabra, "A")):
        contador_vocales_distintas += 1
    if (pertenece_generico (palabra, "e") or pertenece_generico (palabra, "E")):
        contador_vocales_distintas += 1
    if (pertenece_generico (palabra, "i") or pertenece_generico (palabra, "I")):
        contador_vocales_distintas += 1
    if (pertenece_generico (palabra, "o") or pertenece_generico (palabra, "O")):
        contador_vocales_distintas += 1
    if (pertenece_generico (palabra, "u") or pertenece_generico (palabra, "U")):
        contador_vocales_distintas += 1
    return contador_vocales_distintas >= 3
#print (vocales_distintas ("lourdes"))


#SEGUNDA PARTE
#EJERICCIO 2
#2.1
def ceros_en_pares(lista:[int])-> [int]:
    longitud: int = len(lista)
    for i in range (0,longitud):
        if (i%2==0):
           lista[i]=0
    return lista

#2.2
def ceros_en_pares_in(lista:[int])-> [int]:
    lista_nueva: [int] = []
    for i in lista:
        if (i%2==0):
            lista_nueva.append(0)
        else:
            lista_nueva.append(i)
    return lista_nueva
#print (ceros_en_pares_in([1,2,3,4,56,78,9876,233,1]))

#2.3
def sin_vocales(text:[str])->str:
    vocales: [str] = ["a","e","i","o","u","A","E","I","O","U"]
    new_text: [str] = ""
    for letter in text: 
        if (letter not in vocales): #no se si puedo usar el in(sino pertenece)
          new_text += letter
    return new_text

#2.4
def reemplazaVocales (caracteres:[chr])->[chr]:
    lista_vacia: [chr] = []
    vocales: [str] = ["a","e","i","o","u","A","E","I","O","U"]
    new_text: [str] = ""
    for char in caracteres:
        if char in vocales :
            lista_vacia.append("_")  
        else:
            lista_vacia.append(char)
    return lista_vacia

#2.5
def daVueltaStr (palabra:[chr])->[chr]:
    salida: [chr] = []
    longitud:int = len(palabra)
    for i in range (0, longitud):
        salida += palabra [longitud-i-1]
    return salida 
#print (daVueltaStr(["o","p","a"]))

#2.6
def eliminarRepetidos (palabra:[chr])->[chr]:
    lista_vacia: [chr] = []
    long:int = len(palabra)
    for i in range (0,long):
        if (palabra[i] not in lista_vacia):
            lista_vacia.append(palabra[i])
    return lista_vacia
#print (eliminarRepetidos(["o","eco","bokita","7","p","7","a"]))


#EJERCICIO 3
def todas_mayores_a(minimo, notas:[int]) -> bool:
    todas_mayores_a = True
    for nota in notas :
        if nota < minimo :
            todas_mayores_a = False
    return todas_mayores_a

def aprobado (notas:[int])->int:
    longitud :int = len(notas)
    promedio: int = suma_total(notas)//longitud
    for i in range (0,longitud):
        if ((todas_mayores_a (4,notas)) and (promedio>=7)):
            res = 1
        elif ((todas_mayores_a (4,notas))  and (promedio>=4) and (promedio<7)):
            res = 2
        else:
            res = 3
    return res 


#EJERCICIO 4
#4.1
def listaDeEstudiantes () -> [str]:
    lista : [str] = []
    nombre : str = input ("Ingrese nombre de estudiante \n")
    while nombre != "listo":
        lista.append(nombre)
        nombre = input()
    return lista

#4.2
def saldo_sube()->[(str,int)]:
    res:[(str,int)] =[]
    opcion : str = ""
    monto: int = 0
    plataActual:int = 0
    while (opcion!= "X"):
        print ("Ingrese una opción (C: Cargar, D: Descontar, X: Cerrar):")
        opcion = input ()
        if (opcion == "C"):
            print ("Ingrese un monto")
            monto = int (input())
            plataActual += monto
            res.append ((opcion,monto))
        elif (opcion == "D"):
            print ("Ingrese un monto")
            monto = int (input())
            plataActual -= monto
            res.append ((opcion,monto))
    print ("Terminó con " +str(plataActual)+" pesos")
    return res 

#4.3
import random
def juego7ymedio() -> [int]:
    historialDeCartas:[int]=[]
    opcion:str='S'
    contador:int=0
    while((opcion=='S') and( contador <= 7.5)):
        print("----")
        num:int=random.choice([1,2,3,4,5,6,7,10,11,12])
        print("Te toco un "+str(num))
        historialDeCartas.append(num)
        if(num==10 or num==11 or num==12):
            contador+=0.5
        else:
            contador+=num
        if(contador>7.5):
            print('Contador= '+str(contador)+' => PERDISTE')
            opcion='X'
        elif(contador==7.5):
            print('Contador= '+str(contador)+' => GANASTE')
            opcion='X'
        else:
            print('Contador= '+str(contador)+' => (S para seguir, X para parar)')
            opcion=input()
    return historialDeCartas


#EJERCICIO 5 
#5.1
def perteneceACadaUno(s:[[int]], e:int) -> [bool]:
    res = []
    indice:int = 0
    longitud:int = len(s)
    for lista in s:
        res.append(pertenece (lista, e))
    return res

#5.2
def esMatriz (s: list()[list()[int]]) -> bool:
    if len(s) == 0:
        return False 
    for columna in s:
        longitudColumna = len(s[0])
        if len(columna) == 0:
            return False
        elif len(columna) != longitudColumna:
            return False
    return True

#5.3
def filasOrdenadas(m: list()[list()[int]]):
    res: list[bool] = []
    for i in m:
        if ordenados(i) == True:
            res.append(True)
        else:
            res.append(False)
    print(res)

#5.4
import numpy as np
def potenciaMatriz(d: int, p: float):
    m = np.random.random((d, d))**2 # se generaria una matriz random de tamanio d
    nuevaMatriz = m
    # si se eleva a 1 directamente imprime m
    if p == 1:
        print(m)
    else:
        incremento = 1
        while incremento != p: 
            #esta parte multiplica una m por la nueva matriz
            matrizActualizada = []
            nuevaFila = []
            for fila in range(len(m)):
                if nuevaFila != []:
                    matrizActualizada.append(nuevaFila)
                    nuevaFila = []
                for columna in range(len(m[fila])):
                    n = 0
                    elem = 0
                    while n!= d:
                        elem += nuevaMatriz[fila][n] * m[n][columna]
                        n += 1 
                    nuevaFila.append(elem) #va creando la nueva fila de la matriz actualizada
            #agrega la ultima fila a matriz actualizada
            matrizActualizada.append(nuevaFila)
            nuevaMatriz = matrizActualizada
            incremento += 1
    print(nuevaMatriz)