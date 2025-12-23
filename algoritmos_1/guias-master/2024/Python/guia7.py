#PRIMERA PARTE
#Ejercicio 1
#1.1
def pertenece (s:list[int], e:int) -> bool:
    longitud: int = len(s)
    i: int = 0
    res:bool = False
    while i < longitud:
        if e == s[i]:
            res = True
        i +=1
    return res 
#print(pertenece([1,2,24,5,32],3))

def pertenece_for (s:list[int], e:int) -> bool:
    for i in range (0,len(s)):
        if e == s[i]:
            return True
    return False 
#print(pertenece_for([1,2,24,5,35],3))

def pertenece_generico (s:list ,e) -> bool:
    for elem in s:
        if elem == e:
            return True
    return False
#print(pertenece_generico([1,2,24,3,5,3],3))


#1.2 me gustaría no poner return False, pero no me sale de otra forma, y si lo saco, no funciona
def divide_a_todos (s:list[int],e:int) -> bool:
    longitud: int = len(s)
    i: int = 0
    res:bool = False
    while i < longitud :
        if (s[i] % e)== 0:
            i += 1
            res = True
        else:
            return False
    return res  
#print(divide_a_todos([10,250,30],10))

def divide_a_todos_for (s:list[int],e:int) -> bool:
    for i in s:
        if i % e == 0:
            return True
    return False


#1.3
def suma_total (s: list[int])-> int:
    res:int = 0
    longitud : int = len(s)
    indice_actual: int = 0
    while indice_actual < longitud:
        res += s[indice_actual]
        indice_actual += 1
    return res 
#print(suma_total([1,2,3,4]))


#1.4
def ordenados (s:list[int]) -> bool:
    res: bool = True
    elemento_anterior: int = s[0]
    s = s[1::]   # modifica la lista s, empezando desde el segundo elementos (ya que el prmero sería s[0] que no toma) y va hasta el ultimo, de a 1 porque puse :: entonces usa lo estandar
    for i in s:   #esto toma elementos i de s, desde elemento 1 (porque el 0 no lo toma ya que lo saco en condicion anterior) hasta el ultimo elemento en s, en orden
        if i < elemento_anterior:
            res = False
        else: 
            elemento_anterior = i 
    return res        

#1.5
def longitud_mayor7(s:list[str]) -> bool:
    res: bool = False
    for i in s:
        if len(i) > 7:
            res = True
    return res
 
#1.6
def es_palindromo(texto:str) -> bool:
    longitud: int = len(texto)
    res:bool = False
    if longitud == 1:
        res = True
    for i in range (0,longitud//2):
        if (texto[i] == texto[(longitud-1)-i]):   # longittud-1 porque al emepzar en 0, es uno menos. y le voy restando i pq a medida que avanza en el rango disminuye aca
            res = True
    return res 

#1.7 #trato con str como si fuese una lista de char. python no tiene char
def fortaleza_contrasena (contrasena:str) -> str:
    longitud: int = len(contrasena)
    longitud_mayor_a_8: bool = longitud > 8
    longitud_menor_a_5: bool = longitud < 5
#verifico tiene una minuscula 
#verifico tiene una mayuscula
#verifico tiene un numero
    tiene_una_minuscula: bool = False
    tiene_una_mayuscula: bool = False
    tiene_un_numero: bool = False
    i:int = 0
    while i < longitud:
        if 'a' <= contrasena[i] and contrasena[i] <= 'z':
            tiene_una_minuscula = True
        if 'A' <= contrasena[i] and contrasena[i] <= 'Z':
            tiene_una_mayuscula = True
        if '0' <= contrasena[i] and contrasena[i] <= '9':
            tiene_un_numero = True
        i += 1
    if longitud_mayor_a_8 and tiene_una_minuscula and tiene_una_mayuscula and tiene_un_numero:
        print ("VERDE")
    elif longitud_menor_a_5:
        print ("ROJO")
    else:
        print ("AMARILLO")


#1.8
def cuenta_bancaria(movimiento:tuple[str,float])->float:
    saldo_inicial:float = 0
    longitud:int = len(movimiento)
    for i in range (0, longitud):
        if (movimiento[i][0]=="I"):             # esto indica en la tupla i el primer elemento 
            saldo_inicial += movimiento[i][1]   # y esto en la tupla i el segundo elemento
        elif (movimiento[i][0]=="R"):
            saldo_inicial -= movimiento[i][1]
    return saldo_inicial

#1.9
def tres_vocales_distintas(palabra:str)->bool:
    numero_vocales:int = 0
    res:bool = False
    if pertenece_generico (palabra, "a") or pertenece_generico (palabra, "A"):
        numero_vocales +=1
    if pertenece_generico (palabra,"e") or pertenece_generico (palabra, "E"):
        numero_vocales +=1
    if pertenece_generico (palabra,"i") or pertenece_generico (palabra, "I"):
        numero_vocales +=1
    if pertenece_generico (palabra,"o") or pertenece_generico (palabra,"O"):
        numero_vocales +=1
    if pertenece_generico (palabra,"u") or pertenece_generico (palabra,"U"):
        numero_vocales +=1
    if numero_vocales >=3:
        res=True
    return res


#SEGUNDA PARTE
#Ejercicio 2
#2.1   #parametro inout  # al ser inout no devuelve nada, cambia el de entrada
def poner_pos_pares_cero(lista:list[int]):
    longitud:int = len(lista)
    for i in range(0,longitud):
        if i % 2 == 0:
            lista[i] = 0
    print (lista) 

#2.2    #lista es una variable in, y devuelvo otra lista  
def poner_pos_pares_cero2(lista:list[int])->list[int]:
    lista_vacia:list[int] = []
    longitud:int = len(lista)
    for i in range(0,longitud):   #no me sirve for elem in lista porque necesito posicion no valor de elem   #range funciona con un rango[...)
        if i % 2 == 0 :
            lista_vacia.append(0)  #para agregar uso .append(lo q quiero agregar)
        else:
            lista_vacia.append(lista[i])
    return lista_vacia

#2.3
def lista_sin_vocales (s:list[chr])->list[chr]:
    lista_vacia:list[chr] = []
    vocales:list[chr] = ['a','e','i','o','u','A','E','I','O','U']
    for letra in s:
        if letra not in vocales:
            lista_vacia.append(letra)
    return lista_vacia

#2.4   #CREO QUE ES IN, ENTONCES NO PUEDO CAMBIAR MI LISTA!!!
def reemplaza_vocales (s:list[chr]) -> list[chr]:
    lista_vacia:list[chr] = []
    longitud:int = len(s)
    vocales:list[chr] = ['a','e','i','o','u','A','E','I','O','U']
    for i in range(0,longitud):
        if s[i] in vocales:
            lista_vacia.append('_')
        else:
            lista_vacia.append(s[i])
    return lista_vacia 

#2.5
def da_vuelta_str (s:list[chr]) -> list[chr]:
    lista_vacia: list[chr] = []
    longitud:int = len(s)
    for i in range(0,longitud):
        lista_vacia += s[longitud-1-i]   #este += no se que onda
    return lista_vacia

#2.6
def eliminar_repetidos (s:list[chr]) -> list[chr]:
    lista_vacia: list[chr] =[]
    for elem in s:
        if not pertenece_generico (lista_vacia, elem):    #creo que tambien puedo usar not in 
            lista_vacia.append(elem)
    return lista_vacia


#Ejercicio 3
def todos_mayores_a (minimo:int,notas:list[int])->bool:
    res: bool = True
    for nota in notas:
        if nota < minimo:
            res = False 
    return res

def aprobado(notas:list[int])->int:
    longitud:int = len(notas)
    promedio:int = (suma_total (notas))/longitud
    for nota in notas:
        if todos_mayores_a(4,notas) and promedio >= 7 :
            res:int = 1
        elif todos_mayores_a(4,notas)and promedio >=4 and promedio < 7:
            res:int = 2 
        else:
            res:int = 3 
    return res 



#Ejercicio 4
#4.1
def lista_nombre_estudiantes()->list[str]:
    lista_nombres: list[str] = []
    nombre:str =input("Ingrese su nombre \n")
    while nombre!= "listo":
        lista_nombres.append(nombre)
        nombre = input()
    return lista_nombres

#4.2


#4.3


#Ejercicio 5 
#5.1


#5.2 asi esta la espécificacion, me ingresa un parametro out
def pertenece_a_cada_uno_version_2(s:list[list[int]],e:int, res:list[bool]):
    res.clear()  #limpio res, asi esta vacio cuando empiece
    for lista in s:
        res.append(pertenece(lista,e))



#5.3

#5.4 



