import pandas as pd
import pymongo
import json
#from pymongo.mongo_client import MongoClient

client = "mongodb+srv://prasanth95:prasanth95@cluster0.f3pkkpq.mongodb.net/?retryWrites=true&w=majority"


DATA_FILE_PATH = (r"C:\Users\prasanth vattikonda\Desktop\train.csv")
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)

    print(f"Rows and Columns of our Data: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    joson_record = list(json.loads(df.T.to_json()).values())

    print(joson_record[0])

    client[DATABASE][COLLECTION_NAME].insert_many(joson_record)