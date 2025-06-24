import yfinance as yf

# Download GameStop stock data
gme = yf.Ticker('GME')
gme_data = gme.history(period = "max")
# Reset the index
gme_data.reset_index(inplace=True)
# Add a Revenue column with sample values for the last 5 rows
# Replace these with actual revenue values if available
revenue_values = [1667, 534, 416, 475, 709]
gme_data['Revenue'] = None  # Initialize the column
gme_data.loc[gme_data.index[-5:], 'Revenue'] = revenue_values
gme_revenue_date = gme_data[['Date', 'Revenue']]
# Display the last five rows
print(gme_revenue_date.tail())
