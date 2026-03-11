import pandas as pd
import plotly.express as px
import dash
from dash import dcc,html
# Create dash App
app = dash.Dash()
# Create a dataframe
df = pd.read_excel("..//Dash-Data-Systems-Mastery/data/Equality_Table.xlsx", sheet_name="Equality Data")
#print(df.head())
# to check the columns in the dataframe 
print(df.columns)
# to check the data types of the columns in the dataframe
print(df.dtypes) 
# to check if there are any missing values in the dataframe
print(df.info())
# to check the number of missing values in the dataframe
print(df.isnull().sum())
# to check the number of rows and columns in the dataframe
print(df.shape)
#select the rows where the Equality Score is b/w -10 and 10 (Fair)
df1 = df[(df["Equality Score"] >= -10) & (df["Equality Score"] <= 10)]
Total_Fair = df1["Equality Score"].count()
print(Total_Fair)
# similarly we can select the rows where the Equality Score is b/w -20 and 20 (Unfair)
# But will exclude the rows where the Equality Score is b/w -10 and 10 (Fair) to get the total number of Unfair countries
df2 = df[(df["Equality Score"] >= -20) & (df["Equality Score"] <= 20) 
         & ~((df["Equality Score"] >= -10) & (df["Equality Score"] <= 10))]
Total_Unfair = df2["Equality Score"].count()
print(Total_Unfair)
# Now just minus the total rows from comibe sum of total fair and unfair 
# to get the total number of factories which are very Highly Discriminative (Equality Score < -20 or > 20)
Highly_discriminative = df.shape[0] - (Total_Fair + Total_Unfair)
print(Highly_discriminative)
# Getting unique values from the Factory 
Factory = df["Factory"].unique()
print(Factory)

# Will use factory names as x axis and Equality Score as y axis to create a bar chart to visualize the Equality Score of each factory and to compare them with each other
Bar_Chart = px.bar(df, x = "Equality Class" , y="Factory" , title="Bar_Chart" ,color="Factory", color_discrete_sequence = ["Red","Yellow","Black","Purple"])
# Create a beautiful layout
app.layout=html.Div([
    html.H1("Time to present charts side by side " ,style={"textAlign" : "center", "color": "Maroon" , "font-family": "Arial"}), 
    html.Div([dcc.Graph(id="bar_chart",
              figure=Bar_Chart)], style= {"display" : "inline-block" , "width" : "100%"}),
])
# Styling the main div to center the content
#style={"textAlign" : "center" , "color": "DarkBlue" , "font-family": "Arial"}
if __name__ == "__main__":
  app.run(debug=True)
