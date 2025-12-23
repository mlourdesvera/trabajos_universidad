#ejercicios importantes?
def pertenece_generico(s:[],e) -> bool :
    longitud : int = len(s)
    for elem in s:
        if elem == e:
            return  True
    return False 

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


def perteneceACadaUno(s:[[int]], e:int) -> [bool]:
    res = []
    indice:int = 0
    longitud:int = len(s)
    for lista in s:
        res.append(pertenece_generico (lista, e))
    return res




#importar pila....
from queue import LifoQueue as Pila
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


def ultima_aparicion(s:list , e:int)->int:
    for i in range (len(s)):
        if s[i] == e:
            res = i
    return res




def contar_traducciones_iguales(ingles:dict, aleman:dict) -> int:
    contador:int = 0
    for key in ingles:
        for key2 in aleman:
            if (key==key2) and (ingles[key]==aleman[key2]):
                contador += 1
    return contador



def convertir_a_diccionario(lista:list)-> dict:
    diccionario = dict()
    for elem in lista:
        diccionario[elem] = (lista.count(elem))
    return diccionario

