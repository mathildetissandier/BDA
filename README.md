# BASE DE DONNÉES PROJET FINAL

## Installation : 

Pour obtenir toutes les extensions utilisées dans ce projet, veuillez exécuter cette commande : 

```bash 
pip install -r requirements.txt
```

## Pour créer la base de données, veuillez suivre les étapes suivantes

    - si la database n'est pas créée :

        * datas/connect.py : Connexion à la base de données "database = postgres" + Création de la base de données "bda1"

    - si la database est déjà créée :

        * datas/connect.py : Connexion à la base de données "database = bda1"

### Pour drop les tables de la base de données :

Lancer le fichier drop.py.

intermède 1 (terminal SQL shell) :

    - utiliser notre base de données : \c bda1

    - visionner les tables créées : \dt

    - voir le contenu d'une table : select * from region;

### Pour lancer l'application :

Lancer le fichier main.py.\
Ce fichier exéctutera les fichiers suivants dans l'ordre pour le bon fonctionnement de l'application :\
    - datas/database.py : ce fichier va créer les tables.\
    - datas/import_data.py : dans ce fichier nous importons les données.\
    - vues.py : il s'agit de la question qui crée les vues de la question 2.\
    - procedure.py : il s'agit de la question qui crée la procédure stockée de la question 3.\
    - triggers.py : il s'agit de la question qui crée un trigger à partir de la procédure stockée de la question 3.\
    - question5.py : ici nous importons 3 nouvelles années de données et nous faisons les mises à jours nécessaires.\
    - app.py : ce fichier permet de lancer notre application dash pour visualiser les requêtes et les résultats.\

Pour relancer l'application une deuxième fois, exécuter le fichier drop.py avant.

## Contributeurs  : 

| [<img src="https://avatars.githubusercontent.com/u/102798630?v=4" width="50" height="50" alt=""/>](https://github.com/suhailaabarkan) | [<img src="https://avatars.githubusercontent.com/u/102798610?v=4" width="50" height="50" alt=""/>](https://github.com/douniamouchrif) | [<img src="https://avatars.githubusercontent.com/u/102798509?v=4" width="50" height="50" alt=""/>](https://github.com/mathildetissandier) |
| :-----------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------: |
|                                        [Suhaila Abarkan](https://github.com/suhailaabarkan)                                        |                                    [Dounia Mouchrif](https://github.com/douniamouchrif)                                    |                               [Mathilde Tissandier](https://github.com/mathildetissandier)                               |
