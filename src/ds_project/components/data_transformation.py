import os
from ds_project import logger
from sklearn.model_selection import train_test_split
from ds_project.entity.config_entity import DatatransformationConfig
import pandas as pd


#not much to transform in this data : so we just go 
#with train_test_split shit


class DataTransormation:
    def __init__(self,config : DatatransformationConfig):
        self.config = config
        
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)
        
        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)