import os
from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR , MODEL_FILE_NAME

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
import sys

class NetworkModel:
    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def predict(self, x):
        try:
            x_transform = self.preprocessor.transform(x)
            return self.model.predict(x_transform)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

class ModelResolver:
    def __init__(self, model_dir = SAVED_MODEL_DIR) :
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def get_best_model_path(self) -> str:
        try:
            timestamp = list(map(int, os.listdir(self.model_dir)))
            latest_timestamp = max(timestamp)
            latest_model_path = os.path.join(self.model_dir, str(latest_timestamp), MODEL_FILE_NAME)
            return latest_model_path
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def is_model_exist(self) -> bool:
        try:
            if not os.path.exists(self.model_dir):
                return False
            
            timestamp = os.listdir(self.model_dir)
            if len(timestamp) == 0:
                return False
            
            latest_model_path = self.get_best_model_path()

            if not os.path.exists(latest_model_path):
                return False

            return True
        except Exception as e:
            raise NetworkSecurityException(e,sys)