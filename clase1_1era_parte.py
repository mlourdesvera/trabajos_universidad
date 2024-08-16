a = "Hoy es lunes"
#print (a)

#print(a[2])

lista=['Ana','Juan']
s= f'lista de alumnos:\n{lista}'
#print (s)

frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'
lista_frutas = frutas.split(',') # separa en las comas
#print(lista_frutas)

def es_palindromo(palabra:str)->bool:
    res = False
    if len(palabra)==5:
        if palabra[0] == palabra[4] and palabra[1] == palabra[3]:
            res = True
    return res 

#print(es_palindromo('jujuy'))
#print(es_palindromo('nadan'))

def es_palindromo_2 (palabra:str)->bool:
    res = True
    longitud = len (palabra)
    if longitud != 5: 
         res = False
    for i in range(0,longitud//2):
        if palabra[i] != palabra[((longitud-1 )- i)]:
            res = False
    return res

#print(es_palindromo_2('jujuy'))
#print(es_palindromo_2('nadan'))


def palindromo(palabra):
    return palabra [0:3] == palabra[-1:-4:-1]    # -1:-4 de donde a donde va ,el ultimo -1 da vuelta la palabra
#print(palindromo('nadan'))

def divisible13():
    numero = 0
    while numero <214:
        if numero % 13 == 0:
            print (numero)
        numero +=1
    
#print(divisible13())

def alturaBilletesObelisco():
    dias= 1
    alturaObelisco = 67500
    pilaBilletes = 0.11
    while pilaBilletes < alturaObelisco:
        pilaBilletes = pilaBilletes*2
        dias += 1
    return dias 

#print(alturaBilletesObelisco())

