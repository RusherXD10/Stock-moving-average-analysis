import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("stocks.csv")

#We are visualizing the closing stock price and the 5-day average of the closing stock price using a double line plot.

data.plot(y=["Close","Avg Price"], kind="line", figsize = (15, 5), label = ["Close Price", "5-Day Average"], color = ["blue", "red"])
plt.ylabel("Price[$]")
plt.xlabel("Day")
plt.legend(loc = "upper left")
plt.title("Closing Stock Price vs 5-Day Average")
plt.grid(True)
plt.savefig("closing_stock_price_vs_5_day_average.png")
plt.show()

