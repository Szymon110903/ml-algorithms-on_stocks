import pandas as pd
import os

from loader.DataProvider import DataProvider
from eda.cleaner import DataCleanerAndValidation

if __name__ == "__main__":
    data_provider = DataProvider()
    # etfs_data = data_provider.load_all_etfs()
    # stocks_data = data_provider.load_all_stocks()
    # print(etfs_data[0])
    # print(stocks_data[0])

    cleaner = DataCleanerAndValidation("data/stocks/ZUO.csv")
    df = cleaner.df_cleaner(cleaner.single_file)
    print(df)
    cleaner.check_data(df)
