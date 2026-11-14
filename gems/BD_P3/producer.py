
from kafka import KafkaProducer
import json
import time

# Connect to the three Kafka brokers
producer = KafkaProducer(
    bootstrap_servers=[
        "localhost:29092",
        "localhost:39092",
        "localhost:49092"
    ],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Send 10 student messages
for i in range(10):
    message = {
        "student_id": i + 1,
        "name": f"Student-{i + 1}",
        "course": "Data Science",
        "message": f"Hello from student {i + 1}"
    }

    producer.send("student-events", value=message)
    print("Produced:", message)
    time.sleep(1)

# Ensure all messages are delivered
producer.flush()
producer.close()

print("All messages sent successfully!")
