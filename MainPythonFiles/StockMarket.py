import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stockMarket_data.csv")


df['date'] = pd.to_datetime(df['date'])


df['daily_return'] = df['close'].pct_change()

plt.plot(df['date'], df['close'])
plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.show()
