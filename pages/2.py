import dash
from dash import html, Input, Output, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from vues import view1, view2, df_pop_dep, df_pop_reg

question = "2. Vues : Créer deux vues (cf commande CREATE OR REPLACE VIEW) qui donnent la population des départements et des régions pour les différentes années ainsi que les indicateurs existants."

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
        html.Div(id='query-results2')
    ])


def display_query_results():
    children = []
    children.append(html.Div([
        html.H1('2. Vues', style={'textAlign': 'center',
                'color': '#F8F9FA', 'font-size': '2.5em'})
    ], style=card_style))
    children.append(html.Div([
        html.H3("Vue 1 : La population des départements pour les différentes années ainsi que les indicateurs existants."),
        html.Pre(view1),
        html.Table(style={'border': '1px solid black', 'border-collapse': 'collapse'}, children=[
            html.Thead(html.Tr([
                html.Th("Numéro de département", style={
                        'border': '1px solid black', 'padding': '8px'}),
                html.Th("Département", style={
                        'border': '1px solid black', 'padding': '8px'}),
                html.Th("ID de la Statistique", style={
                        'border': '1px solid black', 'padding': '8px'}),
                html.Th("Libellé de la Statistique", style={
                        'border': '1px solid black', 'padding': '8px'}),
                html.Th("Population", style={
                        'border': '1px solid black', 'padding': '8px'})
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(row[1], style={
                            'border': '1px solid black', 'padding': '8px'}),
                    html.Td(str(row[2]), style={
                            'border': '1px solid black', 'padding': '8px'}),
                    html.Td(row[3], style={
                            'border': '1px solid black', 'padding': '8px'}),
                    html.Td(str(row[4]), style={
                            'border': '1px solid black', 'padding': '8px'}),
                    html.Td(str(row[5]), style={
                            'border': '1px solid black', 'padding': '8px'})
                ])
                for row in df_pop_dep.itertuples()
            ])
        ]),
        html.Br(),
        html.H3("Vue 2 : La population des régions pour les différentes années ainsi que les indicateurs existants."),
        html.Pre(view2),
        html.Table(style={'border': '1px solid black', 'border-collapse': 'collapse'}, children=[
            html.Thead(html.Tr([
                html.Th("Numéro de la région", style={
                        'border': '1px solid black', 'padding': '8px'}),
                html.Th("Région", style={
                        'border': '1px solid black', 'padding': '8px'}),
                html.Th("ID de la Statistique", style={
                        'border': '1px solid black', 'padding': '8px'}),
                html.Th("Libellé de la Statistique", style={
                        'border': '1px solid black', 'padding': '8px'}),
                html.Th("Population", style={
                        'border': '1px solid black', 'padding': '8px'})
            ])),
            html.Tbody([
                html.Tr([
                    html.Td(str(row[1]), style={
                            'border': '1px solid black', 'padding': '8px'}),
                    html.Td(str(row[2]), style={
                            'border': '1px solid black', 'padding': '8px'}),
                    html.Td(row[3], style={
                            'border': '1px solid black', 'padding': '8px'}),
                    html.Td(str(row[4]), style={
                            'border': '1px solid black', 'padding': '8px'}),
                    html.Td(str(row[5]), style={
                            'border': '1px solid black', 'padding': '8px'})
                ])
                for row in df_pop_reg.itertuples()
            ])
        ]),

    ]))

    return children


@callback(
    Output('query-results2', 'children'),
    [Input('query-results2', 'id')]
)
def update_query_results(trigger):
    return display_query_results()
