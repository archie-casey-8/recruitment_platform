from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import csv

from app import app

layout = html.Div(
    [
        html.P("First Name:"),
        dcc.Input(
            id="first_name_input",
            type="text",
            placeholder="Enter First Name",
        ),
        html.P("Second Name:"),
        dcc.Input(
            id="second_name_input",
            type="text",
            placeholder="Enter Second Name",
        ) ,
        html.Button('Submit', id='button'),

    ]
    + [html.Div(id="out-all-types")]
)


@app.callback(
    Output("out-all-types", "children"),
    [Input("first_name_input", "value"),
     Input("second_name_input", "value"),
     Input('button', 'n_clicks')],
)
def save_details(first_name_input,second_name_input):

    with open('database.csv', mode='w') as database_file:
        database_file = csv.writer(database_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        database_file.writerow([first_name_input])
    return first_name_input + second_name_input

def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )
