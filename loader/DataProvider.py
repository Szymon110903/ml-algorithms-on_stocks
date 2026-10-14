import pandas as pd
import numpy as np
import os


class DataProvider:
    def __init__(self, path_to_etfs: str = "data/etfs/", path_to_stocks: str = "data/stocks/"):
        self.path_to_etfs = path_to_etfs
        self.path_to_stocks = path_to_stocks

    # loading a single file from path
    def load_data(self, path: str) -> pd.DataFrame:
        if not path:
            return None
        df = pd.read_csv(path)
        return df
    
    # loading all files from a directory
    def load_all_etfs(self) -> list:
        data = []
        for filename in os.listdir(self.path_to_etfs):
            if filename.endswith(".csv"):
                file_path = os.path.join(self.path_to_etfs, filename)
                df = pd.read_csv(file_path)
                data.append(df)
        return data
    
    # loading all files from a directory
    def load_all_stocks(self) -> list:
        data = []
        for filename in os.listdir(self.path_to_stocks):
            if filename.endswith(".csv"):
                file_path = os.path.join(self.path_to_stocks, filename)
                df = pd.read_csv(file_path)
                data.append(df)
        return data

    
