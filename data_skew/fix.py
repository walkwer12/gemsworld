from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, sum
import time

# Create Spark session
spark = (
    SparkSession.builder
    .appName("FixedSpark")
    .master("local[4]")
    .config("spark.sql.shuffle.partitions", "8")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

print("====================================")
print("Spark application started!")
print("====================================")

# Create 5 million records
df = spark.range(5_000_000)

print("Dataset created!")

# Create intentionally skewed data
df = df.withColumn(
    "key",
    when(
        col("id") < 4_500_000,
        lit(0)
    ).otherwise(
        (col("id") % 999) + 1
    )
)

print("Skewed dataset created!")

# FIX: Apply salting to distribute the skewed key
df = df.withColumn(
    "salt",
    when(
        col("key") == 0,
        (col("id") % 10).cast("int")
    ).otherwise(
        lit(0)
    )
)

print("\nRunning salted GROUP BY...")

# First aggregation: distribute records using key and salt
partial_result = df.groupBy("key", "salt").count()

print("\nDistribution after salting:")
partial_result.filter(
    col("key") == 0
).orderBy("salt").show(10)

# Second aggregation: combine results using original key
result = partial_result.groupBy("key").agg(
    sum("count").alias("count")
)

# Execute Spark job
print("\nFinal aggregated results:")
result.orderBy("key").show(10)

print("\nFIXED JOB COMPLETED!")

print("====================================")
print("Open Spark UI:")
print("http://localhost:4040")
print("====================================")

# Keep Spark running for Spark UI inspection
time.sleep(120)

spark.stop()