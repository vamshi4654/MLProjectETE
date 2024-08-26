import os
import sys
from src.Exceptions import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.Data_transformation import DataTransformation
from src.components.Data_transformation import DataTransformationConfig
## when we use this data class no need to use init in the class while defining variables
## but when we have functions in the class using init is only preferable


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts","train.csv")
    test_data_path: str = os.path.join("artifacts","test.csv")
    raw_data_path: str = os.path.join("artifacts","raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion method")
        try:
            study_df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the study dataset into the dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)
            logging.info("importing the data from Dataframe to raw data path")
            study_df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Initiating the train test split")
            train_data,test_data = train_test_split(study_df,test_size=0.2,random_state=46)
            logging.info("importing the data from train and test dataframes to their paths")
            train_data.to_csv(self.ingestion_config.train_data_path,index =False,header =True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header = True)
            logging.info("Ingestion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path


            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()
    '''
    Here we are returning the paths of train and test data and capturing in the respective variables
    '''
    data_transformer = DataTransformation()
    train_arr,test_arr,_ = data_transformer.initiate_data_transformation(train_data,test_data)


##

    ##Now in the below class we are just initiating the ingestion 
##that is getting the data and storing in the above path
#os.makedirs Purpose: Creates a directory (or multiple nested directories) at the specified path.
#os.path.dirname Purpose: Returns the directory name of the specified path. 
#example for path.dirname 
# import os
# path = "/home/user/new_folder/file.txt"
# dirname = os.path.dirname(path)
# print(dirname)  # Output: "/home/user/new_folder" thats why in our scenario it will retrieve till artifacts folder 

##we are ingesting the data and returning the corresponding paths






