# Import Dependencies
import dash 
from dash import dcc , html
import plotly.express as px
import pandas as pd

# Create dash app
app = dash.Dash()

# Create a dataframe
df = pd.DataFrame({
    "Profession" : ["IT", "Marketing" ,"Finance"],
    "Quantity" : [120, 70, 20]
})

#print(df)

# Create Plotly Graphs
Bar = px.bar(df , x= "Profession" , y="Quantity" , color= "Profession", color_discrete_sequence=["Blue","Orange","Green"])
Pie = px.pie(df, names="Profession", values="Quantity",color= "Profession", color_discrete_sequence=["Blue","Orange","Green"])

#Create App layout
app.layout= html.Div([
    html.H1("Time to present the charts"),
    dcc.Graph(
        figure=Bar),
    dcc.Graph(
        figure=Pie
    )
])

# Run the App
if __name__== "__main__":
    app.run(debug=True)