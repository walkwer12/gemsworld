
import os
import sys
import shutil

# Use the current Python interpreter
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from delta.tables import DeltaTable

# Create Delta Lake Spark session
builder = (
    SparkSession.builder
    .appName("DeltaLakeDemo")
    .master("local[*]")
    .config(
        "spark.sql.extensions",
        "io.delta.sql.DeltaSparkSessionExtension"
    )
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog"
    )
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()
spark.sparkContext.setLogLevel("WARN")

print("Spark started successfully!")

# Define Delta table location
table_path = os.path.abspath("student_delta_table")

# Remove previous table to start a fresh experiment
if os.path.exists(table_path):
    shutil.rmtree(table_path)

# Create sample student data
data = [
    (1, "ABC", 90),
    (2, "DEF", 88),
    (3, "GHI", 75),
    (4, "JKL", 90),
    (5, "MNO", 88),
    (6, "PQR", 75)
]

df = spark.createDataFrame(
    data,
    ["id", "name", "marks"]
)

print("\nOriginal Student Data:")
df.show()

# Write data in Delta format
df.write.format("delta").save(table_path)

print("\nDelta Lake table created successfully!")

# Read the Delta table
delta_df = spark.read.format("delta").load(table_path)

print("\nReading Delta Table:")
delta_df.show()

# Update student marks using an ACID transaction
delta_table = DeltaTable.forPath(spark, table_path)

delta_table.update(
    condition="id = 2",
    set={"marks": "95"}
)

print("\nStudent marks updated successfully!")

# Display updated data
print("\nUpdated Student Data:")
spark.read.format("delta").load(table_path).show()

# Demonstrate Time Travel
print("\nOriginal Data using Time Travel (Version 0):")

old_df = (
    spark.read.format("delta")
    .option("versionAsOf", 0)
    .load(table_path)
)

old_df.show()

# Display transaction history
print("\nDelta Lake Transaction History:")
delta_table.history().show(truncate=False)

print("\nPRACTICAL 2 COMPLETED!")

spark.stop()
