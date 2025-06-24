"""
    Question 1: Use yfinance to Extract Stock Data

    Reset the index, save, and display the first five rows
    of the tesla_data dataframe using the head function.
    Upload a screenshot of the results and code from the beginning
    of Question 1 to the results below.
"""
import yfinance as yf
tesla= yf.Ticker('TSLA')
telsa_data = tesla.history(period = "max")
# Reset the index
telsa_data.reset_index(inplace=True)

# Display the first five rows
print(telsa_data.head())
