from dash import Dash, html, dcc
# import dash_core_components as dcc
# import dash_html_components as html
from datetime import datetime as dt

app = Dash(__name__)
server = app.server
app.layout = html.Div([item1, item2])
html.Div(
    [html.P("Welcome to the stock market prediction app",className="start"),html.Div([#stock code input
    ])],className = "nav")


if __name__ == '__main__': 
    app.run_server(debug=True)