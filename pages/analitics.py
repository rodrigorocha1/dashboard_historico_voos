import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')


class Analitics:

    def __init__(self):
        self.layout = self._get_layout()
        self._calbacks()

    def _get_layout(self):
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col('Coluna1', md=4),
                                        dbc.Col('Coluna2', md=4),
                                        dbc.Col('Coluna3', md=4),
                                    ]

                                ),
                                dbc.Row(
                                    [
                                        dbc.Col('Coluna1', md=9),
                                        dbc.Col('Coluna2', md=3)
                                    ]
                                ),
                            ],
                            md=9
                        ),
                        dbc.Col(
                            'Coluna 2',
                            md=3
                        )
                    ],
                    className='class_layout'
                ),
                dbc.Row(
                    'Segunda Linha',
                    className='class_layout'
                ),
            ]
        )

    def _calbacks(self):
        @callback(
            Output(component_id='analytics-output', component_property='children'),
            Input(component_id='analytics-input', component_property='value'))
        def update_city_selected(input_value):
            return f'You selected: {input_value}'


a = Analitics()
layout = a.layout
