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

image_style = {
    'width': '100%',
    'max-width': '700px',
    'height': 'auto',
    'display': 'block',
    'margin': '0 auto',
}


def calculate_width(question):
    return min(300, max(150, 200 // len(question)))


def layout():
    children = []
    children.append(html.Div([
        html.H1('Questions', style={'textAlign': 'center',
                'color': '#670907', 'font-size': '2.5em'})
    ], style=card_style))
    children.append(
        html.P("Nous allons chercher à répondre aux demandes suivantes : ", style={'fontSize': '1.25em'}))

    question_links = [
        dcc.Link(
            pi['question'],
            href=pi['path'],
            style={
                'fontSize': min(30, max(15, 400 // len(pi['question']))),
                'margin': '20px', 'padding': '10px', 'border': '5px double white',
                'backgroundColor': '#670907', 'color': 'white',
                'width': f"{calculate_width(pi['question'])}px",
                'height': 'auto', 'text-align': 'center',
                'textDecoration': 'none'
            }
        )
        for pi in dash.page_registry.values() if 'question' in pi
    ]

    top_questions = question_links[:4]
    bottom_questions = question_links[4:]

    children.append(html.Div([
        html.Div(top_questions, style={
                 'display': 'flex', 'justifyContent': 'space-evenly'}),
        html.Div(bottom_questions, style={
                 'display': 'flex', 'justifyContent': 'space-evenly'}),
    ], style={'display': 'flex', 'flexDirection': 'column'}))

    return html.Div(children=children)
