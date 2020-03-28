import dash_html_components as html
import dash_core_components as dcc
import csv
from datetime import datetime as dt
from app import app
from dash.dependencies import Input, Output
from call_booker_functions import date_time_dict_constructor

layout = html.Div(
    [
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

         html.P("Select date:"),
         dcc.DatePickerSingle(
         id='my_date_picker_single',
         min_date_allowed=dt(1995, 8, 5),
         max_date_allowed=dt(2023, 9, 19),
         initial_visible_month=dt(2017, 8, 5),
         date=str(dt(2017, 8, 25, 23, 59, 59))
         ),
         html.Button('Submit', id='button'),

         html.P("Select time:"),
         dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montreal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            searchable=False
        )
    ]
    + [html.Div(id="out-all-types-call-booker")]
)

@app.callback(
    Output("out-all-types-call-booker", "children"),
    [Input("first_name_input", "value"),
    Input("second_name_input", "value"),
    Input("phone_number_input", "value"),
    Input("email_address_input", "value"),
    Input('my_date_picker_single', 'date'),
    Input('button', 'n_clicks')],
)
#this is what decides what is saved to the database
def save_details(first_name_input, second_name_input, phone_number_input, email_address_input, my_date_picker_single, n_clicks):

    if n_clicks is None:
        return None
    else:

        with open('database/call_booker_table.csv', mode='a') as database_file:
            database_file = csv.writer(database_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            database_file.writerow([first_name_input, second_name_input, phone_number_input, email_address_input, my_date_picker_single])

def parse_datetime(value, date):
    string_prefix = 'You have selected: '
    if date is not None:
        date = dt.strptime(date.split(' ')[0], '%Y-%m-%d')
        date_string = date.strftime('%B %d, %Y')
        return string_prefix + date_string

def get_available_times(my_date_picker_single):
    date_time_dict = date_time_dict_constructor(30)
    print(date_time_dict[my_date_picker_single])


def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks

    )