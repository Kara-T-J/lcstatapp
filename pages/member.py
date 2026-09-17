import dash
from dash import html


dash.register_page(
    __name__,
    path="/member",
    name="Member",
)


layout = html.Div(
    [
        html.H2("Individual Analysis", className='header-title'),

        html.Div(
            id="individual-filters"
        ),

        html.Div(
            id="individual-content"
        ),
    ]
)