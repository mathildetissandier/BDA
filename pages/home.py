import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', location="sidebar", external_stylesheets=[
                   dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

card_style = {
    'padding': '20px',
    'border': '2px solid #D3D3D3',
    'border-radius': '10px',
    'margin': '20px',
    'background-color': '#F8F9FA',
}


layout = html.Div(style={'color': 'black', 'min-height': '100vh'}, children=[
    html.Div([
        html.H1('Home', style={'textAlign': 'center',
                'color': '#670907', 'font-size': '2.5em'}),
    ], style=card_style),
    html.Br(),
    html.H2("Sujet : conception bases de données, implémentation BD, interrogation depuis un programme",
            style={'textAlign': 'center', 'fontSize': '3.0em'}),
    html.Br(),
    html.Div(style={'color': 'black'}, children=[
        html.P("Nous allons construire et manipuler une base de données relationnelles avec beaucoup de données. Il s'agira dans "
               "un premier temps de modéliser la base de données à partir de données réelles prises sur le web. Puis nous essaierons"
                " différentes méthodes pour importer les données, les manipuler, interroger la base, la mettre à jour, manipuler les"
                 " index, les transactions, les vues, les triggers, les procédure stockées, etc.", style={'fontSize': '1.25em'}),
        html.P("Nous allons utiliser des données disponibles sur le site de l'INSEE.", style={'fontSize': '1.25em'}),
        html.P("Dans un premier temps, il faut modéliser et construire la base de données des régions, départements et villes "
               "françaises disponible ici. La base de données devra être en 3FN et gérer les régions, départements et villes "
               "françaises. Il s'agira d'utiliser au maximum les données des fichiers. Les régions et département ont chacun une "
               "commune chef-lieu. Les villes sont dans des départements qui sont eux-mêmes dans des régions. Vous devez faire un "
               "programme écrit en C, Python, Java ou autre qui lit les fichiers csv et importe les données dans la relation en "
               "utilisant PostgreSQL. Pour importer simplement et rapidement un volume de données important, PostgreSQL a une "
               "commande 'COPY' dédié pour cela (pour Python cf.https://www.psycopg.org/docs/usage.html#using-copy-to-and-copy-from). "
               "Evidemment, vous pouvez utiliser la librairie Python pandas.", style={'fontSize': '1.25em'}),
        html.P("Dans un deuxième temps, il faudra importer la population de chaque commune depuis les séries historiques 2020 et "
               "les statistiques régionales et départementales sur les mariages en 2021. Dans un premier temps, vous n'importerez "
               "qu'une partie des données. Il faut prendre en compte le fait que cette base sera enrichie dans le futur.", style={'fontSize': '1.25em'}),
        html.P("Indications:", style={'fontSize': '1.45em'}),
        html.P("- Pour les communes, on peut se limiter aux communes de type COM", style={
               'fontSize': '1.25em'}),
        html.P("- Nous n'utilisons pas le code d'arrondissement et de cantons pour les communes", style={
               'fontSize': '1.25em'}),
        html.P("-  Dans les communes, il ne faut pas utiliser le code de la région. Une commune est dans un département et le "
               "département est dans une région. Vous devrez donc faire la double jointure pour savoir dans quel département se "
               "trouve une commune.", style={
               'fontSize': '1.25em'}),
    ])
])