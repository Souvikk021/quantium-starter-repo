import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load cleaned sales data
df = pd.read_csv("data/formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Build Dash app
app = dash.Dash(__name__)
app.layout = html.Div(
    style={"font-family": "Arial, sans-serif", "backgroundColor": "#f9f9f9", "padding": "20px"},
    children=[
        html.H1(
            "Soul Foods Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#e74c3c"}
        ),
        html.Div([
            html.Label("Select Region:", style={"font-weight": "bold", "margin-right": "10px"}),
            dcc.RadioItems(
                id="region-radio",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"}
                ],
                value="all",
                labelStyle={"display": "inline-block", "margin-right": "15px"}
            )
        ], style={"margin-bottom": "20px"}),
        dcc.Graph(id="sales-line-chart")
    ]
)

# Callback to update chart based on selected region
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        df_filtered = df
    else:
        df_filtered = df[df["region"].str.lower() == selected_region.lower()]
    
    df_grouped = df_filtered.groupby("date", as_index=False)["sales"].sum()
    
    fig = px.line(
        df_grouped,
        x="date",
        y="sales",
        labels={"date": "Date", "sales": "Sales ($)"},
        title=f"Pink Morsel Sales Over Time - {selected_region.title()}"
    )
    fig.add_vline(x="2021-01-15", line_width=2, line_dash="dash", line_color="red")
    fig.add_annotation(
        x="2021-01-15", y=df_grouped["sales"].max(),
        text="Price Increase",
        showarrow=True, arrowhead=2
    )
    fig.update_layout(template="plotly_white")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
