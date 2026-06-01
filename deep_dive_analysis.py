import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")

print(df.head())

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
total_orders = len(df)

print("\nKPI RESULTS")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Total Orders:", total_orders)

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.show()
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(6,4))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.show()