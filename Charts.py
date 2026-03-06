# Import Dependencies
import dash 
from dash import dcc , html
import plotly.express as px
import pandas as pd

# Create dash app
app = dash.Dash(__name__)

# Create a dataframe
df = pd.DataFrame({
    # 2 columns, one for profession and one for quantity of students in that profession.
    "Profession" : ["IT", "Marketing" ,"Finance"],
    "Quantity" : [120, 70, 20]
})

#print(df)

# Create Plotly Graphs
Bar = px.bar(df , x= "Profession" , y="Quantity" , color= "Profession", color_discrete_sequence=["Blue","Orange","Green"])
Pie = px.pie(df, names="Profession", values="Quantity",color= "Profession", color_discrete_sequence=["Blue","Orange","Green"])

#Create App layout
# A div is basically a section in the webpage, and we can add different components(children) to it.
# Here we are adding a heading and two graphs.
app.layout= html.Div([
    # Heading 1 is the largest heading.
    html.H1("Time to present the charts"),
    # Graph component is used to display the graphs created using plotly.
    dcc.Graph(
        figure=Bar),
    dcc.Graph(
        figure=Pie
    )
])

# Run the App
# The if statement is used to check if the script(file) is being run directly (as the main program) 
# or imported as a module in another script.
if __name__== "__main__":
    # The run() method starts the Dash application server, allowing you to view the app in a web browser.
    # The debug=True argument enables debug mode, which provides helpful error messages 
    # and automatically reloads the app when changes are made to the code.
    # Make sure to set debug to False in production to avoid exposing sensitive information.
    app.run(debug=True)