# Import all dependencies
import pandas as pd
import plotly.express as px
import dash
from dash import dcc,html
# Create dash App
app = dash.Dash()
# Create a dataframe
df = pd.DataFrame({
  #Two columns one is Fruits and other is Amount
  "Fruits": ["Apples","Mango","Dates" ,"Grapes"],
   "Amount" :[10, 5, 20, 40]
 })
# Create plotly graph
# Bar_char requieres the dataframe, x and y axis, title (optional), 
# color(its neccassary to use it when we want color_discrete_sequence based on some criteria("Fruits")) and 
# color_discrete_sequence( optional used to give different colors to different bars hard coded for visual clarity)
Bar_Chart = px.bar(df, x = "Fruits" , y="Amount" , title="Bar_Chart" ,color="Fruits", color_discrete_sequence = ["Red","Yellow","Black","Purple"])
# Pie_chart requieres the dataframe, names and values,  and rest is same as bar_chart
Pie_Chart = px.pie(df, names="Fruits" , values= "Amount" , title="Pie_Chart", color="Fruits", color_discrete_sequence = ["Red","Yellow","Black","Purple"])
# Create a beautiful layout
app.layout=html.Div([
    html.H1("Time to present charts side by side " ,style={"textAlign" : "center", "color": "Maroon" , "font-family": "Arial"}),  
    # 2 Child divs for 2 graphs and styling them to be inline and take 50% of the width each (so they can be side by side) 
    # id is used to style the graph when usinng external css  also to link the graph with callback functions when we want to make it interactive
    #  and figure is used to pass the graph object we created above (Bar_Chart and Pie_Chart)
    html.Div([dcc.Graph(id="bar_chart",
              figure=Bar_Chart)], style= {"display" : "inline-block" , "width" : "50%"}),
    html.Div([dcc.Graph(id="Pie_chart",
              figure=Pie_Chart)],style= {"display" : "inline-block" , "width" : "50%"} )               
]
# Styling the main div to center the content
#style={"textAlign" : "center", "color": "DarkBlue" , "font-family": "Arial"}
)
# Run App(debug mode)
if __name__ == "__main__":
  app.run(debug=True)


