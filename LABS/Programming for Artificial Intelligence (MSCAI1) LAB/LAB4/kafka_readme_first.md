# Iris Veri Seti için Kafka Üretici ve Tüketici

Bu proje, Iris veri setinden veri akışı sağlamak ve bu verileri tüketmek için Apache Kafka'nın nasıl kullanılacağını göstermektedir. Proje, iki ana betik içerir: `kafka_producer.py` ve `kafka_consumer.py`.

## Gereksinimler

- Python 3.x
- Apache Kafka
- Gerekli Python paketleri: `pandas`, `kafka-python`, `json`

## Kurulum

1. **Python paketlerini yükleyin**:
    ```sh
    pip install pandas kafka-python
    ```

2. **Kafka'yı başlatın**:
    Kafka'nın yerel makinenizde çalıştığından emin olun. Kafka'yı başlatmak için aşağıdaki komutları kullanabilirsiniz:
    ```sh
    # Zookeeper'ı başlatın
    zookeeper-server-start.sh config/zookeeper.properties

    # Kafka broker'ını başlatın
    kafka-server-start.sh config/server.properties
    ```

3. **Kafka Konusu Oluşturun**:
    `iris_data` adında bir Kafka konusu oluşturun:
    ```sh
    kafka-topics.sh --create --topic iris_data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
    ```

## kafka_producer.py

Bu betik, Iris veri setini okur ve verileri `iris_data` adlı bir Kafka konusuna akıtır.

### Kod Açıklaması

1. **İçe Aktarımlar**:
    ```python
    import pandas as pd
    import time
    from kafka import KafkaProducer
    import json
    ```

2. **Iris veri setini yükleyin**:
    ```python
    iris_data = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
        header=None,
        names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    )
    ```

3. **Kafka üreticisi oluşturun**:
    ```python
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    ```

4. **Verileri Kafka'ya akıtmak için fonksiyon**:
    ```python
    def stream_iris_to_kafka(data, delay=1):
        for index, row in data.iterrows():
            producer.send('iris_data', value=row.to_dict())
            print(f"Sent data to Kafka: {row.to_dict()}")
            time.sleep(delay)  # Simulate a delay
    ```

5. **Verileri akıtın**:
    ```python
    stream_iris_to_kafka(iris_data, delay=1)
    ```

6. **Üreticiyi kapatın**:
    ```python
    producer.close()
    ```

## kafka_consumer.py

Bu betik, `iris_data` adlı Kafka konusundan veri tüketir ve işler.

### Kod Açıklaması

1. **İçe Aktarımlar**:
    ```python
    from kafka import KafkaConsumer
    import json
    ```

2. **Kafka tüketicisi oluşturun**:
    ```python
    consumer = KafkaConsumer(
        'iris_data',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='iris-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    ```

3. **Gelen verileri işlemek için fonksiyon**:
    ```python
    def process_data(data):
        print(f"Processing data: {data}")
    ```

4. **Mesajları tüketin**:
    ```python
    try:
        for message in consumer:
            process_data(message.value)
    except KeyboardInterrupt:
        print("Stopping consumer...")
    ```

5. **Tüketiciyi kapatın**:
    ```python
    consumer.close()
    ```

## Özet

- **kafka_producer.py**: Iris veri setini okur ve her satırı `iris_data` adlı Kafka konusuna akıtır.
- **kafka_consumer.py**: `iris_data` adlı Kafka konusundan mesajları tüketir ve işler.

Bu proje, Kafka'nın Python kullanarak veri akışı ve tüketimi için temel kullanımını göstermektedir. Üretici betiği verileri bir Kafka konusuna akıtır ve tüketici betiği bu konudan verileri okur ve işler.