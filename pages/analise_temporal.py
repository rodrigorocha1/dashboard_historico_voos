import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)


class AnaliseTemporal:

    def __init__(self):
        self.layout = self._get_layout()

    def _get_layout(self):
        return html.Div(
            children=[
                html.H1(
                    children='Analise Temporal'
                ),

                html.Br()
            ]
        )


a = AnaliseTemporal()
layout = a.layout
