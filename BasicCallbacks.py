# Importing the necessary libraries for our dash application
import dash
import pandas as pd
from dash import dcc, html , Input, Output , callback
import plotly.express as px
df = pd.DataFrame({
    # 2 columns, one for profession and one for quantity of students in that profession.
    "Profession" : ["IT", "Marketing" ,"Finance"],
    "Quantity" : [120, 70, 20 ]
})
# Calculating the total students in all professions using pandas sum function 
total = df["Quantity"].sum()
#print(total)
# and creating a new dataframe with the total students in all professions as a new row in the dataframe.
# to add it as a row in the dataframe for better visualization in the bar chart
df1 = pd.DataFrame({
    "Profession" : ["IT", "Marketing" ,"Finance","Total"],  
    "Quantity" : [120,70,20, total]
})
# Same styling as we did in last file but added a new Color for Total 
Bar_Chart = px.bar(df1, x = "Profession" , y="Quantity" ,
                    title="Bar_Chart" ,color="Profession",
                    color_discrete_sequence = ["Red","Yellow","Orange","Blue"])
# Updating the layout of the bar chart to make it visually appealing and consistent with the theme of the app
Bar_Chart.update_layout(plot_bgcolor="#111111", paper_bgcolor="#111111", font_color="#1CC040")
Pie_Chart = px.pie(df, names="Profession" , values= "Quantity" ,
                    title="Pie_Chart", color="Profession", 
                    color_discrete_sequence = ["Red","Yellow","Orange"])
# Creating Dash App
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Time to learn about callbacks",
            style={"textAlign" : "center", "color": "DarkBlue" , "font-family": "Arial"}),
    html.Br(),
    html.H2("Enter your Profession to get students in that profession instead of getting percentage in the pie chart ", 
            style={"textAlign" : "center", "color": "Green" , "font-family": "Arial"}),
  html.Div([
     "Enter your Profession (IT , Marketing or Finance):" ,
     # Input component to take user input and link it with the callback function to make the app interactive
     dcc.Input(
            id="Input",
            placeholder="Enter your Profession here to get total students in that profession",
            # Default value for the input box 
            value="IT",
            # Type of input box
            type="text")
]),
    html.Br(),
    html.Div(id="Output" , style={"textAlign" : "center", "color": "DarkBlue" , "font-family": "Arial" ,"bold": "True"}),
    html.Br(),
    html.Br(),
    dcc.Graph(id="Pie_chart", figure=Pie_Chart ,style={"width": "100%", "display": "inline-block"}),
    html.Br(),
    html.H3("Verify the number of students you got from the input box with the bar chart below ",
            style={"textAlign" : "center", "color": "Maroon" , "font-family": "Arial"}),
    dcc.Graph(id="Bar_Chart", figure=Bar_Chart ,style={"width": "100%", "display": "inline-block"})
]) 
@callback(
    Output(component_id="Output", component_property="children"),
    Input(component_id="Input", component_property="value")
)
def update_output_div(input_value):
    total_students = df1[df1["Profession"] == input_value]["Quantity"].sum()
    return f'Total students in {input_value} profession is {total_students}'
if __name__ == "__main__":
    app.run(debug=True)