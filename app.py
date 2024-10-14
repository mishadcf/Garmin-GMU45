import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from datetime import datetime
import plotly.express as px 
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the target date (March 1st, 2025)
target_date = datetime(2025, 3, 1)

# Function to calculate time difference
def calculate_time_remaining():
    now = datetime.now()
    delta = target_date - now
    return delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds % 60



# Create app layout
app.layout = html.Div(style={'backgroundColor': '#F9F9F9', 'padding': '20px'}, children=[
    html.H1("Garmin Running Data Dashboard", style={'textAlign': 'center', 'color': '#333', 'font-family': 'Arial'}),
    
    # Countdown Widget Section
    html.Div(children=[
        html.H2("Countdown to Winter Green Man Ultra", 
                style={'textAlign': 'center', 'color': '#555', 'font-family': 'Arial', 'marginBottom': '10px'}),
        
        # Countdown timer text
        html.Div(id="countdown-timer", 
                 style={
                     'textAlign': 'center',
                     'fontSize': '36px',
                     'color': '#FF5733',
                     'backgroundColor': '#ffffff',
                     'padding': '20px',
                     'borderRadius': '10px',
                     'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)',
                     'width': '50%',
                     'margin': '0 auto'
                 }),
        
        # Interval updates every second
        dcc.Interval(id='interval-component', interval=1000, n_intervals=0)  
    ], style={
        'backgroundColor': '#FFFBF0',  # Light background to contrast timer
        'borderRadius': '10px',
        'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)',
        'padding': '30px',
        'margin': '20px auto',
        'width': '60%',
    }),

    # Row of Metrics: Total Distance, Total Time, Average Pace
    html.Div(children=[
        html.Div([
            html.H2("Total Distance", style={'textAlign': 'center', 'color': '#555'}),
            html.P("X miles", style={'textAlign': 'center', 'fontSize': '24px', 'color': '#007BFF'}),
        ], style={
            'backgroundColor': 'white',
            'borderRadius': '10px',
            'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)',
            'padding': '20px',
            'margin': '10px',
            'width': '30%',
            'display': 'inline-block',
            'verticalAlign': 'top'
        }),

        html.Div([
            html.H2("Total Time", style={'textAlign': 'center', 'color': '#555'}),
            html.P("X hours", style={'textAlign': 'center', 'fontSize': '24px', 'color': '#28A745'}),
        ], style={
            'backgroundColor': 'white',
            'borderRadius': '10px',
            'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)',
            'padding': '20px',
            'margin': '10px',
            'width': '30%',
            'display': 'inline-block',
            'verticalAlign': 'top'
        }),

        html.Div([
            html.H2("Average Pace", style={'textAlign': 'center', 'color': '#555'}),
            html.P("X min/mile", style={'textAlign': 'center', 'fontSize': '24px', 'color': '#DC3545'}),
        ], style={
            'backgroundColor': 'white',
            'borderRadius': '10px',
            'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)',
            'padding': '20px',
            'margin': '10px',
            'width': '30%',
            'display': 'inline-block',
            'verticalAlign': 'top'
        }),
    ], style={'textAlign': 'center'}),

    # Graph Section (replace this part with the Iframe component)
html.Div([
    html.H2("Weekly Distance Over Time", style={'textAlign': 'center', 'color': '#333', 'marginTop': '40px'}),
    html.Iframe(
        srcDoc=open('weekly_mileage.html', 'r').read(),  # Load the saved HTML file
        style={
            'border': 'none', 
            'width': '100%', 
            'height': '600px',  # Adjust the height as needed
            'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)', 
            'borderRadius': '10px'
        }
    )
], style={
    'backgroundColor': 'white',
    'borderRadius': '10px',
    'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)',
    'padding': '20px',
    'margin': '20px auto',
    'width': '80%',
})

])

# Update countdown timer every second
@app.callback(
    Output('countdown-timer', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_countdown(n):
    days, hours, minutes, seconds = calculate_time_remaining()
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
