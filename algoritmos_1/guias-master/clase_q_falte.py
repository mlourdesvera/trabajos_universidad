def clonarSinComentarios (nombre_archivo:str):
    #abro el archivo para leer
    archivo = open (nombre_archivo,"r")
    #abro el archivo en el que voy a escribir
    arch_sin_comentarios = open ("clonadoSinComentarios.py","w")
    # leo todas las lineas
    lineas = archivo.readlines()
    for linea in lineas:
        #si no una linea NO comienza con # entoces la escribo
        #if not linea.lstrip().startswith("#"):
        if not linea.strip()[0] == "#":
            arch_sin_comentarios.write(linea)
    archivo.close()
    arch_sin_comentarios.close()

#clonarSinComentarios ("conComentarios.py") #esto lo uso para probar (conComentarios.py es un archivo que hay que crear)

#ejemplos de pila y cola

from queue import LifoQueue as Pila

p= Pila()
p.put(1) #apilar
p.put(2) #apilar
p.put(3) #apilar
print(list(p.queue))
elemento = p.get()
print(elemento) #desapilar
print(p.empty()) #vacia ?
print(list(p.queue))

from queue import Queue as Cola

c= Cola()
c.put(1) #encolar
c.put(2) #encolar
c.put(3) #encolar
print(list(c.queue))
elemento= c.get()
print(elemento) #desapilar
print(c.empty()) #vacia ?
print(list(c.queue))

#ej 10 (este lo hizo el profe pero dice que no cumplia con la especificacion o algo asi 
#xq arruina la pila y no se podria denuevo de la misma forma??)

def buscarElMaximo_malHecho(p:Pila) -> int:
    maximo= p.get()
    while (not p.empty()):
        elem= p.get()
        if (elem>maximo):
            maximo = elem
    return maximo

p.put(43)
print(buscarElMaximo_malHecho(p))

#ej 10 bien hecho

def buscarElMaximo(p:Pila) -> int:
    res: int = p.get()
    paux: Pila = Pila()
    while not p.empty():
        elem: int = p.get()
        paux.put(elem)
        if elem>res:
            res=elem
    while not paux.empty():
        elem = paux.get()
        p.put(elem)

    return res

##version con especificacion que NO garantiza nada sobre la pila
# en el caso de que la lista sea vacia, devuelve None
#no lo copie bien!!!

def buscarElMaximo2(p:Pila) -> int:
    res: int = None
    paux: Pila = Pila()
    while not p.empty():
        elem: int = p.get() 
        paux.put(elem)
        if elem>res:
            res=elem
    while not paux.empty():
        elem = paux.get()
        p.put(elem)

    return res

#contar los elem de una pila
def ContarElemPila (p:Pila) -> int:
    res:int = 0
    paux: Pila = Pila()
    while not p.empty():
        elem:int= p.get()
        paux.put(elem)
        res= res + 1
    while not paux.empty():
        elem = paux.get()
        p.put(elem)

    return res

print(ContarElemPila(p))
#LO DE ARRIBA me da 0 xq en la pila no hay nada, si quiero probarlo con otro resultado 
# deberia hacer un p.put(1) o cualquiero otro num la cant de veces q quiera

#como armo una lista con los numeros del 0 al 9:
#lista: list = list(range(0,10))
#desordena de forma random la lista (hay que importar arriba random)
#random.shuffle(lista)

# EJERCICIO 16 

#esto lo hice yo
import random

def armarSecuenciaDeBingo_mio ():
    c= Cola()
    lista: list = list(range(0,100))
    random.shuffle(lista)
    for numero in lista:
        c.put(numero)
    return c

#lo q hizo el profe:

def armarSecuenciaDeBingo() -> Cola:
    lista: list = list(range(0,100))
    random.shuffle(lista)
    bolillero: Cola = Cola()
    for bolilla in lista:
        bolillero.put(bolilla)
    return bolillero
    
#print (armarSecuenciaDeBingo())

def jugarCartonDeBingo(carton:list,bolillero:Cola):
    cantSinMarcar: int = len(carton)
    jugadas: int= 0
    bolilleroAux: Cola = Cola()
    #mientras no marque todos los numeros del carton saco bolillas
    while cantSinMarcar>0:
        num:int= bolillero.get()
        bolilleroAux.put(num)
        if num in carton:
            cantSinMarcar -= 1
        jugadas +=1
    while not bolillero.empty():
        num:int = bolillero.get()
        bolilleroAux.put(num)
    while not bolilleroAux.empty():
        num:int= bolilleroAux.get()
        bolillero.put(num)
    return jugadas

#diccionario
#ej19
def agruparPorLongitud(nombre_archivo:str) -> dict:
    archivo= open(nombre_archivo,"r")
    d= dict()

    lineas= archivo.readlines()

    for linea in lineas:
        palabras= linea.split() #hace una lista con las palabras
        for palabra in palabras:
            longitud= len(palabra)
            if (longitud in d): #aca toma como que d[longitud] ya existe en el diccionario
                d[longitud] += 1
            else: 
                d[longitud]= 1 #aca como no existe le asigna un valor
    return d 

#ej21
def frecuencias(nombre_archivo:str)-> str:
    archivo= open(nombre_archivo,"r")
    frec= dict()
    lineas= archivo.readlines()
    for linea in lineas:
        palabras= linea.split()
        for palabra in palabras:
            if palabra in frec:
                frec[palabra] +=1
            else:
                frec[palabra] = 1
    archivo.close()
    return frec
            
def laPalabraMasFrecuente (nombre_archivo:str)-> str:
    dicFrec= frecuencias(nombre_archivo)
    frecuenciaMaxima:int= 0
    palabraMaxima: str
    for palabra,frecuencia in dicFrec.items():
        if (frecuencia>frecuenciaMaxima):
            frecuenciaMaxima = frecuencia
            palabraMaxima= palabra

    return palabraMaxima

print (laPalabraMasFrecuente("archivo_palabras.txt")) #hay q crear el archivo_palabras.txt
