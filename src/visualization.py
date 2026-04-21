"""Utility to visualize photo plans.
"""

import typing as T

import plotly.graph_objects as go

from src.data_model import Waypoint


def plot_photo_plan(photo_plans: T.List[Waypoint]) -> go.Figure:
    """Plot the photo plan on a 2D grid.

    Args:
        photo_plans: List of waypoints for the photo plan.

    Returns:
        Plotly figure object.
    """
    xs = [wp.x_coordinate for wp in photo_plans]
    ys = [wp.y_coordinate for wp in photo_plans]

    fig = go.Figure()

    # Flight path line
    fig.add_trace(go.Scatter(
        x=xs, y=ys,
        mode="lines",
        line=dict(color="royalblue", width=1.5, dash="dot"),
        name="Flight path"
    ))

    # Waypoints (photo positions)
    fig.add_trace(go.Scatter(
        x=xs, y=ys,
        mode="markers",
        marker=dict(color="red", size=6, symbol="circle"),
        name="Photo waypoints",
        text=[f"Waypoint {i}<br>({wp.x_coordinate:.1f}m, {wp.y_coordinate:.1f}m)"
              for i, wp in enumerate(photo_plans)],
        hoverinfo="text"
    ))

    # Start and end markers
    fig.add_trace(go.Scatter(
        x=[xs[0]], y=[ys[0]],
        mode="markers+text",
        marker=dict(color="green", size=12, symbol="star"),
        text=["Start"], textposition="top center",
        name="Start"
    ))
    fig.add_trace(go.Scatter(
        x=[xs[-1]], y=[ys[-1]],
        mode="markers+text",
        marker=dict(color="black", size=12, symbol="square"),
        text=["End"], textposition="top center",
        name="End"
    ))

    fig.update_layout(
        title="Photo Plan Grid",
        xaxis_title="X distance (m)",
        yaxis_title="Y distance (m)",
        yaxis=dict(scaleanchor="x", scaleratio=1),  # equal aspect ratio
        legend=dict(x=0, y=1),
        hovermode="closest"
    )

    return fig
