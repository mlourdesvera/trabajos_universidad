module MisFunciones where 
  
quitar:: (Eq t) => t-> [t]-> [t]
quitar _ [] = []
quitar n (x:xs) | n /= x && xs == [] = [x]
                | n == x = xs 
                | n /= x && (not (pertenece n xs)) = (x:xs)
                | otherwise = [x] ++ quitar n xs 

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece n l | longitud l == 0 = False
              | n == head l = True
              | otherwise = pertenece n (tail l)

longitud:: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs
