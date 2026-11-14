from confluent_kafka import DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer

# Connect to Schema Registry
schema_registry_conf = {
    "url": "http://localhost:8081"
}

schema_registry_client = SchemaRegistryClient(
    schema_registry_conf
)

# Load V2 as the reader schema
with open("schemas/patient_v2.avsc", "r") as f:
    schema_str = f.read()

# Configure Consumer
consumer_conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "healthcare-consumer",
    "auto.offset.reset": "earliest",
    "key.deserializer": StringDeserializer("utf_8")
}

# Create Avro Deserializer using V2 reader schema
avro_deserializer = AvroDeserializer(
    schema_registry_client,
    schema_str
)

consumer_conf["value.deserializer"] = avro_deserializer

# Create Consumer
consumer = DeserializingConsumer(consumer_conf)

# Subscribe to topic
consumer.subscribe(["healthcare-patients"])

print("Consumer started...")
print("Reading healthcare records...\n")

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print("Consumer error:", msg.error())
            continue

        patient = msg.value()

        print("Received Patient:")
        print(patient)
        print("------------------------")

except KeyboardInterrupt:
    print("Consumer stopped.")

finally:
    consumer.close()