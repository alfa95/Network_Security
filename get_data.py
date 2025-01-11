import sys
import os 
import json

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def csv_tojson_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def pushing_data_to_mongodb(self, data, database_name, collection_name):
        try:
            self.database = database_name
            self.collection = collection_name
            self.records = data
            self.client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
if __name__ == "__main__":
    FILE_PATH = "./Network_data/NetworkData.csv"
    DATABASE_NAME = "NetworkSecurity"
    COLLECTION_NAME = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_tojson_convertor(FILE_PATH)
    pushed_records_count = networkobj.pushing_data_to_mongodb(records, DATABASE_NAME, COLLECTION_NAME)
