import pandas as pd
from sklearn.linear_model import LinearRegression

# Load financial data
financial_df = pd.read_csv('financial_projections.csv')

# Example data: marketing spend vs sales
marketing_spend = [[1000], [2000], [3000], [4000], [5000]]
sales = [15000, 25000, 35000, 45000, 55000]

# Create a linear regression model
model = LinearRegression()
model.fit(marketing_spend, sales)

# Predict sales for a new marketing spend
new_spend = [[6000]]
predicted_sales = model.predict(new_spend)

# Save the sales projections
sales_projections = pd.DataFrame({
    'Marketing Spend': [1000, 2000, 3000, 4000, 5000, 6000],
    'Sales': sales + [predicted_sales[0]]
})
sales_projections.to_csv('sales_projections.csv', index=False)

print(f'Predicted Sales for ${new_spend[0][0]} marketing spend: ${predicted_sales[0]}')
