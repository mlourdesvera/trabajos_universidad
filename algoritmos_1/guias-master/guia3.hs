doubleMe:: Int -> Int
doubleMe x = x + x

--EJERCICIO 1
--a
f:: Int -> Int
f x |x == 1 = 8
    |x == 4 = 131
    |x == 16 = 16

--b
{-problema g (n:Z):Z{
    req: {n = 8 ∨ n = 16 ∨ n= 131}
    ase: {(n = 8 -> result = 16) ∧ (n = 16 -> result = 4) ∧ (n = 131 -> result = 1)}
}
-}
g:: Int -> Int
g x |x == 8 = 16
    |x == 16 = 4
    |x == 131 = 1

--c       
--h= fog
h:: Int -> Int
h x = f(g (x))
--k=gof
k:: Int -> Int
k x = g(f (x))

--EJERCICIO 2  (FALTA ESPECIFICAR!!!)
--a
absoluto:: Int -> Int
absoluto x | x > 0 = x
           | x < 0 = -x
           | otherwise = 0


--b
maximoAbsoluto:: Int -> Int -> Int
maximoAbsoluto x y | absoluto x > absoluto y = absoluto x
                   | absoluto x < absoluto y = absoluto y
                   | otherwise = absoluto x

--c
{-problema maximo3 (x,y,z:Z): Z{
    requiere: True
    asegura: { res es igual a x, o a y o a z}
    asegura: { res es mayor o igual a x, y a y, y a z}
} 
-}
maximo3:: Int -> Int -> Int -> Int
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | z >= x && z >= y = z 

--d  (FALTA HACERLO CON PATTERN MATCHING)
algunoEs0:: Float -> Float -> Bool
algunoEs0 x y | x == 0 || y == 0 = True
              | otherwise = False

--e  (FALTA HACERLO CON PATTERN MATCHING)
ambosSon0:: Float -> Float -> Bool
ambosSon0 x y | x == 0 && y == 0 = True
              | otherwise = False

--f  (−∞, 3], (3, 7] y (7, ∞),
mismoIntervalo:: Float -> Float -> Bool
mismoIntervalo x y | (x <= 3) && (y <= 3) = True
                   | ((x > 3) && (x <= 7)) && ((y > 3) && (y <= 7)) = True
                   | (x > 7) && (y > 7) = True
                   | otherwise = False 

--g 
{-problema sumaDistintos (x,y,z: Z) : Z {
requiere: { - }
asegura: {si los 3 parametros son distintos entonces res = x + y + z}
asegura: {si 2 parametros son iguales, res es igual al no repetido}
asegura: {si los 3 parametros son iguales, res = 0}
}
-}
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | (x /= y) && (y /= z) && (x /= z) = x + y + z 
                    | (x == y) && (y /= z) = x + z 
                    | (x /= y) && (y == z) = x + y 
                    | (x == z) && (y /= z) = y + z
                    | (x == y) && (y == z) = 0 

--h 
esMultiplo:: Int -> Int -> Bool 
esMultiplo x y | mod x y == 0 = True
               | otherwise = False

--i
digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10

--j
digitoDecenas :: Int -> Int
digitoDecenas x = div (mod x 100) 10

--EJERCICIO 3
estanRelacionados:: Int -> Int -> Bool
estanRelacionados a b | mod a b == 0 = True
                      | otherwise = False

--EJERCICIO 4
--a
prodInt:: (Float,Float) -> (Float,Float) -> Float
prodInt (a,b) (c,d) = (a*c) + (b*d)

--b
todoMenor:: (Float,Float) -> (Float,Float) -> Bool 
todoMenor (a,b) (c,d) | (a < c) &&  (b < d) = True
                      | otherwise = False

--c 
distanciaPuntos:: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos (a,b) (c,d) = sqrt((c-a)^2+(d-b)^2)

--d
sumaTerna:: (Int,Int,Int) -> Int
sumaTerna (a,b,c) = a + b + c

--e
sumarSoloMultiplos:: (Int,Int,Int) -> Int -> Int
sumarSoloMultiplos (a,b,c) n | ((mod a n == 0) && (mod b n == 0) && (mod c n == 0)) = a + b + c
                             | ((mod a n /= 0) && (mod b n == 0) && (mod c n == 0)) = b + c
                             | ((mod a n == 0) && (mod b n /= 0) && (mod c n == 0)) = a + c
                             | ((mod a n == 0) && (mod b n == 0) && (mod c n /= 0)) = a + b 
                             | ((mod a n == 0) && (mod b n /= 0) && (mod c n /= 0)) = a
                             | ((mod a n /= 0) && (mod b n == 0) && (mod c n /= 0)) = b
                             | ((mod a n /= 0) && (mod b n /= 0) && (mod c n == 0)) = c
                             | otherwise = 0

--f 
posPrimerPar:: (Int,Int,Int) -> Int
posPrimerPar (a,b,c) | mod a 2 == 0 = 1
                     | mod b 2 == 0 = 2
                     | mod c 2 == 0 = 3
                     | otherwise = 4

--g   
crearPar:: t -> t -> (t,t)
crearPar a b = (a,b)

--h
invertir :: (t,t) -> (t,t)
invertir (a,b) = (b,a)

--EJERCICIO 5 (f_ y g_ pq ya tengo f y g)
todosMenores:: (Int,Int,Int) -> Bool
todosMenores (t0,t1,t2) | ((f_(t0) > g_(t0)) && (f_(t1) > g_(t1)) && (f_(t2) > g_(t2))) = True
                        | otherwise = False

f_:: Int -> Int
f_ n | ( n <= 7) = n^2
     | otherwise = (2*n) - 1

g_:: Int -> Int
g_ n | mod n 2 == 0 = div n 2 
     | otherwise = (3*n) + 1

--EJERCICIO 6
bisiesto :: Int -> Bool
bisiesto n | (mod n 4 /= 0) || ((mod n 100 == 0) && (mod n 400 /= 0)) = False
           | otherwise = True

--EJERCICIO 7 
distanciaManhattan :: (Float,Float,Float) -> (Float,Float,Float) -> Float
distanciaManhattan (p0,p1,p2) (q0,q1,q2) = (absoluto_ (p0-q0)) + (absoluto_ (p1-q1)) + (absoluto_ (p2-q2))

absoluto_:: Float -> Float
absoluto_ x | x > 0 = x
            | x < 0 = -x
            | otherwise = 0

--EJERCICIO 8 
comparar:: Int -> Int -> Int
comparar a b | sumaUltimosDosDigitos (a) < sumaUltimosDosDigitos (b) = 1
             | sumaUltimosDosDigitos (a) > sumaUltimosDosDigitos (b) = -1
             | sumaUltimosDosDigitos (a) == sumaUltimosDosDigitos (b) = 0

sumaUltimosDosDigitos:: Int -> Int
sumaUltimosDosDigitos x = (mod (absoluto x) 10) + (mod (div (absoluto x) 10) 10)