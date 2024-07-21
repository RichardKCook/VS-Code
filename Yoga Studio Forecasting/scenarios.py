import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load financial data
financial_df = pd.read_csv('financial_projections.csv')

# Define parameters for simulation
revenue_mean = financial_df['Revenue'].mean()
revenue_stddev = financial_df['Revenue'].std()
iterations = 1000

# Run Monte Carlo simulation
simulated_revenues = np.random.normal(revenue_mean, revenue_stddev, iterations)

# Save the simulation results
simulation_df = pd.DataFrame(simulated_revenues, columns=['Simulated Revenue'])
simulation_df.to_csv('monte_carlo_simulation.csv', index=False)

# Plot the distribution of simulated revenues
plt.hist(simulated_revenues, bins=50, edgecolor='k')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.title('Monte Carlo Simulation of Revenues')
plt.savefig('monte_carlo_simulation.png')
plt.show()
