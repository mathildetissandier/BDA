from connect import conn

# Connextion à la base de données
conn.autocommit = True
cursor = conn.cursor()

# Création des tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Region (
    num_reg INTEGER PRIMARY KEY,
    nom_reg TEXT NOT NULL,
    chef_lieu TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Departement (
    num_dep TEXT PRIMARY KEY,
    nom_dep TEXT NOT NULL,
    chef_lieu TEXT,
    num_reg INTEGER REFERENCES Region(num_reg)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Commune (
    num_com TEXT PRIMARY KEY,
    nom_com TEXT NOT NULL,
    num_dep TEXT REFERENCES Departement(num_dep)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Stats_Var (
    id_stat TEXT PRIMARY KEY,
    annee_debut INTEGER NOT NULL CHECK (annee_debut >= 1968 AND annee_debut <= 2021),
    annee_fin INTEGER NOT NULL CHECK (annee_fin >= 1968 AND annee_fin <= 2021 AND annee_fin >= annee_debut),
    libelle TEXT NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pop_Commune (
    num_com TEXT REFERENCES Commune(num_com),
    id_stat TEXT REFERENCES Stats_Var(id_stat),
    valeur BIGINT,
    PRIMARY KEY(num_com, id_stat)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Stats_Mar1 (
    type_couple TEXT NOT NULL,
    dep TEXT NOT NULL,
    ages TEXT NOT NULL,
    nb_mar INTEGER NOT NULL,
    id_stat TEXT REFERENCES Stats_Var(id_stat),
    PRIMARY KEY(type_couple, dep, ages, id_stat)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Stats_Mar2 (
    type_couple TEXT NOT NULL,
    dep_domi TEXT NOT NULL,
    lieu TEXT NOT NULL,
    nb_mar INTEGER NOT NULL,
    id_stat TEXT REFERENCES Stats_Var(id_stat),
    PRIMARY KEY(type_couple, dep_domi, lieu, id_stat)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Stats_Mar3 (
    type_couple TEXT NOT NULL,
    dep TEXT NOT NULL,
    sexe TEXT NOT NULL,
    etat_mar TEXT NOT NULL,
    nb_mar INTEGER NOT NULL,
    id_stat TEXT REFERENCES Stats_Var(id_stat),
    PRIMARY KEY(type_couple, dep, sexe, etat_mar)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Stats_Mar4 (
    type_couple TEXT NOT NULL,
    dep TEXT NOT NULL,
    mois TEXT NOT NULL,
    nb_mar INTEGER NOT NULL,
    id_stat TEXT REFERENCES Stats_Var(id_stat),
    PRIMARY KEY(type_couple, dep, mois)
    );
""")

conn.commit()
cursor.close()
conn.close()
