#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 08:46:35 2024

@author: Estudiante
"""

import pandas as pd
from inline_sql import sql, sql_val

#%%
carpeta = "~/Descargas/tp/"


listaSedes = pd.read_csv(carpeta+"lista-sedes.csv")

listaSecciones = pd.read_csv(carpeta+"lista-secciones.csv")

listaSedesDatos = pd.read_csv(carpeta+"lista-sedes-datos.csv")

listaDatosMigraciones = pd.read_csv(carpeta+"datos_migraciones.csv")


#%%

#limpiamos sedes

SedesLimpia = sql^"""
SELECT DISTINCT sede_id, sede_desc_castellano, REPLACE(pais_iso_3,'GRB','GBR') AS Codigo_Pais
FROM listaSedes
"""

#limpiamos secciones

SeccionesLimpia= sql^"""
SELECT DISTINCT sede_id, sede_desc_castellano
FROM listaSecciones
WHERE sede_id IS NOT NULL
"""
#%%
#limpiamos redes en sedesDatos

listaSedesDatosLimpia = sql^ """
SELECT sede_id, redes_sociales, REPLACE(pais_iso_3,'GRB','GBR') AS Codigo_Pais, pais_castellano, region_geografica
FROM listaSedesDatos
WHERE redes_sociales!='None'
"""

#%%
datos_copia = listaSedesDatos.copy() #copio listaSedesDatos para no perder los demas datos CREO Q HACER ESTO YA NO HACE FALTA REVISAR!!

datos_copia["redes_sociales"] = datos_copia["redes_sociales"].str.split("  //  ") # separo los datos por //

datos_copia = datos_copia.explode("redes_sociales") #los pone en distintas filas

sedesDatos2 = sql^"""
SELECT DISTINCT sede_id, redes_sociales
FROM datos_copia
"""

redes_unidas_sin_null  = sql^ """
                                SELECT sede_id, redes_sociales AS RedSocial
                                FROM sedesDatos2
                                WHERE redes_sociales!=''
                                """

#agregamos la columna red social en la que
Redes_Sociales = sql^"""
                SELECT DISTINCT sede_id, RedSocial AS URL,
                CASE
                    WHEN RedSocial LIKE '%twitter%' THEN 'Twitter'
                    WHEN RedSocial LIKE '%instagram%' THEN 'Instagram'
                    WHEN RedSocial LIKE '%Instagram%' THEN 'Instagram'
                    WHEN RedSocial LIKE '%facebook%' THEN 'Facebook'
                    WHEN RedSocial LIKE '%Facebook%' THEN 'Facebook'
                    WHEN RedSocial LIKE '%youtube%' THEN 'Youtube'
                    WHEN RedSocial LIKE '%flickr%' THEN 'Flickr'
                    WHEN RedSocial LIKE '%linkedin%' THEN 'LinkedIn'
                ELSE NULL END AS Nombre
                FROM redes_unidas_sin_null
                """
                
Redes_Sociales_Limpia = sql ^ """
                SELECT DISTINCT *
                FROM Redes_Sociales
                WHERE Nombre != 'None'
                """
#%%
#creo tabla país

Tabla_Pais = sql ^"""
                    SELECT DISTINCT REPLACE(pais_iso_3,'GRB','GBR') AS Codigo_Pais, pais_castellano AS Nombre_Pais, region_geografica
                    FROM listaSedesDatos
                    """
#%%
#tabla redes por pais (ejercicio h iv)
Redes_por_pais = sql ^ """
                        SELECT DISTINCT *
                        FROM Tabla_Pais AS t
                        INNER JOIN SedesLimpia AS s
                        ON t.Codigo_Pais = s.Codigo_Pais
                        INNER JOIN Redes_Sociales_Limpia AS r
                        ON r.sede_id = s.sede_id;
                        """


Redes_por_pais_final = sql ^ """
                        SELECT DISTINCT Nombre_Pais AS Pais, sede_id AS Sede, Nombre AS Red_Social, URL
                        FROM Redes_por_pais;
                        """
                        

#%% h iii)


Cantidad_Redes = sql ^ """
                 SELECT DISTINCT Pais, Red_Social
                 FROM Redes_por_pais_final
                 """
Cantidad_Redes_total = sql ^ """
                 SELECT DISTINCT Pais, COUNT(Pais) AS Cantidad
                 FROM Cantidad_Redes
                 GROUP BY Pais
                 """
#%%   h i)


limpieza_tabla_migracion = sql ^ """
                          SELECT DISTINCT
                              "Country Origin Name" AS Pais_Origen,
                              "Country Origin Code" AS Codigo_Pais_Origen,
                              "Country Dest Name" AS Pais_Destino,
                              "Country Dest Code" AS Codigo_Pais_Destino,
                              "1960 [1960]" AS "1960",
                              "1970 [1970]" AS "1970",
                              "1980 [1980]" AS "1980",
                              "1990 [1990]" AS "1990",
                              CASE
                                  WHEN "2000 [2000]" = '..' THEN 0
                                  ELSE CAST("2000 [2000]" AS INTEGER)
                              END AS year2000
                          FROM listaDatosMigraciones
                          WHERE "Migration by Gender Code" = 'TOT';
                          """




flujo_migratorio_inmigrantes = sql ^ """
                        SELECT DISTINCT
                            Codigo_Pais_Destino AS Codigo_Pais, SUM(year2000) AS Inmigrantes
                        FROM limpieza_tabla_migracion
                        GROUP BY Codigo_Pais_Destino
                        """


flujo_migratorio_emigrantes = sql ^ """
                        SELECT DISTINCT
                            Codigo_Pais_Origen AS Codigo_Pais, SUM(year2000) AS Emigrantes
                        FROM limpieza_tabla_migracion
                        GROUP BY Codigo_Pais_Origen 
                        """

casi_flujo_migratorio = sql ^ """
                        SELECT DISTINCT i.Codigo_Pais, i.Inmigrantes, e.Emigrantes
                        FROM flujo_migratorio_inmigrantes AS i
                        INNER JOIN flujo_migratorio_emigrantes AS e
                        ON i.Codigo_Pais = e.Codigo_Pais
                        """

flujo_migratorio = sql ^ """
                        SELECT DISTINCT
                            f1.Codigo_Pais,
                            f1.Inmigrantes,
                            f2.Emigrantes,
                            (f1.Inmigrantes - f2.Emigrantes) AS Diferencia
                        FROM casi_flujo_migratorio AS f1
                        INNER JOIN casi_flujo_migratorio AS f2
                        ON f1.Codigo_Pais = f2.Codigo_Pais
                        """

#cantidad de secciones que tiene cada sede
SeccionesPorSede= sql^"""
SELECT DISTINCT sede_id, COUNT(*) AS CantidadSecciones
FROM SeccionesLimpia
GROUP BY sede_id
"""
#%%
sedes_por_pais= sql^"""
SELECT DISTINCT Codigo_Pais, COUNT(sede_id) AS CantidadSedes
FROM SedesLimpia
GROUP BY Codigo_Pais
"""
#%%
relacionSeccionesPais=sql^"""
SELECT DISTINCT s.sede_id, s.Codigo_Pais, sc.CantidadSecciones
FROM SedesLimpia AS s
INNER JOIN SeccionesPorSede AS sc
ON s.sede_id=sc.sede_id
"""

secciones_por_pais= sql^"""
SELECT DISTINCT Codigo_Pais, SUM(CantidadSecciones) AS Cantidad_Secciones 
FROM relacionSeccionesPais
GROUP BY Codigo_Pais
"""

secciones_promedio= sql^"""
SELECT DISTINCT s.Codigo_Pais, (sc.Cantidad_Secciones/s.CantidadSedes) AS Secciones_Promedio, s.CantidadSedes
FROM sedes_por_pais AS s
INNER JOIN secciones_por_pais AS sc
ON s.Codigo_Pais= sc.Codigo_Pais
"""

#%%

Sedes_Seccion_Flujo =sql^"""
SELECT DISTINCT t.Codigo_Pais, t.Nombre_Pais AS Pais, sp.CantidadSedes AS sedes, sp.Secciones_Promedio, f.Diferencia AS flujo_migratorio_neto
FROM secciones_promedio AS sp
INNER JOIN flujo_migratorio AS f
ON sp.Codigo_Pais= f.Codigo_Pais
INNER JOIN Tabla_Pais AS t
ON t.Codigo_Pais= f.Codigo_Pais
"""

#%%
a= sql^"""
SELECT DISTINCT b.*
FROM secciones_promedio AS b
LEFT JOIN Sedes_Seccion_Flujo  AS c ON b.Codigo_Pais = c.Codigo_Pais
WHERE c.Codigo_Pais IS NULL
"""



