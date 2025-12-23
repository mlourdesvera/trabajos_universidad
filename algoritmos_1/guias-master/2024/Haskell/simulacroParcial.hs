relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((p1,p2):rs) = cadaRelValida && noHayRelRepetidas && relacionesValidas rs
              where 
                cadaRelValida = p1 /= p2
                noHayRelRepetidas = not (pertenece (p1,p2) rs) && not (pertenece (p2,p1) rs)

pertenece::(Eq t) => t -> [t] -> Bool
pertenece n l | l == [] = False
              | n == head l = True
              | otherwise = pertenece n (tail l) 




personas :: [(String, String)] -> [String]
personas rs = eliminarRepetidos (personasAux rs)

personasAux:: [(String, String)] -> [String]
personasAux [] = []
personasAux ((p1,p2):xs) = p1 : p2 : personasAux xs 

eliminarRepetidos :: [String] -> [String]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = pasoRecursivo
                         | otherwise = x : pasoRecursivo 
                    where 
                      pasoRecursivo = eliminarRepetidos xs 




amigosDe:: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe p ((p1,p2):xs) | (p == p1) = p2 : pasoRecursivo
                        | (p == p2) = p1 : pasoRecursivo
                        | otherwise = pasoRecursivo
                    where
                      pasoRecursivo = amigosDe p xs 




personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos rs = maximo listaPersonas cantAmigosPersonas
                where
                  listaPersonas = personas rs 
                  cantAmigosPersonas = cantidaDeAmigos listaPersonas rs 

cantidaDeAmigos:: [String] -> [(String,String)] -> [Int]
cantidaDeAmigos [] _ = []
cantidaDeAmigos (p:ps) rs = (cantidadDeAmigosDe p rs) : (cantidaDeAmigos ps rs)

maximo:: [String] -> [Int] -> String
maximo [p] _ = p 
maximo (p0:p1:ps) (c0:c1:cs) | c0 > c1 = maximo (p0:ps) (c0:cs)
                             | otherwise = maximo (p1:ps) (c1:cs)

cantidadDeAmigosDe:: String -> [(String,String)] -> Int
cantidadDeAmigosDe p rs = longitud (amigosDe p rs)

longitud:: [t] -> Int
longitud [] = 0 
longitud (x:xs) = 1 + longitud xs 