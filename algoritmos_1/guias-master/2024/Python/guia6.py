import math 
#Ejercicio 1 
#1
def imprimir_hola_mundo():
    print('Hola Mundo')


#2
def imprimir_un_verso():
    print('bla bla bla')

#3
def raizDe2() -> float :
    return round (math.sqrt (2),4)

#4
def factorialDe2()-> int:
    return math.factorial (2)

def factorialDe2Aux()-> int: 
    return  (2*1)

#5
def perimetro() -> float:
    return 2 * math.pi 


#Ejercicio 2
#1
def imprimir_saludo(nombre: str):
    print ('Hola ' + nombre)

#2
def raiz_cuadrada_de(numero: int)-> float:
    return math.sqrt (numero)

#3
def farenheit_a_celsius(temp_far: float)-> float:
    return (temp_far - 32 )* 5/9

#4
def imprimir_dos_veces (estribillo:str):
    print ((estribillo + '\n') *2 )    #'\n' se usa para poner espacio. *2 dentro del parentesis repite lo del parentesis. + para agregar mas de una cosa, sea variable o palabra

#5
def es_multiplo_de(n:int, m:int)-> bool:
    return (n%m) == 0                   # mod en python es %

#6
def es_par(numero:int) -> bool:
    return es_multiplo_de (numero, 2)

#7
def cantidad_de_pizzas (comensales:int, min_cant_de_porciones:int) -> int:
    res = math.ceil((comensales * min_cant_de_porciones)/8 )
    return res 


#Ejercicio 3  # len(a) te devuelve longitud de a.  # s[2] me devuelve el segundo elemento de mi lista s   # se usa and, or y not
#1
def alguno_es_0 (numero1:float, numero2:float)->bool:
    return (numero1 == 0) or (numero2 == 0)

#2
def ambos_son_0 (numero1:float, numero2:float)->bool:
    return (numero1 == 0) and (numero2 == 0)

#3    
def es_nombre_largo (nombre:str) -> bool:
    return (3 <= len(nombre)) and (len(nombre) <= 8)

#4
def es_bisiesto(año:int) -> bool:
    return (es_multiplo_de (año, 400)) or ((es_multiplo_de (año, 4)) and not(es_multiplo_de (año, 100)))


#Ejercicio 4  #usar min y max
#3 kg por cada centímetro hasta 3 metros,    2 kg por cada centímetro arriba de los 3 metros.
#Los pinos se usan para llevarlos a una fábrica de muebles, a la que le sirven árboles de entre 400 y 1000 kilos,
# un pino fuera de este rango no le sirve a la fábrica.

#1 peso_pino 
#2 es_peso_util   #recibe un peso en kg y responde si un pino de ese peso le sirve a la fábrica.
#3 sirve_pino   #recibe la altura de un pino y responde si un pino de ese peso le sirve a la fábrica
#4 sirve_pino   #usando composición de funciones.

#1
def peso_pino(altura:float) -> float:
    if altura < 3:
        res:float = altura * 300 
    else:
        res:float = 900 + ((altura-3) * 200)
    return res 

# 2
def es_peso_util (peso:float) -> bool:
    res: bool = False
    if peso <= 1000 and peso >= 400:
        res = True 
    return res 

# 3
def sirve_pino (altura: float) -> bool:
    res: bool = False
    peso: float = 0
    if altura > 3:
        peso = altura * 300
    else :
        peso = 900 + ((altura -3)*200)
    if peso <= 1000 and peso >= 400:
        res:bool = True
    return res 

# 4
def sirve_pino_comp (altura:float) -> bool:
    res: bool = False
    if es_peso_util (peso_pino (altura)) == True:
        res: bool = True
    return res 


#Ejercicio 5   #usa if, else, elif 
#1
def devolver_el_doble_si_es_par(un_numero: int) -> int:
    if (un_numero % 2) == 0:
        return un_numero *2
    else: 
        return un_numero 
    
#2
def devolver_valor_si_es_par_sino_el_que_sigue (numero:int) -> int:
    res: int = 0
    if numero % 2 == 0:
        res = numero
    else:
        res = numero +1
    return res 

def devolver_valor_si_es_par_sino_el_que_sigue2 (numero:int) -> int:
    res: int = 0
    if numero % 2 == 0:
        res = numero
    if numero %2 != 0:
        res = numero +1
    return res

# 3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (numero:int) -> int:
    res: int = 0
    if numero % 3 == 0 :
        res = numero *2
    elif numero % 9 == 0:
        res = numero *3
    else:
        res = numero
    return res

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_2 (numero:int) -> int:
    res: int = 0
    if numero % 3 == 0 :
        res = numero *2
    if numero % 9 == 0:
        res = numero *3
    if numero % 3 != 0 and numero % 9 != 0:
        res = numero
    return res

#4
def lindo_nombre (nombre:str):
    if len (nombre) >= 5:
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")


#5
def elRango(numero:int):
    if numero < 5:
        print("Menor a 5")
    elif numero >= 10 and numero <= 20:
        print ("Entre 10 y 20")
    elif numero > 20:
        print ("Mayor a 20")
 

#6
def estado (sexo:str,edad:int):
    if sexo == "M":
        if edad < 18 or edad > 65:
            print ("Andá de vacaciones")
        else :
            print ("Te toca trabajar")
    if sexo == "F":
        if edad < 18 or edad > 60:
            print ("Andá de vacaciones")
        else :
            print ("Te toca trabajar")



#Ejercicio 6
    #while condicion
         #lo que quiero que pase
#1
def ej6_1():
    i:int = 1
    while i <= 10:
        print (i)
        i += 1

#2
def ej6_2():
    i: int = 10
    while i <= 40:
        print (i) 
        i += 2 


#3
def ej6_3():
    i:int = 0
    while i < 10:
        print ("ECO")
        i += 1


#4
def ej6_4(numero):
    i : int = numero
    while i >=1:
        print (i) 
        i -= 1
    print ('Despegue')


#5
def viaje_en_el_tiempo (partida:int, llegada:int):
    año:int = partida
    while llegada <= año:
        print ("Viajó un año al pasado, estamos en el año " + str (año))
        año -= 1

#6
def viaje_en_el_tiempo2 (partida:int):
    año:int = partida
    while -384 <= año:
        print ("Viajó 20 años al pasado, estamos en el año " + str (año))
        año -= 20



#Ejercicio 7 
   #for i in range (desde,hasta (hay que poner uno mas),incremento) 
#1
def ej7_1():
    for i in range (1,11,1):
        print (i)


#2
def ej7_2():
    for i in range (10,41,2):
        print (i) 


#3
def ej7_3():
    for i in range (1,11,1):
        print("ECO")


#4
def ej7_4(numero):
    for i in range (numero,0,-1):
        print (i)
    print('Despegue')


#5
def viaje_en_el_tiempo_for(partida:int, llegada:int):
    for i in range(partida,llegada-1,-1):
        print ("Viajó un año al pasado, estamos en el año " + str (i))
        
#6
def viaje_en_el_tiempo2_for(partida:int):
    for i in range (partida, -384, -20):
        print ("Viajó 20 años al pasado, estamos en el año " + str (i))



#Ejericio 8 --> no se que es ejecución simbolica
#Ejercicio 9 --> no tengo ganas ;)