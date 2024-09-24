import dash
from dash import html, Input, Output, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from plan_exe import explain_results_1, exe_query1, exe_query2, explain_results_2, exe_query3, explain_results_3, exe_query4, explain_results_4, exe_query5, explain_results_5, exe_query6, explain_results_6, exe_query7, explain_results_7

question = "6. Plan d\'exécution (EXPLAIN) : Comparer et expliquer le coût d'exécution de différentes requêtes. Faites apparaître les différents algorithmes de jointure ou différentes stratégies de tri en jouant en particulier sur la cardinalité des relations."

dash.register_page(__name__, question=question, external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

card_style = {
    'padding': '20px',
    'border': '2px solid #D3D3D3',
    'border-radius': '10px',
    'margin': '20px',
    'background-color': '#670907',
}

formatted_results_1 = [', '.join(map(str, row)) for row in explain_results_1]
formatted_results_2 = [', '.join(map(str, row)) for row in explain_results_2]
formatted_results_3 = [', '.join(map(str, row)) for row in explain_results_3]
formatted_results_4 = [', '.join(map(str, row)) for row in explain_results_4]
formatted_results_5 = [', '.join(map(str, row)) for row in explain_results_5]
formatted_results_6 = [', '.join(map(str, row)) for row in explain_results_6]
formatted_results_7 = [', '.join(map(str, row)) for row in explain_results_7]

analyse_1 = "Utilisation d'une jointure entre Departement et Region basée sur num_reg. " \
            "Filtre sur nom_reg = 'Nouvelle-Aquitaine'. " \
            "Exécution efficace avec un coût faible (cost=0.16..18.63) et un temps d'exécution rapide (Execution Time: 0.163 ms)."

analyse_2 = "Filtre sur num_dep = '33' et pc.valeur > 30000 dans une jointure entre Commune et Pop_Commune. "\
            "Utilisation d'un tri par ordre décroissant des résultats (ORDER BY pc.valeur DESC). "\
            "Le tri prend le plus de temps dans le temps total (Execution Time: 21.796 ms)."

analyse_3 = "Agrégation par nom_reg avec SUM(pc.valeur) pour calculer la population totale par région. "\
            "Utilisation de tri par ordre décroissant (ORDER BY population_totale DESC) et de limit (LIMIT 1). "\
            "Coût élevé en raison de l'agrégation sur de grandes données de commune et pop_commune (cost=14377.66..14377.66)."

analyse_4 = "Similaire à la requête 3 mais avec un tri différent, il est par ordre croissant (ORDER BY population_totale ASC). "\
            "Coût autant élevé en raison de l'agrégation sur de grandes données (cost=14377.66..14377.66)."

analyse_5 = "Filtres sur c.num_dep = '33' et pc.id_stat = 'P20_POP'. "\
            "Tri de pc.valeur par ordre décroissant (ORDER BY pc.valeur DESC). "\
            "Temps d'exécution assez rapide (Execution Time: 2.172 ms)."

analyse_6 = "Similaire à la requête 5 mais avec un tri différent, il est par ordre croissant (ORDER BY population_totale ASC). "\
            "Temps d'exécution aussi rapide (Execution Time: 1.986 ms)."

analyse_7 = "Agrégation par type_couple avec SUM(nb_mar) pour obtenir le total de mariages par type de couple dans un département spécifique. "\
            "Filtre sur dep = '1177' et id_stat = 'MAR21AGE_2'. "\
            "Exécution rapide (Execution Time: 0.514 ms)."
avertissement = "ATTENTION : Les temps affichés dans nos analyses sont différents de ceux retournés par les plans d'éxécution (tout en restant similaires/comparables). Nous nous sommes basées sur les résultats obtenus lors de la première exécution du code. Malgré des résultats différents, les analyses restent les mêmes et aboutissent aux mêmes conclusions."


def layout():
    return html.Div([
        # Div pour afficher les résultats des requêtes
        html.Div(id='query-results6')
    ])


def display_query_results():
    children = []
    children.append(html.Div([
        html.H1('6. Plan d\'exécution (EXPLAIN)', style={'textAlign': 'center',
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
        html.H2("Plan d'exécution de la 1ère requête :"),
        html.Pre(exe_query1),
        html.Div(id='query-results6',
                 children=[html.Pre(result) for result in formatted_results_1]),
        html.H4("Analyse de ce 1er plan d'exécution :"),
        html.P(html.Span(analyse_1, style={"white-space": "pre-line"})),
        html.H2("Plan d'exécution de la 2ème requête : "),
        html.Pre(exe_query2),
        html.Div(id='query-results6',
                 children=[html.Pre(result) for result in formatted_results_2]),
        html.H4("Analyse de ce 2ème plan d'exécution :"),
        html.P(html.Span(analyse_2, style={"white-space": "pre-line"})),
        html.H2("Plan d'exécution de la 3ème requête : "),
        html.Pre(exe_query3),
        html.Div(id='query-results6',
                 children=[html.Pre(result) for result in formatted_results_3]),
        html.H4("Analyse de ce 3ème plan d'exécution :"),
        html.P(html.Span(analyse_3, style={"white-space": "pre-line"})),
        html.H2("Plan d'exécution de la 4ème requête : "),
        html.Pre(exe_query4),
        html.Div(id='query-results6',
                 children=[html.Pre(result) for result in formatted_results_4]),
        html.H4("Analyse de ce 4ème plan d'exécution :"),
        html.P(html.Span(analyse_4, style={"white-space": "pre-line"})),
        html.H2("Plan d'exécution de la 5ème requête : "),
        html.P("Carastéristique de la requête : %s = 33"),
        html.Pre(exe_query5),
        html.Div(id='query-results6',
                 children=[html.Pre(result) for result in formatted_results_5]),
        html.H4("Analyse de ce 5ème plan d'exécution :"),
        html.P(html.Span(analyse_5, style={"white-space": "pre-line"})),
        html.H2("Plan d'exécution de la 6ème requête : "),
        html.P("Carastéristique de la requête : %s = 33"),
        html.Pre(exe_query6),
        html.Div(id='query-results6',
                 children=[html.Pre(result) for result in formatted_results_6]),
        html.H4("Analyse de ce 6ème plan d'exécution :"),
        html.P(html.Span(analyse_6, style={"white-space": "pre-line"})),
        html.H2("Plan d'exécution de la 7ème requête : "),
        html.P("Carastéristique de la requête : %s = 1177"),
        html.Pre(exe_query7),
        html.Div(id='query-results6',
                 children=[html.Pre(result) for result in formatted_results_7]),
        html.H4("Analyse de ce 7ème plan d'exécution :"),
        html.P(html.Span(analyse_7, style={"white-space": "pre-line"})),
        html.H2("Analyse générale :"),
        html.P("- Toutes les requêtes ont des jointures entre au moins deux tables, parfois plus. Ces jointures peuvent être un point critique pour les performances."),
        html.P("- Chaque requête comporte des 'WHERE' qui filtrent les données en fonction de certaines conditions."),
        html.P("- Plusieurs requêtes utilisent des fonctions d'agrégation comme SUM pour calculer des effectifs totaux."),
        html.P("- Certaines requêtes ont un tri des résultats, soit pour présenter les données (ORDER BY), soit pour limiter le nombre de résultats (LIMIT)."),
        html.P("Pour conclure, les requêtes ont des schémas d'accès aux données similaires mais avec des besoins de traitement différents selon ceux rappelés ci-dessus. Une attention aux détails d'indexation, d'optimisation des requêtes ou encore des performances, contribuera à améliorer les performances de notre système de base de données.")
    ]))

    return children


@callback(
    Output('query-results6', 'children'),
    [Input('query-results6', 'id')]
)
def update_query_results(trigger):
    return display_query_results()
