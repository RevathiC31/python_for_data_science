import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Fetch GameStop stock data
game_stop = yf.Ticker('GME')
game_stop_data = game_stop.history(period="max")
game_stop_data.reset_index(inplace=True)

# Create subplots with shared x-axis
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

# First graph: Open price
fig.add_trace(go.Scatter(x=game_stop_data['Date'], y=game_stop_data['Open'], mode='lines', name='Open Price'), row=1, col=1)

# Second graph: Close price
fig.add_trace(go.Scatter(x=game_stop_data['Date'], y=game_stop_data['Close'], mode='lines', name='Close Price'), row=2, col=1)

# Add range slider and layout
fig.update_layout(
    title='GameStop Stock Data',
    xaxis=dict(rangeslider=dict(visible=True)),
    yaxis_title='US Dollar'
)

fig.show()
