from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FunctionalExample").getOrCreate()
sc = spark.sparkContext

# Data: A list of integers
data = [2, 4, 6, 8, 10]

# Parallelize data into an RDD
rdd = sc.parallelize(data)

# FUNCTIONAL PIPELINE:
# 1. Filter: Keep only even numbers (x % 2 == 0)
# 2. Map: Square the remaining numbers (x * x)
# 3. Reduce: Sum the results (a + b)
result = rdd.filter(lambda x: x % 2 == 0) \
            .map(lambda x: x * x) \
            .reduce(lambda a, b: a + b)

print(f"Result: {result}")
# Output will be sum of (2^2, 4^2, 6^2, 8^2, 10^2) -> 220