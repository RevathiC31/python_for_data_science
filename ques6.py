from ques3 import gme_data

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
# Example GameStop stock DataFrame: gme_data with 'Date' and 'Close' columns
make_graph(gme_data, 'GameStop Stock Price Over Time')