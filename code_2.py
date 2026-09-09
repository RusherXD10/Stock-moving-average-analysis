import pandas as pd

#We are reading the CSV file named "stocks.csv" and rearranging the columns to a specific order.

data = pd.read_csv("stocks.csv")

#We are interchanging the columns of the data to a specific order.

cols = list(data.columns)
cols[1] , cols[3] = cols[3], cols[1]
cols[0], cols[1] = cols[1], cols[0]
cols[4], cols[0] = cols[0], cols[4]
data = data[cols]

#We are also dropping the first row of the data and renaming the index to "AAPL".

data.drop(0, inplace = True)
data.index.name = "AAPL"

#Finally, we are saving the modified data back to the same CSV file and printing the first 5 rows of the modified data to verify that it has been saved correctly.

filepath = r"C:\Users\exidi\Desktop\project-1\stocks.csv"
data.to_csv(filepath, index=False)
print(data.head(5).to_string())
