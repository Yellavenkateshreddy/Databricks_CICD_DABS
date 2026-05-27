df = spark.sql("SELECT count(*) FROM silver_table")
df.write.mode("overwrite").saveAsTable("gold_table")
