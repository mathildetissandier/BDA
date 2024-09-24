from datas.connect import conn

# Connexion à la base de données
cursor = conn.cursor()

# Plan d'exécution de la 1ère requête
nom_region = 'Nouvelle-Aquitaine'
exe_query1 = f"""
    EXPLAIN ANALYZE 
    SELECT d.num_dep, d.nom_dep, d.chef_lieu
    FROM Departement d
    JOIN Region r ON d.num_reg = r.num_reg
    WHERE r.nom_reg = '{nom_region}';
"""
cursor.execute(exe_query1)
explain_results_1 = cursor.fetchall()


# Plan d'exécution de la 2ème requête
num_dep = '33'
seuil_population = 30000
exe_query2 = f"""
    EXPLAIN ANALYZE 
    SELECT c.num_com, c.nom_com, pc.valeur AS population
    FROM Commune c
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    WHERE c.num_dep = '{num_dep}' AND pc.valeur > {seuil_population} AND pc.id_stat = 'P20_POP'
    ORDER BY pc.valeur DESC;
"""
cursor.execute(exe_query2)
explain_results_2 = cursor.fetchall()


# Plan d'exécution de la 3ème requête
exe_query3 = """
    EXPLAIN ANALYZE 
    SELECT r.nom_reg, SUM(pc.valeur) AS population_totale
    FROM Region r
    JOIN Departement d ON r.num_reg = d.num_reg
    JOIN Commune c ON d.num_dep = c.num_dep
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    GROUP BY r.nom_reg
    ORDER BY population_totale DESC
    LIMIT 1;
"""
cursor.execute(exe_query3)
explain_results_3 = cursor.fetchall()


# Plan d'exécution de la 4ème requête
exe_query4 = """
    EXPLAIN ANALYZE 
    SELECT r.nom_reg, SUM(pc.valeur) AS population_totale
    FROM Region r
    JOIN Departement d ON r.num_reg = d.num_reg
    JOIN Commune c ON d.num_dep = c.num_dep
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    GROUP BY r.nom_reg
    ORDER BY population_totale ASC
    LIMIT 1;
"""
cursor.execute(exe_query4)
explain_results_4 = cursor.fetchall()


# Plan d'exécution de la 5ème requête
code_departement33 = '33'
exe_query5 = """
    EXPLAIN ANALYZE 
    SELECT c.nom_com, pc.valeur AS population
    FROM Commune c
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    WHERE c.num_dep = %s AND pc.id_stat = 'P20_POP'
    ORDER BY pc.valeur DESC
    LIMIT 10;
"""
cursor.execute(exe_query5, (code_departement33,))
explain_results_5 = cursor.fetchall()


# Plan d'exécution de la 6ème requête
code_departement33 = '33'
exe_query6 = """
    EXPLAIN ANALYZE 
    SELECT c.nom_com, pc.valeur AS population
    FROM Commune c
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    WHERE c.num_dep = %s AND pc.id_stat = 'P20_POP'
    ORDER BY pc.valeur ASC
    LIMIT 10;
"""
cursor.execute(exe_query6, (code_departement33,))
explain_results_6 = cursor.fetchall()


# Plan d'exécution de la 7ème requête
code_departement77 = '1177'
exe_query7 = """
    EXPLAIN ANALYZE 
    SELECT type_couple, SUM(nb_mar) AS total_mariages
    FROM Stats_Mar1
    WHERE dep = %s AND id_stat = 'MAR21AGE_2'
    GROUP BY type_couple
    ORDER BY total_mariages DESC;
"""
cursor.execute(exe_query7, (code_departement77,))
explain_results_7 = cursor.fetchall()

cursor.close()
# conn.close()
