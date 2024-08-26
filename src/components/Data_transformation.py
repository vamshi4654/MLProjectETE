import os
import sys
from src.Exceptions import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator,TransformerMixin
from src.Utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path:str= os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    '''
    Now we need to write the function which will handle data cleaning and data transformation
    '''
    def get_data_transformation_object(self):
        '''
        before doing data transformation we need to identify on what columns we need to do
        for that check EDA
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())

                ]

            )
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info("completed writing the pipelines for both numerical and categorical columns")
            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline",numerical_pipeline,numerical_columns),
                    ("cat_pipeline",categorical_pipeline,categorical_columns)
                ]
            )
            logging.info("completed the preparing of transormers")
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("reading the train and test df is completed")

            preprocessor_obj =self.get_data_transformation_object()

            target_column = 'math_score'
            input_train_df = train_df.drop(columns=[target_column],axis=1)
            target_train_df = train_df["math_score"]
            input_test_df = test_df.drop(columns=[target_column],axis=1)
            target_test_df = test_df["math_score"]

            logging.info("Applying the preprocessing on train and test dataframes begins")

            input_train_arr = preprocessor_obj.fit_transform(input_train_df)
            input_test_arr = preprocessor_obj.transform(input_test_df)

            logging.info("applying the preprocessing object on train and test dataframes is completed")

            logging.info("combining the input and traget columns for both test begins")

            train_arr = np.c_[input_train_arr,np.array(target_train_df)]

            test_arr = np.c_[input_test_arr,np.array(target_test_df)]

            logging.info("combining the input and traget columns for both test is completed")

            '''
            now we want save this object as pickle save so that we can reuse again when new data comes in
            '''
            save_object(
                filepath=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj

            )
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path


            )


        except Exception as e:
            raise CustomException(e,sys)
            


















##try handling outliers when building the customer risk profile estimation model
##check on np.c