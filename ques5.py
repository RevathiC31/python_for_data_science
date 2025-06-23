from ques1 import tesla_data

def make_graph(data, title):
   import matplotlib.pyplot as plt
   plt.figure(figsize=(10, 6))
   plt.plot(data['Date'], data['Close'])
   plt.title(title)
   plt.xlabel('Date')
   plt.ylabel('Closing Price (USD)')
   plt.grid(True)
   plt.xticks(rotation=45)
   plt.tight_layout()
   plt.show()
# Example Tesla stock DataFrame: tesla_data with 'Date' and 'Close' columns
make_graph(tesla_data, 'Tesla Stock Price Over Time')