import pandas as pd
import numpy as np
from loader.DataProvider import DataProvider

class DataCleanerAndValidation:
    def __init__(self, single_file_path: str = '', etfs_path: str = 'data/etfs/', stocks_path: str = 'data/stocks/'):
        self.data_provider = DataProvider()
        # self.etfs_data = self.data_provider.load_all_etfs()
        # self.stocks_data = self.data_provider.load_all_stocks()
        self.single_file = self.data_provider.load_data(single_file_path)

    def df_cleaner(self, df: pd.DataFrame) -> pd.DataFrame:
        print(df.head())

        df = df.ffill().bfill()
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)
        df.sort_index(inplace=True)

        full_business_days = pd.date_range(
            start=df.index.min(), end=df.index.max(), freq='B'
        )

        df = df.reindex(full_business_days)
        # df = self.check_data(df)

        df['Close'] = df['Close'].ffill()

        df['Open'] = df['Open'].fillna(df['Close'])
        df['High'] = df['High'].fillna(df['Close'])
        df['Low'] = df['Low'].fillna(df['Close'])
        df['Volume'] = df['Volume'].fillna(0)
        
        df.index.name = 'Date'

        df['DayOfWeek'] = (
            df.index.dayofweek
        )
        df['DayOfMonth'] = df.index.day
        df['Month'] = df.index.month
        df['Year'] = df.index.year
        df['IsQuarterEnd'] = (
            df.index.is_quarter_end
        )
        return df   

    # należy zrobić tutaj usuwanie tych anomalii i ekstremalnych zmian
    def check_data(self, df: pd.DataFrame):
        anomalies = df[
            (df['Close'] < 0)
            | (df['Open'] < 0)
            | (df['Low'] < 0)
            | (df['Volume'] < 0)
        ]
        print('Liczba wykrytych anomalii:', len(anomalies))

        df = df[
            (df['Close'] > 0)
            & (df['Open'] > 0)
            & (df['Low'] > 0)
            & (df['Volume'] >= 0)
        ]

        df['Daily_Return'] = df['Close'].pct_change()
        extreme_jumps = df[abs(df['Daily_Return']) > 0.5] 
        print('Dni z ekstremalnymi ruchami (>50%):')
        print(extreme_jumps[['Close', 'Daily_Return']])
