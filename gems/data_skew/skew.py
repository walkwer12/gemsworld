from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit
import time

# Create a Spark session
spark = (
    SparkSession.builder
    .appName("SparkSkewPractical")
    .master("local[4]")
    .config("spark.sql.shuffle.partitions", "8")
    .getOrCreate()
)

# Reduce unnecessary messages in the terminal
spark.sparkContext.setLogLevel("WARN")

print("====================================")
print("Spark application started!")
print("====================================")

# Create 5 million records
number_of_records = 5_000_000

df = spark.range(number_of_records)

print("Dataset created!")

# Create intentionally skewed data
# About 90% of records get key = 0
skewed_df = df.withColumn(
    "key",
    when(
        col("id") < number_of_records * 0.90,
        lit(0)
    ).otherwise(
        (col("id") % 999) + 1
    )
)

print("Skewed dataset created!")

# Show distribution of keys
print("\nKey distribution:")

skewed_df.groupBy("key").count().orderBy(
    col("count").desc()
).show(10)

# Perform GROUP BY
print("\nStarting GROUP BY...")

result = skewed_df.groupBy("key").count()

# Execute Spark job
result.collect()

print("\nGROUP BY completed!")

print("====================================")
print("Open Spark UI:")
print("http://localhost:4040")
print("====================================")

# Keep Spark running for Spark UI inspection
time.sleep(120)

spark.stop()
