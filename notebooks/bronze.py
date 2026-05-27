df = spark.range(10)
df.write.mode("overwrite").saveAsTable("bronze_table")
display(df)