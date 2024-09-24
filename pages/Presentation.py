import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, location="sidebar", use_pages=True, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

card_style = {
    'padding': '20px',
    'border': '2px solid #D3D3D3',
    'border-radius': '10px',
    'margin': '20px',
    'background-color': '#F8F9FA',
}

modele_relationnel = """
- **Region**(**num_reg**, nom_reg, chef_lieu)\n
 ⮑ _Region.chef_lieu référence Commune.num_com_\n
\n
- **Departement**(**num_dep**, nom_dep, chef_lieu, num_reg)\n
 ⮑ _Departement.chef_lieu référence Commune.num_com_\n
 ⮑ _Departement.num_reg référence Region.num_reg_\n
\n
- **Commune**(**num_com**, nom_com, num_dep)\n
 ⮑ _Commune.num_dep référence Departement.num_dep_\n
\n
- **Stats_Var**(**id_stat**, annee_debut, annee_fin, libelle)\n
\n
- **Pop_Commune**(**num_com, id_stat**, valeur)\n
 ⮑ _Pop_Commune.num_com référence Commune.num_com_\n
 ⮑ _Pop_Commune.id_stat référence Stats_Var.id_stat_\n
\n
- **Stats_Mar1**(**type_couple, dep, ages, id_stat**, nb_mar)\n
 ⮑ _Stats_Mar1.id_stat référence Stats_Var.id_stat_\n
\n
- **Stats_Mar2**(**type_couple, dep_domi, lieu, id_stat**, nb_mar)\n
 ⮑ _Stats_Mar2.id_stat référence Stats_Var.id_stat_\n
\n
- **Stats_Mar3**(**type_couple, dep, sexe, etat_mar**, id_stat, nb_mar)\n
 ⮑ _Stats_Mar3.id_stat référence Stats_Var.id_stat_\n
\n
- **Stats_Mar4**(**type_couple, dep, mois**, id_stat, nb_mar)\n
 ⮑ _Stats_Mar4.id_stat référence Stats_Var.id_stat_\n
"""

layout = html.Div(style={'color': 'black', 'min-height': '100vh'}, children=[
    html.Div([
        html.H1('Présentation de la base de données', style={'textAlign': 'center',
                'color': '#670907', 'font-size': '2.5em'}),
    ], style=card_style),
    html.Br(),
    html.H2("Modèle relationnel",
            style={'textAlign': 'center', 'fontSize': '3.0em'}),
    html.Br(),
    html.Div(style={'color': 'black'}, children=[
        html.P("Pour la création de la base de données nous nous sommes basées sur le modèle relationnel suivant :", style={
               'fontSize': '1.25em'}),
        dcc.Markdown(children=modele_relationnel, style={'fontSize': '0.9em'}),
        html.P("Les attributs en gras de chaque table sont les clés primaires.", style={
               'fontSize': '1.em'}),
        html.P("Nous avons donc un total de 9 tables pour stocker les données de nos 11 fichiers.", style={
               'fontSize': '1.25em'}),
        html.P("Au départ, nous avons importé les données dans les tables Region et Departement sans la référence des chef_lieu vers les communes. "
               "Une fois que la table Commune est complète, nous ajoutons la référence.", style={'fontSize': '1.25em'}),
    ])
])
