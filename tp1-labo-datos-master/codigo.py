 # -*- coding: utf-8 -*-
"""
Integrantes: Maria Lourdes Vera Oliver, Maria Eugenia Rosada, Victoria Schufer

En este codigo se presentan los procesos de importacion de las tablas originales, 
su limpieza y su utilización en la generación de tablas, gráficos e información 
requeridos para los ejercicios solicitados. Además, se incluyen gráficos y tablas 
adicionales que han sido creados para ofrecer una conclusión más completa.
"""


import pandas as pd
from inline_sql import sql, sql_val

import matplotlib.pyplot as plt 
import seaborn as sns          

#%% Subimos tablas originales

carpeta = "~/Downloads/tp1-labo-datos-master/TablasOriginales/"


listaSedes = pd.read_csv(carpeta+"lista-sedes.csv")

listaSecciones = pd.read_csv(carpeta+"lista-secciones.csv")

listaSedesDatos = pd.read_csv(carpeta+"lista-sedes-datos.csv")

listaDatosMigraciones = pd.read_csv(carpeta+"datos_migraciones.csv")

#%% Limpiamos y creamos tablas:
    
#lo que necesitamos limpiar y tener es:
    
#sedes: sede_id, nombre_sede, codigo_pais
#pais:  codigo_pais, nombre_pais y region
#redes_sociales: url, red_social, sede_idd
#secciones: sede_id, descripcion_sede
#migracion: codigo_iso(origen y destino), años, cantidad

# PARA SEDES
# Para sedes, nos dimos cuenta del error de código país que tiene Gran Bretaña y lo cambiamos para
# que luego no nos traiga problemas. A Sede_ID le cambiamos el nombre a ID, ya que se sobreentiende
# que se habla de Sede_ID, ya que es su tabla. Tambien, con select distinct se eliminaran los
# repetidos
Sedes_Limpia = sql^""" 
                    SELECT DISTINCT 
                        sede_id AS ID, 
                        sede_desc_castellano AS Nombre, 
                        REPLACE(pais_iso_3,'GRB','GBR') AS Codigo_Pais
                    FROM listaSedes
                    """
                    
# PARA PAIS 
# Realizamos el cambio anterior sobre los códigos de país para que el de Gran Bretaña sea el correcto.
# También, en vez de poner Código_Pais, lo dejamos como Código, ya que nos encontramos en la tabla
# país, por lo que se entiende que se habla de Código_Pais. Ademas, se eliminaran los repetidos 
# gracias a select distinct
#Acá corregimos la tabla de Pais:Limpia, ya que la habiamos separado antes, 
#pero decidimos que quede en una sola. Luego las dividimos para una correcta reslución de los ejercicios
Pais_Limpia= sql ^"""
                 SELECT DISTINCT
                      REPLACE(pais_iso_3,'GRB','GBR') AS Codigo, 
                      pais_castellano AS Nombre, 
                      region_geografica AS Region
                 FROM listaSedesDatos
                 """

Pais_Limpia_1 = sql ^"""
                    SELECT DISTINCT 
                        Codigo, 
                        Nombre
                    FROM Pais_Limpia
                    """


Pais_Limpia_2  = sql ^"""
                    SELECT DISTINCT 
                        Nombre, 
                        Region
                    FROM Pais_Limpia
                    """
 
# PARA SECCIONES    
# Para una correcta analización de los datos, se eliminaron las secciones que no tenían sede_id, ya
# que entonces no provenían de ninguna sede. Por lo tanto, esas secciones no existían. También se
# eliminaron registros repetidos y se realizaron cambios de nombres en las columnas para que
# coincidan con las del modelo relacional.
Secciones_Limpia = sql^"""
                    SELECT DISTINCT 
                        sede_id AS Sede_ID, 
                        sede_desc_castellano AS Descripcion
                    FROM listaSecciones
                    WHERE sede_id IS NOT NULL
                    """
                    

# PARA REDES SOCIALES
# Proceso en el cual, con distintos pasos, hicimos la columna de redes sociales atómica y creamos
# la tabla para las redes sociales:

# Utilizando SPLIT_PART, separamos las redes a partir de "//" para no separar el URL en sí y las
# pusimos en diferentes columnas según el país.
redes_sociales_1 = sql ^"""
                    SELECT DISTINCT
                        sede_id AS Sede_ID,
                        SPLIT_PART(redes_sociales, ' // ', 1) AS Red_social1,
                        SPLIT_PART(redes_sociales, ' // ', 2) AS Red_social2,
                        SPLIT_PART(redes_sociales, ' // ', 3) AS Red_social3,
                        SPLIT_PART(redes_sociales, ' // ', 4) AS Red_social4,
                        SPLIT_PART(redes_sociales, ' // ', 5) AS Red_social5,
                        SPLIT_PART(redes_sociales, ' // ', 6) AS Red_social6
                    FROM listaSedesDatos
                        """
                 
                
# Como la anterior tabla nos deja muchos null o espacios vacíos, la unimos en una sola columna en la
# que sede_id se repite por la cantidad de redes sociales que tiene. Además, utilizando TRIM, le
# sacamos los espacios adelante y atrás del URL (si es que tiene).
redes_sociales_2= sql^ """
                    SELECT DISTINCT Sede_ID, Red_Social
                    FROM (
                        SELECT Sede_ID, TRIM(Red_social1) AS Red_Social FROM redes_sociales_1
                        UNION ALL 
                        SELECT Sede_ID, TRIM(Red_social2) FROM redes_sociales_1
                        UNION ALL 
                        SELECT Sede_ID, TRIM(Red_social3) FROM redes_sociales_1
                        UNION ALL 
                        SELECT Sede_ID, TRIM(Red_social4) FROM redes_sociales_1
                        UNION ALL 
                        SELECT Sede_ID, TRIM(Red_social5) FROM redes_sociales_1
                        UNION ALL 
                        SELECT Sede_ID, TRIM(Red_social6) FROM redes_sociales_1
                    ) AS RedesUnidas
                    WHERE Red_Social != '' AND Red_Social IS NOT NULL;
                        """

# Le agregamos la columna Nombre, que nos indica a qué red social pertenece el URL.
redes_sociales_3 = sql^"""
                SELECT DISTINCT 
                    Sede_ID, 
                    Red_Social AS URL,
                    CASE
                        WHEN Red_Social LIKE '%twitter%' THEN 'Twitter'
                        WHEN Red_Social LIKE '%instagram%' THEN 'Instagram'
                        WHEN Red_Social LIKE '%Instagram%' THEN 'Instagram'
                        WHEN Red_Social LIKE '%facebook%' THEN 'Facebook'
                        WHEN Red_Social LIKE '%Facebook%' THEN 'Facebook'
                        WHEN Red_Social LIKE '%youtube%' THEN 'Youtube'
                        WHEN Red_Social LIKE '%flickr%' THEN 'Flickr'
                        WHEN Red_Social LIKE '%linkedin%' THEN 'LinkedIn'
                    ELSE NULL END AS Nombre
                FROM redes_sociales_2;
                    """
# Finalmente, se crea la tabla final en la que se eliminan las redes sociales que consideramos no
# válidas.
Redes_Sociales_Limpia = sql ^ """
                SELECT DISTINCT *
                FROM redes_sociales_3
                WHERE Nombre != 'None'
                """


# PARA MIGRACION
# Para que las consultas posteriores de SQL procesen correctamente los datos, convertimos
# los puntos ('..') en 0 y los números en formato string los pasamos a enteros
migraciones_1 = sql ^ """
                          SELECT DISTINCT
                              "Country Origin Code" AS Codigo_Pais_Origen,
                              "Country Dest Code" AS Codigo_Pais_Destino,
                              CASE
                                  WHEN "1960 [1960]" = '..' THEN 0
                                  ELSE CAST("1960 [1960]" AS INTEGER)
                              END AS "1960",
                              CASE
                                  WHEN "1970 [1970]" = '..' THEN 0
                                  ELSE CAST("1970 [1970]" AS INTEGER)
                              END AS "1970",
                              CASE
                                  WHEN "1980 [1980]" = '..' THEN 0
                                  ELSE CAST("1980 [1980]" AS INTEGER)
                              END AS "1980",
                              CASE
                                  WHEN "1990 [1990]" = '..' THEN 0
                                  ELSE CAST("1990 [1990]" AS INTEGER)
                              END AS "1990",
                              CASE
                                  WHEN "2000 [2000]" = '..' THEN 0
                                  ELSE CAST("2000 [2000]" AS INTEGER)
                              END AS "2000"
                          FROM listaDatosMigraciones
                          WHERE "Migration by Gender Code" = 'TOT';
                          """
                          
Migraciones_Limpia = sql ^ """
                             SELECT DISTINCT 
                                 Codigo_Pais_Origen,
                                 Codigo_Pais_Destino,
                                 1960 AS Año,
                                 "1960" AS Cantidad
                             FROM migraciones_1
                             
                             UNION ALL
                             
                             SELECT DISTINCT
                                 Codigo_Pais_Origen,
                                 Codigo_Pais_Destino,
                                 1970 AS Año,
                                 "1970" AS Cantidad
                             FROM migraciones_1
                             
                             UNION ALL
                             
                             SELECT DISTINCT
                                 Codigo_Pais_Origen,
                                 Codigo_Pais_Destino,
                                 1980 AS Año,
                                 "1980" AS Cantidad
                             FROM migraciones_1
                             
                             UNION ALL
                             
                             SELECT DISTINCT
                                 Codigo_Pais_Origen,
                                 Codigo_Pais_Destino,
                                 1990 AS Año,
                                 "1990" AS Cantidad
                             FROM migraciones_1
                             
                             UNION ALL
                             
                             SELECT DISTINCT
                                 Codigo_Pais_Origen,
                                 Codigo_Pais_Destino,
                                 2000 AS Año,
                                 "2000" AS Cantidad
                             FROM migraciones_1
                             """

#%% Ejercicios

#h i)
# Contamos la cantidad de sedes por país en una columna nueva a partir de Sedes_Limpia, agrupando
# por código del país.
sedes_por_pais = sql^"""
                    SELECT DISTINCT 
                        Codigo_Pais, 
                        COUNT(ID) AS Cantidad_Sedes
                    FROM Sedes_Limpia
                    GROUP BY Codigo_Pais
                    """

# Contamos la cantidad de secciones que tiene cada sede y la colocamos en una columna nueva.
secciones_por_sede = sql^"""
                    SELECT DISTINCT
                        Sede_ID, 
                        COUNT(*) AS Cantidad_Secciones
                    FROM Secciones_Limpia
                    GROUP BY Sede_ID
                    """


# Unimos Sedes_Limpia con secciones_por_sede para tener la cantidad de secciones vinculada a
# Código_Pais.
secciones_por_pais_1 =sql^"""
                    SELECT DISTINCT s.ID, s.Codigo_Pais, sc.Cantidad_Secciones
                    FROM Sedes_Limpia AS s
                    INNER JOIN secciones_por_sede AS sc
                    ON s.ID=sc.sede_id
                    """
                    
# Sumamos la cantidad de secciones (que antes estaba dada por sede) por país.
secciones_por_pais_2= sql^"""
                    SELECT DISTINCT Codigo_Pais, SUM(Cantidad_Secciones) AS Cantidad_Secciones 
                    FROM secciones_por_pais_1
                    GROUP BY Codigo_Pais
                    """

# Dividimos la cantidad de secciones totales de cada país por la cantidad de sedes de cada país para
# obtener el promedio de secciones por país.
secciones_promedio_por_pais= sql^"""
                            SELECT DISTINCT 
                                s.Codigo_Pais, 
                                (sc.Cantidad_Secciones/s.Cantidad_Sedes) AS Secciones_Promedio, 
                                s.Cantidad_Sedes
                            FROM sedes_por_pais AS s
                            INNER JOIN secciones_por_pais_2 AS sc
                            ON s.Codigo_Pais = sc.Codigo_Pais
                            """

# Agrupamos y sumamos los datos de la columna 2000 a partir del código del país destino, lo que nos
# da la cantidad total de inmigrantes de ese país en ese año.
inmigrantes = sql ^ """
                        SELECT DISTINCT
                            Codigo_Pais_Destino AS Codigo_Pais, 
                            SUM("Cantidad") AS Inmigrantes
                        FROM Migraciones_Limpia
                        WHERE Año = '2000'
                        GROUP BY Codigo_Pais_Destino
                        ORDER BY Codigo_Pais_Destino ASC
                        """

# Agrupamos y sumamos los datos de la columna 2000 a partir del código del país de origen, lo que
# nos da la cantidad total de personas que salen de ese país en ese año, es decir, los emigrantes.
emigrantes = sql ^ """
                        SELECT DISTINCT
                            Codigo_Pais_Origen AS Codigo_Pais,
                            SUM("Cantidad") AS Emigrantes
                        FROM Migraciones_Limpia
                        WHERE Año = '2000' AND Codigo_Pais_Origen != 'zzz'
                        GROUP BY Codigo_Pais_Origen 
                        ORDER BY Codigo_Pais_Origen ASC
                        """

# Juntamos los datos de las dos tablas creadas anteriormente para tener la información combinada.
migracion = sql ^ """
                        SELECT DISTINCT 
                            i.Codigo_Pais, 
                            i.Inmigrantes, 
                            e.Emigrantes
                        FROM inmigrantes AS i
                        INNER JOIN emigrantes AS e
                        ON i.Codigo_Pais = e.Codigo_Pais
                        ORDER BY i.Codigo_Pais ASC
                        """

# Calculamos el flujo migratorio neto (llamado diferencia) restando la cantidad de emigrantes de la
# cantidad de inmigrantes según el país.
flujo_migratorio = sql ^ """
                        SELECT DISTINCT
                            m1.Codigo_Pais,
                            m1.Inmigrantes,
                            m2.Emigrantes,
                            (m1.Inmigrantes - m2.Emigrantes) AS Diferencia
                        FROM migracion AS m1
                        INNER JOIN migracion AS m2
                        ON m1.Codigo_Pais = m2.Codigo_Pais
                        ORDER BY m1.Codigo_Pais ASC
                        """
                        
                       
# Unimos todos los datos obtenidos para lograr el resultado esperado del ejercicio.
Sedes_Seccion_Flujo =sql^"""
                        SELECT DISTINCT  
                            p.Nombre AS Pais, 
                            sp.Cantidad_Sedes AS sedes, 
                            ROUND(sp.Secciones_Promedio,2) AS Secciones_Promedio, 
                            f.Diferencia AS flujo_migratorio_neto
                        FROM secciones_promedio_por_pais AS sp
                        INNER JOIN flujo_migratorio AS f
                        ON sp.Codigo_Pais= f.Codigo_Pais
                        INNER JOIN Pais_Limpia_1 AS p
                        ON p.Codigo= f.Codigo_Pais
                        ORDER BY Cantidad_Sedes DESC, Pais ASC
                        """



#%% h ii)

#A través de la unión de Pais_Limpia_1 y Sedes_Limpia, nos quedamos solo con los países que tienen
# al menos una sede Argentina.
paises_con_sedes_en_Arg = sql ^"""
                        SELECT DISTINCT
                            p.Nombre AS Pais,
                            p.Codigo
                        FROM Pais_Limpia_1 AS p
                        INNER JOIN Sedes_Limpia AS s
                        ON p.Codigo = s.Codigo_Pais
                        ORDER BY Pais ASC
                        """

# Sumamos los países que tienen al menos una sede argentina por región. Para determinar a qué región
# pertenecen, hacemos un join con Pais_Limpia_2, que contiene el nombre del país y su región. La
# suma por región se logra agrupando por región y contando los países.
paises_con_sedes_en_Arg_por_region = sql ^"""
                        SELECT
                            p2.Region AS Region,
                            COUNT(p1.Pais) AS Cantidad
                        FROM paises_con_sedes_en_Arg AS p1
                        INNER JOIN Pais_Limpia_2 AS p2
                        ON p1.Pais = p2.Nombre
                        GROUP BY p2.Region
                        ORDER BY Region ASC
                        """

# De Migraciones_Limpia, nos quedamos con los códigos de país de origen que sean "ARG", es decir,
# con sus emigrantes. Esto nos servirá para luego calcular su flujo migratorio. Nos aseguramos,
# haciendo un join con la tabla anterior, de que los países que reciben inmigración argentina sean
# los países que tienen al menos una sede argentina.
origen_Arg= sql ^"""
                        SELECT DISTINCT
                            p.Pais AS Pais,
                            p.Codigo AS Codigo ,
                            m.Cantidad AS Cantidad
                        FROM Migraciones_Limpia AS m
                        INNER JOIN paises_con_sedes_en_Arg AS p
                        ON m.Codigo_Pais_Destino = p.Codigo
                        WHERE Año = '2000' AND m.Codigo_Pais_Origen = 'ARG'
                        ORDER BY Pais ASC
                        """

# Calculamos la inmigración hacia Argentina de los países en los cuales hay sedes argentinas. Esto
# lo logramos con un razonamiento parecido al anterior.
destino_Arg = sql ^"""
                        SELECT DISTINCT
                            p.Pais AS Pais,
                            p.Codigo AS Codigo ,
                            m.Cantidad AS Cantidad
                        FROM Migraciones_Limpia AS m
                        INNER JOIN paises_con_sedes_en_Arg AS p
                        ON m.Codigo_Pais_Origen = p.Codigo
                        WHERE Año = '2000' AND m.Codigo_Pais_Destino = 'ARG'
                        ORDER BY Pais ASC
                        """

# Unimos los datos de las dos tablas anteriores y, a su vez, calculamos el flujo migratorio (llamado
# diferencia en esta tabla) restando los emigrantes de los inmigrantes.
flujo_migratorio_Arg = sql ^ """
                        SELECT DISTINCT
                            d.Codigo,
                            d.Pais,
                            d.Cantidad AS Inmigrantes,
                            o.Cantidad AS Emigrantes,
                            (d.Cantidad - o.Cantidad) AS Diferencia
                        FROM origen_Arg AS o
                        INNER JOIN destino_Arg AS d
                        ON o.Codigo = d.Codigo
                        ORDER BY o.Codigo ASC
                        """

# Calculamos el promedio del flujo migratorio anterior según la región. Esto se logra a través de un
# join con la tabla Pais_Limpia_2, que contiene la región, y luego agrupando por región para que el
# promedio (calculado con AVG) sea obtenido por región.
flujo_migratorio_Arg_por_region = sql ^"""
                        SELECT
                            p.Region,
                            AVG(f.Diferencia) AS Promedio_Flujo_con_Arg
                        FROM flujo_migratorio_Arg AS f
                        INNER JOIN Pais_Limpia_2 AS p
                        ON f.Pais = p.Nombre
                        GROUP BY p.Region
                        ORDER BY Promedio_Flujo_con_Arg DESC;
                        """

# Unimos países_con_sedes_en_Arg_por_región con la tabla anterior para tener en una misma tabla
# todos los datos finales del ejercicio.
Region_Sedes_Flujo_Arg= sql ^"""
                        SELECT
                            f.Region AS Region_Geografica,
                            p.Cantidad AS Paises_Con_Sedes_Argentinas,
                            ROUND(f.Promedio_Flujo_con_Arg,2) AS Promedio_Flujo_con_Argentina
                        FROM flujo_migratorio_Arg_por_region AS f
                        INNER JOIN paises_con_sedes_en_Arg_por_region AS p
                        ON f.Region = p.Region
                        ORDER BY Promedio_Flujo_con_Arg DESC;
                        """

# Consulta de SQL extra para un análisis más completo de la tabla final.                      
Redes_Mas_Usadas = sql ^ """
                        SELECT
                                r.Nombre AS Red_Social,
                            COUNT(*) AS Cantidad
                        FROM
                            Pais_Limpia_1 AS p
                        INNER JOIN
                            Sedes_Limpia AS s ON p.Codigo = s.Codigo_Pais
                        INNER JOIN
                            Redes_Sociales_Limpia AS r ON r.Sede_ID = s.ID
                        GROUP BY
                            r.Nombre
                        ORDER BY
                            Cantidad DESC;
                        """

#%% h  iv)

# Se unió Pais_Limpia_1 con Sedes_Limpia para obtener las distintas sedes que tiene un país. Luego,
# a esa tabla se la unió con Redes_Sociales_Limpia a través de la Sede_ID para así obtener las redes
# sociales de todas las sedes que tienen al menos una.
Redes_Por_Pais = sql ^ """
                        SELECT DISTINCT 
                            p.Nombre As Pais,
                            r.Sede_ID AS Sede, 
                            r.Nombre AS Red_Social,
                            r.URL
                        FROM Pais_Limpia_1 AS p
                        INNER JOIN Sedes_Limpia AS s
                        ON p.Codigo = s.Codigo_Pais
                        INNER JOIN Redes_Sociales_Limpia AS r
                        ON r.Sede_ID = s.ID
                        ORDER BY Pais ASC, Sede ASC, Red_Social ASC, URL ASC;
                        """

#%% h iii) Hicimos este punto después del IV, ya que utilizamos elementos de él.

# Hacemos un SELECT DISTINCT con país y red_social para que nos elimine los repetidos y quedarnos
# solo con los distintos tipos de redes sociales que tiene un país (sin importar que sedes distintas
# tengan el mismo tipo).
tipo_red_por_pais = sql ^ """
                 SELECT DISTINCT Pais, Red_Social
                 FROM Redes_Por_Pais
                 """
# Utilizamos COUNT para contar cuántas veces aparece un país (ya que aparecerá según la cantidad de
# distintos tipos de redes sociales que tiene).
Cantidad_Tipo_Redes_Por_Pais = sql ^ """
                 SELECT DISTINCT Pais, COUNT(Pais) AS Cantidad_Tipos_de_Redes
                 FROM tipo_red_por_pais
                 GROUP BY Pais
                 ORDER BY Pais ASC
                 """
     
#%% i i)

# A partir de una tabla obtenida del punto h)i), que nos dice cuántas sedes tiene un país,
# realizamos un join con Pais_Limpia_1 y Pais_Limpia_2 para saber a qué región corresponde cada país
# y sumamos la cantidad de sedes, agrupando por regiones.
region_sedes = sql ^ """
                 SELECT DISTINCT p2.Region, SUM(s.Cantidad_Sedes) AS Cantidad_Sedes_Por_Region 
                 FROM sedes_por_pais AS s
                 INNER JOIN Pais_Limpia_1 AS p1
                 ON s.Codigo_Pais = p1.Codigo
                 INNER JOIN Pais_Limpia_2 AS p2
                 ON p1.Nombre = p2.Nombre
                 GROUP BY p2.Region
                 ORDER BY Cantidad_Sedes_Por_Region DESC
                 """

# Graficamos
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           

ax.bar(data=region_sedes,x='Region', height='Cantidad_Sedes_Por_Region',color='lightpink' )

ax.set_title(' Promedio del Flujo Migratorio por Región Geográfica')  # le ponemos título al grafico
ax.set_xlabel('Región Geográfica', fontsize='medium')  # le ponemos etiqueta al eje x                      
ax.set_ylabel('Cantidad de Sedes', fontsize='medium')  # le ponemos etiqueta al eje y      
ax.bar_label(ax.containers[0], fontsize=9)  # le ponemos etiquetas a las barras segun la cantidad    
plt.xticks(rotation=90, fontsize=7)  # cambiamos el tamaño y la rotación de las etiquetas del eje X para que sean legibles
plt.figtext(0.5, -0.58, 'Gráfico 1. Gráfico de barras que muestra la cantidad de sedes por región geográfica que tiene Argentina', ha='center', va='center', fontsize=9)  # agregamos una leyenda en el pie


#%% i ii)

# Siguiendo el razonamiento del punto h)i), sumamos la cantidad total de inmigrantes en todos los
# años.
inmigrantes_todos_los_años = sql ^ """
                        SELECT DISTINCT
                            Codigo_Pais_Destino AS Codigo_Pais, 
                            SUM("Cantidad") AS Inmigrantes
                        FROM Migraciones_Limpia
                        GROUP BY Codigo_Pais_Destino
                        ORDER BY Codigo_Pais_Destino ASC
                        """

# Siguiendo el razonamiento del punto h)i), sumamos la cantidad total de inmigrantes en todos los
# años.
emigrantes_todos_los_años = sql ^ """
                        SELECT DISTINCT
                            Codigo_Pais_Origen AS Codigo_Pais,
                            SUM("Cantidad") AS Emigrantes
                        FROM Migraciones_Limpia
                        WHERE Codigo_Pais_Origen != 'zzz'
                        GROUP BY Codigo_Pais_Origen 
                        ORDER BY Codigo_Pais_Origen ASC
                        """

# Juntamos la información de las últimas dos tablas.
migracion_todos_los_años = sql ^ """
                        SELECT DISTINCT 
                            i.Codigo_Pais, 
                            i.Inmigrantes, 
                            e.Emigrantes
                        FROM inmigrantes_todos_los_años AS i
                        INNER JOIN emigrantes_todos_los_años AS e
                        ON i.Codigo_Pais = e.Codigo_Pais
                        ORDER BY i.Codigo_Pais ASC
                        """

# Calculamos el flujo migratorio de la misma manera que en los puntos anteriores.
flujo_migratorio_todos_los_años = sql ^ """
                        SELECT DISTINCT
                            m1.Codigo_Pais,
                            m1.Inmigrantes,
                            m2.Emigrantes,
                            (m1.Inmigrantes - m2.Emigrantes) AS Diferencia
                        FROM migracion_todos_los_años AS m1
                        INNER JOIN migracion_todos_los_años AS m2
                        ON m1.Codigo_Pais = m2.Codigo_Pais
                        ORDER BY m1.Codigo_Pais ASC
                        """

# Calculamos el promedio del flujo migratorio según región.
flujo_migratorio_promedio_por_region = sql ^"""
                         SELECT DISTINCT p2.Region, f.Codigo_Pais, f.Diferencia
                         FROM flujo_migratorio_todos_los_años AS f
                         INNER JOIN Pais_Limpia_1 AS p1
                         ON p1.Codigo=f.Codigo_Pais
                         INNER JOIN Pais_Limpia_2 AS p2
                         ON p1.Nombre = p2.Nombre
                         ORDER BY p2.Region ASC
                         """

# Graficamos
order = flujo_migratorio_promedio_por_region.groupby('Region')['Diferencia'].median().sort_values(ascending=False).index
fig, ax = plt.subplots()
ax = sns.boxplot(x="Diferencia",
                 y="Region",
                 data=flujo_migratorio_promedio_por_region,
                 order=order,
                 color='lightpink',
                 )

ax.set_title(' Promedio del Flujo Migratorio por Región Geográfica')  # le ponemos título al grafico
ax.set_xlabel('Flujo Migratorio (en 1x10^7)', fontsize='medium')  # le ponemos etiqueta al eje x                     
ax.set_ylabel('Región Geográfica', fontsize='medium')  # le ponemos etiqueta al eje y
plt.figtext(0.235, -0.05, 'Gráfico 2. Boxplot que muestra el promedio del flujo migratorio donde Argentina tiene una sede por region geografica', ha='center', va='center', fontsize=9)  # agregamos una leyenda en el pie

#%% i iii)

# Juntamos la información de sedes_por_pais (tabla obtenida del punto h)i) con la de destino_Arg,
# que nos indica la cantidad de inmigrantes que recibe Argentina de esos países (es decir, la
# cantidad de personas que migran de esos países hacia Argentina). Esto es para ver si existe alguna
# relación entre ambos datos.
relacion_inmigrantes_sedes = sql ^"""
                         SELECT DISTINCT d.Pais, d.Codigo, d.Cantidad AS Inmigrantes, s.Cantidad_Sedes
                         FROM destino_Arg AS d
                         INNER JOIN sedes_por_pais AS s
                         ON d.Codigo=s.Codigo_Pais
                         """

# Graficamos

fig, ax = plt.subplots() 

plt.rcParams['font.family'] = 'sans-serif'           
ax.scatter(data = relacion_inmigrantes_sedes,  
           x='Cantidad_Sedes', 
           y='Inmigrantes',
           s=15,                       # tamano de los puntos
           color='purple'       # color de los puntos
           )           

ax.set_xlabel('Cantidad Sedes', fontsize='medium')  # le ponemos etiqueta al eje x                     
ax.set_ylabel('Inmigrantes', fontsize='medium')  # le ponemos etiqueta al eje y 
plt.figtext(0.45, -0.05, 'Gráfico 3. Gráfico de dispersión que muestra la relacion que hay entre la cantidad de sedes que tiene un pais \n con la cantidad de personas que inmigran a Argentina en el año 2000', ha='center', va='center', fontsize=8)  # agregamos una leyenda en el pie



#%% EXTRA

# Ahora juntamos los datos del flujo migratorio relacionando los países solo con Argentina con la
# cantidad de sedes dada por países (sedes_por_pais).
relacion_flujo_sedes_arg = sql ^"""
                         SELECT DISTINCT f.Codigo, f.Diferencia, s.Cantidad_Sedes
                         FROM flujo_migratorio_Arg AS f
                         INNER JOIN sedes_por_pais AS s
                         ON f.Codigo=s.Codigo_Pais
                         """

# graficamos

fig, ax = plt.subplots() 

plt.rcParams['font.family'] = 'sans-serif'           
ax.scatter(data = relacion_flujo_sedes_arg,  
           x='Cantidad_Sedes', 
           y='Diferencia',
           s=15,                       # tamano de los puntos
           color='purple')

ax.set_xlabel('Cantidad Sedes Argentinas en el Exterior', fontsize='medium')  # le ponemos etiqueta al eje x                       
ax.set_ylabel('Flujo Migratorio Argentino', fontsize='medium')  # le ponemos etiqueta al eje y
plt.figtext(0.45, -0.05, 'Gráfico 4. Gráfico de dispersión que muestra la relacion que hay entre la cantidad de sedes que tiene un pais \n con la cantidad de flujo migratorio de argentina con esos paises en el año 2000', ha='center', va='center', fontsize=8) # agregamos una leyenda en el pie 


#%% seccion métrica para GQM_1

# Contamos la cantidad de sedes que no tienen redes sociales registradas.
metrica1 =sql^ """       
            SELECT COUNT(*) AS nulos
            FROM listaSedesDatos
            WHERE 
                redes_sociales == '' OR 
                redes_sociales IS NULL ;
                """
                
# Contamos la cantidad de sedes que tienen al menos una red social registrada.               
metrica2 = sql ^ """
            SELECT COUNT(redes_sociales) AS validos
            FROM listaSedesDatos
            WHERE redes_sociales != ''
               AND redes_sociales IS NOT NULL
            """
nulos = metrica1['nulos']
validos = metrica2['validos']
#print(nulos) 
#print(validos)           
metrica_final = nulos / validos
print(metrica_final)

#%% seccion métrica para GQM_2

total_consulados = len(listaSedes)
activos = (listaSedes["estado"] == "Activo").sum()

# Calcular la proporción de activos sobre el total
proporcion_activos = activos / total_consulados
print(activos)
print(total_consulados)
print(proporcion_activos)
#%% seccion métrica para GQM_3

total_codigos = listaDatosMigraciones["Country Origin Code"].count() + listaDatosMigraciones["Country Dest Code"].count()

codigos_no_zzz_origen = (listaDatosMigraciones["Country Origin Code"] != "zzz").sum()
codigos_no_zzz_destino = (listaDatosMigraciones["Country Dest Code"] != "zzz").sum()

codigos_no_zzz = codigos_no_zzz_origen + codigos_no_zzz_destino
proporcion_no_zzz = codigos_no_zzz / total_codigos
print(codigos_no_zzz)
print(total_codigos)
print(proporcion_no_zzz)
#%%  seccion métrica para GQM_4

telefonos_adicionales_secciones=sql ^ """
                SELECT DISTINCT COUNT (*) AS telefono
                FROM listaSecciones
                WHERE telefonos_adicionales IS NOT NULL OR
                    telefonos_adicionales  != '' 
                """
print (telefonos_adicionales_secciones)

seccionetotales=sql ^ """
                SELECT DISTINCT COUNT (sede_desc_castellano) AS totales
                FROM listaSecciones
                """
print(telefonos_adicionales_secciones)


consular = telefonos_adicionales_secciones['telefono']
totales = seccionetotales ['totales']
print(telefonos_adicionales_secciones) 
print(totales)           
metrica_final = consular /totales
print(metrica_final)