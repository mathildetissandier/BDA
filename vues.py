from datas.connect import conn
import pandas as pd 
cursor = conn.cursor()

# Vue pour la population des départements pour différentes années
view1 = f"""
CREATE OR REPLACE VIEW Pop_Dep AS
SELECT d.num_dep AS num_departement, d.nom_dep AS departement, p.id_stat, s.libelle AS libelle_indicateur, SUM(p.valeur) AS population
FROM Departement d
JOIN Commune c ON d.num_dep = c.num_dep
JOIN Pop_Commune p ON c.num_com = p.num_com
JOIN Stats_Var s ON p.id_stat = s.id_stat
WHERE p.id_stat = 'D99_POP' OR p.id_stat = 'D90_POP' OR p.id_stat = 'D82_POP' OR p.id_stat = 'D75_POP' OR p.id_stat = 'D68_POP'
GROUP BY num_departement, p.id_stat, libelle_indicateur
ORDER BY departement;
"""
cursor.execute(view1)
query1 = """SELECT * FROM Pop_Dep"""
cursor.execute(query1)
pop_dep = cursor.fetchall()
df_pop_dep = pd.DataFrame(pop_dep, columns=['num_dep', 'departement', 'id_stat', 'libelle_indicateur', 'population'])
"""print(df_pop_dep.head())"""

# Vue pour la population des régions pour différentes années
view2 = """
CREATE OR REPLACE VIEW Pop_Reg AS
SELECT r.num_reg AS num_region, r.nom_reg AS region, p.id_stat, s.libelle AS libelle_indicateur, SUM(p.valeur) AS population
FROM Region r
JOIN Departement d ON r.num_reg = d.num_reg
JOIN Commune c ON d.num_dep = c.num_dep
JOIN Pop_Commune p ON c.num_com = p.num_com
JOIN Stats_Var s ON p.id_stat = s.id_stat
WHERE p.id_stat = 'D99_POP' OR p.id_stat = 'D90_POP' OR p.id_stat = 'D82_POP' OR p.id_stat = 'D75_POP' OR p.id_stat = 'D68_POP'
GROUP BY num_region, p.id_stat, libelle_indicateur
ORDER BY region;
"""

cursor.execute(view2)
query2 = """SELECT * FROM Pop_Reg"""
cursor.execute(query2)
pop_reg = cursor.fetchall()
df_pop_reg = pd.DataFrame(pop_reg, columns=['num_reg', 'region', 'id_stat','libelle_indicateur', 'population'])
"""print(df_pop_reg.head())"""


conn.commit()

