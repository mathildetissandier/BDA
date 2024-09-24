import dash
from dash import html, Input, Output, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from affichage import query5, query6, query7, query8, results_1, query9, query10, update_pop_com4

question = "4. Triggers : Faire en sorte que les tables REGIONS et DEPARTEMENTS ne soit pas modifiables. Ajoutez un trigger qui utilise la procédure stockée précédente pour mettre à jour la population d'un département/région quand la population d'une ville est mise à jour."

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
        html.Div(id='query-results4')
    ])


def display_query_results():
    children = []
    children.append(html.Div([
        html.H1('4. Triggers', style={'textAlign': 'center',
                'color': '#F8F9FA', 'font-size': '2.5em'})
    ], style=card_style))
    children.append(html.Div([
        html.H3("Faire en sorte que les tables REGIONS et DEPARTEMENTS ne soient pas modifiables. Il faut bloquer les commandes INSERT, UPDATE et DELETE :"),
        html.Pre(query5),
        html.Pre(query6),
        html.H3("Ajoutez un trigger qui utilise la procédure stockée précédente pour mettre à jour la population d'un département/région quand la population d'une ville est mise à jour :"),
        html.Pre(query7),
        html.H3("Test du trigger :"),
        html.H4("Valeur de la population pour la région Auvergne-Rhône-Alpes en 1999 :"),
        html.Pre(query8),
        html.Ul([
            html.Li(f"{row[0]} - {row[1]} - {row[2]}") for row in results_1
        ]),
        html.H4("Mise à jour de la population d'une commune qui va déclancher le trigger :"),
        html.Pre(query9),
        html.H4("Valeur de la population pour la région Auvergne-Rhône-Alpes en 1999 après la mise à jour :"),
        html.Pre(query10),
        html.Ul([
            html.Li(f"{row[0]} - {row[1]} - {row[2]}") for row in update_pop_com4(query9, query10)
        ]),
        html.P("Nous pouvons voir que la valeur de de population pour la région Auvergne-Rhône-Alpes en 1999 s'est mise à jour.")
    ]))

    return children


@callback(
    Output('query-results4', 'children'),
    [Input('query-results4', 'id')]
)
def update_query_results(trigger):
    return display_query_results()
