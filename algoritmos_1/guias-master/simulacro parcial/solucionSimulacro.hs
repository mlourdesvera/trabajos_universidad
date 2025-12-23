--solucion
--ej1
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((p1,p2),rs) = p1 /= p2 && not (pertenece (p1,p2) rs) && not (pertenece (p2,p1) rs) && relacionesValidas rs


--ej2 
personas:: [(String, String)] -> [String]
personas rs = sacarRepes (personasConRepes rs)

personasConRepes :: [(String, String)] -> [String]
personasConRepes [] = []
personasConRepes ((p1, p2):rs) = p1 : p2 : personasConRepes rs

sacarRepes :: (Eq t) => [t] -> [t]
sacarRepes [] = []
sacarRepes (x:xs) | pertenece x xs = pasoRecursivo
                  | otherwise = x : pasoRecursivo 
                  where pasoRecursivo = sacarRepes xs
        
pertenece:: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece y (x:xs) | y == x = True
                   | otherwise = pertenece y xs 

--ej 3
amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe p ((p1, p2):rs) |p == p1 = p2 : pasoRecursivo
                         |p == p2 = p1 : pasoRecursivo
                         |otherwise = pasoRecursivo
                         where pasoRecursivo = amigosDe p rs

--ej 4
personaConMasAmigos::[(String, String)] -> [String]
personaConMasAmigos rs = personaConMasAmigosAux (personas rs) rs

personaConMasAmigosAux:: String -> [(String, String)] -> [String]
personaConMasAmigosAux [x] rels = x
personaConMasAmigosAux (x:(y:ys)) rels | cantidadDeAmigosDe x rels >= cantidadDeAmigosDe y rels = personaConMasAmigosAux (x:ys) rels
                                       | otherwise = personaConMasAmigosAux (y:ys) rels

cantidadDeAmigosDe::String -> [(String, String)] -> Int
cantidadDeAmigosDe p rs = length (amigosDe p rs)