import dash
from dash import html
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#670907",  
}
NAV_LINK_STYLE = {
    "color": "white",
}

PAGE_ORDER = ["Home","Presentation", "Questions"]


def generate_sidebar(pathname):
    sidebar = html.Div(
        [
            html.H2("PROJET BDA", style={"color": "white"}),
            html.Hr(style={"border-color": "white"}),
            html.P("Menu", className="lead", style={"color": "white"}),
            dbc.Nav(
                # créer une liste de liens
                [
                    dbc.NavLink(
                        f"{page['name']}", #Le texte du lien est le nom de la page.
                        href=page["relative_path"], #L'attribut "href" spécifie le chemin relatif vers la page.
                        id=f"{page['name'].lower()}-link", #L'ID du lien, converti en minuscules (dash met en majuscules)
                        style={
                            **NAV_LINK_STYLE,
                            "font-size": "1.5rem" 
                        },
                        active={
                            'font-weight': 'bold'
                        } if page["name"].lower() == pathname.strip('/') else {},
                        className="nav-link-hover", 
                    )
                    for page_name in PAGE_ORDER
                    for page in dash.page_registry.values() if page["name"] == page_name and 'location' in page and page['location'] == 'sidebar'
                ],
                vertical=True,
                pills=True,
            ),
            html.P("ABARKAN Suhaila", style={"color": "white",
                   "font-size": "1.1rem", "margin-top": "100px"}),
            html.P("MOUCHRIF Dounia", style={
                   "color": "white", "font-size": "1.1rem"}),
            html.P("TISSANDIER Mathilde", style={
                   "color": "white", "font-size": "1.1rem"})
        ],
        style=SIDEBAR_STYLE,
    )

    return sidebar