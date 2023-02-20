import dash_bootstrap_components as dbc
from dash import dcc, html

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Card title", className='class_cartao_info'),


        ], className='class_cartao_info'
    )
)

second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Card title", className='class_cartao_info'),
            html.H5("Card title", className='class_cartao_info'),
            html.H5("Card title", className='class_cartao_info'),
            html.H5("Card title", className='class_cartao_info'),
            html.H5("Card title", className='class_cartao_info'),
            html.H5("Card title", className='class_cartao_info'),


        ], className='class_cartao_info'
    )
)
