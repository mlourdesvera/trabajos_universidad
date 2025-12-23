"""
Integrantes: Maria Lourdes Vera Oliver, Maria Eugenia Rosada, Victoria Schufer

En este código se presentan los procesos de importacion de la tabla original,
su manipulación y manejo para el armado de modelos. Además del armado de 
modelos, y su testeo para obtener los resultados más eficientes posibles. 
También el creado de gráficos o figuras para  ofrecer una conclusión más 
completa.
"""

#%% importación de las librerias con las cuales vamos a trabajar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from inline_sql import sql, sql_val
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score

#%%
tabla_completa = pd.read_csv("~/Downloads/tp2/TMNIST_Data.csv")

#La divido en un DataFrame que contiene los valores numéricos de los píxeles
tabla_solo_numeros = tabla_completa.iloc[:,2:]

#%% Ejercicio 1-a
#Calculamos la varianza de todos los datos
#La varianzza nos da una medida de dispersión de los valores de cada pixel en el conjunto de datos
#Cuanto mayor sea la varianza, mayor es la diferencia entre los valores de ese pixel a lo largo de todas las imágenes.
#Cada columna es un pixel de una dígito, y cada fila es un dígito 
varianzas = tabla_solo_numeros.var(axis=0)  # Calculamos la varianza para cada columna en todos los datos. axis=0 se refiere a que se calcula sobre las columnas.
#Graficamos con las variables calculadas
plt.figure(figsize=(10, 6))
plt.plot(varianzas, color='purple') #elegimos el color 
#nombramos los ejes x e y, arreglamos medidas así se puede visualizar mejor el gráfico
plt.xlabel('Pixel') 
plt.ylabel('Varianza')
plt.xticks(range(0, 784, 50))
plt.grid(True) #activamos la cuadrícula así es mas sencillo de leeer
#agregamos un pie al gráfico. Que se centre con la figura con un tamaño específico
plt.figtext(0.5, 0, 'Gráfico 1. Gráfico que muestra la varianza de cada pixel en los distintos números', wrap=True, horizontalalignment='center', fontsize=10)
plt.show() #mostramos el gráfico


#%%Ejercicio 1-b
#El objetivo de este ejercicio es visualizar cómo se comparan gráficamente los números 3 con 1 y 3 con 8

# Elegimos los números 3, 8 y 1 desde el DataFrame `tabla_solo_numeros`, con el mismo tipo de letra para poder compararlos mejor.
#Se accede a las filas correspondientes a cada número mediante su índice.
# El índice 28195 corresponde a un número 3, 16004 a un 8, y 24968 a un 1. De la fuente Aladin-Regular
tres= tabla_solo_numeros.iloc[28195] #Corresponde al número 3
ocho= tabla_solo_numeros.iloc[16004] #Corresponde al número 8
uno= tabla_solo_numeros.iloc[24968] #Corresponde al número 1

#Convertimos las filas (dígitos) que estaban como números en una matriz de 28x28
# Usamos reshape para reorganizar los valores en una matriz de 28x28 píxeles (cada imagen tiene 28x28 píxeles)
img3= np.array(tres).reshape((28,28)) #Imagen del 3
img8= np.array(ocho).reshape((28,28)) #Imagen del 8
img1= np.array(uno).reshape((28,28)) #Imagen del 1

#Imagen 1: Muestra la relación entre el número 3 y el 8.
#Decidimos hacer un mismo gráfico en el cual cambien las transparencias con la función alpha para que se distingan ambos
# Con 'alpha=0.9' el 3 es más visible, y con 'alpha=0.5' el 8 es más transparente. Esto nos permite superponer ambas imágenes y ver cómo se combinan visualmente.
# Eegimos los colores verde y naranja para el 3 y el 8 respectivamente así tienen una mejor visualización
plt.imshow(img3, cmap='Greens', alpha=0.9)
plt.imshow(img8, cmap='Oranges', alpha=0.5)
#Añadimos un texto descriptivo abajo de la imagen
plt.figtext(0.5, -0.02, 'Gráfico 2. Imagen que muestra la relación entre el 3 y el 8, con diferentes sombreados', wrap=True, horizontalalignment='center', fontsize=10)
plt.show()

#Imagen 2: Muestra la relación entre el npumero 3 y el 1.
#Similar a la imagen 1 pero está vez mostramos al 3 más opaco y al 1 más transparente
plt.imshow(img3, cmap='Greens', alpha=0.9)
plt.imshow(img1, cmap='Purples', alpha=0.6)
#Agregamos un pie a la imagen, para entender su explicación mejor
plt.figtext(0.5, -0.02, 'Gráfico 3. Imagen que muestra la relación entre el 3 y el 1, con diferentes sombreados', wrap=True, horizontalalignment='center', fontsize=10)
plt.show()


#%% Ejercicio 1-c

#Hicimos una consulta de SQL para extraer todas los ceros de la tabla_completa
ceros= sql ^"""
            SELECT DISTINCT *
            FROM tabla_completa
            WHERE labels = 0
        """
#Eliminamos las primeras dos columnas de la ceros, ya que son datos que no utilizaremos      
ceros = ceros.iloc[:,2:]  
      
#Calculamos el promedio de los valores de los pixeles, para generar un cero "común" entre todos
promedioceros = ceros.mean()
            
#Convertimos esto en matriz 28x28 para poder visualizarlo como imagen
img_prom_0 = np.array(promedioceros).reshape((28,28))  #promedio de todas las imágenes del 0

#Mostramos la imagen promedio del dígito 0, con la gama magma que se llega a distinguir bien.
plt.imshow(img_prom_0, cmap ='magma')
#Agregamos una breve descripción debajo de la imagen
plt.figtext(0.5, -0.02, 'Gráfico 4. Imagen que muestra un promedio entre los diferentes valores del dígito 0', wrap=True, horizontalalignment='center', fontsize=10)
plt.show()

#Ahora seleccionamos un 0 de la tabla, en este caso fue el de la tipografía Lato-ExtraBoldItalic, para compararlo con el anterior
img0 = np.array(tabla_solo_numeros.iloc[38]).reshape((28,28))
#Mostramos la imagen del dígito 0, con la gama de azules
plt.imshow(img0, cmap ='Blues')
#Añadimos un texto descriptivo de la figura
plt.figtext(0.5, 0, 'Gráfico 5. Muestra la imagen de un dígito 0', wrap=True, horizontalalignment='center', fontsize=10)
plt.show()

#%%
# =============================================================================
# EJERCICIO 2
# =============================================================================
#%% 2-a

#Realizamos una consulta de SQL dónde separamos de tabla_completa los dígitos 0s y 1s
#Usamos solo SELECT y no SELECT DISTINCT, porque este último nos generaba error al momento de hacer las cuentas y usar le modelo
binarios = sql ^"""
            SELECT *
            FROM tabla_completa
            WHERE labels = 0 OR labels = 1
            """
# Verificamos la cantidad de 1s y 0s      
longitud_ceros = len(binarios[binarios['labels']==0]) 
longitud_unos = len(binarios[binarios['labels']==1])
#Vemos que son la misma cantidad
print(longitud_ceros)
print(longitud_unos)

#%% 2-b

#Separamos los datos en Xb e Yb, para poder después entrenar y testear nuestro modelo
Xb = binarios.iloc[:,2:] # Características (todas las columnas excepto las primeras dos)
Yb = binarios['labels']  # Etiquetas (columna 'labels'), es decir los resultados que debería arrojar nuestro modelo

#%%
# Dividimos los datos en conjuntos de entrenamiento (80%) y prueba (20%), 
#usamos la función random_state para controlar un poco el azar y que no cambien nuestros datos cada vez que ejecutabamos el modelo
Xb_train, Xb_test, Yb_train, Yb_test = train_test_split(Xb, Yb, test_size=0.2, stratify=Yb, random_state= 10)            

#%% 2-c

resultados = [] #lista vacía para apilar resultados

# Primer conjunto de características (columnas 180, 407 y 606)
Xb_train_ijk = Xb_train.iloc[:, [180, 407, 606]]
Xb_test_ijk = Xb_test.iloc[:, [180, 407, 606]]
    
#Entrenamos el modelo KNN con k=5
model = KNeighborsClassifier(n_neighbors = 5)
model.fit(Xb_train_ijk, Yb_train) #Entrenamos el modelo
Yb_pred = model.predict(Xb_test_ijk) #Predicciones para el conjunto de prueba

#Calculamos la exactitud y mostramos el resultado
exactitud= metrics.accuracy_score(Yb_test, Yb_pred)
resultados.append(exactitud)
print("Exactitud del modelo KNN:", exactitud)
print(metrics.confusion_matrix(Yb_test, Yb_pred))



#Repetimos lo mismo pero con las columnas 541, 407 y 214

Xb_train_ijk = Xb_train.iloc[:, [541, 407, 214]]
Xb_test_ijk = Xb_test.iloc[:, [541, 407, 214]]

model = KNeighborsClassifier(n_neighbors = 5)
model.fit(Xb_train_ijk, Yb_train)

Yb_pred = model.predict(Xb_test_ijk)

exactitud= metrics.accuracy_score(Yb_test, Yb_pred)
resultados.append(exactitud)
print("Exactitud del modelo KNN:", exactitud)
print(metrics.confusion_matrix(Yb_test, Yb_pred))



#Repetimos lo mismo pero con las columnas 448, 430 y 440

Xb_train_ijk = Xb_train.iloc[:, [448,430,440]]
Xb_test_ijk = Xb_test.iloc[:, [448,430,440]]
    
model = KNeighborsClassifier(n_neighbors = 5)
model.fit(Xb_train_ijk, Yb_train) 

Yb_pred = model.predict(Xb_test_ijk)

exactitud= metrics.accuracy_score(Yb_test, Yb_pred)
resultados.append(exactitud)
print("Exactitud del modelo KNN:", exactitud)
print(metrics.confusion_matrix(Yb_test, Yb_pred))

#se agregan las exactitudes al resultado y se muestra
print(resultados)

#%% 2-d

#Creamos diferentes secuencias vacías que luego nos ayudarán en el armado de los gráficos
resultados_1=[]
resultados_2=[]
resultados_3=[]
yb_pred_lista = []

# Definimos las columnas que se van a usar para el modelo.
columnas= [[180, 407, 606],[448,430,440],[541, 407, 214]]
# Definimos los valores de k que se probarán en el modelo KNN.
valores_k = (3, 4, 5, 6)


# Entrenar y predecir para cada valor de k y cada conjunto de columnas, para elegir el que más preciso sea
for c in columnas: #iteramos en las distintas columnas
    for k in valores_k:  #iteramos en las diferentes k (vecinos)
        #Seleccionamos los datos de entrenamiento y test
        Xb_train_ijk = Xb_train.iloc[:, c]
        Xb_test_ijk = Xb_test.iloc[:, c]
        
        #Creamos y entrenamos el modelo KNN con k vecinos
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(Xb_train_ijk, Yb_train) #Entrenamos el modelo con los datos de entrenamiento
        Yb_pred = model.predict(Xb_test_ijk) # Realizamos la predicción con los datos de prueba
        
        #Almacenamos los datos de prueba
        yb_pred_lista.append(Yb_pred)
        
        #Calculamos la exactitud del modelo
        exactitud= metrics.accuracy_score(Yb_test, Yb_pred)
        
        #Guardamos la exactitud del modelo  en la lista correspondiente
        if c == [180, 407, 606]:
            resultados_1.append(exactitud)
        elif c == [448, 430, 440]:
            resultados_2.append(exactitud)
        elif c == [541, 407, 214]:
            resultados_3.append(exactitud)
            
        #Imprimimos la exactitud y la matriz de confusión    
        print(f"Exactitud del modelo KNN con {c} y n_neighbors = {k}:", exactitud)
        print(metrics.confusion_matrix(Yb_test, Yb_pred))
        
#%%
#Gráfico de los resultados
ind = np.arange(4) #Índices para el eje X (valores de k)
resultados_1 = pd.Series(resultados_1)
resultados_2 = pd.Series(resultados_2)
resultados_3 = pd.Series(resultados_3)

#Creamos un DataFrame con los resultados
results = pd.DataFrame({'Indice': ind,'resultados_1': resultados_1,'resultados_2': resultados_2,'resultados_3': resultados_3})

#Creamos los gráficos
fig, ax = plt.subplots() 
plt.rcParams['font.family'] = 'sans-serif'   
  
#Graficamos los resultados, para cada conjunto de columnas      
ax.plot('Indice', 'resultados_1', data=results, 
        marker='.', linestyle='-', linewidth=0.5,  label='Columnas [180, 407, 606]')

ax.plot('Indice', 'resultados_2', data=results, 
        marker='.', linestyle='-',  linewidth=0.5, label='Columnas [448,430,440]')

ax.plot('Indice', 'resultados_3', data=results, 
        marker='.',  linestyle='-',   linewidth=0.5,  label='Columnas [541, 407, 214]' )

#Agregamos mejoras para la visualización
ax.set_xlabel('Cantidad vecinos') #Etiqueta eje x
ax.set_ylabel('Exactitud') #Etiqueta eje Y
plt.xticks(ticks=[0, 1, 2, 3], labels=['3', '4', '5', '6']) #Valores del eje x
ax.legend(loc='center right', bbox_to_anchor=(1, 0.5)) #ubicación del cuadradito descriptivo
#Agregamos un pie para la figura
plt.figtext(0.5, -0.02, 'Gráfico 6. Muestra la exactitud en función de la cantidad de vecinos y las columnas elegidas.', wrap=True, horizontalalignment='center', fontsize=8)
plt.show()

#%%
#Coordenadas de los píxeles a resaltar
pixel1 = (19, 8)
pixel2 = (14, 14)
pixel3 = (7, 17)

# Mostrar la imagen de los promedio del 0
fig, ax = plt.subplots()
ax.imshow(img_prom_0, cmap ='gray')

# Dibujar puntos rojos en las coordenadas especificadas
for x, y in [pixel1, pixel2, pixel3]:
    ax.scatter(y, x, color='red', s=50)  # s=50 ajusta el tamaño del punto

# Agregar descripción y mostrar la imagen    
plt.figtext(0.5, 0, 'Gráfico 7. Muestra los pixeles elegidos en el promedio de ceros', wrap=True, horizontalalignment='center', fontsize=10)
plt.show() 

# Mostrar la imagen del 1
fig, ax = plt.subplots()
ax.imshow(img1, cmap ='gray')

# Dibujar puntos rojos en las coordenadas especificadas
for x, y in [pixel1, pixel2, pixel3]:
    ax.scatter(y, x, color='red', s=50)  # s=50 ajusta el tamaño del punto
   
# Agregar descripción y mostrar la imagen    
plt.figtext(0.5, 0, 'Gráfico 8. Muestra los pixeles elegidos en la imagen de un 1', wrap=True, horizontalalignment='center', fontsize=10)
plt.show()

#%% 
# =============================================================================
# EJERCICIO 3
# =============================================================================
#3a 
#Diviimos los datos en dos partes: una para desarrollo (entrenamiento/train)
#y otra para pruebas(Test)
X= tabla_solo_numeros
Y= tabla_completa['labels']

Desarrollo_X, Held_Out_X, Desarrollo_Y, Held_Out_Y = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=6)

# Configurar K-Fold Cross-Validation con 5 folds
kf = KFold(n_splits=5, shuffle=True, random_state=1)

# Parámetros del modelo
rango_alturas = range(1, 21)
criteria = ['gini', 'entropy']
clf_info = []
i= 0

# Loop para cada criterio
for altura in rango_alturas:
    for criterion in criteria:
        # Crear un modelo con la configuración actual de criterio y profundidad
        model = DecisionTreeClassifier(max_depth=altura, criterion=criterion,random_state=16)
        
        #para ver que fold es
        i= 0

        # Cross-validation manual en cada fold
        for train_index, val_index in kf.split(Desarrollo_X):
            # Dividir los datos de entrenamiento y validación en cada fold
            X_train_fold, X_val_fold = Desarrollo_X.iloc[train_index], Desarrollo_X.iloc[val_index]
            Y_train_fold, Y_val_fold = Desarrollo_Y.iloc[train_index], Desarrollo_Y.iloc[val_index]

            # Entrenar el modelo en el fold actual
            model.fit(X_train_fold, Y_train_fold)

            # Calcular precisión en el conjunto de entrenamiento
            Y_train_pred = model.predict(X_train_fold)
            train_score = accuracy_score(Y_train_fold, Y_train_pred)

            # Calcular precisión en el conjunto de validación
            Y_val_pred = model.predict(X_val_fold)
            val_score = accuracy_score(Y_val_fold, Y_val_pred)
            
            #para el fold
            i+=1

            # Guardar la información en el diccionario `clf_info`
            clf_info.append({
               'criterion': criterion,
               'alturas': altura,
               'fold': i,
               'train_accuracies': train_score,
               'test_accuracies': val_score
           })
        
df_clf_info = pd.DataFrame(clf_info)        

#%% 
#3b
#Creamos una tabla pivoteada de presiciones de datos de entrenamiento usando como indices el criterio y la altura  (profundidad del árbol)
# Las columnas representan los distintos folds, y los valores corresponden a las precisiones de entrenamiento 
train_df = df_clf_info.pivot_table(
    index=['criterion', 'alturas'], 
    columns='fold',                 
    values='train_accuracies'      
).reset_index()                   

## Renombramos las columnas de train_df para mejorar la legibilidad
train_df.columns = ['Criterio', 'Altura'] + [f'Fold_{i}' for i in range(1, 6)]

# Crear tabla pivotada de precisiones de prueba con el mismo formato
# Las columnas representan los distintos folds, y los valores corresponden a las precisiones de prueba

test_df = df_clf_info.pivot_table( 
    index=['criterion', 'alturas'],
    columns='fold',               
    values='test_accuracies'      
).reset_index()
# Renombramos las columnas de test_df para hacer el formato consistente con train_df
test_df.columns = ['Criterio', 'Altura'] + [f'Fold_{i}' for i in range(1, 6)]
# Calculamos el promedio de precisión de entrenamiento en los 5 folds y agregarlo como una nueva columna
train_df['promedio_exactitud'] = train_df.loc[:, 'Fold_1':'Fold_5'].mean(axis=1)
# Calculamos el promedio de precisión de prueba en los 5 folds y agregarlo como una nueva columna
test_df['promedio_exactitud'] = test_df.loc[:, 'Fold_1':'Fold_5'].mean(axis=1)

#%%
# Consultas para obtener el promedio de precisión de entrenamiento y prueba por criterio y altura (profundidad del árbol)

# Extraemos el promedio de precisión de entrenamiento usando el criterio "entropy" en todos los niveles de profundidad
promedio_ent_alt_train = sql^"""
                      SELECT Criterio, Altura, promedio_exactitud
                      FROM train_df
                      WHERE Criterio='entropy'
"""
# Extraemos el promedio de precisión de entrenamiento usando el criterio "gini" en todos los niveles de profundidad
promedio_gini_alt_train = sql^"""
                      SELECT Criterio, Altura, promedio_exactitud
                      FROM train_df
                      WHERE Criterio='gini'
"""
#Sacamos el promedio de precisión de prueba usanso el criterio "entropy" en todos los niveles de profundidad
promedio_ent_alt_test = sql^"""
                      SELECT Criterio, Altura, promedio_exactitud
                      FROM test_df
                      WHERE Criterio='entropy'
"""
#Sacamos el promedio de precisión de prueba usanso el criterio "gini" en todos los niveles de profundidad
promedio_gini_alt_test = sql^"""
                      SELECT Criterio, Altura, promedio_exactitud
                      FROM test_df
                      WHERE Criterio='gini' 
"""
# Extraemos el promedio precisión de entrenamiento usando el criterio "entropy"
# con alturas>=8 para que se vea mejor
promedio_ent_alt_train_8 = sql^"""
                      SELECT Criterio, Altura, promedio_exactitud
                      FROM train_df
                      WHERE Criterio='entropy' AND Altura>=8
"""
# Extraemos el promedio precisión de entrenamiento usando el criterio "gini"
# con alturas>=8 para que se vea mejor
promedio_gini_alt_train_8 = sql^"""
                      SELECT Criterio, Altura, promedio_exactitud
                      FROM train_df
                      WHERE Criterio='gini' AND Altura>=8
"""
# Extraemos el promedio precisión de prueba usando el criterio "entropy"
# con alturas>=8 para que se vea mejor
promedio_ent_alt_test_8 = sql^"""
                      SELECT Criterio, Altura, promedio_exactitud
                      FROM test_df
                      WHERE Criterio='entropy' AND Altura>=8
"""
# Extraemos el promedio precisión de prueba usando el criterio "gini"
# con alturas>=8 para que se vea mejor
promedio_gini_alt_test_8 = sql^"""
                      SELECT Criterio, Altura, promedio_exactitud
                      FROM test_df
                      WHERE Criterio='gini' AND Altura>=8
"""

#%%
#3c
# Realizamos un grafico paraobservar los distintos modelos realizados,
# utilizando tanto los conjuntos de train como test, y considerando criterios entropy y gini, 
#con árboles de decisión de profundidades que van del 1 al 20

fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           

ax.plot('Altura', 'promedio_exactitud', data=promedio_ent_alt_train,
        marker='.',  linestyle='-', linewidth=0.5, color= 'red', label='exactitud entropy con train')

ax.plot('Altura', 'promedio_exactitud', data=promedio_ent_alt_test,
        marker='.', linestyle='--', linewidth=0.5, color= 'orange', label='exactitud entropy con test')

ax.plot('Altura', 'promedio_exactitud', data=promedio_gini_alt_train,
        marker='.', linestyle='-',  linewidth=0.5, color= 'blue', label='exactitud gini con train')    

ax.plot('Altura', 'promedio_exactitud', data=promedio_gini_alt_test,
        marker='.', linestyle='--', linewidth=0.5, color= 'skyblue', label='exactitud gini con test')   

ax.set_xlabel('Profundidad(altura) del arbol')
ax.set_ylabel('Promedio de exactitud')
ax.legend()
plt.figtext(0.5, -0.03, 'Gráfico 9. Gráfico que muestra el promedio de exactitud según la profundidad del árbol', wrap=True, horizontalalignment='center', fontsize=8)
plt.show()

#%%
#Visualizacion que muestra la evolución de la exactitud de dos modelos de 
#árbol de decisión al variar la profundidad del árbol, a partir de una altura de 8

fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           

ax.plot('Altura', 'promedio_exactitud', data=promedio_ent_alt_train_8,
        marker='.',linestyle='-', linewidth=0.5, color= 'red', label='exactitud entropy con train')

ax.plot('Altura', 'promedio_exactitud', data=promedio_ent_alt_test_8,
        marker='.',  linestyle='--',  linewidth=0.5, color= 'orange', label='exactitud entropy con test')

ax.plot('Altura', 'promedio_exactitud', data=promedio_gini_alt_train_8,
        marker='.', linestyle='-', linewidth=0.5, color= 'blue', label='exactitud gini con train')    

ax.plot('Altura', 'promedio_exactitud', data=promedio_gini_alt_test_8,
        marker='.', linestyle='--', linewidth=0.5, color= 'skyblue', label='exactitud gini con test')   

ax.set_xlabel('Profundidad(altura) del arbol')
ax.set_ylabel('Promedio de exactitud')
ax.legend()
ax.grid(True, which='both', linestyle='-', color='gray', linewidth=0.5)
ax.set_xticks(np.arange(min(promedio_ent_alt_train_8['Altura']), max(promedio_ent_alt_train_8['Altura']) + 1, 1))
ax.set_yticks(np.arange(0.91, 1.02, 0.01))
plt.figtext(0.5, -0.03, 'Gráfico 10. Gráfico que muestra el Gráfico 8 comenzando desde la altura 8', wrap=True, horizontalalignment='center', fontsize=8)
plt.show()


#%%
#3d
#entrenamos el modelo elegido en el conjunto desarrollo entero

modelo_elegido = DecisionTreeClassifier(max_depth=12, criterion='entropy',random_state=16)
modelo_elegido.fit(Desarrollo_X, Desarrollo_Y)

Y_pred = modelo_elegido.predict(Held_Out_X)       

print("Exactitud del modelo:", metrics.accuracy_score(Held_Out_Y, Y_pred))
matriz_confusion= metrics.confusion_matrix(Held_Out_Y, Y_pred) #Realizamos la matriz de confusion para tener una visualizacion de que tan exacto es el modelo
print(matriz_confusion)

