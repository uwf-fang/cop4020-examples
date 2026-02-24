import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder.appName("FunctionalExample").getOrCreate()
val sc = spark.sparkContext

// Data: A sequence of integers
val data = Seq(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

// Parallelize data into an RDD
val rdd = sc.parallelize(data)

// FUNCTIONAL PIPELINE:
// Uses '=>' (Arrow Syntax) as described in Source [1]
val result = rdd.filter(x => x % 2 == 0)  // Keep evens
                .map(x => x * x)          // Square them
                .reduce((a, b) => a + b)  // Sum them

// ALTERNATIVE (More "Functional" Placeholder Syntax):
// val result = rdd.filter(_ % 2 == 0).map(x => x * x).reduce(_ + _)

println(s"Result: $result")
