import os
import sys
from src.Exceptions import CustomException
from src.logger import logging
import pickle
import dill

def save_object(filepath,obj):
    try:
        dir_name = os.path.dirname(filepath)
        os.makedirs(dir_name,exist_ok=True)

        with open(filepath,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)



    