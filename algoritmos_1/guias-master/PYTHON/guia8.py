# (1) ARCHIVOS
#EJERCICIO 1
#1.1
def contar_lineas(nombre_archivo:str) -> int:
    archivo = open(nombre_archivo, 'r')
    sumador: int = 0
    for linea in archivo.readlines():
        sumadir += 1
    archivo.close()
    return sumador



#1.2
def existe_palabra (palabra:str, nombre_archivo:str) -> bool:
    result = False
    archivo = open (nombre_archivo, 'r')
    for linea in archivo.readlineas():
        if palabra in linea:
            result = True
    archivo.close
    return result

#1.3
def cantidad_de_apariciones (nombre_archivo:str, palabra:str) -> int:
    sumador: int = 0
    archivo = open(nombre_archivo,'r')
    contenidoDelArchivo = archivo.read()
    palabrasDelArchivo = contenidoDelArchivo.split()
    for palabraDelArchivo in palabrasDelArchivo:
        if palabra == palabrasDelArchivo:
            sumador += 1
    archivo.close()
    return sumador

#EJERCICIO 2
def clonar_sin_comentarios(nombre_archivo:str):
    archivo = open(nombre_archivo, 'r')
    archivo_sin_comentarios = open("clon.py","w")
    lineas = archivo.readlines()
    for linea in lineas:
        if not linea.strip()[0] == "#":
            archivo_sin_comentarios.write(linea)
    archivo.close()
    archivo_sin_comentarios.close()

#EJERCICIO 3
def invertir_texto(nombre_archivo:str):
    archivo = open(nombre_archivo,'r')
    lineas = archivo.readlines()
    lineas_al_reves = lineas[::-1]
    reverso = open('reverso.txt','w')
    for linea in lineas_al_reves:
        reverso.write(linea)
    archivo.close()
    reverso.close()

#EJERCICIO 4
def agregar_frase(nombre_archivo:str, frase:str):
    archivo = open(nombre_archivo,'a') 
    archivo.write(frase)
    archivo.close()
#https://recursospython.com/guias-y-manuales/lectura-y-escritura-de-archivos/

#EJERCICIO 5
def agregar_frase_principio(nombre_archivo:str, frase:str):
    archivo = open(nombre_archivo, 'r+')
    contenido = archivo.read()
    archivo.seek(0,0)
    archivo.write(frase.rstrip('\r\n') + '\n' + contenido)
    archivo.close()

#EJERCICIO 6    #no se si esta bien
def binario_to_legible(nombre_archivo:str):
    archivo = open(nombre_archivo,'rb')
    contenido = archivo.read()
    res:[str] = []
    for linea in contenido:
        caracter:str = chr(linea)
        if (caracter>'A' and caracter<'Z') or (caracter>'a' and caracter<'z') or (caracter == '') or (caracter == '_'):
            res.append(chr(linea))
        archivo.close()
        print(res) 


#EJERCICIO 7
def promedioEstudiante(lu:str) -> float:
    archivo = open ('notas.csv','r')
    lineas = archivo.readlines()
    contador:int = 0
    notaAcumulada:int = 0
    for linea in lineas:
        datos = linea.split(",")
        if datos[0] == lu:
            contador += 1
            notaAcumulada += int[datos[3]]
    archivo.close()
    promedio: float = notaAcumulada/contador
    return promedio


# (2)  PILAS
from queue import LifoQueue as Pila
import random
#EJERCICIO 8
def generar_nros_al_az(n:int, desde:int, hasta:int) -> Pila:
    p:Pila = Pila()
    for i in range (0,n):
        p.put(random.randint(desde,hasta))
    return p

#EJERCICIO 9
def cantidad_elementos(p:Pila)->int:
    contenido= []
    contador:int = 0
    while not p.empty():
        contenido.append(p.get())
        contador += 1
    for elemento in contenido[::-1]:
        p.put(elemento)
    return contador
'''#p=Pila()
p.put(1)
p.put(2)
p.put(3)
print(cantidad_elementos(p))
#Esto para chequear que la pila sigue igual que al principio
while not p.empty():
    print(p.get())#'''

#EJERCICIO 10
def buscar_el_maximo(p:Pila)->int:
    maximo:int = p.get()
    while not p.empty():
        nuevo_elemento = p.get()
        if nuevo_elemento > maximo:
            maximo = nuevo_elemento
    return maximo
'''#p=Pila()
p.put(1)
p.put(2)
p.put(3)
print(buscar_el_maximo(p))#'''

#EJERCICIO 11
def esta_bien_balanceada(s:str) -> bool:
    res:bool = True
    p = Pila()
    parentesis_abierto:int = 0
    for letra in s[::-1]:
        p.put(letra)
    while not p.empty():
        letra_sacada = p.get()
        if letra_sacada == "(":
            parentesis_abierto += 1
        if letra_sacada == ")":
            parentesis_abierto -= 1
        if parentesis_abierto < 0:
            res = False
    if parentesis_abierto > 0:
            res = False
    return res 
'''#print(
esta_bien_balanceada("3*(1x2)-(5-4)"),
esta_bien_balanceada("7((2x7)"),
esta_bien_balanceada("8*(9/3))")
)'''
#print(esta_bien_balanceada('1 + (2 x 3 - (20 / 5))'))

#EJERCICIO 12
def evaluar_expresion(expresion:str) -> str:
    operandos = Pila()
    tokens = expresion.split(" ")
    print(tokens)
    for token in tokens:
        if '0' < token <'9' :
            operandos.put(token)
        elif token in ['+','-','*','/']:
            n2 = int(operandos.get())
            n1 = int(operandos.get())
            if token == '+':
                operandos.put(n1+n2)
            if token == '-':
                operandos.put(n1-n2)
            if token == '*':
                operandos.put(n1*n2)
            if token == '/':
                operandos.put(n1/n2)
    return operandos.get()
#print(evaluar_expresion("3 4 + 5 * 2 -"))

# (3)  COLAS
from queue import Queue as Cola
#EJERCICIO 13
def generar_nros_al_azar_cola(n:int,desde:int,hasta:int)-> Cola:
    c = Cola()
    p:Pila = generar_nros_al_az(n,desde,hasta)
    for i in range(0,n):
        c.put(p.get())
    return c
'''c:Cola=generar_nros_al_azar_cola(5,1,10)
while not c.empty():
    print(c.get())'''

#EJERCICIO 14
def cantidad_de_elementos_cola(c:Cola)-> int:
    contenido = []
    contador:int = 0
    while not c.empty():
        contenido.append(c.get())
        contenido += 1
    for elemento in contenido:
        c.put(elemento)
    return contador
'''c=Cola()
c.put(1)
c.put(2)
c.put(3)
c.put(4)
print(cantidad_elementos(c))
#Esto es para chequear que la cola sigue igual que al principio
while not c.empty():
    print(c.get())'''

#EJERCICIO 15
def buscar_el_maximo_cola(c:Cola)->int:
    maximo:int = c.get()
    while not c.empty():
        nuevo_elemento = c.get()
        if nuevo_elemento > maximo:
            maximo = nuevo_elemento
    return maximo
'''c=Cola()
c.put(9)
c.put(2)
c.put(7)
c.put(4)
print(buscar_el_maximo(c))'''

#EJERCICIO 16
#16.1
def armar_secuencia_bingo() -> Cola:
    lista:list[int] = list(range(1,100))
    random.shuffle(lista)
    cola:Cola[int] = Cola()
    for elemento in lista:
        cola.put(elemento)
    return cola 

#16.2
def jugar_carton_del_bingo(carton:list,bolillero:Cola)-> int:
    jugadas:int = 0
    numeros_marcados:int = 0
    bolillero_aux:Cola[int] = Cola()
    #sigo sacando bolillas hasta que marque todos los numeros
    while numeros_marcados < 12:
        bolilla_sacada = bolillero.get()
        bolillero_aux.put(bolilla_sacada)
        if bolilla_sacada in carton:
            numeros_marcados += 1
        jugadas += 1
    #una vez que marque todos, paso todas las bolillas restantes al bolillero auxiliar
    while not bolillero.empty():
        bolilla_sacada:int = bolillero.get()
        bolillero_aux.put(bolilla_sacada)
    #luego, las devuelvo del bolillero auxiliar al original, para que quede igual que al principio
    while not bolillero_aux.empty():
        bolilla_sacada:int = bolillero_aux.get()
        bolillero.put(bolilla_sacada)
    return jugadas
#print(jugar_carton_del_bingo([1,20,21,50,71,22,41,28,9,77,51,91],armar_secuencia_bingo()))

#EJERCICIO 17
def n_pacientes_urgentes(cola:'Cola[(int,str,str)]')->int:
    contador:int = 0
    cola_aux: Cola[(int,str,str)] = Cola()
    while not cola.empty():
        paciente:(int,str,str) = cola.get()
        cola_aux.put(paciente)
        if paciente[0] in [1,2,3]:
            contador += 1
        while not cola_aux.empty():
            paciente:(int,str,str) = cola_aux.get()
            cola.put(paciente)
    return contador

'''cola=Cola()
cola.put((1,'Jorge','gine'))
cola.put((7,'Maria','ocu'))
cola.put((2,'Alejandro','fono'))
cola.put((4,'Martin','cardi'))
print(n_pacientes_urgentes(cola))'''


#EJERCICIO 18
def _a_clientes (cola:Cola)->Cola:
    cola_prioridades:Cola[(str,int,bool,bool)] = Cola()
    cola_preferenciales:Cola[(str,int,bool,bool)] = Cola()
    cola_resto:Cola[(str,int,bool,bool)] = Cola()
    cola_ordenada:Cola[(str,int,bool,bool)] = Cola()
    cola_aux:Cola[(str,int,bool,bool)] = Cola()
    
    while not cola.empty():
        cliente:(str,int,bool,bool) = cola.get()
        cola_aux.put(cliente)
        if cliente[3]:
            cola_prioridades.put(cliente)
        elif cliente[2]:
            cola_preferenciales.put(cliente)
        else:
            cola_resto.put(cliente)

    while not cola_aux.empty():
        cliente:(str,int,bool,bool) = cola_aux.get()
        cola.put(cliente)
    
    while not cola_prioridades.empty():
        cola_ordenada.put(cola_prioridades.get())
    while not cola_preferenciales.empty():
        cola_ordenada.put(cola_preferenciales.get())
    while not cola_resto.empty():
        cola_ordenada.put(cola_resto.get())

    return cola_ordenada
'''cola=Cola()
cola.put(('Jorge',19391293,False,False))
cola.put(('Andrea',11523351,True,False))
cola.put(('Adelina',7976723,False,True))
cola.put(('Roberto',12452413,True,False))
cola_ordenada=_a_clientes(cola)
while not cola_ordenada.empty():
    print(cola_ordenada.get())'''


# (4)  DICCIONARIOS
#EJERCICIO 19
def agrupar_por_longitud(nombre_archivo:str) -> dict:
    archivo = open(nombre_archivo,'r',encoding='utf8')
    res:dict[int] = {}
    lineas = archivo.readlines()
    for linea in lineas:
        palabras = linea.split()
        for palabra in palabras:
            longitud = len(palabra)
            if longitud in res:
                res[longitud] += 1
            else:
                res[longitud] = 1
    archivo.close()
    return res


#EJERCICIO 20
def promedio_alumno()-> dict:
    archivo = open('notas.csv','r')
    lineas = archivo.readlines()
    promedios:dict = {}

    for linea in lineas: 
        data = linea.rstrip('\n').split(',')
        lu:str = data[0]
        #si el alumno no esta en el diccionario de promedios, calculo su promedio y lo añado
        if lu not in promedios:
            promedios[lu] = promedioEstudiante(lu)

    archivo.close()
    return promedios

#EJERCICIO 21
def frecuencias(nombre_archivo:str)->dict:
    archivo = open(nombre_archivo,'r', encoding='utf8')
    lineas = archivo.readlines()
    frec:dict = {}

    for linea in lineas: 
        palabras = linea.split()
        for palabra in palabras:
            if palabra not in frec:
                frec[palabra] = 1
            else:
                frec[palabra] += 1
    archivo.close()
    return frec

def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    frec = frecuencias(nombre_archivo)
    la_palabra_mas_frecuente:str
    frecuencia_max:int = 0

    for palabra,frecuencia in frec.items():
        if frecuencia >frecuencia_max:
            frecuencia_max = frecuencia
            palabra_mas_frecuente = palabra

    return palabra_mas_frecuente
#print(la_palabra_mas_frecuente('ej1.txt'))

#EJERCICIO 22
#22.1
historiales = dict()
#22.2
def visitar_sitio(historiales:'dict[str,(Pila,Pila)]', usuario:str, sitio:str)->dict:
    if usuario in historiales.keys():
        historiales[usuario][0].put(sitio)
    else:
        historiales[usuario] = (Pila(),Pila())
        historiales[usuario][0].put(sitio)
    return historiales
#22.3
def navegar_atras(historiales: 'dict[str,(Pila,Pila)]', usuario:str) -> dict:
    sitio_atras = historiales[usuario][0].get()
    historiales[usuario][1].put(sitio_atras)
    return historiales[usuario][0].queue
#22.4
def navegar_adelante(historiales: 'dict[str,(Pila,Pila)]', usuario:str) -> dict:
    sitio_adelante = historiales[usuario][1].get()
    historiales[usuario][0].put(sitio_adelante)
    return historiales[usuario][0].queue


'''visitar_sitio(historiales,'martin','netflix.com')
#print(historiales)
visitar_sitio(historiales,'martin','apple.com')
print(navegar_atras(historiales, 'martin'))
visitar_sitio(historiales, 'martin','youtube.com')
print(navegar_adelante(historiales,'martin'))'''


#EJERCICIO 23
inventario = {}
#23.1
def agregar_producto(invertario:dict, nombre:str, precio:float, cantidad:int) -> dict:
    inventario[nombre] = {'precio':precio, 'cantidad':cantidad}
    return inventario
#23.2
def actualizar_stock(inventario, nombre, cantidad) -> dict:
    inventario[nombre]['cantidad'] = cantidad
    return inventario
#23.3
def actualizar_precios(inventario, nombre, precio)-> dict:
    inventario[nombre]['precio'] = precio
    return inventario
#23.4
def calcular_valor_inventario(inventario) -> float:
    total:int = 0
    for producto in inventario:
        total += inventario[producto]['precio'] + inventario[producto]['cantidad']
    return total


'''agregar_producto(inventario, 'remera', 20.0, 50)
agregar_producto(inventario, 'camisa', 30.0, 30)
print(actualizar_stock(inventario,'remera',10))
actualizar_precios(inventario,'remera',120)
print(calcular_valor_inventario(inventario))'''

