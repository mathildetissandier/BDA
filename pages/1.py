import dash
from dash import html, Input, Output, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from requests import query_1, query_2, query_3, query_4, query_5, query_6, query_7
from requests import results_1, results_2, result_3, result_4, results_5, results_6, results_7

question = "1. Requêtes : Dans un programme réalisé dans le langage de votre choix (de préférence C, C++, Java ou Python), réalisez au moins trois requêtes."

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
        html.Div(id='query-results')
    ])


def display_query_results():
    children = []
    children.append(html.Div([
        html.H1('1. Requêtes', style={'textAlign': 'center',
                'color': '#F8F9FA', 'font-size': '2.5em'})
    ], style=card_style))
    children.append(html.Div([
        html.H3(
            "Requête 1 : Liste des départements de la Nouvelle-Aquitaine"),
        html.Pre(query_1),
        html.Table(style={'border': '1px solid black'}, children=[
            html.Thead(html.Tr([
                html.Th("Numéro du département", style={
                        'border': '1px solid black'}),
                html.Th("Nom du département", style={
                        'border': '1px solid black'}),
                html.Th("Chef lieu", style={
                        'border': '1px solid black'})
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(row[0], style={'border': '1px solid black'}),
                    html.Td(row[1], style={'border': '1px solid black'}),
                    html.Td(row[2], style={'border': '1px solid black'})
                ])
                for row in results_1
            ])
        ]),
        html.Br(),
        html.H3(
            "Requête 2 : Liste des communes de plus de 30 000 habitants du département de la Gironde (33) en 2020"),
        html.Pre(query_2),
        html.Table(style={'border': '1px solid black'}, children=[
            html.Thead(html.Tr([
                html.Th("Numéro de la commune", style={
                        'border': '1px solid black'}),
                html.Th("Nom de la commune", style={
                        'border': '1px solid black'}),
                html.Th("Population", style={
                        'border': '1px solid black'})
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(row[0], style={'border': '1px solid black'}),
                    html.Td(row[1], style={'border': '1px solid black'}),
                    html.Td(row[2], style={'border': '1px solid black'})
                ])
                for row in results_2
            ])
        ]),
        html.Br(),
        html.H3("Requête 3 : La région la plus peuplée ainsi que sa population totale"),
        html.Pre(query_3),
        html.Table(style={'border': '1px solid black'}, children=[
            html.Thead(html.Tr([
                html.Th("Nom de la région", style={
                        'border': '1px solid black'}),
                html.Th("Population totale", style={
                        'border': '1px solid black'})
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(result_3[0], style={'border': '1px solid black'}),
                    html.Td(result_3[1], style={'border': '1px solid black'})
                ])
            ])
        ]),
        html.Br(),
        html.H3(
            "Requête 4 : La région la moins peuplée ainsi que sa population totale"),
        html.Pre(query_4),
        html.Table(style={'border': '1px solid black'}, children=[
            html.Thead(html.Tr([
                html.Th("Nom de la région", style={
                        'border': '1px solid black'}),
                html.Th("Population totale", style={
                        'border': '1px solid black'})
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(result_4[0], style={'border': '1px solid black'}),
                    html.Td(result_4[1], style={'border': '1px solid black'})
                ])
            ])
        ]),
        html.Br(),
        html.H3(
            "Requête 5 : Les 10 communes les plus peuplées du département de la Gironde (33) en 2020"),
        html.Pre(query_5),
        html.Table(style={'border': '1px solid black'}, children=[
            html.Thead(html.Tr([
                html.Th("Nom de la commune", style={
                        'border': '1px solid black'}),
                html.Th("Population", style={
                        'border': '1px solid black'})
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(row[0], style={'border': '1px solid black'}),
                    html.Td(row[1], style={'border': '1px solid black'})
                ])
                for row in results_5
            ])
        ]),
        html.Br(),
        html.H3(
            "Requête 6 : Les 10 communes les moins peuplées du département de la Gironde (33) en 2020"),
        html.Pre(query_6),
        html.Table(style={'border': '1px solid black'}, children=[
            html.Thead(html.Tr([
                html.Th("Nom de la commune", style={
                        'border': '1px solid black'}),
                html.Th("Population", style={
                        'border': '1px solid black'})
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(row[0], style={'border': '1px solid black'}),
                    html.Td(row[1], style={'border': '1px solid black'})
                ])
                for row in results_6
            ])
        ]),
        html.Br(),
        html.H3("Requête 7 : Le nombre total de mariages pour la 1ère fois par type de couple dans le département de Seine-et-Marne (77)"),
        html.Pre(query_7),
        html.Table(style={'border': '1px solid black'}, children=[
            html.Thead(html.Tr([
                html.Th("Type de couple", style={
                        'border': '1px solid black'}),
                html.Th("Total de mariages", style={
                        'border': '1px solid black'})
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(row[0], style={'border': '1px solid black'}),
                    html.Td(row[1], style={'border': '1px solid black'})
                ])
                for row in results_7
            ])
        ]),
        html.Br()
    ]))

    return children


@ callback(
    Output('query-results', 'children'),
    [Input('query-results', 'id')]
)
def update_query_results(trigger):
    return display_query_results()
