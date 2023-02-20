from app import *
import dash_bootstrap_components as dbc
from dash import dcc, html
from src.layouts.layouts_cartoes import first_card, second_card

app.layout = html.Div(
    [
        dbc.Row(
            '   Cabeçalho',
            id='linha_principal_1'
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(first_card, md=4),
                                dbc.Col(first_card, md=4),
                                dbc.Col(first_card, md=4),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col('coluna1', md=8, className='class_graficos'),
                                dbc.Col('coluna2', md=4, className='class_graficos'),
                            ], id='id_linha_graficos'
                        ),
                    ],
                    md=9
                ),
                dbc.Col(
                    second_card,
                    md=3
                ),
            ],
            id='id_linha_principal_2'
        ),
        dbc.Row(
            [
                dbc.Col('coluna1', md=3),
                dbc.Col('coluna2', md=3),
                dbc.Col('coluna3', md=3),
                dbc.Col('coluna4', md=3),
            ],
            id='id_linha_principal_3',
            className='class_graficos'
        ),
    ],
    id='id_caixa_gandre'
)

if __name__ == '__main__':
    app.run(port=8065, debug=True)
