import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State

from get import get
from parse import parse

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Лабораторна работа №2"),
    html.Div([
        "Сайт: ",
        dcc.Input(id='input-site', value='', type='text')
    ]),
    html.Div([
        "Глубина: ",
        dcc.Input(id='input-deep', value='0', type='text')
    ]),
    html.Br(),
    html.Button(id='input-btn', n_clicks=0, children='Выполнить'),
    html.Br(),
    html.Div(id='my-output'),
])

def create_list(list):
    return [
        html.P(children=['Сайт: ', list['site']]),
        html.P(children=['Файлы (кол-во: ', len(list['file']) , ', общ. размер: ', sum( (int(item['size']) for item in list['file']) ) ,' Байт):']),
        html.Ol(children=[html.Li(children=[
            html.P(children=['Файл: ', item['file']]),
            html.P(children=['Content-Length: ', item['size'], ' Байт'])])  for item in list['file']]),
        html.P(children=['Дочернии сайты:']),
        html.Ol(children=[html.Li(children=create_list(item)) for item in list['subsite']])]

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='input-btn', component_property='n_clicks'),
    State(component_id='input-site', component_property='value'),
    State(component_id='input-deep', component_property='value'))
def update_output_div(_, site, deep):
    if site == '' or deep == '':
        return 'Ошибка при вводе данных'

    if 'https://' in site:
        host = site.replace('https://', '')
    elif 'http://' in site:
        host = site.replace('http://', '')
    else:
        return 'Ошибка при вводе данных'

    host = host.replace('/', '')

    return [html.P(children=get(host)), 
            html.Br(), 
            html.Div(children=create_list(parse(site, int(deep))))]

if __name__ == '__main__':
    app.run_server(debug=True)