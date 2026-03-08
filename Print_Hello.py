# importing the necessary dependencies(libraries)
import dash
from dash import dcc, html
# Create dash app
app = dash.Dash()
# Create App layout
app.layout= html.Div(
    html.H1("Hello")
)
# Run the App
if __name__ == "__main__":
    app.run(debug=True)