import dash
from dash import dcc, html

app = dash.Dash()

app.layout= html.Div(
    html.H1("Hello")
)

if __name__ == "__main__":
    app.run(debug=True)