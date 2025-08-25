import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load cleaned sales data
df = pd.read_csv("data/formatted_sales_data.csv")

# Make sure date column is datetime type
df["date"] = pd.to_datetime(df["date"])

# Aggregate sales per day (in case multiple regions)
df_grouped = df.groupby("date", as_index=False)["sales"].sum()

# Create line chart
fig = px.line(
    df_grouped,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales ($)"}
)

# Add a vertical line for Jan 15, 2021 (price increase)
fig.add_vline(x="2021-01-15", line_width=2, line_dash="dash", line_color="red")
fig.add_annotation(
    x="2021-01-15", y=df_grouped["sales"].max(),
    text="Price Increase",
    showarrow=True, arrowhead=2
)

# Build Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)
