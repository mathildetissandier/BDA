from datas.connect import conn

cursor = conn.cursor()
 
#Faire en sorte que les tables REGIONS et DEPARTEMENTS ne soit pas modifiables.
#Il faut bloquer les commandes INSERT, UPDATE et DELETE.
query5 = f"""
REVOKE INSERT, UPDATE, DELETE ON Region FROM PUBLIC;
"""
query6 = """
REVOKE INSERT, UPDATE, DELETE ON Departement FROM PUBLIC;
"""
cursor.execute(query5)
cursor.execute(query6)

#Ajoutez un trigger qui utilise la procédure stockée précédente pour mettre à jour 
#la population d'un département/région quand la population d'une ville est mise à jour.

query7 = """
CREATE OR REPLACE FUNCTION maj_pop()
RETURNS TRIGGER AS $$
BEGIN
    CALL calcul_pop_dep_reg2();
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_maj_pop
AFTER INSERT OR UPDATE OR DELETE ON Pop_Commune
FOR EACH STATEMENT EXECUTE FUNCTION maj_pop();
"""
cursor.execute(query7) 

conn.commit()