from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact


import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def export_collection_as_datafram(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def export_data_into_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size = self.data_ingestion_config.train_test_split_ratio
            )
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Exporting training and testing file path")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
            logging.info(f"Exported training and testing file path")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_datafram()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe=dataframe)

            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,test_file_pat=self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)