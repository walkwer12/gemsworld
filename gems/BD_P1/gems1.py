


















































































"""
P1

skew.py
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


============================

fix.py
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

"""





















