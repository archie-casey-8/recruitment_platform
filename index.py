import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app
from apps import cv_uploader, call_booker


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H2("Main Menu"),
        html.Img("src=assets/image.png")
    ], className=("body"),)
])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return html.Div([
            dcc.Link('Go to CV uploader', href='/cv_uploader'),
            html.Br(),
            dcc.Link('Go to Call Booker', href='/apps/call_booker')
        ])

    if pathname == '/cv_uploader':
         return cv_uploader.layout
    elif pathname == '/apps/call_booker':
         return call_booker.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)