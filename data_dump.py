import pandas as pd
import pymongo
import json
# MangoDB connection URL

uri = "mongodb+srv://prasanth95:prasanth95@cluster0.wmy1spa.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = (r"C:\Users\prasanth vattikonda\Desktop\train.csv")
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

if __name__ == "__main__":
    #Read data from the CSV file into a Pandas DataFrame
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns of our Data: {df.shape}")

    # Convert the DataFrame to a list of dictionaries (JSON records)
    joson_records = json.loads(df.to_json(orient="records"))
    print(joson_records[0])

    #Establish a connection to MongoDB
    client = pymongo.MongoClient(uri)

    #Access the desired database and collection
    db = client[DATABASE]
    collection =db[COLLECTION_NAME]

    # Insert the JSON records in the collection
    collection.insert_many(joson_records)

    #Close the MongoDB connection
    client.close()