#ARCHIVOS
#Ejercicio 1
#1.1
def contar_lineas(nombre_archivo:str)-> int:
    archivo = open(nombre_archivo)   #si no le pongo nada, asume que el modo es r
    lineas: list[str] = archivo.readlines()
    cantidad_lineas:int = len(lineas)
    archivo.close()
    return cantidad_lineas

#1.2
def existe_palabra(palabra:str, nombre_archivo:str) -> bool:
    res:bool = False
    archivo=open(nombre_archivo,'r')
    lineas: list[str] = archivo.readlines()
    for linea in lineas:
        if palabra in linea:    # podria usar pertenece, pero no lo tengo hecho en esta guia
            res = True 
    return res

#1.3
def cantidad_de_apariciones(nombre_archivo:str, palabra:str) -> int:
    archivo = open(nombre_archivo)
    contador: int = 0
    lineas: list[str] = archivo.readlines()
    for i in range(0,len(lineas)):
        if palabra in lineas[i]:
            contador +=1
    return contador 


#Ejercicio 2
#no me gusta el break que quedo ahi
def clonar_sin_comentarios(nombre_archivo:str):
    res = open("sin_comentarios_"+nombre_archivo,"w")
    sin_comentarios:list[str] = [] 
    archivo = open(nombre_archivo)
    lineas: list[str] = archivo.readlines() 
    for linea in lineas:
        for caracter in linea:
            if not caracter == " ":
                if not caracter == "#":
                    sin_comentarios.append(linea)
                break
    res.writelines(sin_comentarios)
    res.close()
    archivo.close()


#Ejercicio 3
def invertir_lineas(nombre_archivo:str):
    archivo = open(nombre_archivo)
    res = open("reverso.txt","w")
    invertir_lineas: list[str] = []
    lineas: list[str] = archivo.readlines()
    longitud: int = len(lineas)
    for i in range(0,longitud):
        invertir_lineas.append(lineas[(longitud-1)-i])
    res.writelines(invertir_lineas)
    res.close
    archivo.close()


#Ejercicio 4
def agregar_frase_al_final(nombre_archivo:str, frase:str):
    archivo = open (nombre_archivo,"a")   # "a" => opens the file for appending; any data written to the file is automatically added to the end. 
    archivo.write(frase)
    archivo.close()


#Ejercicio 5  #podria haber sido con insert
def agregar_frase_al_principio(nombre_archivo:str, frase:str):
    archivo = open (nombre_archivo,"r+")  # con r+ leo el archivo y lo escribo, si uno solo "w" no lo puedo leer
    archivo_anterior = archivo.read()  #lee el archivo antes de modificarlo porque sino lo pierdo, cuando lo lee el puntero que al final del arhcivo
    archivo.seek(0)   # la funcion seek va a la posicion que quiero   
    archivo.write(frase+"\n")
    archivo.write(archivo_anterior)
    archivo.close()

#Ejercicio 6
def listar_palabras_de_archivo (nombre_archivo:str) -> list:
    archivo = open(nombre_archivo,'r')
    lista_vacia:list = []
    for palabras in archivo.readlines():  
        palabra = palabras.strip()
        if (len(palabra) >=5) :
                caracter = str(palabra)
                if (caracter>'A' and caracter<'Z') or (caracter>'a' and caracter<'z') or (caracter == '') or (caracter == '_'): 
                    lista_vacia.append(palabra)
    archivo.close()
    return lista_vacia


#Ejercicio 7
def promedio_estudiante(nombre_archivo:str, lu:str) ->  float:
    archivo= open(nombre_archivo,'r')
    lineas = archivo.readlines()
    contador: int = 0
    nota_acumulada: int = 0
    for linea in lineas:
        datos = linea.split(",")
        if datos[0] == lu:
            contador += 1
            nota_acumulada += int[datos[3]]    # porque segun la especificacion las notas estan en este lugar
    archivo.close()
    promedio: float = nota_acumulada/contador
    return promedio

def calcular_promedio_por_estudiante (nombre_archivo_notas:str, nombre_archivo_promedios:str):
    archivo =open(nombre_archivo_notas,'r')
    archivo_nuevo = open(nombre_archivo_promedios,'w')
    archivo_nuevo.write(promedio_estudiante(nombre_archivo_notas))
    archivo.close()
    archivo_nuevo.close()



from queue import Queue as Pila
#PILAS
#Ejercicio 8  
#no se como probarlo, no se como hacer para que me devuelva la pila
import random
def generar_nros_al_azar(cantidad:int, desde: int, hasta:int) -> Pila[int]:
    p = Pila()
    while cantidad > 0:
        p.put(random.randint(desde,hasta))
        cantidad -= 1
    return p

#Ejercicio 9 
def cantidad_elementos (p:Pila) -> int:
    contenido = []
    contador : int = 0
    while not p.empty():
        contenido.append(p.get())
        contador +=1
    for elemento in contenido:    # porque la especificacion me pide que si cambio el tipo de entrada, debo restaurarla por ser de tipo in
        p.put(elemento)
    return contador

# p = Pila()
# p.put(1)
# p.put(4)
# p.put(8)
# print(cantidad_elementos(p))

#Ejercicio 10
def buscar_el_maximo(p:Pila[int]) -> int:
    maximo: int = p.get()
    while not p.empty():
        nuevo_elemento = p.get()
        if nuevo_elemento > maximo:
            maximo = nuevo_elemento
    return maximo  

# p = Pila()
# p.put(1)
# p.put(42)
# p.put(878)
# print(buscar_el_maximo(p))


#Ejercicio 11
# en el caso de "1 + ) 2 x 3 ( ( )", me dice como si es True y debería darme False
#tendria que hacer una pila de parentesis abiertos y cada vez que hay un parentesis cerrado, saco uno abierto de la pila. la pila tiene que terminar vacia y no se puede vaciar antes de que termine
#HACER DE NUEVO!!!!!!!
def esta_bien_balanceada (s:str) -> bool:
    res: bool = True
    p = Pila()
    parentesis_abierto = 0
    for letra in s[::-1]:
        p.put(letra)
    while not p.empty():
        letra_sacada = p.get()
        if letra_sacada == "(":
            parentesis_abierto +=1
        if letra_sacada == ")":
            parentesis_abierto -=1
    if parentesis_abierto !=0:
        res = False
    return res 
    
#Ejercicio 12   
def evaluar_expresion (s:str) -> float:
    operandos = Pila()
    tokens = s.split(" ")
    for token in tokens: 
        if '0' < token < '9':
            operandos.put(token)
        elif token in ['+','-','*','/']:
            n1 = int(operandos.get())
            n2 = int(operandos.get())
            if token == '+':
                operandos.put(n1+n2)
            if token == '-':
                operandos.put(n1-n2)
            if token == '*':
                operandos.put(n1*n2)
            if token == '/':
                operandos.put(n1/n2)
    return operandos.get()

#expresion = "3 4 + 5 * 2 -"
#resultado = evaluar_expresion(expresion)
#print(resultado) # Debería devolver 33


from queue import Queue as Cola
from random import randint


def imprimir_cola(c:Cola)->list:  
    lista = []
    while not c.empty():
        lista.append(c.get())
    for elem in lista:
        c.put(elem)
    return lista

#Ejercicio 13
def generar_nros_al_azar_cola(cantidad:int, desde:int, hasta:int) -> Cola[int]:
    c: Cola[int] = Cola()
    for i in range:
        c.put(randint(desde,hasta))
    return c 

#azar = generar_nros_al_azar(3,1,10)
#print(imprimir_cola(azar))

#Ejercicio 14
#lo hice igual que pila, me gustaria ver si la cola queda igual a la que yo doy al principio
def cantidad_elementos_cola(c:Cola) -> int:
    contenido = []
    contador: int = 0
    while not c.empty():
        contenido.append(c.get())
        contador += 1
    for elemento in contenido:
        c.put(elemento)
    return contador

#c = Cola()
#c.put(1)
#c.put(4)
#c.put(8)
#print(imprimir_cola (c))
#print(cantidad_elementos_cola(c))
#print(imprimir_cola (c))

#Ejercicio 15   
def buscar_el_maximo_cola(c:Cola[int]) -> int:
    contenido:list[int] = []
    maximo = c.get()
    contenido.append(maximo)
    while not c.empty():
        nuevo_elemento = c.get()
        contenido.append(nuevo_elemento)
        if nuevo_elemento > maximo:
            maximo = nuevo_elemento
    for elemento in contenido:
        c.put(elemento)
    return maximo 

# c = Cola()
# c.put(21)
# c.put(4)
# c.put(12)
# c.put(83)
# print(imprimir_cola (c))
# print(buscar_el_maximo_cola(c))
# print(imprimir_cola (c))

#Ejercicio 16
def armar_secuencia_bingo() -> Cola[int]:
    lista: list[int] = list(range(0,100))
    random.shuffle(lista)
    c: Cola[int] = Cola()
    for elem in lista:
        c.put(elem)
    return c 
# print(imprimir_cola(armar_secuencia_bingo()))


def jugar_carton_de_bingo(carton:list[int],bolillero:Cola[int]) -> int:
    jugadas: int = 0
    numeros_marcados: int = 0
    bolillero_aux: Cola[int] = Cola()
    while numeros_marcados < 12:   #sigo sacando numero hasta que salgan todos los marcados
        bolilla_sacada: int = bolillero.get()
        bolillero_aux.put(bolilla_sacada)   
        if bolilla_sacada in carton:
            numeros_marcados +=1
        jugadas +=1    #una vez que marque todos, paso todas las bolillas restantes al bolillero auxiliar
    while not bolillero.empty():
        bolilla_sacada: int = bolillero.get()
        bolillero_aux.put(bolilla_sacada)    #las devuelvo al bolillero original para que quede igual que antes
    while not bolillero_aux.empty():
        bolilla_sacada: int = bolillero_aux.get()
        bolillero.put(bolilla_sacada)
    return jugadas

# print(jugar_carton_de_bingo([1,20,21,50,71,22,41,28,16,77,51,91],armar_secuencia_bingo()))


#Ejercicio 17
def n_pacientes_urgentes(c:Cola[int,str,str])->int:
    cola_aux = Cola()
    contador: int = 0
    while not c.empty():
        paciente = c.get()
        cola_aux.put(paciente)
        if paciente[0] == 1 or paciente[0] == 2 or paciente[0] == 3:
            contador +=1 
    while not cola_aux.empty():
        paciente_sacado = cola_aux.get()
        c.put(paciente_sacado)
    return contador

# c = Cola()
# c.put((1,"e","r"))
# c.put((4,"m","r"))
# c.put((9,"r","ñ"))
# c.put((3,"w","l"))
# print(imprimir_cola (c))
# print(n_pacientes_urgentes(c))
# print(imprimir_cola (c))



#Ejercicio 18

def atencion_al_cliente(c:Cola[str,int,bool,bool]) -> Cola[str,int,bool,bool]:
    cola_aux: Cola[str,int,bool,bool] = Cola()
    cola_preferencial: Cola[str,int,bool,bool] = Cola()
    cola_prioridad: Cola[str,int,bool,bool] = Cola()
    cola_resto: Cola[str,int,bool,bool] = Cola()
    cola_ordenada: Cola[str,int,bool,bool] = Cola()
    while not c.empty():
        paciente = c.get()
        cola_aux.put(paciente)
        if paciente[3] == True:
            cola_prioridad.put(paciente)
        elif paciente[2] == True:
            cola_preferencial.put(paciente)
        else:
            cola_resto.put(paciente)
    while not cola_aux.empty():
        paciente = cola_aux.get()
        c.put(paciente)
    while not cola_prioridad.empty():
        cola_ordenada.put(cola_prioridad.get())
    while not cola_preferencial.empty():
        cola_ordenada.put(cola_preferencial.get())
    while not cola_resto.empty():
        cola_ordenada.put(cola_resto.get())
    return cola_ordenada

# cola=Cola()
# cola.put(('Jorge',19391293,False,False))
# cola.put(('Andrea',11523351,True,False))
# cola.put(('Adelina',7976723,False,True))
# cola.put(('Roberto',12452413,True,False))
# print(imprimir_cola(cola))
# print(imprimir_cola(atencion_al_cliente(cola)))






#DICCIONARIOS
# claves no repetidas- valores se pueden repetir - claves y valores no necesariamente son del mismo tipo - todas las claves son mismo tipo y todos valores son mismo tipo - 
#lo recorro accediendo a las claves - keys (mas usada), values, items (recorre clave valor) - valor de keys es con get()
#Ejercicio 19
def agrupar_por_longitud(nombre_archivo:str) -> dict[int,int]:
    archivo = open(nombre_archivo)
    res: dict[int,int] = {}   #creo mi diccionario vacio
    lineas=archivo.readlines()
    for i in range(len(lineas)):
        palabras: list[str] = lineas[i].split()    # creo que no puedo usar .split() ver con q reemplazar
        for j in range (len(palabras)):
            long: int = len(palabras[j])
            if long in res.keys():              # me fijo sin longitud esta en las claves de mi diccionario
                res[long] = res[long] + 1
            else:
                res[long] = 1                   # con res[long] accedo al valor  - tb puedo usar get()
    archivo.close()   
    return res 

#Ejercicio 20
def calcular_promedio_por_estudiante_dict(nombre_archivo_notas:str) -> dict[str,float]:
    archivo = open (nombre_archivo_notas)
    promedios : dict[str,float] = {}
    lineas = archivo.readlines()
    for linea in lineas:
        data = linea.rstrip("\n").split(",")
        lu:str = data[0]
        if lu not in promedios:     #si el alumno no esta en el diccionario, calculo su promedio y lo añado
            promedios[lu] = promedio_estudiante(lu)
    archivo.close()
    return promedios

#Ejercicio 21
def frecuencias(nombre_del_archivo:str) -> dict[str,int]:
    archivo = open(nombre_del_archivo)
    lineas = archivo.readlines()
    frec:dict[str,int] = {}
    for linea in lineas:
        palabras = linea.split()
        for palabra in palabras:
            if palabra not in frec:
                frec[palabra] = 1
            else: 
                frec[palabra] +=1
    archivo.close()
    return frec

def la_palabra_mas_frecuente(nombre_del_archivo:str) -> str:
    frec = frecuencias(nombre_del_archivo)
    frecuencia_max: int = 0
    for palabra,frecuencia in frec.items():
        if frecuencia > frecuencia_max:
            frecuencia_max = frecuencia
            palabra_mas_frecuente = palabra 
    return palabra_mas_frecuente
    
# print(la_palabra_mas_frecuente("archivo.txt"))


#Ejercicio 22
#1
historiales: dict[str,Pila] = {}

#2
def visitar_sitio (historiales:dict[str,Pila],usuario:str,sitio:str):
    if usuario in historiales.keys():
        historiales[usuario][0].put(sitio)
    else:
        historiales[usuario] = Pila()
        historiales[usuario][0].put(sitio)
    return historiales

#3
def navegar_atras (historiales:dict[str,Pila],usuario:str)->dict:
    sitio_atras = historiales[usuario][0].get()
    historiales[usuario][1].put(sitio_atras)
    return historiales[usuario][0]

# historiales = {} 
# visitar_sitio(historiales, "Usuario1", "google.com") 
# visitar_sitio(historiales, "Usuario1", "facebook.com") 
# navegar_atras(historiales, "Usuario1") 
# visitar_sitio(historiales, "Usuario2", "youtube.com")

#Ejercicio 23
#1
def agregar_producto(inventario:dict[str,dict[str,float,int]], nombre:str, precio:float, cantidad:int):
    inventario[nombre] ={"$":precio,"cant":cantidad}
    return inventario

#2
def actualizar_stock(inventario:dict[str,dict[str,float,int]], nombre:str, cantidad:int):
    inventario[nombre]["cant"] = cantidad
    return inventario
#3
def actualizar_precios(inventario:dict[str,dict[str,float,int]], nombre:str, precio:int):
    inventario[nombre]["$"] = precio
    return inventario
#4
def calcular_valor_inventario(inventario:dict[str,dict[str,float,int]])-> float:
    total: float = 0
    for producto in inventario:
        total += inventario[producto]["$"] * inventario[producto]["cant"]
    return total

# inventario = {}
# agregar_producto(inventario, 'remera', 20.0, 50)
# agregar_producto(inventario, 'camisa', 30.0, 20)
# print(inventario)
# actualizar_stock(inventario,'remera',10)
# actualizar_precios(inventario,'camisa',35.0)
# print(inventario)
# print(calcular_valor_inventario(inventario))

