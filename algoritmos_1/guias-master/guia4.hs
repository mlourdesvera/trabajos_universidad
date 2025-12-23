--EJERCICIO 1
fibonacci:: Int-> Int
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci (n-1) + fibonacci (n-2)

--EJERCICIO 2
parteEntera:: Float -> Int
parteEntera x | (x < 1) && (x >= 0) = 0
              | (x > -1) && (x < 0) = -1
              | (x >= 1) = 1 + parteEntera (x-1)
              | otherwise = (-1) + parteEntera (x+1) 

--EJERCICIO 3
esDivisible:: Int -> Int -> Bool
esDivisible x n | x == 0 = True
                | x < 0 = esDivisible (x+n) n
                | x < n = False
                | otherwise = esDivisible (x-n) n

--EJERCICIO 4
sumaImpares:: Int -> Int
sumaImpares n | n == 1 = 1
              | n > 1 =  sumaImpares (n-1) + ((2*(n-1))+1)
 
--EJERCICIO 5
medioFact:: Int -> Int
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = n * medioFact(n-2)

--EJERCICIO 6
sumaDigitos:: Int -> Int
sumaDigitos n | n < 10 = n
              | otherwise = mod n 10 + sumaDigitos(div n 10) 

--EJERCICIO 7
todosDigitosIguales:: Int -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = (digitoUnidades n == digitoUnidades (sacarUnidades n)) && todosDigitosIguales (sacarUnidades n)

digitoUnidades:: Int -> Int
digitoUnidades n = mod n 10

sacarUnidades:: Int -> Int
sacarUnidades n = div n 10
                      
--EJERCICIO 8
iesimoDigito:: Int -> Int -> Int
iesimoDigito n i = mod (div n (10^(cantDigitos(n)-i))) 10

cantDigitos:: Int -> Int
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos(sacarUnidades n)

--EJERCICIO 9
esCapicua:: Int -> Bool
esCapicua n | n < 10 = True
            | n == darVuelta n = True
            | otherwise = False

darVuelta:: Int -> Int
darVuelta n | cantDigitos n == 1 = n
            | otherwise = (digitoUnidades n*10^(cantDigitos n-1)) + darVuelta(sacarUnidades n)

--EJERCICIO 10
--a
f1 :: Int -> Int
f1 0 = 1
f1 n = 2^n + f1 (n-1)
--b
f2 :: Int -> Float -> Float
f2 0 _ = 0
f2 1 q = q
f2 n q = q^n + f2 (n-1) q
--c
f3 :: Int -> Float -> Float
f3 0 q = 1
f3 1 q = q + q^2
f3 n q = q^(2*n) + q^((2*n)-1) + f3 (n-1) q
--d 
f4 :: Int -> Float -> Float
f4 0 q = 1
f4 1 q = q + q^2
f4 n q = f3 n q - f2 (n-1) q

--EJERCICIO 11
eAprox:: Int -> Float
eAprox 0 = 1
eAprox 1 = 2
eAprox n = (1 / fromIntegral( factorial n)) + eAprox (n-1)

factorial::Int -> Int
factorial 0 = 1
factorial 1 = 1
factorial n = n * factorial (n-1)

e:: Float
e = eAprox 10

--EJERCICIO 12
raizDe2Aprox:: Int -> Float
raizDe2Aprox 1 = 1
raizDe2Aprox n = (sucesionAux n) -1

sucesionAux:: Int -> Float
sucesionAux 1 = 2
sucesionAux n = 2 + (1/sucesionAux (n-1))

--EJERCICIO 13
sumatoriaDoble:: Int -> Int -> Int
sumatoriaDoble 0 _ = 0
sumatoriaDoble n m = (sumatoriaDesdeM n m) + sumatoriaDoble (n-1) m 

sumatoriaDesdeM :: Int -> Int -> Int
sumatoriaDesdeM i 0 = 0
sumatoriaDesdeM i m = i^m + sumatoriaDesdeM i (m-1)

--EJERCICIO 14
sumaPotencias:: Int -> Int -> Int -> Int
sumaPotencias q n m | n == 0 = 0
                    | otherwise = sumaDeM q n m + sumaPotencias q (n-1) m

sumaDeM:: Int -> Int -> Int -> Int
sumaDeM q n m | m == 0 = 0
              | otherwise = q^(n+m) + sumaDeM q n (m-1)

--EJERCICIO 15
sumaRacionales:: Int -> Int -> Float
sumaRacionales 0 m = 0
sumaRacionales n m = sumatoriaDeM n m + sumaRacionales (n-1) m 

sumatoriaDeM:: Int -> Int -> Float 
sumatoriaDeM n 1 = fromIntegral n
sumatoriaDeM n m = (fromIntegral n / fromIntegral m) + sumatoriaDeM n (m-1)

--EJERCICIO 16
--a
menorDivisor:: Int -> Int
menorDivisor n = menorDivisorAux n 2

menorDivisorAux:: Int -> Int -> Int
menorDivisorAux n k | mod n k == 0 = k
                    | otherwise = menorDivisorAux n (k+1)
    
--b
esPrimo :: Int -> Bool
esPrimo n | menorDivisor n == n = True
          | otherwise = False
        
--c
sonCoprimos:: Int -> Int -> Bool
sonCoprimos n m | n == 1 = True
                | m == 1 = True
                | esPrimo n && esPrimo m = True
                | (mod n m == 0) || (mod m n == 0) = False
                | n > m = sonCoprimos n (m-1)
                | m > n = sonCoprimos (n-1) m

--d
nEsimoPrimo:: Int -> Int
nEsimoPrimo 1 = 2
nEsimoPrimo n = proximoPrimo (nEsimoPrimo (n-1) + 1)

proximoPrimo:: Int -> Int
proximoPrimo n | esPrimo n = n
               | otherwise = proximoPrimo (n+1)

--EJERCICIO 17
esFibonacci:: Int -> Bool
esFibonacci n = esFibonacciAux n 0 

esFibonacciAux:: Int -> Int -> Bool
esFibonacciAux n i | n == fibonacci i = True
                   | fibonacci i > n = False
                   | otherwise = esFibonacciAux n (i+1)

--EJERCICIO 18
mayorDigitoPar:: Int -> Int
mayorDigitoPar n | n < 10 && par n = n
                 | n < 10 = -1
                 | par (digitoUnidades n) = max (digitoUnidades n) resultadoRecursion
                 | otherwise = resultadoRecursion
        where 
            par a = mod a 2 == 0
            resultadoRecursion = mayorDigitoPar (div n 10)

--EJERCICIO 19
sumaInicialDePrimos::Int -> Bool
sumaInicialDePrimos n = sumaInicialDePrimosAux n 1 

sumaInicialMPrimos:: Int -> Int
sumaInicialMPrimos m | m == 1 = 2
                     | otherwise = nEsimoPrimo m + sumaInicialMPrimos (m-1)

sumaInicialDePrimosAux:: Int -> Int -> Bool
sumaInicialDePrimosAux n m | sumaInicialMPrimos m == n = True
                           | sumaInicialMPrimos m > n = False
                           | otherwise = sumaInicialDePrimosAux n (m+1)

--EJERCICIO 20
--NO LO ENTENDI!! NO ENTENDI QUE ME PIDE
tomaValorMax:: Int -> Int -> Int
tomaValorMax n1 n2 | sumaDivisores n2 == comparaValores n1 n2 = n2
                   | otherwise = tomaValorMax n1 (n2-1)

comparaValores:: Int -> Int -> Int
comparaValores a b | a == b = b 
                   | otherwise = max (sumaDivisores b) (sumaDivisores (comparaValores a (b-1)))

sumaDivisores:: Int -> Int
sumaDivisores n = sumaDivisoresHasta n n 

sumaDivisoresHasta:: Int -> Int -> Int
sumaDivisoresHasta n i | i == 0 = 0
                       | mod n i == 0 = i + sumaDivisoresHasta n (i-1)
                       | otherwise = sumaDivisoresHasta n (i-1)

--EJERCICIO 21  
pitagoras:: Int -> Int -> Int -> Int
pitagoras m n r | n == 0 = sumaTernas m 0 r 
                | otherwise = sumaTernas m n r + pitagoras m (n-1) r 

sumaTernas:: Int -> Int -> Int -> Int
sumaTernas m n r | m == 0 && esTernaPiatgorica m n r = 1
                 | m == 0 = 0
                 | esTernaPiatgorica m n r = 1 + sumaTernas (m-1) n r 
                 | otherwise = sumaTernas (m-1) n r 
            where
                esTernaPiatgorica a b c = a^2 + b^2 <= c^2
