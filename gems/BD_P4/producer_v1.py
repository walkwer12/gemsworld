import json
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

# Connect to Schema Registry
schema_registry_conf = {'url': 'http://localhost:8081'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# Load V1 schema
with open('schemas/patient_v1.avsc', 'r') as f:
    schema_str = f.read()

# Create Avro Serializer
avro_serializer = AvroSerializer(
    schema_registry_client,
    schema_str
)

# Configure Kafka Producer
producer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'key.serializer': StringSerializer('utf_8'),
    'value.serializer': avro_serializer
}

producer = SerializingProducer(producer_conf)

# Patient records
patients = [
    {'patient_id': 101, 'patient_name': 'Rahul', 'age': 35},
    {'patient_id': 102, 'patient_name': 'Priya', 'age': 28}
]

# Send records to Kafka
for patient in patients:
    producer.produce(
        topic='healthcare-patients',
        key=str(patient['patient_id']),
        value=patient
    )
    print("Sent:", patient)

producer.flush()
print("V1 messages sent successfully!")