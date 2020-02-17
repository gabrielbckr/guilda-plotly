import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.io as pio

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

plot_3d = pio.read_json('../plots/plot_3d.json')
plot_2d = pio.read_json('../plots/plot_2d.json')

app.layout = html.Div(children=[
    dcc.Markdown(children='''
        # Dash > Power BI
        Por que?
        
        * Gratis
        * Python
        * Flex
        
    '''),

    dcc.Graph(
        id="3d",
        figure=plot_3d
    ),
    dcc.Graph(
        id="2d",
        figure=plot_2d
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)