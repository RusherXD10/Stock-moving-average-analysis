import pandas as pd
data = pd.read_csv("stocks.csv")
data["Avg Price"] = pd.NA

#We are calculating the 5-day average of the "Close" price and storing it in a new column named "Avg Price".
#The calculation starts from the 5th row (index 4) and continues until the end of the data.

for i in range(4,len(data)):
    avg_5d = data.iloc[i-4:i+1, 4].mean()
    data.loc[i, "Avg Price"] = avg_5d
print(data)
data.to_csv("stocks.csv", index=False)
