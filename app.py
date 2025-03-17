import sqlite3
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def load_data():
    """Tải dữ liệu từ database SQLite"""
    conn = sqlite3.connect('iot_data.db')
    query = "SELECT temperature, humidity FROM sensor_data"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def train_anomaly_detector(df):
    """Huấn luyện mô hình phát hiện bất thường"""
    model = IsolationForest(
        n_estimators=100,  # số lượng cây trong rừng
        contamination=0.05,  # tỉ lệ dữ liệu bất thường dự kiến
        random_state=42  # đảm bảo kết quả reproducible
    )
    model.fit(df)
    return model

def detect_anomalies(model, df):
    """Phát hiện các điểm dữ liệu bất thường"""
    df['anomaly'] = model.predict(df)
    return df[df['anomaly'] == -1]  # -1 chỉ ra điểm dữ liệu bất thường

def main():
    # Tải dữ liệu
    df = load_data()
    
    # Huấn luyện mô hình
    model = train_anomaly_detector(df)
    
    # Phát hiện bất thường
    anomalies = detect_anomalies(model, df)
    
    # In kết quả
    if not anomalies.empty:
        print("Detected Anomalies in IoT Data:")
        print(anomalies)
    else:
        print("No anomalies detected.")

if __name__ == "__main__":
    main()