# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:18:25 2024

@author: lourdes
"""

import pandas as pd
from inline_sql import sql, sql_val

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # Para graficar series multiples
from   matplotlib import ticker   # Para agregar separador de miles
import seaborn as sns           # Para graficar histograma

#%% subir tablas
carpeta = "~/Downloads/tp/"


listaSedes = pd.read_csv(carpeta+"lista-sedes.csv")

listaSecciones = pd.read_csv(carpeta+"lista-secciones.csv")

listaSedesDatos = pd.read_csv(carpeta+"lista-sedes-datos.csv")

listaDatosMigraciones = pd.read_csv(carpeta+"datos_migraciones.csv")

#%% limpiar tablas
#lo que necesito limpiar y tener es:
    
#sedes: sede_id, nombre_see, codigo_pais
#pais: 1) codigo_pais y nombre_pais   2) codigo_pais y region
#redes_sociales: url, red_social, sede_idd
#secciones: sede_id, descripcion_sede
#migracion: codigo_iso(origen y destino), años, cantidad

Sedes_Limpia = sql^"""
                    SELECT DISTINCT 
                        sede_id AS ID, 
                        sede_desc_castellano AS Nombre, 
                        REPLACE(pais_iso_3,'GRB','GBR') AS Codigo_Pais
                    FROM listaSedes
                    """

Pais_Limpia_1 = sql ^"""
                    SELECT DISTINCT 
                        REPLACE(pais_iso_3,'GRB','GBR') AS Codigo, 
                        pais_castellano AS Nombre
                    FROM listaSedesDatos
                    """


Pais_Limpia_2  = sql ^"""
                    SELECT DISTINCT 
                        pais_castellano AS Nombre, 
                        region_geografica AS Region
                    FROM listaSedesDatos
                    """
                    
Secciones_Limpia = sql^"""
                    SELECT DISTINCT 
                        sede_id AS Sede_ID, 
                        sede_desc_castellano AS Descripcion
                    FROM listaSecciones
                    WHERE sede_id IS NOT NULL
                    """
                    

#limpieza de la de redes sociales
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
#TRIM le saca los eespacios adelante y atras si es que tiene

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

Redes_Sociales_Limpia = sql ^ """
                SELECT DISTINCT *
                FROM redes_sociales_3
                WHERE Nombre != 'None'
                """


#limpieza migraciones
Migraciones_Limpia = sql ^ """
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
                          
#%% descargar tablas limpias
Sedes_Limpia.to_csv('Sedes_Limpia.csv', index=False)
Redes_Sociales_Limpia.to_csv('Redes_Sociales_Limpia.csv', index=False)
Secciones_Limpia.to_csv('Secciones.csv', index=False)
Migraciones_Limpia.to_csv('Migraciones_Limpia.csv', index=False)
Pais_Limpia_1.to_csv('Pais_Limpia_1.csv', index=False)
Pais_Limpia_2.to_csv('Pais_Limpia_2.csv', index=False)

    


#%% ejercicios

#h i)
#cantidad sedes por pais
sedes_por_pais = sql^"""
                    SELECT DISTINCT 
                        Codigo_Pais, 
                        COUNT(ID) AS Cantidad_Sedes
                    FROM Sedes_Limpia
                    GROUP BY Codigo_Pais
                    """

#cantidad de secciones que tiene cada sede
secciones_por_sede = sql^"""
                    SELECT DISTINCT
                        Sede_ID, 
                        COUNT(*) AS Cantidad_Secciones
                    FROM Secciones_Limpia
                    GROUP BY Sede_ID
                    """


#secciones por pais
secciones_por_pais_1 =sql^"""
                    SELECT DISTINCT s.ID, s.Codigo_Pais, sc.Cantidad_Secciones
                    FROM Sedes_Limpia AS s
                    INNER JOIN secciones_por_sede AS sc
                    ON s.ID=sc.sede_id
                    """

secciones_por_pais_2= sql^"""
                    SELECT DISTINCT Codigo_Pais, SUM(Cantidad_Secciones) AS Cantidad_Secciones 
                    FROM secciones_por_pais_1
                    GROUP BY Codigo_Pais
                    """

secciones_promedio_por_pais= sql^"""
                            SELECT DISTINCT 
                                s.Codigo_Pais, 
                                (sc.Cantidad_Secciones/s.Cantidad_Sedes) AS Secciones_Promedio, 
                                s.Cantidad_Sedes
                            FROM sedes_por_pais AS s
                            INNER JOIN secciones_por_pais_2 AS sc
                            ON s.Codigo_Pais = sc.Codigo_Pais
                            """

#flujo migratorio
inmigrantes = sql ^ """
                        SELECT DISTINCT
                            Codigo_Pais_Destino AS Codigo_Pais, 
                            SUM("2000") AS Inmigrantes
                        FROM Migraciones_Limpia
                        GROUP BY Codigo_Pais_Destino
                        ORDER BY Codigo_Pais_Destino ASC
                        """

emigrantes = sql ^ """
                        SELECT DISTINCT
                            Codigo_Pais_Origen AS Codigo_Pais,
                            SUM("2000") AS Emigrantes
                        FROM Migraciones_Limpia
                        WHERE Codigo_Pais_Origen != 'zzz'
                        GROUP BY Codigo_Pais_Origen 
                        ORDER BY Codigo_Pais_Origen ASC
                        """

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
                        
                       
#resultado del ejercicio
Sedes_Seccion_Flujo =sql^"""
                        SELECT DISTINCT  
                            p.Nombre AS Pais, 
                            sp.Cantidad_Sedes AS sedes, 
                            sp.Secciones_Promedio, 
                            f.Diferencia AS flujo_migratorio_neto
                        FROM secciones_promedio_por_pais AS sp
                        INNER JOIN flujo_migratorio AS f
                        ON sp.Codigo_Pais= f.Codigo_Pais
                        INNER JOIN Pais_Limpia_1 AS p
                        ON p.Codigo= f.Codigo_Pais
                        ORDER BY Cantidad_Sedes DESC, Pais ASC
                        """



#%% h ii)
paises_con_sedes_en_Arg = sql ^"""
                        SELECT DISTINCT
                            p.Nombre AS Pais,
                            p.Codigo
                        FROM Pais_Limpia_1 AS p
                        INNER JOIN Sedes_Limpia AS s
                        ON p.Codigo = s.Codigo_Pais
                        ORDER BY Pais ASC
                        """

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

origen_Arg= sql ^"""
                        SELECT DISTINCT
                            p.Pais AS Pais,
                            p.Codigo AS Codigo ,
                            m."2000" AS Cantidad
                        FROM Migraciones_Limpia AS m
                        INNER JOIN paises_con_sedes_en_Arg AS p
                        ON m.Codigo_Pais_Destino = p.Codigo
                        WHERE m.Codigo_Pais_Origen = 'ARG'
                        ORDER BY Pais ASC
                        """


destino_Arg = sql ^"""
                        SELECT DISTINCT
                            p.Pais AS Pais,
                            p.Codigo AS Codigo ,
                            m."2000" AS Cantidad
                        FROM Migraciones_Limpia AS m
                        INNER JOIN paises_con_sedes_en_Arg AS p
                        ON m.Codigo_Pais_Origen = p.Codigo
                        WHERE m.Codigo_Pais_Destino = 'ARG'
                        ORDER BY Pais ASC
                        """

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

Region_Sedes_Flujo_Arg= sql ^"""
                        SELECT
                            f.Region AS Region_Geografica,
                            p.Cantidad AS Paises_Con_Sedes_Argentinas,
                            f.Promedio_Flujo_con_Arg AS Promedio_Flujo_con_Argentina
                        FROM flujo_migratorio_Arg_por_region AS f
                        INNER JOIN paises_con_sedes_en_Arg_por_region AS p
                        ON f.Region = p.Region
                        ORDER BY Promedio_Flujo_con_Arg DESC;
                        """


#%% h  iv)
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

#%% h iii)
#es el h iii), pero uso cosas del h iv), por eso esta escrito después

#como quiero saber la cantidad de tipos de redes, hago una tabla (usando distinct) que solo me deje los tipos de redes (sin enlaces y sin cuantas de cada tipo)
tipo_red_por_pais = sql ^ """
                 SELECT DISTINCT Pais, Red_Social
                 FROM Redes_Por_Pais
                 """
#y las cuento
Cantidad_Tipo_Redes_Por_Pais = sql ^ """
                 SELECT DISTINCT Pais, COUNT(Pais) AS Cantidad_Tipos_de_Redes
                 FROM tipo_red_por_pais
                 GROUP BY Pais
                 ORDER BY Pais ASC
                 """
     
#%% i i)

region_sedes = sql ^ """
                 SELECT DISTINCT Region_Geografica, Paises_Con_Sedes_Argentinas
                 FROM Region_Sedes_Flujo_Arg
                 ORDER BY Paises_Con_Sedes_Argentinas DESC
                 """

fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           

ax.bar(data=region_sedes,x='Region_Geografica', height='Paises_Con_Sedes_Argentinas')

ax.set_title('Cantidad de sedes  por region geografica')
ax.set_xlabel('Region', fontsize='medium')                       
ax.set_ylabel('Flujo', fontsize='medium')    
ax.set_xlim(-1, 9)
ax.set_ylim(0, 25)
ax.bar_label(ax.containers[0], fontsize=8) 
plt.xticks(rotation=90, fontsize=6)

#%% i ii)

inmigrantes_todos_los_años = sql ^ """
                        SELECT DISTINCT
                            Codigo_Pais_Destino AS Codigo_Pais, 
                            (SUM("1960")+SUM("1970")+SUM("1980")+SUM("1990")+SUM("2000")) AS Inmigrantes
                        FROM Migraciones_Limpia
                        GROUP BY Codigo_Pais_Destino
                        ORDER BY Codigo_Pais_Destino ASC
                        """

emigrantes_todos_los_años = sql ^ """
                        SELECT DISTINCT
                            Codigo_Pais_Origen AS Codigo_Pais,
                            (SUM("1960")+SUM("1970")+SUM("1980")+SUM("1990")+SUM("2000")) AS Emigrantes
                        FROM Migraciones_Limpia
                        WHERE Codigo_Pais_Origen != 'zzz'
                        GROUP BY Codigo_Pais_Origen 
                        ORDER BY Codigo_Pais_Origen ASC
                        """

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

flujo_migratorio_promedio_por_region = sql ^"""
                         SELECT DISTINCT p2.Region, f.Codigo_Pais, f.Diferencia
                         FROM flujo_migratorio_todos_los_años AS f
                         INNER JOIN Pais_Limpia_1 AS p1
                         ON p1.Codigo=f.Codigo_Pais
                         INNER JOIN Pais_Lim pia_2 AS p2
                         ON p1.Nombre = p2.Nombre
                         ORDER BY p2.Region ASC
                         """

# gráfico
order = flujo_migratorio_promedio_por_region.groupby('Region')['Diferencia'].median().sort_values(ascending=False).index
fig, ax = plt.subplots()
ax = sns.boxplot(x="Diferencia",
                 y="Region",
                 data=flujo_migratorio_promedio_por_region,
                 order=order,
                 color='#F4C2C2',
                 )

#%% i iii)

relacion_inmigrantes_sedes = sql ^"""
                         SELECT DISTINCT d.Pais, d.Codigo, d.Cantidad AS Inmigrantes, s.Cantidad_Sedes
                         FROM destino_Arg AS d
                         INNER JOIN sedes_por_pais AS s
                         ON d.Codigo=s.Codigo_Pais
                         """

# gráfico

fig, ax = plt.subplots() 

plt.rcParams['font.family'] = 'sans-serif'           
ax.scatter(data = relacion_inmigrantes_sedes,  
           x='Cantidad_Sedes', 
           y='Inmigrantes',
           s=15,                       # Tamano de los puntos
           color='magenta')           # Color de los puntos

ax.set_title('Relacion Inmigrantes con sedes')
ax.set_xlabel('Cantidad Sedes', fontsize='medium')                       
ax.set_ylabel('Inmigrantes', fontsize='medium')   

#%%
#rel entre emigrantes y sedes

relacion_emigrantes_sedes = sql ^"""
                         SELECT DISTINCT o.Pais, o.Codigo, o.Cantidad AS Emigrantes, s.Cantidad_Sedes
                         FROM origen_Arg AS o
                         INNER JOIN sedes_por_pais AS s
                         ON o.Codigo=s.Codigo_Pais
                         """

# gráfico

fig, ax = plt.subplots() 

plt.rcParams['font.family'] = 'sans-serif'           
ax.scatter(data = relacion_emigrantes_sedes,  
           x='Cantidad_Sedes', 
           y='Emigrantes',
           s=15,                       # Tamano de los puntos
           color='magenta')

ax.set_title('Relacion Emigrantes con sedes')
ax.set_xlabel('Cantidad Sedes', fontsize='medium')                       
ax.set_ylabel('Emigrantes', fontsize='medium') 

#%%
#rel entre flujo y sedes

relacion_flujo_sedes = sql ^"""
                         SELECT DISTINCT f.Codigo_Pais, f.Diferencia, s.Cantidad_Sedes
                         FROM flujo_migratorio AS f
                         INNER JOIN sedes_por_pais AS s
                         ON f.Codigo_Pais=s.Codigo_Pais
                         """

# gráfico

fig, ax = plt.subplots() 

plt.rcParams['font.family'] = 'sans-serif'           
ax.scatter(data = relacion_flujo_sedes,  
           x='Cantidad_Sedes', 
           y='Diferencia',
           s=15,                       # Tamano de los puntos
           color='magenta')

ax.set_title('Relacion flujo migratorio con sedes')
ax.set_xlabel('Cantidad Sedes', fontsize='medium')                       
ax.set_ylabel('Flujo', fontsize='medium') 
 

#%%
# boxplot sin america del norte
flujo_migratorio_promedio_por_region_sin_an = sql ^"""
                         SELECT DISTINCT Region, Codigo_Pais, Diferencia
                         FROM flujo_migratorio_promedio_por_region
                         WHERE Region!= 'AMÉRICA  DEL  NORTE'
                         """
fig, ax = plt.subplots()   
                      
order = flujo_migratorio_promedio_por_region_sin_an.groupby('Region')['Diferencia'].median().sort_values(ascending=False).index
ax = sns.boxplot(x="Diferencia",
                 y="Region",
                 data=flujo_migratorio_promedio_por_region_sin_an,
                 order=order,
                 color='#F4C2C2',
                 )

#%%
#rel entre flujo migratorio arg con cant sedes

relacion_flujo_sedes_arg = sql ^"""
                         SELECT DISTINCT f.Codigo, f.Diferencia, s.Cantidad_Sedes
                         FROM flujo_migratorio_Arg AS f
                         INNER JOIN sedes_por_pais AS s
                         ON f.Codigo=s.Codigo_Pais
                         """

# gráfico

fig, ax = plt.subplots() 

plt.rcParams['font.family'] = 'sans-serif'           
ax.scatter(data = relacion_flujo_sedes_arg,  
           x='Cantidad_Sedes', 
           y='Diferencia',
           s=15,                       # Tamano de los puntos
           color='magenta')

ax.set_title('Relacion flujo migratorio Arg con sedes')
ax.set_xlabel('Cantidad Sedes', fontsize='medium')                       
ax.set_ylabel('Flujo', fontsize='medium') 



#%% seccion métrica para GQM
   
metrica1 =sql^ """       
            SELECT COUNT(*) AS nulos
            FROM listaSedesDatos
            WHERE 
                redes_sociales == '' OR 
                redes_sociales IS NULL ;
                """
metrica2 = sql ^ """
            SELECT COUNT(redes_sociales) AS validos
            FROM listaSedesDatos
            WHERE redes_sociales != ''
               AND redes_sociales IS NOT NULL
            """
nulos = metrica1['nulos']
validos = metrica2['validos']
print(nulos) 
print(validos)           
metrica_final = nulos / validos
print(metrica_final)

#%% descargar tablas ejericicos (primeras filas y completas)
#h i)
ej_hi_primeras_filas = Sedes_Seccion_Flujo.head()
ej_hi_primeras_filas.to_csv('ej_hi_primeras_filas.csv', index=False)
ej_hi_entera = Sedes_Seccion_Flujo
ej_hi_entera.to_csv('ej_hi_entera.csv', index=False)

#%%h ii)
ej_hii_primeras_filas = Region_Sedes_Flujo_Arg.head()
ej_hii_primeras_filas.to_csv('ej_hii_primeras_filas.csv', index=False)
ej_hii_entera = Region_Sedes_Flujo_Arg
ej_hii_entera.to_csv('ej_hii_entera.csv', index=False)

#%%h iii)
ej_hiii_primeras_filas = Cantidad_Tipo_Redes_Por_Pais.head()
ej_hiii_primeras_filas.to_csv('ej_hiii_primeras_filas.csv', index=False)
ej_hiii_entera = Cantidad_Tipo_Redes_Por_Pais
ej_hiii_entera.to_csv('ej_hiii_entera.csv', index=False)

#%%h iv)
ej_hiv_primeras_filas = Redes_Por_Pais.head()
ej_hiv_primeras_filas.to_csv('ej_hiv_primeras_filas.csv', index=False)
ej_hiv_entera = Redes_Por_Pais
ej_hiv_entera.to_csv('ej_hiv_entera.csv', index=False)