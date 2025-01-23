import yaml
import pickle
import os,sys
import numpy as np
import dill
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

def read_yaml_file(file_path):
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e

def write_yaml_file(file_path, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as file:
                yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e

def save_numpy_array_data(file_path: str, array: np.array) -> None:
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            np.save(file, array)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e

def load_numpy_array_data(file_path: str) -> np.array:
    try:
        with open(file_path, 'rb') as file:
            return np.load(file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e

def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info("save_object called")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e
    
def load_object(file_path: str) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e