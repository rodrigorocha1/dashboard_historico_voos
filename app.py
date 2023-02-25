from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc


class APP:
    def __init__(self):
        self.app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.app.config['suppress_callback_exceptions'] = True
        self.app.scripts.config.serve_locally = True
        self.app.layout = self.get_layout()

    def get_layout(self):
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.NavbarSimple(
                            children=[
                                dbc.NavItem(
                                    dbc.NavLink(
                                        f'{page["name"]}',
                                        href=page["relative_path"],
                                    )
                                ) for page in dash.page_registry.values()
                            ],
                            color='#1A1CE',
                            brand='Dashboard de Analise de Voos',
                            dark=True,
                            brand_href='/',
                            id='id_main_navbar',
                            style={
                                'margin-botton': '10px'
                            }

                        )
                    ], id='linha_menu'
                ),
                dbc.Row(
                    dash.page_container,
                    id='linha_analise'
                ),
            ]
        )

    def rodar_servico(self):
        self.app.run_server(debug=True, port=8061)


a = APP()
server = a.app.server

if __name__ == '__main__':
    a.rodar_servico()
