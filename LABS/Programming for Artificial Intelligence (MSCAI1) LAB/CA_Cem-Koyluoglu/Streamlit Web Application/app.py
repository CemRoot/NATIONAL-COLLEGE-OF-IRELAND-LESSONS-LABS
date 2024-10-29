from flask import Flask, jsonify
import pandas as pd
from kafka import KafkaConsumer
import json

app = Flask(__name__)


# Read and return cleaned weather data
@app.route('/data', methods=['GET'])
def get_cleaned_data():
    try:
        # Load data from file in data folder
        data = pd.read_csv(
            r'C:\Users\eminc\OneDrive\Desktop\NATIONAL-COLLEGE-OF-IRELAND-LESSONS-LABS\LABS\Programming for Artificial Intelligence (MSCAI1) LAB\CA_Cem-Koyluoglu\GlobalWeatherRepository.csv')
        return jsonify(data.to_dict(orient="records")) # Return data as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500 # Return error message with status code 500


# Providing live weather data from Kafka
@app.route('/live', methods=['GET'])
def get_live_data():
    consumer = KafkaConsumer(
        'global_weather',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    live_data = []
    for message in consumer:
        live_data.append(message.value)
        if len(live_data) >= 5:
            break
    return jsonify(live_data)


if __name__ == '__main__':
    app.run(debug=True)
