import pandas as pd
import numpy as np

customers = pd.read_csv("Customers.csv")
sales = pd.read_csv("Sales.csv")
support = pd.read_csv("Support.csv")

customers.columns = customers.columns.str.replace(" ", "")
sales.columns = sales.columns.str.replace(" ", "")
support.columns = support.columns.str.replace(" ", "")

print(customers.shape, sales.shape, support.shape)
print(customers.columns)
print(sales.columns)
print(support.columns)

print(customers.isnull().sum())
print(sales.isnull().sum())
print(support.isnull().sum())

price_array = sales['Price'].to_numpy()
sales['DiscountedPrice'] = price_array * 0.90

sales['Revenue'] = sales['Quantity'] * sales['Price']

sales['OrderDate'] = pd.to_datetime(sales['OrderDate'])
customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])

jan_orders = sales[sales['OrderDate'].dt.month == 1]
print(jan_orders)

print(sales.iloc[:10])

north_customers = customers[customers['Region'] == "North"]
print(north_customers)

high_value_orders = sales[sales['Revenue'] > 10000]
print(high_value_orders)

customers_sorted = customers.sort_values('SignupDate')
sales_sorted = sales.sort_values('Revenue', ascending=False)

sales_temp = sales.merge(customers[['CustomerID', 'Region']],
                         on='CustomerID',
                         how='left')

avg_revenue_region = sales_temp.groupby('Region')['Revenue'].mean()
print(avg_revenue_region)

avg_resolution_issue = support.groupby('IssueType')['ResolutionTime'].mean()
print(avg_resolution_issue)

customers['Age'] = customers['Age'].fillna(customers['Age'].median())

merged = customers.merge(sales, on='CustomerID', how='left')
merged = merged.merge(support, on='CustomerID', how='left')

clv = merged.groupby('CustomerID')['Revenue'].sum().reset_index()
clv = clv.rename(columns={'Revenue': 'CLV'})

avg_resolution = merged.groupby('CustomerID')['ResolutionTime'].mean().reset_index()
avg_resolution = avg_resolution.rename(columns={'ResolutionTime': 'AvgResolutionTime'})

merged = merged.merge(clv, on='CustomerID', how='left')
merged = merged.merge(avg_resolution, on='CustomerID', how='left')

merged.to_csv("Cleaned_Data.csv", index=False)

print("Data wrangling complete. File saved as Cleaned_Data.csv")
