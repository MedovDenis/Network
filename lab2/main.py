import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State

from parser import parse
from get import get

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Лабораторна работа №2"),
    html.Div([
        "Сайт: ",
        dcc.Input(id='input-site', value='initial value', type='text')
    ]),
    html.Div([
        "Глубина: ",
        dcc.Input(id='input-deep', value='initial value', type='text')
    ]),
    html.Br(),
    html.Button(id='input-btn', n_clicks=0, children='Выполнить'),
    html.Br(),
    html.Div(id='my-output'),
])

def create_list(list):
    return [
    html.P(children=['Сайт:', list['site']]),
    html.P(children=['Файлы:']),
    html.Ul(children=[html.Li(children=['Файл:', item['file']])  for item in list['file']]),
    html.P(children=['Дочернии сайты:']),
    html.Ul(children=[create_list(item) for item in list['subsite']])]

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='input-btn', component_property='n_clicks'),
    State(component_id='input-site', component_property='value'),
    State(component_id='input-deep', component_property='value'))
def update_output_div(_, site, deep):
    return create_list(parse(site, deep))


if __name__ == '__main__':
    app.run_server(debug=True)