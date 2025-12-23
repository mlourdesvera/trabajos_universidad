import Data.Char
-- EJ 7
frecuencia :: String -> [Float]
frecuencia _ = [16.666668,0.0,0.0,0.0,16.666668,0.0,0.0,0.0,0.0,0.0,0.0,33.333336,0.0,0.0,0.0,0.0,0.0,16.666668,0.0,16.666668,0.0,0.0,0.0,0.0,0.0,0.0]

--del ejercicio 2 saco
letraANatural :: Char -> Int
letraANatural  c = ord c - ord 'a'


longitudPalabra:: String -> Int
longitudPalabra [] = 0
longitudPalabra (x:xs) = 1 + longitudPalabra xs 


porcentajeLetra :: Char -> String -> Float
porcentajeLetra _ [] = 0
porcentajeLetra letra palabra = (division (cantidadApariciones letra palabra) (longitudPalabra palabra)) * 100

cantidadApariciones:: Char-> String -> Int
cantidadApariciones _ [] = 0
cantidadApariciones n (s:sn) | n == s = 1 + cantidadApariciones n sn 
                             | otherwise = cantidadApariciones n sn 

division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b




lugarEnLista:: Int ->[Int] -> Int
lugarEnLista 0 (x:xs) = x 
lugarEnLista n (x:xs) = lugarEnLista (n-1) xs 


frecuenciaAux:: 








-- EJ 11
--expandirClave :: String -> Int -> String
--expandirClave clave n = clave ++ hastaNLugar clave (mod n (longitud clave))



-- EJ 15
combinacionesVigenere :: [String] -> [String] -> String -> [(String, String)]
combinacionesVigenere _ _ _ = [("hola", "b")]