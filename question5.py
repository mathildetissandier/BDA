import psycopg2
from datas.connect import conn
import pandas as pd
from io import StringIO
 
cursor = conn.cursor()
#Procédure stockée pour calculer la population des départements des 3 nouvelles années 
query1 = """CREATE OR REPLACE PROCEDURE calcul_pop_departements_new_years()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Departement d
    SET pop2020 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P20_POP'),
        pop2014 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P14_POP'),
        pop2009 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P09_POP');
END;
$$;"""
cursor.execute(query1)

#Procédure stockée pour calculer la population des régions des 3 nouvelles années 
query2 = """CREATE OR REPLACE PROCEDURE calcul_pop_regions_new_years()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Region r
    SET pop2020 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P20_POP'),
        pop2014 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P14_POP'),
        pop2009 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P09_POP');
END;
$$;
"""
cursor.execute(query2)

### procedure pour update les populations reg et dep maintenant qu'il y a toutes les années si il ya des modifications dans Pop_communes 
query4 = """CREATE OR REPLACE PROCEDURE calcul_pop_dep_reg_new_years()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Departement d
    SET pop2020 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P20_POP'),
        pop2014 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P14_POP'),
        pop2009 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'P09_POP'),
        pop1999 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D99_POP'),
        pop1990 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D90_POP'),
        pop1982 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D82_POP'),
        pop1975 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D75_POP'),
        pop1968 = (SELECT SUM(p.valeur) FROM Commune c JOIN Pop_Commune p ON c.num_com = p.num_com WHERE c.num_dep = d.num_dep AND p.id_stat = 'D68_POP');

    UPDATE Region r
    SET pop2020 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P20_POP'),
        pop2014 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P14_POP'),
        pop2009 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'P09_POP'),
        pop1999 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D99_POP'),
        pop1990 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D90_POP'),
        pop1982 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D82_POP'),
        pop1975 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D75_POP'),
        pop1968 = (SELECT SUM(p.valeur) FROM Departement d JOIN Commune c ON d.num_dep = c.num_dep JOIN Pop_Commune p ON c.num_com = p.num_com WHERE d.num_reg = r.num_reg AND p.id_stat = 'D68_POP');

END;
$$;"""
cursor.execute(query4)

#trigger qui déclanche la procédure
query5 = """
CREATE OR REPLACE FUNCTION maj_pop_ny()
RETURNS TRIGGER AS $$
BEGIN
    CALL calcul_pop_dep_reg_new_years();
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_maj_pop_ny
AFTER INSERT OR UPDATE OR DELETE ON Pop_Commune
FOR EACH STATEMENT EXECUTE PROCEDURE maj_pop_ny();
"""
cursor.execute(query5)
conn.commit()

#####IMPORTATION DES 3 ANNÉES SUPPLÉMENTAIRES 
pop_reg = """ALTER TABLE Region 
ADD COLUMN pop2020 BIGINT,
ADD COLUMN pop2014 BIGINT,
ADD COLUMN pop2009 BIGINT;"""

pop_dep = """ALTER TABLE Departement 
ADD COLUMN pop2020 BIGINT,
ADD COLUMN pop2014 BIGINT,
ADD COLUMN pop2009 BIGINT;"""

cursor.execute(pop_dep)
cursor.execute(pop_reg)

###insertion des années dans la table Stats_var
cursor.execute("""INSERT INTO Stats_var (id_stat, annee_debut, annee_fin, libelle) 
VALUES ('P20_POP', 2020, 2020, 'Population en 2020'),
    ('P14_POP', 2014, 2014, 'Population en 2014'),
    ('P09_POP', 2009, 2009, 'Population en 2009');""")

###insertion des données dans la table Pop_commune
column_names = ['CODGEO', 'P20_POP', 'P14_POP', 'P09_POP']
dtype_dict = {'CODGEO': str, 'P20_POP': 'Int64', 'P14_POP': 'Int64', 'P09_POP': 'Int64'}

df_pop = pd.read_csv('datas/files/base-cc-serie-historique-2020.csv', delimiter=";", dtype=dtype_dict)
df_pop_dom = pd.read_csv('datas/files/base-cc-serie-historique-2020-COM.csv', delimiter=";", dtype=dtype_dict)
df_combined = pd.concat([df_pop_dom, df_pop])
df_combined.reset_index(drop=True, inplace=True)

df_com = pd.read_csv('datas/files/v_commune_2023.csv')
df_commune_com = df_com[df_com['TYPECOM'] == 'COM'][['COM']] #pour avoir que les types COM
merged_df = pd.merge(df_combined, df_commune_com, left_on='CODGEO', right_on='COM', how='inner')

for column_name in column_names[1:]:
    df_temp = merged_df
    df_temp['id_stat'] = column_name
    df_temp = merged_df[['CODGEO', 'id_stat',column_name]]
    df_temp.columns = ['num_com', 'id_stat', 'valeur']
    buffer_com = StringIO()
    df_temp.to_csv(buffer_com, sep='\t', header=False, index=False)
    buffer_com.seek(0)
    copy_query = """
        COPY Pop_Commune(num_com, id_stat, valeur)
        FROM STDIN DELIMITER '\t' CSV;
    """
    cursor.copy_expert(sql=copy_query, file=buffer_com)

#appel des procedures stockées
cursor.execute("""CALL calcul_pop_departements_new_years()""")
cursor.execute("""CALL calcul_pop_regions_new_years()""")

conn.commit()
