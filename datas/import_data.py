from connect import conn
import pandas as pd
from io import StringIO

# Connextion à la base de données
cursor = conn.cursor()

# Données Region
df_reg = pd.read_csv('datas/files/v_region_2023.csv')
df_region = df_reg[['REG', 'LIBELLE', 'CHEFLIEU']]
df_region.columns = ['num_reg', 'nom_reg',
                     'chef_lieu']  # renommage des colonnes

buffer_reg = StringIO()  # création d'un buffer mémoire
df_region.to_csv(buffer_reg, sep='\t', header=False, index=False)
buffer_reg.seek(0)

copy_query = """
    COPY Region(num_reg, nom_reg, chef_lieu)
    FROM STDIN DELIMITER '\t' CSV;
"""
cursor.copy_expert(
    sql=copy_query, file=buffer_reg)  # copie des données depuis le buffer vers la bdd

# Données Departement
df_dep = pd.read_csv('datas/files/v_departement_2023.csv')
df_departement = df_dep[['DEP', 'LIBELLE', 'CHEFLIEU', 'REG']]
df_departement.columns = ['num_dep', 'nom_dep',
                          'chef_lieu', 'num_reg']

buffer_dep = StringIO()
df_departement.to_csv(buffer_dep, sep='\t', header=False, index=False)
buffer_dep.seek(0)

copy_query = """
    COPY Departement(num_dep, nom_dep, chef_lieu, num_reg)
    FROM STDIN DELIMITER '\t' CSV;
"""
cursor.copy_expert(
    sql=copy_query, file=buffer_dep)

# Données Commune
df_com = pd.read_csv('datas/files/v_commune_2023.csv')
# on filtre les lignes où 'TYPECOM' est égal à 'COM'
df_commune = df_com[df_com['TYPECOM'] == 'COM'][['COM', 'LIBELLE', 'DEP']]
df_commune.columns = ['num_com', 'nom_com', 'num_dep']

buffer_com = StringIO()
df_commune.to_csv(buffer_com, sep='\t', header=False, index=False)
buffer_com.seek(0)

copy_query = """
    COPY Commune(num_com, nom_com, num_dep)
    FROM STDIN DELIMITER '\t' CSV;
"""
cursor.copy_expert(sql=copy_query, file=buffer_com)

# Ajout de la référence à la colonne chef_lieu dans la table Region et Departement
cursor.execute("""
    ALTER TABLE Region
    ADD FOREIGN KEY (chef_lieu)
    REFERENCES Commune(num_com);
""")

cursor.execute("""
    ALTER TABLE Departement
    ADD FOREIGN KEY (chef_lieu)
    REFERENCES Commune(num_com);
""")

# Données Stats_var
data_to_insert = [
    ('D99_POP', 1999, 1999, 'Population en 1999'),
    ('D90_POP', 1990, 1990, 'Population sans les doubles comptes en 1990'),
    ('D82_POP', 1982, 1982, 'Population sans les doubles comptes en 1982'),
    ('D75_POP', 1975, 1975,
     'Population sans les doubles comptes en 1975 (en 1974 pour les DOM)'),
    ('D68_POP', 1968, 1968,
     'Population sans les doubles comptes en 1968 (en 1967 pour les DOM)'),
    ('NAIS1420', 2014, 2020, 'Nombre de naissances entre 2014 et 2020'),
    ('NAIS0914', 2009, 2014, 'Nombre de naissances entre 2009 et 2014'),
    ('NAIS9909', 1999, 2009, 'Nombre de naissances entre 1999 et 2009'),
    ('NAIS9099', 1990, 1999, 'Nombre de naissances entre 1990 et 1999'),
    ('NAIS8290', 1982, 1990, 'Nombre de naissances entre 1982 et 1990'),
    ('NAIS7582', 1975, 1982,
     'Nombre de naissances entre 1975 (en 1974 pour les DOM) et 1982'),
    ('NAIS6875', 1968, 1975,
     'Nombre de naissances entre 1968 et 1975 (en 1967 et 1974 pour les DOM)'),
    ('DECE1420', 2014, 2020, 'Nombre de décès entre 2014 et 2020'),
    ('DECE0914', 2009, 2014, 'Nombre de décès entre 2009 et 2014'),
    ('DECE9909', 1999, 2009, 'Nombre de décès entre 1999 et 2009'),
    ('DECE9099', 1990, 1999, 'Nombre de décès entre 1990 et 1999'),
    ('DECE8290', 1982, 1990, 'Nombre de décès entre 1982 et 1990'),
    ('DECE7582', 1975, 1982, 'Nombre de décès entre 1975 (en 1974 pour les DOM) et 1982'),
    ('DECE6875', 1968, 1975,
     'Nombre de décès entre 1968 et 1975 (en 1967 et 1974 pour les DOM)'),
    ('MAR21AGE_1', 2021, 2021,
     'Groupe d\'âges des époux selon le département et la région de mariage. Année 2021'),
    ('MAR21AGE_2', 2021, 2021,
     'Groupe d\'âges des époux se mariant pour la première fois selon le département et la région de mariage. Année 2021'),
    ('MAR21NAT', 2021, 2021,
     'Nationalité des époux selon le département et la région de domicile conjugal. Année 2021'),
    ('MAR21PAYS', 2021, 2021,
     'Pays de naissance des époux selon le département et la région de domicile conjugal. Année 2021'),
    ('MAR21EM', 2021, 2021,
     'État matrimonial antérieur des époux selon le département et la région de mariage. Année 2021'),
    ('MAR21MOIS', 2021, 2021,
     'Répartition mensuelle des mariages selon le département et la région de mariage. Année 2021')
]

for row in data_to_insert:
    id_stat, annee_debut, annee_fin, libelle = row
    cursor.execute("""
        INSERT INTO Stats_Var (id_stat, annee_debut, annee_fin, libelle)
        VALUES (%s, %s, %s, %s);
    """, (id_stat, annee_debut, annee_fin, libelle))

# Données Pop_Commune
column_names = ['CODGEO', 'D99_POP', 'D90_POP', 'D82_POP', 'D75_POP', 'D68_POP', 
                'NAIS1420', 'NAIS0914', 'NAIS9909', 'NAIS9099', 'NAIS8290', 'NAIS7582','NAIS6875', 
                'DECE1420', 'DECE0914', 'DECE9909','DECE9099', 'DECE8290', 'DECE7582', 'DECE6875']

#pour avoir les bons types des données
dtype_dict = {'CODGEO': str, 'D99_POP': 'Int64', 'D90_POP': 'Int64', 
              'D82_POP': 'Int64', 'D75_POP': 'Int64', 'D68_POP': 'Int64', 'NAIS1420': 'Int64', 'NAIS0914': 'Int64', 'NAIS9909': 'Int64', 
              'NAIS9099': 'Int64', 'NAIS8290': 'Int64', 'NAIS7582': 'Int64', 'NAIS6875': 'Int64', 'DECE1420': 'Int64', 'DECE0914': 'Int64', 
              'DECE9909': 'Int64', 'DECE9099': 'Int64', 'DECE8290': 'Int64', 'DECE7582': 'Int64', 'DECE6875': 'Int64'}
df_pop = pd.read_csv('datas/files/base-cc-serie-historique-2020.csv', delimiter=";", dtype=dtype_dict)
df_pop_dom = pd.read_csv('datas/files/base-cc-serie-historique-2020-COM.csv', delimiter=";", dtype=dtype_dict)
df_combined = pd.concat([df_pop_dom, df_pop])
df_combined.reset_index(drop=True, inplace=True)

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

# Données Stats_Mar1
files = ['datas/files/Dep1.csv', 'datas/files/Dep3.csv']

for i, file in enumerate(files):
    df_mar1 = pd.read_csv(file, sep=';')
    df_mariages1 = df_mar1[['TYPMAR3', 'REGDEP_MAR', 'GRAGE', 'NBMARIES']]
    df_mariages1.columns = ['type_couple', 'dep', 'ages', 'nb_mar']

    id_stat_value = f'MAR21AGE_{i + 1}'
    df_mariages1['id_stat'] = id_stat_value

    buffer_mar1 = StringIO()
    df_mariages1.to_csv(buffer_mar1, sep='\t', header=False, index=False)
    buffer_mar1.seek(0)
    copy_query = """
        COPY Stats_Mar1(type_couple, dep, ages, nb_mar, id_stat)
        FROM STDIN DELIMITER '\t' CSV;
    """
    cursor.copy_expert(sql=copy_query, file=buffer_mar1)

# Données Stats_Mar2
df_mar2_v1 = pd.read_csv('datas/files/Dep4.csv', sep=';')
df_mariages2_v1 = df_mar2_v1[['TYPMAR2', 'REGDEP_DOMI', 'NATEPOUX', 'NBMAR']]
df_mariages2_v1.columns = ['type_couple', 'dep_domi', 'lieu', 'nb_mar']
df_mariages2_v1['id_stat'] = 'MAR21NAT'

df_mar2_v2 = pd.read_csv('datas/files/Dep5.csv', sep=';')
df_mariages2_v2 = df_mar2_v2[['TYPMAR2', 'REGDEP_DOMI', 'LNEPOUX', 'NBMAR']]
df_mariages2_v2.columns = ['type_couple', 'dep_domi', 'lieu', 'nb_mar']
df_mariages2_v2['id_stat'] = 'MAR21PAYS'

df_mariages2 = pd.concat([df_mariages2_v1, df_mariages2_v2], ignore_index=True)

buffer_mar2 = StringIO()
df_mariages2.to_csv(buffer_mar2, sep='\t', header=False, index=False)
buffer_mar2.seek(0)
copy_query = """
    COPY Stats_Mar2(type_couple, dep_domi, lieu, nb_mar, id_stat)
    FROM STDIN DELIMITER '\t' CSV;
"""
cursor.copy_expert(sql=copy_query, file=buffer_mar2)

# Données Stats_Mar3
df_mar3 = pd.read_csv('datas/files/Dep2.csv', sep=';')
df_mariages3 = df_mar3[['TYPMAR', 'REGDEP_MAR', 'SEXE', 'ETAMAT', 'NBMARIES']]
df_mariages3.columns = ['type_couple', 'dep', 'sexe', 'etat_mar', 'nb_mar']
df_mariages3['id_stat'] = 'MAR21EM'
buffer_mar3 = StringIO()
df_mariages3.to_csv(buffer_mar3, sep='\t', header=False, index=False)
buffer_mar3.seek(0)
copy_query = """
    COPY Stats_Mar3(type_couple, dep, sexe, etat_mar, nb_mar, id_stat)
    FROM STDIN DELIMITER '\t' CSV;
"""
cursor.copy_expert(sql=copy_query, file=buffer_mar3)

# Données Stats_Mar4
df_mar4 = pd.read_csv('datas/files/Dep6.csv', sep=';')
df_mariages4 = df_mar4[['TYPMAR2', 'REGDEP_MAR', 'MMAR', 'NBMAR']]
df_mariages4.columns = ['type_couple', 'dep', 'mois', 'nb_mar']
df_mariages4['id_stat'] = 'MAR21MOIS'
buffer_mar4 = StringIO()
df_mariages4.to_csv(buffer_mar4, sep='\t', header=False, index=False)
buffer_mar4.seek(0)
copy_query = """
    COPY Stats_Mar4(type_couple, dep, mois, nb_mar, id_stat)
    FROM STDIN DELIMITER '\t' CSV;
"""
cursor.copy_expert(sql=copy_query, file=buffer_mar4)

cursor.close()
conn.commit()
conn.close()
