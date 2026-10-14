import pandas as pd
import numpy as np
import os


PATH_TO_ETFS = "data/etfs/"
PATH_TO_STOCKS = "data/stocks/"

class DataProvider:
    def __init__(self):
        self.path = ""

    # loading a single file from path
    def load_data(self, path: str) -> pd.DataFrame:
        df = pd.read_csv(path)
        return df
    
    # loading all files from a directory
    def load_all_etfs(self) -> pd.DataFrame:
        data = []
        for filename in os.listdir(PATH_TO_ETFS):
            if filename.endswith(".csv"):
                file_path = os.path.join(PATH_TO_ETFS, filename)
                df = pd.read_csv(file_path)
                data.append(df)
        return data
    
    # loading all files from a directory
    def load_all_stocks(self) -> pd.DataFrame:
        data = []
        for filename in os.listdir(PATH_TO_STOCKS):
            if filename.endswith(".csv"):
                file_path = os.path.join(PATH_TO_STOCKS, filename)
                df = pd.read_csv(file_path)
                data.append(df)
        return data

    
