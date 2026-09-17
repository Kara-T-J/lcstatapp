from dash import html


def metric_card(
    title: str,
    value,
    subtitle: str | None = None,
    unit: str | None = None,
    card_id: str | None = None,
):
    """
    Generic KPI card.

    Parameters
    ----------
    title : str
        Card title.
    value :
        Value displayed in the card.
    subtitle : str | None
        Optional additional information.
    unit : str | None
        Optional unit displayed next to the value.
    card_id : str | None
        Optional Dash component ID.
    """

    value_content = [
        html.Span(
            value,
            className="metric-card-value",
        )
    ]

    if unit:
        value_content.append(
            html.Span(
                f" {unit}",
                className="metric-card-unit",
            )
        )

    children = [
        html.Div(
            title,
            className="metric-card-title",
        ),

        html.Div(
            value_content,
            className="metric-card-main",
        ),
    ]

    if subtitle:
        children.append(
            html.Div(
                subtitle,
                className="metric-card-subtitle",
            )
        )

    props = {"className": "metric-card"}
    if card_id is not None:
        props["id"] = card_id

    return html.Div(
        children,
        **props,
    )