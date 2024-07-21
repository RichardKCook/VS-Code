import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load geographic data (example: a built-in dataset)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter for a specific region (e.g., United States)
usa = world[world.name == 'United States']

# Load demographic data
demographic_df = pd.read_csv('segmented_data.csv')

# Plot the geographic data
usa.plot()
plt.title('Geographic Analysis')
plt.savefig('geographic_analysis.png')
plt.show()

# Save the combined data
demographic_df.to_csv('geographic_segmented_data.csv', index=False)
