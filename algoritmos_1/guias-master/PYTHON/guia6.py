import math 
#EJERCICIO 1
#1
def imprimir_hola():
    print("Hola")

#2
def imprimir_un_verso():
    print("bla \n bla \n bla")
#imprimir_un_verso()

#3
def raiz_de_2():
    print(round (math.sqrt (2),4))
#raiz_de_2()

#4
#def factorial_de_dos() -> int:
#    print(math.factorial(2))

#con for
def factorial(n:int) -> int:
    res: int = 1
    for i in range (1,n+1):
        res = res * i 
        print(res)
    return res 
#con while
def factorial_w(n:int) ->int:
    res:int = n 
    i = int = n-1
    while i>0:
        print(res)
        res=res*i
        i=i-1
    return res 

#5
def perimetro() -> float:
    print(2*math.pi)

#EJERCICIO 2
#1
def imprimir_saludo(nombre:str):
    print("Hola "+ nombre) 

#2
def raiz_cuadrada_de(numero:int)->float:
    res : float = math.sqrt (numero)
    return res 

#3
def fahrenheit_a_celsius(t:float) -> float:
    res : float = ((t-32)*5)/9
    return res 

#4 
def imprimir_dos_veces(estribillo:str):
    print((estribillo +"\n") *2)

#5
def es_multiplo_de(n:int,m:int) -> bool:
    res : bool = (n%m)==0 # mod n m == 0
    return res 
#6
def es_par(n:int) -> bool:
    res : bool = es_multiplo_de(n,2)
    return res 

#7
def cantidad_de_pizzas(comensales:int,min_cant_de_porciones:int) -> int:
    if es_multiplo_de(comensales * min_cant_de_porciones,8):
        res : int = (comensales * min_cant_de_porciones)/8
    else:
        res : int = math.floor ((comensales * min_cant_de_porciones)/8)+1
    return res 

#2
def ambos_son_0(n1:float,n2:float)->bool:
    res : bool = n1 == 0 and n2 == 0
    return res

#3
def es_nombre_largo(nombre:str) -> bool:
    res : bool = 3<=len(nombre) and len(nombre)<=8 #&& ahora es and
    return res

#4
def es_bisiesto(año:int)-> bool:
    res : bool = es_multiplo_de(año,400) or (es_multiplo_de(año,4)and not es_multiplo_de(año,100))
    return res  

#EJERCICIO 4 (no use min y max, pq no me salen (el 3 y 4 los hice en el mismo))

def peso_pino (altura:float) -> float :
    if (altura <= 3):
        res : float = (300*altura)
    else :
        res : float = (900)+(200*(altura-3))
    return res 

def es_peso_util (peso:float) -> bool :
    if (400<= peso <= 1000):
        res : bool = True
    else :
        res : bool = False


def sirve_pino(n:float) -> bool :
    res: bool = (es_peso_util (peso_pino (n))==True)
    return res  


#EJERCICIO 5
#1
def devoler_el_doble(n:int) -> int:
    if (n%2==0):
        res: int = 2*n
    else :
        res = n
    return res 


#2
def devolver_valor_si_es_par_sino_el_que_sigue (n:int) -> int :
    if (n%2==0): 
        res: int = n
    else :
        res = n + 1
    return res 

 
#3  
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (n:int) -> int :
    if (n%3==0 and n%9!=0):  # != distinto
        res: int = 2*n
    elif (n%9==0) :
        res: int = 3*n
    else :
        res: int = n
    return res 


#4
def lindo_nombre (nombre:str) -> str: 
    if len(nombre) >= 5:
        res : str = "Tu nombre tiene muchas letras!"
    else:
        res : str = "Tu nombre tiene menos de 5 caracteres"
    return res 


#5
def elRango(n:int) -> str:
    if n<5 : 
        res: str = "Menor a 5"
    elif 10<n<20:
        res: str = "Entre 10 y 20"
    elif n>20 :
        res: str = "Mayor a 20"
    return res 


#6
def vacaciones_trabajo (sexo:str,edad:int) -> str :
    if (sexo == "F" and edad >= 60) or (sexo == "M" and edad >= 65) or (edad <=18):
        res : str = "Andá de vacaciones"
    else :
        res : str = "Te toca trabajar"
    return res 


#EJERCICIO 6
#1
def numeros_del_1_al_10():
    numero:int = 1
    while numero <=10:
        print (numero)
        numero += 1
#numeros_del_1_al_10()


#2 
def numeros_pares_entre_10_y_40 ():
    numero:int = 10
    while numero <= 40:
        print (numero)
        numero += 2
#numeros_pares_entre_10_y_40()


#3 Escribir una funcion que imprima la palabra “eco” 10 veces.
def palabra_eco_10_veces():
    contador=1
    while contador<=10:
        print ("eco")
        contador+=1
#palabra_eco_10_veces()

#4
def cuenta_regresiva(contador:int):
    while contador >= 1:
        print (contador)
        contador -= 1
    print ("DESPEGUE")
#cuenta_regresiva(6)

#5
def viaje_en_el_tiempo (partida:int, llegada:int): #llegada<partida
    while partida > llegada:
        print ("Viajo un año al pasado, estamos en el año " + str (partida-1))
        partida -=1

#6
def viaje_en_el_tiempo_2 (partida:int):
    while partida > -384 :
        print ("Viajo 20 años al pasado, estamos en el año "+ str (abs (partida - 20)) + " a.c" if partida -20 < 0 else "Viajo 20 años al pasado, estamos en el año "+ str (partida) )
        partida -= 20
     

#EJERCICIO 7   (funciones anteriores con for)
#1
def numeros_del_1_al_10_for():
    i: int = 1
    for i in range (1,11,1):
        print (i) 

#2
def numeros_pares_entre_10_y_40_for ():
    i: int = 10
    for i in range (10, 41, 2):
        print (i)

#3
def palabra_eco_10_veces_for():
    i : int = 1
    for i in range (1, 11, 1):
        print ("eco ")

#4
def cuenta_regresiva_for():
    i : int = 1
    for i in range (1, 11, 1):
        print ("eco ")

#4
def cuenta_regresiva_for(contador:int):
    i: int = 1
    for i in range (contador,0,-1):
        print (i)
    print ("DESPEGUE")
     
#5
def viaje_en_el_tiempo_for (partida:int, llegada:int): #llegada<partida
    i:int = 1
    for i in range (partida,llegada,-1):
        print ("Viajo un año al pasado, estamos en el año " + str (i-1))


#6 
def viaje_en_el_tiempo_2_for (partida:int):
    i:int = 1
    for i in range (partida-20,-384,-20):
        print ("Viajo 20 años al pasado, estamos en el año "+ str (i))





#EJERCICIOS 8 Y 9 NO LOS HICE (NO ENTIENDO QUE ME PIDEN)
