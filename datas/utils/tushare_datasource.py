import tushare as ts
import pandas as pd


class Tushare_DataSource():
    """
        tushare datas source
    """
    TOKEN = "3d8a826d5abb159ed9682816f5138168344e56a9a873d19d75710b56"

    def __init__(self):
        self.ts_pro = ts.pro_api(self.TOKEN)
        ts.set_token(self.TOKEN)

    def get_data_csv_1d(self, stock_code, from_date, to_date):
        df = ts.pro_bar(ts_code=stock_code, start_date=from_date, end_date=to_date)
        df['average_price'] = round(df.amount / df.vol*10,3)
        df['volume'] = df['vol']
        df = df.loc[:, ['trade_date', 'open', 'high', 'low', 'close', 'volume', 'amount','average_price']]
        df.sort_values(by='trade_date',inplace=True)
        df.to_csv("../tushare/daily/" + stock_code + ".csv",index=False)


    def get_data_1d(self, stock_code, from_date, to_date):
        df = self.ts_pro.daily(ts_code=stock_code, start_date=from_date, end_date=to_date)
        df['average_price'] = round(df.amount / df.vol*10,3)
        df['volume'] = df['vol']
        df = df.loc[:, ['trade_date', 'open', 'high', 'low', 'close', 'volume', 'amount','average_price']]
        df.sort_values(by='trade_date',inplace=True)
        return df

    def get_data_5min(self, stock_code, from_date, to_date):
        df = ts.pro_bar(ts_code=stock_code,start_date=from_date, end_date=to_date,freq='5min')
        df['average_price'] = round(df.amount / df.vol,3)
        df['volume'] = df['vol']
        df = df.loc[:, ['trade_date', 'open', 'high', 'low', 'close', 'volume', 'amount', 'average_price']]
        df.sort_values(by='trade_date', inplace=True)
        #df.to_csv("../" + stock_code + "_5m.csv", index=False)
        return df

    def get_data_weekly(self,stock_code, from_date, to_date):
        df = self.ts_pro.weekly(ts_code=stock_code, start_date=from_date, end_date=to_date)
        df['average_price'] = round(df.amount / df.vol * 10, 3)
        df['volume'] = df['vol']
        df = df.loc[:, ['trade_date', 'open', 'high', 'low', 'close', 'volume', 'amount', 'average_price']]
        df.sort_values(by='trade_date', inplace=True)
        return df

    def get_data_monthly(self,stock_code, from_date, to_date):
        df = self.ts_pro.monthly(ts_code=stock_code, start_date=from_date, end_date=to_date)
        df['average_price'] = round(df.amount / df.vol * 10, 3)
        df['volume'] = df['vol']
        df = df.loc[:, ['trade_date', 'open', 'high', 'low', 'close', 'volume', 'amount', 'average_price']]
        df.sort_values(by='trade_date', inplace=True)
        return df


    def get_data_weekly_csv(self,stock_code, from_date, to_date):
        df = self.ts_pro.weekly(ts_code=stock_code, start_date=from_date, end_date=to_date)
        df['average_price'] = round(df.amount / df.vol * 10, 3)
        df['volume'] = df['vol']
        df = df.loc[:, ['trade_date', 'open', 'high', 'low', 'close', 'volume', 'amount', 'average_price']]
        df.sort_values(by='trade_date', inplace=True)
        return df

    def get_data_monthly_csv(self,stock_code, from_date, to_date):
        df = self.ts_pro.monthly(ts_code=stock_code, start_date=from_date, end_date=to_date)
        df['average_price'] = round(df.amount / df.vol * 10, 3)
        df['volume'] = df['vol']
        df = df.loc[:, ['trade_date', 'open', 'high', 'low', 'close', 'volume', 'amount', 'average_price']]
        df.sort_values(by='trade_date', inplace=True)
        return df

def get_daily_data():
    ts_ds = Tushare_DataSource()
    #stock_codes = ['159995.SZ', '512880.SH', '512290.SH']
    stock_codes = ['300059.SZ']
    from_date = '20200503'
    to_date = '20201207'
    for stock in stock_codes:
        ts_ds.get_data_csv_1d(stock, from_date=from_date,to_date=to_date)

def get_minute_data():
    ts_ds = Tushare_DataSource()
    stock_codes = ['159995.SZ','512880.SH','512290.SH']
    for stock in stock_codes:
        df1 = ts_ds.get_data_5min(stock, '20200212', '20200331')
        time.sleep(60)
        df2 = ts_ds.get_data_5min(stock, '20200401', '20201203')
        df1 = df1.append(df2)
        time.sleep(60)
        df1.to_csv("../" + stock + "_5m.csv", index=False)


import time
if __name__ == "__main__":
    get_daily_data()
