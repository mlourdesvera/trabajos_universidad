def prueba():
    print ("Funciona")
#tendria que poner prueba() para ejecutarlo en la terminal

def imprimir_hola():
    print("Hola")

def es_multiplo_de(n:int,m:int) -> bool:
    res : bool = (n%m)==0 # mod n m == 0
    return res  

def es_nombre_largo(nombre:str) -> bool:
    res : bool = 3<=len(nombre) and len(nombre)<=8 #&& ahora es and
    return res 

def devolver_el_doble_si_es_par( n : int ) -> int:
    if es_multiplo_de(n,2):
        res : int = 2*n 
    else:
        res : int = n 
    return res 

def imprimir_pares():
    i : int = 10
    while i<=40 :
        if es_multiplo_de(i,2): #esto no es necesario pero tb funciona (como el de abajo)
            print(i)        
        i=i+2
#misma funcion usando for
def imprimir_pares_for():
    for i in range (10, 41, 2):
        print(i)

