# Create Spark Session
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Practice").getOrCreate()

data = [(1, "Rahul"), (2, "Amit")]
df = spark.createDataFrame(data, ["id", "name"])

df.show()
