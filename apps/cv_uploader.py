import dash_html_components as html
import dash_core_components as dcc
import csv
import base64

from app import app
from dash.dependencies import Input, Output

layout = html.Div(
    [
        #This creates the title and the boxs for the inputs
        html.P("First Name:"),
        dcc.Input(
            id="first_name_input",
            type="text",
            #This is what appears in grey within the textbox
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
             type="tel",
             placeholder="Enter Mobile Number",
         ),
         html.P("Email Address:"),
         dcc.Input(
             id="email_address_input",
             type="text",
             placeholder="Enter Email Address",
         ),
        #This creates the box in which the user can upload their CV by either selecting or dragging and dropping
        html.P("Upload your CV here:"),
        dcc.Upload(
            id='upload_data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            #This is the styling for the box in which they upload their CV
            style={
                'width': '50%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # does not allow multiple files to be uploaded
            multiple=False
        ),
        #This is the submit button in which it uploads the data inputted
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
     Input('upload_data', 'contents'),
     Input('button', 'n_clicks')],
)
#this is what decides what is saved to the database
def save_details(first_name_input, second_name_input, phone_number_input,  email_address_input,contents, n_clicks):

    if n_clicks is None:
        return None
    else:
        decoded = base64.b64decode(contents.encode('latin1').decode('cp1251'))

        with open('database.csv', mode='a') as database_file:
            database_file = csv.writer(database_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            database_file.writerow([first_name_input, second_name_input, phone_number_input, email_address_input, decoded])


def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )
