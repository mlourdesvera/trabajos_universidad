#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:33:07 2024

@author: Estudiante
"""
import pandas as pd
from inline_sql import sql, sql_val



#%%
carpeta = "~/Downloads/tp/"


listaSedes = pd.read_csv(carpeta+"lista-sedes.csv")

listaSecciones = pd.read_csv(carpeta+"lista-secciones.csv")

listaSedesDatos = pd.read_csv(carpeta+"lista-sedes-datos.csv")

listaDatosMigraciones = pd.read_csv(carpeta+"datos_migraciones.csv")




#%%


redesSociales =sql^  """
            SELECT DISTINCT sede_id, redes_sociales
            FROM listaSedesDatos
            WHERE redes_sociales!='None';            
            """





redesSociales2 = sql^ """
                    SELECT DISTINCT sede_id , REPLACE(redes_sociales, ' // ', '///') AS Redes_Sociales,
                    CASE WHEN TRIM(SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 1)) = '' THEN NULL ELSE SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 1) END AS Red_social1,
                    CASE WHEN TRIM(SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 2)) = '' THEN NULL ELSE SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 2) END AS Red_social2,
                    CASE WHEN TRIM(SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 3)) = '' THEN NULL ELSE SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 3) END AS Red_social3,
                    CASE WHEN TRIM(SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 4)) = '' THEN NULL ELSE SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 4) END AS Red_social4,
                    CASE WHEN TRIM(SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 5)) = '' THEN NULL ELSE SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 5) END AS Red_social5,
                    CASE WHEN TRIM(SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 6)) = '' THEN NULL ELSE SPLIT_PART(REPLACE(redes_sociales, ' // ', '///'), '///', 6) END AS Red_social6
                    FROM redesSociales;  
                    """
                    
tablaRedes= sql^ """
                SELECT sede_id,Red_social1, Red_social2, Red_social3, Red_social4, Red_social5, Red_social6
                FROM redesSociales2;
                """                   
          
redes_unidas_sin_null  = sql^ """
                                SELECT sede_id, Red_social1 AS RedSocial 
                                FROM tablaRedes 
                                WHERE Red_social1 IS NOT NULL
                                UNION ALL 
                                SELECT sede_id, Red_social2 AS RedSocial 
                                FROM tablaRedes 
                                WHERE Red_social2 IS NOT NULL
                                UNION ALL 
                                SELECT sede_id, Red_social3 AS RedSocial 
                                FROM tablaRedes 
                                WHERE Red_social3 IS NOT NULL
                                UNION ALL 
                                SELECT sede_id, Red_social4 AS RedSocial 
                                FROM tablaRedes 
                                WHERE Red_social4 IS NOT NULL
                                UNION ALL 
                                SELECT sede_id, Red_social5 AS RedSocial 
                                FROM tablaRedes 
                                WHERE Red_social5 IS NOT NULL
                                UNION ALL 
                                SELECT sede_id, Red_social6 AS RedSocial 
                                FROM tablaRedes 
                                WHERE Red_social6 IS NOT NULL;
                                """
                                
                                           
                
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
                FROM redes_unidas_sin_null;
                """
                    
Redes_Sociales_Limpia = sql ^ """
                SELECT DISTINCT *
                FROM Redes_Sociales
                WHERE Nombre != 'None'
                """



#%%
#limpiamos sedes

SedesLimpia = sql^"""
                SELECT DISTINCT 
                    sede_id, 
                    sede_desc_castellano,
                CASE 
                    WHEN pais_iso_3 = 'GRB' THEN 'GBR' 
                    ELSE pais_iso_3 
                END AS Codigo_Pais
                FROM listaSedes;
                    """

#%%
#creo tabla país

Tabla_Pais = sql ^"""
                    SELECT DISTINCT pais_iso_3 AS Codigo_Pais, pais_castellano AS Nombre_Pais, region_geografica
                    FROM listaSedesDatos
                    """

#%% h iv)

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
                        FROM Redes_por_pais
                        ORDER BY Pais ASC, Sede ASC, Red_Social ASC, URL ASC;
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
                 ORDER BY Pais ASC;
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
                            Pais_Origen AS Pais, SUM(year2000) AS Inmigrantes
                        FROM limpieza_tabla_migracion
                        GROUP BY Pais_Origen  
                        """


flujo_migratorio_emigrantes = sql ^ """
                        SELECT DISTINCT
                            Pais_Destino AS Pais, SUM(year2000) AS Emigrantes
                        FROM limpieza_tabla_migracion
                        GROUP BY Pais_Destino 
                        """
                        
casi_flujo_migratorio = sql ^ """
                        SELECT DISTINCT i.Pais, i.Inmigrantes, e.Emigrantes
                        FROM flujo_migratorio_inmigrantes AS i
                        INNER JOIN flujo_migratorio_emigrantes AS e
                        ON i.Pais = e.Pais
                        """
                        
flujo_migratorio = sql ^ """
                        SELECT DISTINCT 
                            f1.Pais,
                            f1.Inmigrantes,
                            f2.Emigrantes,
                            (f1.Inmigrantes - f2.Emigrantes) AS Diferencia
                        FROM casi_flujo_migratorio AS f1
                        INNER JOIN casi_flujo_migratorio AS f2 
                        ON f1.Pais = f2.Pais
                        """
                        
                        
                        
                        
                




