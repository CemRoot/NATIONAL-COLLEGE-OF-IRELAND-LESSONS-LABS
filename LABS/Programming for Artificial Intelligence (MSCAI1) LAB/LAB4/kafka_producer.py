import pandas as pd
import time
from kafka import KafkaProducer
import json

# Load the Iris dataset
iris_data = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    header=None,
    names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
)

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Function to stream data to Kafka
def stream_iris_to_kafka(data, delay=1):
    for index, row in data.iterrows():
        producer.send('iris_data', value=row.to_dict())
        print(f"Sent data to Kafka: {row.to_dict()}")
        time.sleep(delay)  # Simulate a delay

# Stream data
stream_iris_to_kafka(iris_data, delay=1)

# Close the producer
producer.close()