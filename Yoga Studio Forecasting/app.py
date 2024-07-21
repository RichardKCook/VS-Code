from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
plt.switch_backend('Agg')  # Use a non-interactive backend

app = Flask(__name__)

# Function to read specific cells from Excel
def read_excel_data(file_path, sheet_name):
    # Load the specific sheet from the Excel file
    sheet = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

    # Extract revenue and cost data
    revenues = sheet.loc[140:199, 1].values  # Adjust these indices if needed
    costs = sheet.loc[204:263, 1].values     # Adjust these indices if needed

    # Ensure both arrays have the same length
    if len(revenues) != len(costs):
        raise ValueError("Revenues and costs arrays must have the same length")

    # Create a DataFrame
    years = [2025, 2026, 2027, 2028, 2029]
    months = list(range(1, 13)) * len(years)
    year_column = [year for year in years for _ in range(12)]

    data = {
        'Year': year_column,
        'Month': months,
        'Revenue': revenues,
        'Cost': costs
    }

    return pd.DataFrame(data)

# Load the monthly data from Excel
def load_monthly_data():
    file_path = 'Yoga_Studio_Forecast_Updated.xlsx'
    sheet_name = 'Inputs'
    return read_excel_data(file_path, sheet_name)

# Load the monthly data
monthly_df = load_monthly_data()

@app.route('/')
def home():
    try:
        # Calculate mean and standard deviation for each year based on monthly data
        stats = monthly_df.groupby('Year').agg({
            'Revenue': ['mean', 'std'],
            'Cost': ['mean', 'std']
        }).reset_index()
        stats.columns = ['Year', 'Mean Revenue', 'Revenue Std Dev', 'Mean Cost', 'Cost Std Dev']

        return render_template('index.html', monthly_df=monthly_df.to_dict(orient='records'), stats_table=stats.to_html(index=False))
    except Exception as e:
        return str(e)

@app.route('/update_monthly_data', methods=['POST'])
def update_monthly_data():
    try:
        # Reload the monthly data
        global monthly_df
        monthly_df = load_monthly_data()

        # Calculate new stats
        stats = monthly_df.groupby('Year').agg({
            'Revenue': ['mean', 'std'],
            'Cost': ['mean', 'std']
        }).reset_index()
        stats.columns = ['Year', 'Mean Revenue', 'Revenue Std Dev', 'Mean Cost', 'Cost Std Dev']

        # Prepare the updated data for the input forms
        updated_data = {
            'year': monthly_df['Year'].tolist(),
            'month': monthly_df['Month'].tolist(),
            'revenue': monthly_df['Revenue'].tolist(),
            'cost': monthly_df['Cost'].tolist()
        }

        return jsonify({'updated_data': updated_data, 'stats_table': stats.to_html(index=False)})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/update_simulation', methods=['POST'])
def update_simulation():
    try:
        # Get form data
        iterations = int(request.form['iterations'])

        # Load monthly data
        monthly_df = load_monthly_data()

        # Define years for the simulation
        years = monthly_df['Year'].unique()

        # Run Monte Carlo simulation for each month
        all_simulated_data = {year: {'Revenue': [], 'Cost': [], 'Profit': []} for year in years}
        for year in years:
            for month in range(1, 13):
                month_data = monthly_df[(monthly_df['Year'] == year) & (monthly_df['Month'] == month)]
                if month_data.empty:
                    continue
                revenue_mean = month_data['Revenue'].values[0]
                revenue_stddev = month_data['Revenue'].std()
                cost_mean = month_data['Cost'].values[0]
                cost_stddev = month_data['Cost'].std()
                
                # Handle potential NaNs
                revenue_stddev = 0 if np.isnan(revenue_stddev) else revenue_stddev
                cost_stddev = 0 if np.isnan(cost_stddev) else cost_stddev

                simulated_revenues = np.random.normal(revenue_mean, revenue_stddev, iterations)
                simulated_costs = np.random.normal(cost_mean, cost_stddev, iterations)
                simulated_profits = simulated_revenues - simulated_costs
                all_simulated_data[year]['Revenue'].extend(simulated_revenues)
                all_simulated_data[year]['Cost'].extend(simulated_costs)
                all_simulated_data[year]['Profit'].extend(simulated_profits)

        # Save the simulation results for each year
        simulation_df = pd.concat({year: pd.DataFrame(data) for year, data in all_simulated_data.items()}, axis=1)
        simulation_df.to_csv('monte_carlo_simulation.csv', index=False)

        # Calculate key statistics for each year
        stats_data = []
        for year in years:
            simulated_profits = all_simulated_data[year]['Profit']
            stats = {
                'Year': year,
                'Mean Profit': np.mean(simulated_profits),
                'Median Profit': np.median(simulated_profits),
                'Standard Deviation': np.std(simulated_profits),
                '5th Percentile': np.percentile(simulated_profits, 5),
                '50th Percentile': np.percentile(simulated_profits, 50),
                '95th Percentile': np.percentile(simulated_profits, 95)
            }
            stats_data.append(stats)
        
        stats_df = pd.DataFrame(stats_data)
        stats_df.to_csv('monte_carlo_statistics.csv', index=False)

        # Ensure 'static' directory exists
        if not os.path.exists('static'):
            os.makedirs('static')

        # Plot the combined projections with confidence intervals for yearly data
        years = [stat['Year'] for stat in stats_data]
        mean_profits = [stat['Mean Profit'] for stat in stats_data]
        lower_bound = [stat['5th Percentile'] for stat in stats_data]
        upper_bound = [stat['95th Percentile'] for stat in stats_data]

        plt.figure(figsize=(10, 5))
        plt.fill_between(years, lower_bound, upper_bound, color='b', alpha=0.1)
        plt.plot(years, mean_profits, 'b-', label='Mean Profit')
        plt.xlabel('Year')
        plt.ylabel('Profit')
        plt.title('Monte Carlo Simulation of Monthly Profits Over Time')
        plt.legend()
        plt.savefig('static/monte_carlo_combined_yearly.png')
        plt.close()

        # Return key statistics only
        stats_html = stats_df.to_html(index=False)
        return jsonify({'stats_table': stats_html})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
