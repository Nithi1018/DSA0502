import pandas as pd

# Assuming you have a DataFrame named sales_data
# Replace this with your actual DataFrame

# Sample data
data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
    'Item': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 150, 120, 200, 180]
}

sales_data = pd.DataFrame(data)

# Convert 'Date' to datetime format (if it's not already in that format)
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Create a Pivot table
pivot_table = pd.pivot_table(sales_data, values='Sales', index='Item', aggfunc=['min', 'max'])

# Display the Pivot table
print("Pivot Table:")
print(pivot_table)

# Find the maximum and minimum sale values for each item
max_sales = pivot_table['max']['Sales']
min_sales = pivot_table['min']['Sales']

# Display the results
print("\nMaximum Sale Values:")
print(max_sales)

print("\nMinimum Sale Values:")
print(min_sales)
