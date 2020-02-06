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
        ),

         html.P("Mobile Number:"),
         dcc.Input(
             id="phone_number_input",
             type="number",
             placeholder="Enter Mobile Number",
         ),
         html.P("Email Address:"),
         dcc.Input(
             id="email_address_input",
             type="text",
             placeholder="Enter Email Address",
         ),

        html.Button('Submit', id='button'),

    ]
    + [html.Div(id="out-all-types")]
)


@app.callback(
    Output("out-all-types", "children"),
    [Input("first_name_input", "value"),
     Input("second_name_input", "value"),
     Input("phone_number_input", "value"),
     Input("email_address_input", "value"),
     Input('button', 'n_clicks')],
)
def save_details(first_name_input, second_name_input, phone_number_input,  email_address_input, n_clicks):

    if n_clicks is None:
        return None
    else:
        with open('database.csv', mode='a') as database_file:
            database_file = csv.writer(database_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            database_file.writerow([first_name_input, second_name_input, phone_number_input, email_address_input])


def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )
