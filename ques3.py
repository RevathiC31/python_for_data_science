import yfinance as yf

# Download GameStop stock data
gme = yf.Ticker('GME')
gme_data = gme.history(period = "max")
# Reset the index
gme_data.reset_index(inplace=True)

# Display the first five rows
print(gme_data.head())
