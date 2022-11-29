import pymongo
import pandas as pd
import json


# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb+srv://yashvij:0000@cluster0.wnq7l.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"
DATA_FILE_PATH = "aps_failure_training_set.csv"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    #print(f"Rows and Columns : {df.shape}")
    #mongoData = df.to_dict("records")
    #db1 = client["aps"]
    #collection_name = db1["sensor"]
    #collection_name.insert_many(mongoData)


    # Convert data to json format
    df.reset_index(drop=True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)



