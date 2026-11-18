
from pyflink.common import Types, WatermarkStrategy, Duration
from pyflink.common.watermark_strategy import TimestampAssigner
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.output_tag import OutputTag
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.common.time import Time

import time

# Create the Flink execution environment
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# Delivery events: order status and event timestamp (milliseconds)
events = [
    ("Picked up", 1000),
    ("At restaurant", 8000),
    ("Delivered", 22000),
    ("Order confirmed", 3000)
]

# Create a DataStream from the collection
data = env.from_collection(
    events,
    type_info=Types.TUPLE([Types.STRING(), Types.LONG()])
)

# Add a delay between events for watermark demonstration
def delay_events(event):
    time.sleep(1)
    return event

data = data.map(
    delay_events,
    output_type=Types.TUPLE([Types.STRING(), Types.LONG()])
)

# Custom timestamp assigner
class DeliveryTimestampAssigner(TimestampAssigner):

    def extract_timestamp(self, event, record_timestamp):
        return event[1]

# Allow events to arrive up to 2 seconds out of order
watermarks = WatermarkStrategy.for_bounded_out_of_orderness(
    Duration.of_seconds(2)
).with_timestamp_assigner(DeliveryTimestampAssigner())

# Assign event timestamps and watermarks
stream = data.assign_timestamps_and_watermarks(watermarks)

# Side output tag for late events
late_tag = OutputTag(
    "late_events",
    Types.TUPLE([Types.STRING(), Types.LONG()])
)

# Create 10-second tumbling event-time windows
windowed = (
    stream
    .key_by(
        lambda event: "delivery",
        key_type=Types.STRING()
    )
    .window(TumblingEventTimeWindows.of(Time.seconds(10)))
    .side_output_late_data(late_tag)
)

# Print events included in each main window
main = windowed.reduce(
    lambda a, b: a,
    output_type=Types.TUPLE([Types.STRING(), Types.LONG()])
)

# Retrieve late events from the side output
late = main.get_side_output(late_tag)

# Print the main output and late-event output
main.print()
late.print()

# Execute the Flink job
env.execute("Food Delivery Late Data")
