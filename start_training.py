import sys
import os 

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logger
from networksecurity.pipeline.training_pipeline import TrainingPipeline


def start_training():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    start_training()