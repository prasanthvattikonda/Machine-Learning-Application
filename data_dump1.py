import pandas as pd
import pymongo
import json
import os, sys
from schema import write_Schema_yaml
#from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://prasanth95:prasanth95@cluster0.f3pkkpq.mongodb.net/?retryWrites=true&w=majority"


DATA_FILE_PATH = (r"C:\Users\prasanth vattikonda\Desktop\train.csv")
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

if __name__=="__main__":

    ROOT_DIR = os.getcwd()

    DATA_FILE_PATH = os.path.join(ROOT_DIR, 'Data', 'train.csv')

    FILE_PATH = os.path.join(ROOT_DIR, DATA_FILE_PATH)

    write_Schema_yaml(csv_file = DATA_FILE_PATH)

    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

# Convert the DataFrame to a list of dictionaries (JSON records)
    json_records = json.loads(df.to_json(orient="records"))
    print(json_records[0])

    # Establish a connection to MongoDB
    client = pymongo.MongoClient(uri)

    # Access the desired database and collection
    db = client[DATABASE]
    collection = db[COLLECTION_NAME]

    # Insert the JSON records into the collection
    collection.insert_many(json_records)

    # Close the MongoDB connection
    client.close()
