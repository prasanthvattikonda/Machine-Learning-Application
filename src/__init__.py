import os, sys
from src.exception import CustomException
from src.logger import logging
from datetime import datetime
from src.constant import *
import yaml

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
            raise CustomException(e, sys)   