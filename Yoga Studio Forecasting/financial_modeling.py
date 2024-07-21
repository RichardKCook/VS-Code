import pandas as pd

# Load segmented data
df = pd.read_csv('geographic_segmented_data.csv')

# Create a simple financial projection dataframe
data = {
    'Year': [2024, 2025, 2026, 2027, 2028],
    'Revenue': [50000, 75000, 100000, 130000, 160000],
    'Cost': [30000, 45000, 60000, 80000, 100000]
}
financial_df = pd.DataFrame(data)
financial_df['Profit'] = financial_df['Revenue'] - financial_df['Cost']

# Save the financial data
financial_df.to_csv('financial_projections.csv', index=False)

print(financial_df)
