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
        n_estimators=100,  # number of trees
        contamination=0.05,  # expected proportion of outliers
        random_state=42  # ensure reproducible results
    )
    model.fit(df)
    return model

def detect_anomalies(model, df):
    """Phát hiện các điểm dữ liệu bất thường"""
    df['anomaly'] = model.predict(df)
    return df[df['anomaly'] == -1]  # -1 indicates an outlier

def main():
    # Load data
    df = load_data()
    
    # Train model
    model = train_anomaly_detector(df)
    
    # Detect anomalies
    anomalies = detect_anomalies(model, df)
    
    # Print results
    if not anomalies.empty:
        print("Detected Anomalies in IoT Data:")
        print(anomalies)
    else:
        print("No anomalies detected.")

if __name__ == "__main__":
    main()