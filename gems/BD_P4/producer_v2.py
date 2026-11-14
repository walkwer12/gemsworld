from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

# Connect to Schema Registry
schema_registry_conf = {'url': 'http://localhost:8081'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# Load V2 schema
with open('schemas/patient_v2.avsc', 'r') as f:
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
    {'patient_id': 103, 'patient_name': 'Amit', 'age': 42, 'blood_group': 'A+'},
    {'patient_id': 104, 'patient_name': 'Sneha', 'age': 31, 'blood_group': 'O+'}
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
print("V2 messages sent successfully!")