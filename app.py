import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
#Get data
data = pd.read_excel('Deal Tracking Report.xlsx', 'Deal Tracking 2020')
data.sort_values("Sale Date", inplace=True)
data['TotalSale_7DayRollingAvg']=data['Total Sale'].rolling(7).mean()

#Format dates
data['week_of_year'] = data['Sale Date'].dt.week
data['day_of_week'] = data['Sale Date'].dt.dayofweek
dw_mapping={
    0: 'Monday', 
    1: 'Tuesday', 
    2: 'Wednesday', 
    3: 'Thursday', 
    4: 'FridayTTe',
    5: 'Saturday', 
    6: 'Sunday'
} 
data['day_of_week_name']=data['Sale Date'].dt.weekday.map(dw_mapping)
data.sort_values(by=['Sale Date'])

########### Define your variables
beers=['Manufacturer']
ibu_values=data['Gross Profit']
abv_values=data['Total Sale']
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'



########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
