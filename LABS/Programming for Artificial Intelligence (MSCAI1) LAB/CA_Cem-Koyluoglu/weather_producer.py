import json
import time

import pandas as pd
from kafka import KafkaProducer

# Load data from data folder
data = pd.read_csv(
    r"C:\Users\eminc\OneDrive\Desktop\NATIONAL-COLLEGE-OF-IRELAND-LESSONS-LABS\LABS\Programming for Artificial Intelligence (MSCAI1) LAB\CA_Cem-Koyluoglu\GlobalWeatherRepository.csv"
)

# Defining Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

# Loop that sends each row to Kafka
for index, row in data.iterrows():
    weather_data = {
        "location": row["location_name"],
        "country": row["country"],
        "temperature": row["temperature_celsius"],
        "condition": row["condition_text"],
        "last_updated": row["last_updated"],
    }
    producer.send("global_weather", value=weather_data)
    print(f"Sent data: {weather_data}")
    time.sleep(1)

producer.flush()
producer.close()
print("Producer finished")
