import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("supermarket_sales.csv")


df['date'] = pd.to_datetime(df['date'])


daily_sales = df.groupby('date')['total_sales'].sum()

plt.figure()
daily_sales.plot()
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()

# -----------------------------------
# 2. Best-Selling Product Categories
# -----------------------------------
top_products = df.groupby('product_category')['units_sold'].sum().sort_values(ascending=False)

plt.figure()
top_products.plot(kind='bar')
plt.title("Best-Selling Product Categories")
plt.xlabel("Product Category")
plt.ylabel("Units Sold")
plt.show()


branch_sales = df.groupby('branch')['total_sales'].sum()

plt.figure()
branch_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Distribution by Branch")
plt.ylabel("")
plt.show()
