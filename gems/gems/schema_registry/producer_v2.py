
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

# Read Schema V2
with open("schemas/patient_v2.avsc", "r") as f:
    schema_str = f.read()

# Create Avro serializer
avro_serializer = AvroSerializer(
    schema_registry_client,
    schema_str
)

# Add serializer
kafka_config["value.serializer"] = avro_serializer

# Create producer
producer = SerializingProducer(kafka_config)

# Same Kafka topic
topic = "healthcare-patients"

# Healthcare records using V2
patients = [
    {
        "patient_id": 103,
        "patient_name": "Amit",
        "age": 42,
        "blood_group": "A+"
    },
    {
        "patient_id": 104,
        "patient_name": "Sneha",
        "age": 31,
        "blood_group": "O+"
    }
]

# Send records
for patient in patients:
    producer.produce(
        topic=topic,
        key=str(patient["patient_id"]),
        value=patient
    )

    print("Produced V2:", patient)

producer.flush()
print("Schema V2 data sent successfully.")
