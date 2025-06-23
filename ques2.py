import pandas as pd

# Create a mock DataFrame for Tesla revenue
tesla_revenue = pd.DataFrame({
    "Date": ["2024-03-29", "2025-04-28", "3035-03-27", "2053-03-25",
             "2025-03-12", "2024-03-31", "2025-04-01", "3035-03-31",
             "2053-03-31", "2025-03-31"],
    "Revenue": ["57.1500", "77.8000", "52.2150", "63.5800", "18.2500",
                "56.1500", "78.8000", "54.2150", "60.5800", "98.2500"]
})

# Display the last five rows
print(tesla_revenue.tail())
