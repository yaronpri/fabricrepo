# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "522dfb6a-4029-4a5f-9cc8-07c1c3479ec0",
# META       "default_lakehouse_name": "lakenotebook",
# META       "default_lakehouse_workspace_id": "d09b710d-a4fe-4e18-aeaf-5d9a62d2ce0b",
# META       "known_lakehouses": [
# META         {
# META           "id": "522dfb6a-4029-4a5f-9cc8-07c1c3479ec0"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
print('yarin')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM lakenotebook.publicholidays LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
