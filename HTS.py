import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# Find the month with the highest total sales
df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M')
monthly_sales = df.groupby('Month').apply(lambda x: (x['Quantity'] * x['Price']).sum())

best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()
print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")
