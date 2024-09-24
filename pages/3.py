import dash
from dash import html, Input, Output, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from affichage import query1, pop_dep, pop_reg, query2

question = "3. Procédure stockée : Écrivez une procédure stockée qui fait ce calcul à partir de la population des communes. N'oubliez pas de modifier au préalable la structure de la base pour accueillir ces nouvelles informations."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

card_style = {
    'padding': '20px',
    'border': '2px solid #D3D3D3',
    'border-radius': '10px',
    'margin': '20px',
    'background-color': '#670907',
}


def layout():
    return html.Div([
        # Div pour afficher les résultats des requêtes
        html.Div(id='query-results3')
    ])


def display_query_results():
    children = []
    children.append(html.Div([
        html.H1('3. Procédure stockée', style={'textAlign': 'center',
                'color': '#F8F9FA', 'font-size': '2.5em'})
    ], style=card_style))
    children.append(html.Div([
        html.H3("Modification des tables Departement et Region"),
        html.Pre(pop_dep),
        html.Pre(pop_reg),
        html.H3("Avec l'utilisation des vues créées :"),
        html.Pre(query1),
        html.H3("Sans l'utilisation des vues créées :"),
        html.Pre(query2)
    ]))

    return children


@callback(
    Output('query-results3', 'children'),
    [Input('query-results3', 'id')]
)
def update_query_results(trigger):
    return display_query_results()
