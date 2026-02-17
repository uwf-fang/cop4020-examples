from pyspark.sql import functions as F

# Creating a fluent chain
final_df = (
    raw_sales_df
    .filter(F.col("category") == "Electronics")        # 1. Filter rows
    .withColumn("total_price", F.col("qty") * F.col("price")) # 2. Add a column
    .groupBy("store_id")                               # 3. Group data
    .agg(F.sum("total_price").alias("revenue"))        # 4. Aggregate
    .orderBy(F.desc("revenue"))                         # 5. Sort
    .limit(10)                                          # 6. Take top 10
)

final_df.show()