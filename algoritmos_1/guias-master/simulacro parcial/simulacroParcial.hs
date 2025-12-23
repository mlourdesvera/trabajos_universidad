relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas [x] | fst x == snd x = False
                      | otherwise = True
relacionesValidas (x:y:xs) | (fst x == fst y) || (fst x == snd y) && (snd x == fst y) || (snd x == fst y) = False
                           | otherwise = relacionesValidas (x:xs) && relacionesValidas (y:xs)

--personas:: [(String, String)] -> [String]
--personas [] = []
--personas [x] = [fst x , snd x]
--personas (x:y) = unirDosListasDif (x:y)
--personas(x:y:xs) = unirDosListasDif (x:xs) && unirDosListasDif (y:xs)

--unirDosListasDif::[(String, String)] -> [String]
--unirDosListasDif   [x,y] | (fst x /= fst y) && (fst x /= snd y) && (snd x /= fst y) && (snd x /= snd y) = [fst x, fst y, snd x, snd y]
  --                       | (fst x == fst y) && (fst x /= snd y) && (snd x /= fst y) && (snd x /= snd y) = [fst x, snd x, snd y]
    --                     | (fst x /= fst y) && (fst x == snd y) && (snd x /= fst y) && (snd x /= snd y) = [fst x, fst y, snd x]
      --                   | (fst x /= fst y) && (fst x /= snd y) && (snd x == fst y) && (snd x /= snd y) = [fst x, fst y, snd y]
        --                 | (fst x /= fst y) && (fst x /= snd y) && (snd x /= fst y) && (snd x == snd y) = [fst x, fst y, snd x]
--amigosDe:: String -> [(String, String)] -> [String]





