from datas.connect import conn

cursor = conn.cursor()

cursor.execute("""drop table stats_mar1 ;
drop table stats_mar2 ;
drop table stats_mar3 ;
drop table stats_mar4 ;
drop table pop_commune CASCADE;
drop table stats_var ;
drop table commune CASCADE;
drop table departement;
drop table region;""")

conn.commit()
