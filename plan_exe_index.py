from datas.connect import conn
import psycopg2

# Connexion à la base de données
cursor = conn.cursor()


# Requête pour vérifier qu'une clé primaire est un index, sur la table région
query1 = """
    SELECT indexname, indexdef
    FROM pg_indexes
    WHERE tablename = 'region';
"""
cursor.execute(query1)
index_details = cursor.fetchall()

'''print(f"Détails des index de la table 'Region':")
for row in index_details:
    index_name, index_definition = row
    print(f"Nom de l'index: {index_name}")
    print(f"Définition de l'index: {index_definition}")
    print("-------------------------------------")
print()'''


# Requête qui liste les communes avec moins de 5000 habitants en 2020 sans index supplémentaire
query2 = """
    EXPLAIN ANALYZE
    SELECT c.num_com, c.nom_com, pc.valeur AS population
    FROM Commune c
    JOIN Pop_Commune pc ON c.num_com = pc.num_com
    WHERE pc.valeur < 5000 AND pc.id_stat = 'P20_POP'
    ORDER BY pc.valeur DESC;
"""
cursor.execute(query2)
results_2 = cursor.fetchall()

# Création de l'index sur l'attribut valeur de la table Pop_Commune
query3 = "CREATE INDEX ON Pop_Commune (valeur);"
cursor.execute(query3)
conn.commit()


# Requête qui liste les communes avec moins de 5000 habitants en utilisant l'index
query4 = """
        EXPLAIN ANALYZE
        SELECT c.num_com, c.nom_com, pc.valeur AS population
        FROM Commune c
        JOIN Pop_Commune pc ON c.num_com = pc.num_com
        WHERE pc.valeur < 5000 AND pc.id_stat = 'P20_POP'
        ORDER BY pc.valeur DESC;
    """
cursor.execute(query4)
results_4 = cursor.fetchall()


cursor.close()
# conn.close()
