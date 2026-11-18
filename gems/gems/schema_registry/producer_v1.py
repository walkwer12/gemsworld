
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

# Kafka configuration
kafka_config = {
    "bootstrap.servers": "localhost:9092",
    "key.serializer": StringSerializer("utf_8")
}

# Schema Registry configuration
schema_registry_conf = {
    "url": "http://localhost:8081"
}

schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# Read Schema V1
with open("schemas/patient_v1.avsc", "r") as f:
    schema_str = f.read()

# Create Avro serializer
avro_serializer = AvroSerializer(
    schema_registry_client,
    schema_str
)

# Add value serializer
kafka_config["value.serializer"] = avro_serializer

# Create producer
producer = SerializingProducer(kafka_config)

# Kafka topic
topic = "healthcare-patients"

# Healthcare records using V1
patients = [
    {
        "patient_id": 101,
        "patient_name": "Rahul",
        "age": 35
    },
    {
        "patient_id": 102,
        "patient_name": "Priya",
        "age": 28
    }
]

# Send records
for patient in patients:
    producer.produce(
        topic=topic,
        key=str(patient["patient_id"]),
        value=patient
    )

    print("Produced V1:", patient)

# Wait for messages
producer.flush()
print("Schema V1 data sent successfully.")
