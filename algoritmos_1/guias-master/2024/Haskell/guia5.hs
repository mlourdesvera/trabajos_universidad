--EJERCICIO 1
--1
longitud:: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

--2
ultimo:: [t] -> t
ultimo (x:[]) = x 
ultimo (x:y:xs) = ultimo (y:xs)

--3
principio:: [t] -> [t]
principio (x:xs) | longitud (x:xs) == 1 = []
                 | otherwise = x : principio xs 

--4
reverso::(Eq t) =>  [t] -> [t]
reverso [] = []
reverso (x:xs) | xs == [] = [x]
               | otherwise = reverso xs ++ [x]


--EJERCICIO 2
--1 
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece n l | longitud l == 0 = False
              | n == head l = True
              | otherwise = pertenece n (tail l)

--2
todosIguales:: (Eq t) => [t] -> Bool
todosIguales (x:xs) | xs == [] = True
                    | x /= head xs = False
                    | otherwise = todosIguales xs 

--3 
todosDistintos:: (Eq t) => [t] -> Bool
todosDistintos (x:xs) | xs == [] = True
                      | pertenece x xs = False
                      | otherwise = todosDistintos xs 

--4
hayRepetidos:: (Eq t) => [t] -> Bool
hayRepetidos (x:xs) | xs == [] = False
                    | pertenece x xs = True
                    | otherwise = hayRepetidos xs 

--5
quitar:: (Eq t) => t-> [t]-> [t]
quitar _ [] = []
quitar n (x:xs) | n /= x && xs == [] = [x]
                | n == x = xs 
                | n /= x && (not (pertenece n xs)) = (x:xs)
                | otherwise = [x] ++ quitar n xs 
 
--6
quitarTodos:: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) | n /= x && xs == [] = [x]
                     | n == x && xs == [] = []
                     | n == x = quitarTodos n xs 
                     | otherwise = [x] ++ quitarTodos n xs 

--7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = [x] ++ quitarTodos x (eliminarRepetidos xs )
                         | otherwise = [x] ++ eliminarRepetidos xs 

--8 
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos xs ys = mismosElementosAux xs ys && mismosElementosAux ys xs 

mismosElementosAux :: (Eq t) => [t] -> [t] -> Bool
mismosElementosAux [] ys = True
mismosElementosAux (x:xs) ys = pertenece x ys && mismosElementosAux xs ys 

--9
capicua:: (Eq t) => [t] -> Bool
capicua [] = True
capicua xs = xs == reverso xs 


--EJERCICIO 3
--1
sumatoria:: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs 

--2
productoria:: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs 

--3
maximo:: [Integer] -> Integer
maximo [x] = x 
maximo (x:xs) = maximoAux x xs 

maximoAux:: Integer -> [Integer] -> Integer 
maximoAux n (x:xs) | xs == [] && x > n = x 
                   | xs == [] = n 
                   | x >= n = maximoAux x xs 
                   | otherwise = maximoAux n xs  

--4
sumarN:: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = [(n+x)] ++ sumarN n xs 

--5
sumarElPrimero:: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = [x] ++ sumarN x (xs) --NO SE SI EL PRIMERO SE SUMA O NO (REVISAR)