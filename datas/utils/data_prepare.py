import pandas as pd
from tushare_datasource import Tushare_DataSource
import time


def get_stock_list():
    df_stocks = pd.read_csv("stocks.csv", encoding='gbk')
    stock_list = df_stocks['股票代码'].tolist()
    return stock_list

def get_stock_list_1():
    df_stocks = pd.read_csv("em-stocks.csv", encoding='utf8')
    stock_list= df_stocks.iloc[:, 1].apply(lambda x: '0' * (6 - len(str(x))) + str(x)).tolist()
    for i,stock in enumerate(stock_list):
        if stock.startswith("6"):
            stock_list[i] = stock + ".SH"
        else:
            stock_list[i] = stock + ".SZ"
    return stock_list


def get_daily_data(stocks,from_date,to_date):
    ds = Tushare_DataSource()
    stock_codes = stocks
    for stock in stock_codes:
        ds.get_data_csv_1d(stock, from_date=from_date, to_date=to_date)
        time.sleep(0.5)

def get_weekly_data(stocks,from_date,to_date):
    ds = Tushare_DataSource()
    stock_codes = stocks
    for stock in stock_codes:
        df = ds.get_data_weekly(stock, from_date=from_date, to_date=to_date)
        df.to_csv("../tushare/weekly_1/" + stock + ".csv", index=False)
        time.sleep(0.5)

def get_monthly_data(stocks,from_date,to_date):
    ds = Tushare_DataSource()
    stock_codes = stocks
    for stock in stock_codes:
        df = ds.get_data_monthly(stock, from_date=from_date, to_date=to_date)
        df.to_csv("../tushare/monthly_1/" + stock + ".csv", index=False)
        time.sleep(0.5)

if __name__ == "__main__":
    from_date = '20120102'
    to_date = '20201214'
    stocks = get_stock_list_1()
    #get_daily_data(stocks)
    #get_weekly_data(stocks,from_date,to_date)
    get_monthly_data(stocks,from_date,to_date)
