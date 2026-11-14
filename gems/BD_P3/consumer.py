
from kafka import KafkaConsumer
import json

# Connect to the Kafka topic
consumer = KafkaConsumer(
    "student-events",
    bootstrap_servers=[
        "localhost:29092",
        "localhost:39092",
        "localhost:49092"
    ],
    auto_offset_reset="earliest",
    group_id="student-consumer-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Consumer started...")
print("Waiting for messages...\n")

# Receive messages continuously
for message in consumer:
    print(
        "Received:",
        message.value,
        "| Partition:",
        message.partition,
        "| Offset:",
        message.offset
    )
