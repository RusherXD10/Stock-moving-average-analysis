import pandas as pd
data = pd.read_csv("stocks.csv")

#Here, we are calculating the 5-day Moving Average by using the rolling() function of pandas.
#As we can see, the rolling() function made it easier to calculate the moving average.

data["New Avg"] = data["Close"].rolling(window=5, min_periods=1).mean()
data.loc[data.index < 4, "New Avg"] = pd.NA
print(data)
data.to_csv("stocks.csv", index=False)
