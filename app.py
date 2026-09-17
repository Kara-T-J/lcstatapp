from dash import Dash, html, dcc, page_container, Input, Output, callback, State, ctx
import dash_ag_grid as dag

import services.temporal_service as temp_serv

from domain.temporal import last_date

import config as cfg


# ---------------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------------

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    title="Support Workload Dashboard",
)

server = app.server


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

from app_data import tasks_df
LAST_DATE = last_date(tasks_df)

# ---------------------------------------------------------------------------
# Global layout
# ---------------------------------------------------------------------------

app.layout = html.Div(
    [
        dcc.Store(
            id="global-filter-state",
            storage_type="memory",
        ),

        # Global application header
        html.Header(
            [
                # Main navigation
                html.Nav(
                    [
                        html.Div(className='main-nav', children=[
                            dcc.Link("Overview", href="/",className='nav-link'),
                            dcc.Link("Team", href="/team",className='nav-link'),
                            dcc.Link("Member", href="/member",className='nav-link'),
                        ]),

                        html.H1("Support Workload Dashboard"),

                        html.Div(className='grid grid-4', children=[
                            html.Button(className='button-secondary', id = 'prev-btn', children='Previous'),
                            html.Button(className='button-secondary', id = 'default-btn', children='Default view'),
                            html.Button(className='button-secondary', id = 'next-btn', children='Next')
                        ]),
                    ]
                ),
            ]
        ),

        # Content of the current page
        html.Main(
            page_container
        ),

        # Footer with data table
        html.Footer(
            html.Div(className='full-width', children=[
                html.H3("Global Filters"),
                dag.AgGrid(
                    id="global-task-grid",

                    rowData=tasks_df.to_dict("records"),

                    columnDefs=[
                        {"field": "Summary"},
                        {"field": "Due Date"},
                        {"field": "Owned By"},
                        {"field": "Type"},
                        {"field": "Size"},
                    ],

                    columnSize="autoSize",

                    defaultColDef={"filter": True,"sortable": True, "resizable": True,},

                    dashGridOptions={
                        "initialState": {
                            "filter": {
                                "filterModel": {
                                    "Due Date": {
                                        "filterType": "date",
                                        "type": "greaterThan",
                                        "dateFrom": cfg.START_DATE.strftime("%Y-%m-%d")
                                    }
                                }
                            }
                        }
                    },

                    className='ag-theme-quartz',
                ),
            ]),
        ),
    ]
)


# ---------------------------------------------------------------------------
# General Callbacks
# ---------------------------------------------------------------------------

@callback(
    Output("global-filter-state", "data"),
    Input("global-task-grid", "filterModel"),
)
def update_global_filters(filter_model):
    return filter_model

@callback(
    Output("global-task-grid", "filterModel"),
    Input("prev-btn", "n_clicks"),
    Input("default-btn", "n_clicks"),
    Input("next-btn", "n_clicks"),
    State("global-task-grid", "filterModel"),
)
def update_time_filter(prev_click,default_click,next_click,current_grid):
    button_id = ctx.triggered_id
    if button_id == "default-btn":
        return temp_serv.default_due_date_filter_model()
    if button_id == "prev-btn":
        due_filter = (current_grid or {}).get("Due Date") or {}
        date_from = due_filter.get("dateFrom", LAST_DATE)
        return temp_serv.set_prev_month(date_from)
    if button_id == "next-btn":
        due_filter = (current_grid or {}).get("Due Date") or {}
        date_from = due_filter.get("dateFrom", cfg.START_DATE)
        return temp_serv.set_next_month(date_from)

# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)