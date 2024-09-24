import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from pages.navbar import generate_sidebar

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
]

app = dash.Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True, assets_folder='assets_folder')

app.layout = html.Div(style={'backgroundColor': '#c0c0bb', 'min-height': '100vh'}, children=[
    dbc.Row([
        dbc.Col(width=2, children=generate_sidebar("")),
        dbc.Col(width=10, children=dash.page_container)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)



