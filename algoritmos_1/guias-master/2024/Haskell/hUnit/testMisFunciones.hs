import MisFunciones
import Test.HUnit

testQuitar = test[
  "caso 1" ~: (quitar 1 []) ~?= [],
  "caso 2" ~: (quitar 1 [1,2,3]) ~?= [2,3],
  "caso 3" ~: (quitar 1 [1]) ~?= [],
  "caso 4" ~: (quitar 1 [2,3,4]) ~?= [2,3,4],
  "caso 1" ~: (quitar 1 [3,1,2]) ~?= [3,2],
  "caso 1" ~: (quitar 1 [1,5,1,1]) ~?= [5,1,1]
  ]

ejecutar = runTestTT testQuitar 