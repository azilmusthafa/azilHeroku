'''import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)
server = app.server

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True) '''


from jupyter_dash import JupyterDash
import dash
import dash_html_components as html
import pandas as pd
 
df = pd.read_csv('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/usa-agricultural-exports-2011.csv')
 
 
def generate_table(dataframe, max_rows=50):
   return html.Table([
       html.Thead(
           html.Tr([html.Th(col) for col in dataframe.columns])
       ),
       html.Tbody([
           html.Tr([
               html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
           ]) for i in range(min(len(dataframe), max_rows))
       ])
   ])
 
 

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
   html.H4(children='US Agriculture Exports (2011)'),
   generate_table(df)
])
 
if __name__ == '__main__':
   app.run_server(debug=True)
