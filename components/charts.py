import plotly.express as px
import plotly.graph_objects as go


def empty_figure(message: str = "No data"):
	figure = go.Figure()
	figure.update_layout(
		template="plotly_white",
		annotations=[
			{
				"text": message,
				"showarrow": False,
				"xref": "paper",
				"yref": "paper",
				"x": 0.5,
				"y": 0.5,
			}
		],
		xaxis={"visible": False},
		yaxis={"visible": False},
	)
	return figure


def workload_timeline(timeline):
	if timeline is None or timeline.empty:
		return empty_figure("No workload data")

	figure = px.line(
		timeline,
		x="Due Date",
		y="Workload",
		markers=True,
	)
	figure.update_layout(
		template="plotly_white",
		xaxis_title="Due Date",
		yaxis_title="Workload",
		hovermode="x unified",
		margin={"l": 40, "r": 0, "t": 20, "b": 40},
	)
	return figure

def headcount_timeline(timeline):
	if timeline is None or timeline.empty:
		return empty_figure("No workload data")

	figure = px.line(
		timeline,
		x="Due Date",
		y="Headcount",
		markers=True,
	)
	figure.update_layout(
		template="plotly_white",
		xaxis_title="Due Date",
		yaxis_title="Members",
		hovermode="x unified",
		margin={"l": 40, "r": 0, "t": 20, "b": 40},
	)
	return figure

def teamload_timeline(timeline):
	if timeline is None or timeline.empty:
		return empty_figure("No workload data")

	figure = px.line(
		timeline,
		x="Due Date",
		y="Teamload",
		markers=True,
	)
	figure.update_layout(
		template="plotly_white",
		xaxis_title="Due Date",
		yaxis_title="Team load",
		hovermode="x unified",
		margin={"l": 40, "r": 0, "t": 20, "b": 40},
	)
	return figure