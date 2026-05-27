df = spark.sql("SELECT * FROM bronze_table")
df.write.mode("overwrite").saveAsTable("silver_table")
