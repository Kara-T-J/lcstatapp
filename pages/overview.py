import dash
from dash import dcc, html, callback, Output, Input

from components import charts
from components import cards

from app_data import tasks_df

from services import workload_service

dash.register_page(
    __name__,
    path="/",
    name="Overview",
)


layout = html.Div(
    [
        html.H2("Overview", className='header-title'),

        html.Div(
            id="overview-kpis"
        ),

        dcc.Graph(
            id="overview-workload-chart"
        ),
    ]
)

@callback(
    Output("overview-kpis", "children"),
    Output("overview-workload-chart", "figure"),
    Input("global-filter-state", "data"),
)
def update_overview(filter_state):

    data = workload_service.get_overview(tasks_df,filter_state)

    summary = html.Div(
        [
            html.H4(
                f"Date from {data['min_date']} to {data['max_date']}",
                className="header-subtitle",
            ),
            html.Div(className='grid grid-4', children=[
                cards.metric_card("Tasks",data['task_count'],"tickets"),
                cards.metric_card("Workload",data['total_workload'],"hours"),
                cards.metric_card("Average Workload",data['average_workload'],"h/day")
            ])            
        ]
    )

    figure = charts.teamload_timeline(
        data["teamload_timeline"]
    )

    return summary, figure