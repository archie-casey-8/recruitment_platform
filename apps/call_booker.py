from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

ALLOWED_TYPES = (
    "text", "text"
)

layout = html.Div(
    [
        html.P("Mobile number:"),
        dcc.Input(
            id="mobile_number_input",
            type="tel",
            placeholder="Enter your mobile number",
        )#,
        # html.P("Second Name:"),
        # dcc.Input(
        #     id="input_{}".format("text"),
        #     type="text",
        #     placeholder="Enter Second Name",
        # )

    ]
    + [html.Div(id="out-all-types")]
)



@app.callback(
    Output('app-2-display-value', 'children'),
    [Input('app-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)