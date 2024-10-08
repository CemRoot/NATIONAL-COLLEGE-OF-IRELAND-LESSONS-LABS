from kafka import KafkaConsumer
import json

# Create Kafka consumer
consumer = KafkaConsumer(
    'iris_data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='iris-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Function to process incoming data
def process_data(data):
    print(f"Processing data: {data}")

# Consume messages
try:
    for message in consumer:
        process_data(message.value)
except KeyboardInterrupt:
    print("Stopping consumer...")

# Close the consumer
consumer.close()