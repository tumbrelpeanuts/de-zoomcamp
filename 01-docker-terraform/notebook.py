#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


# Read a sample of the data
prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100)


# In[8]:


# Display first rows
df.head()


# In[7]:


# Check data types
print(df.dtypes)

print()
# Check data shape
print(df.shape)


# In[9]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    nrows=100,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[10]:


# create database connection
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')


# In[15]:


# Get DDL Schema
print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[13]:


# Create the Table
df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[33]:


### Ingesting Data in Chunks

df_iter = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000
)


# In[32]:


from tqdm.auto import tqdm

# Iterate Over Chunks
count = 0
for df_chunk in tqdm(df_iter):
    count += df_chunk.shape[0]
    print(len(df_chunk), df_chunk.shape, count)


# In[24]:


# inserting data
df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')


# In[34]:


first = True

for df_chunk in tqdm(df_iter):

    if first:
        # Create table schema (no data)
        df_chunk.head(0).to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="replace"
        )
        first = False
        print("Table created")

    # Insert chunk
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )

    print("Inserted:", len(df_chunk))


# In[30]:


from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text('SELECT COUNT(*) FROM yellow_taxi_data'))
    print(result.scalar())


# In[ ]:




