import sqlite3
import numpy as np
import pandas as pd

# Create sample data
np.random.seed(42)
n_samples = 1000

# Create normal data
temperature = np.random.normal(25, 2, n_samples)  # Average temperature 25°C
humidity = np.random.normal(60, 5, n_samples)     # Average humidity 60%

# Add some outliers
anomaly_indices = np.random.choice(n_samples, 50, replace=False)
temperature[anomaly_indices] += np.random.normal(10, 2, 50)
humidity[anomaly_indices] += np.random.normal(20, 5, 50)

# Create DataFrame
df = pd.DataFrame({
    'temperature': temperature,
    'humidity': humidity
})

# Connect to database
conn = sqlite3.connect('iot_data.db')

# Create table and save data
df.to_sql('sensor_data', conn, if_exists='replace', index=False)
conn.close()

print("Database created successfully with sample data!") 