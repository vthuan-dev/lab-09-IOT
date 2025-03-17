import sqlite3
import numpy as np
import pandas as pd

# Tạo dữ liệu mẫu
np.random.seed(42)
n_samples = 1000

# Tạo dữ liệu bình thường
temperature = np.random.normal(25, 2, n_samples)  # Nhiệt độ trung bình 25°C
humidity = np.random.normal(60, 5, n_samples)     # Độ ẩm trung bình 60%

# Thêm một số điểm bất thường
anomaly_indices = np.random.choice(n_samples, 50, replace=False)
temperature[anomaly_indices] += np.random.normal(10, 2, 50)
humidity[anomaly_indices] += np.random.normal(20, 5, 50)

# Tạo DataFrame
df = pd.DataFrame({
    'temperature': temperature,
    'humidity': humidity
})

# Kết nối với database
conn = sqlite3.connect('iot_data.db')

# Tạo bảng và lưu dữ liệu
df.to_sql('sensor_data', conn, if_exists='replace', index=False)
conn.close()

print("Database created successfully with sample data!") 