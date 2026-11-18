import os
import sys
import shutil

# Use the current Python interpreter
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from delta.tables import DeltaTable

# Start Spark with Delta Lake
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

spark.sparkContext.setLogLevel("ERROR")

print("Spark started successfully!")

# Delta table storage location
table_path = "student_delta"

# Reset the demo table for a fresh run
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

print("Original Student Data:")
df.show()

# Create Delta Lake table
df.write.format("delta").mode("overwrite").save(table_path)

print("Delta Lake table created successfully!")

# Load the Delta table
delta_table = DeltaTable.forPath(spark, table_path)

# Update student marks
delta_table.update(
    condition="id = 1",
    set={"marks": "95"}
)

print("Updated Student Data:")
delta_table.toDF().show()

# Display transaction history
print("Transaction History:")
delta_table.history().show(truncate=False)

# Time Travel: Read original version
print("Original Student Data - Version 0:")

old_df = (
    spark.read
    .format("delta")
    .option("versionAsOf", 0)
    .load(table_path)
)

old_df.show()

# Stop Spark
spark.stop()

print("Practical completed successfully!")
