import pandas as pd
import yfinance as yf

#Downlading the stock data for Apple (AAPL) for the last 2 months using yfinance

data = yf.download("AAPL", period = "2mo")

#We are saving the data to a CSV file named "stocks.csv" in the specified directory

filepath = r"C:\Users\exidi\Desktop\project-1\stocks.csv"
data.to_csv(filepath, index=False)
print("File saved successfully!")

#The following code reads the CSV file and prints the first 5 rows of the data to verify that it has been saved correctly.
print(data.head())