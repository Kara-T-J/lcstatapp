import dash
from dash import html


dash.register_page(
    __name__,
    path="/team",
    name="Team",
)


layout = html.Div(
    [
        html.H2("Team Analysis", className='header-title'),

        html.Div(
            id="team-filters"
        ),

        html.Div(
            id="team-content"
        ),
    ]
)