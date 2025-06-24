import yfinance as yf

# Fetch Tesla stock data
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period="max")

# Reset the index
tesla_data.reset_index(inplace=True)

# Add a Revenue column with sample values for the last 5 rows
# Replace these with actual revenue values if available
revenue_values = [31, 28, 21, 46, 27]
tesla_data['Revenue'] = None  # Initialize the column
tesla_data.loc[tesla_data.index[-5:], 'Revenue'] = revenue_values
tesla_revenue_date = tesla_data[['Date', 'Revenue']]
# Display the last five rows
print(tesla_revenue_date.tail())



