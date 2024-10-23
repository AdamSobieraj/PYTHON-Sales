from dash import dcc
from dash import html
import plotly.graph_objects as go


def render_tab(df):

    layout = html.Div([

                        html.H1('Produkty',style={'text-align':'center'}),

                        html.Div([html.H2('Sprzedaż globalna',style={'text-align':'center'}),

                        html.Div([dcc.DatePickerRange(id='chanel-range',
                                    start_date=df['tran_date'].min(),
                                    end_date=df['tran_date'].max(),
                                    display_format='YYYY-MM-DD')],style={'text-align':'center'}),
                                    html.Div([html.Div([dcc.Graph(id='bar-chanel')],style={})]),

                        html.Div([dcc.Dropdown(id='chanel_dropdown',
                                    options=[{'label':prod_cat,'value':prod_cat} for prod_cat in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='barh-chanel-subcat')])])
                        ])

    return layout