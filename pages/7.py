import dash
from dash import html, Input, Output, callback
from dash.dependencies import Input, Output
from plan_exe_index import query1, index_details, query2, results_2, query3, query4, results_4
import dash_bootstrap_components as dbc

question = "7. Plan d\'exécution et index : Montrer l'intérêt des index sur plusieurs exemples. Vérifiez-le. Analyser aussi une requête qui liste les communes avec moins de 5000 habitants. Créer un index sur l'attribut population et refaites la manipulation. Vérifier que le SGBD fait les sélections individuelles avant de calculer les jointures."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


card_style = {
    'padding': '20px',
    'border': '2px solid #D3D3D3',
    'border-radius': '10px',
    'margin': '20px',
    'background-color': '#670907',
}

formatted_results_2 = [', '.join(map(str, row)) for row in results_2]
formatted_results_4 = [', '.join(map(str, row)) for row in results_4]
analyse_1 = "Nous remarquons, en effet, que la clé primaire de la table Region, soit 'num_reg', est l'index de cette table."
analyse_2 = "On remarque un cout très élevé sans index supplémentaire (cost=12758.80..16126.51), mais aussi un temps d'exécution élevé (Execution Time: 93.952 ms)."
analyse_4 = "On remarque un cout similaire avec l'index supplémentaire au cout sans l'index supplémentaire, mais le temps d'exécution a bien diminué (27.733 ms vs 93.952 ms). "
avertissement = "ATTENTION : Les temps affichés dans nos analyses sont différents de ceux retournés par les plans d'éxécution (tout en restant similaires/comparables). Nous nous sommes basées sur les résultats obtenus lors de la première exécution du code. Malgré des résultats différents, les analyses restent les mêmes et aboutissent aux mêmes conclusions."


def layout():
    return html.Div([
        # Div pour afficher les résultats des requêtes
        html.Div(id='query-results7')
    ])


def display_query_results():
    children = []
    children.append(html.Div([
        html.H1('7. Plan d\'exécution et index', style={'textAlign': 'center',
                'color': '#F8F9FA', 'font-size': '2.5em'})
    ], style=card_style))
    children.append(html.Div([
        html.Div([
            html.P(html.Span(avertissement, style={
                   "white-space": "pre-line"})),
        ], style={
            'border': '2px solid #ccc',
            'padding': '10px',
            'background-color': '#f4f4f4',
            'border-radius': '5px',
        }),
        html.Br(),
        html.H2(
            "Requête pour vérifier qu'une clé primaire est un index, sur la table région : "),
        html.Pre(query1),
        html.H4("Détails puis analyses de l'index de la table 'Region' :"),
        html.Pre("\n".join(
            [f"Nom de l'index : {row[0]}\nDéfinition de l'index: {row[1]}\n-------------------------------------" for row in index_details])),
        html.Pre(analyse_1),
        html.Br(),
        html.H2("Plan d'exécution de la requête qui liste les communes avec moins de 5000 habitants en 2020 sans index supplémentaire : "),
        html.Pre(query2),
        html.Div(id='query-results7',
                 children=[html.Pre(result) for result in formatted_results_2]),
        html.H4("Analyse de ce plan d'exécution sans index supplémentaire :"),
        html.P(html.Span(analyse_2, style={"white-space": "pre-line"})),
        html.Br(),
        html.H2("Création de l'index sur l'attribut valeur de la table Pop_Commune : "),
        html.Pre(query3),
        html.Br(),
        html.H2(
            "Requête qui liste les communes avec moins de 5000 habitants en utilisant l'index : "),
        html.Pre(query4),
        html.H4("Analyse de ce plan d'exécution avec index supplémentaire :"),
        html.P(html.Span(analyse_4, style={"white-space": "pre-line"})),
        html.P("Pour conclure, la création de l'index a effectivement amélioré l\'optimisation de la requête.")
    ]))
    return children


@callback(
    Output('query-results7', 'children'),
    [Input('query-results7', 'id')]
)
def update_query_results(trigger):
    return display_query_results()
