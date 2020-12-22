# -*-  encoding='utf8' -*-

import pandas as pd
import numpy as np
import requests
from requests.models import Response
import datetime
import time
import os
import tushare as ts


class hq_transaction_data_fetcher():
    CNN_PATH = 'hqLevel1/connect'
    TRANS_PATH = 'hqLevel1/transactionData'
    HIS_TRANS_PATH = 'hqLevel1/historyTransactionData'
    DETAIL_TRANS_PATH = 'hqLevel2/detailTransactionData'
    IP_PORT = 'http://119.3.27.122:12366/'
    DISCONNECT_PATH = 'hqLevel1/disconnect'
    KBARS_PATH = "hqLevel1/securityBars"
    TOKEN = "3d8a826d5abb159ed9682816f5138168344e56a9a873d19d75710b56"

    def __init__(self):
        self.ts_pro = ts.pro_api(self.TOKEN)
        ts.set_token(self.TOKEN)

    def hq_get_transaction_data(self):
        pass

    def hq_get_history_transaction_data(self):
        pass

    def hq_disconnect(self):
        request_url = self.IP_PORT + self.DISCONNECT_PATH
        response = requests.get(request_url)
        print(response.content)

    def hq_l2_detail_transaction_data(self, stock_code: str, start: int, count: int):
        """"""
        params = {
            'stockCode': stock_code,
            'start': start,
            'count': count
        }
        request_url = self.IP_PORT + self.DETAIL_TRANS_PATH
        response = requests.get(request_url, params)
        df = self.parse_response_str(response.content)
        return df

    def parse_response_str(self, content_str: str):
        """"""

        date_today = datetime.date.today()
        date_str = date_today.isoformat()

        lines = content_str.split(b"\n")
        if len(lines) < 2:
            return None
        field_names_str = lines[1]
        field_names = [str(field_name, encoding='utf8') for field_name in field_names_str.split(b"\t")]
        fields_dict = {field_name: field_names.index(field_name) for field_name in field_names}
        trans_data_list = []

        for line in lines[2:]:
            fields = line.split(b"\t")
            if len(fields) > 1:
                trans_time = str(fields[0], encoding='gbk')
                price = round(float(str(fields[1], encoding='gbk')), 3)
                volume = float(str(fields[2], encoding='gbk'))
                flag = str(fields[3], encoding='gbk')
                flag = 0 if flag == 'B' else 1
                td = (date_str, trans_time, price, volume, flag)
                trans_data_list.append(td)

        # field_names = ["日期","成交时间","价格","成交量","性质"]
        field_names = ["日期"] + field_names
        df = pd.DataFrame(trans_data_list, columns=field_names)
        return df

    def fetch_today_detail_trans_data(self, stockCode):
        df_trans_data = None
        date_today = datetime.date.today()
        date_str = date_today.isoformat()
        for i in range(0, 1000, 1):
            start = i * 1000
            count = 1000
            df_trans_data_ = self.hq_l2_detail_transaction_data(stockCode, start, count)
            time.sleep(1)
            if df_trans_data is None:
                df_trans_data = df_trans_data_
            else:
                # print(i)
                # print(len(df_trans_data_))
                if len(df_trans_data_) == 0:
                    break
                df_trans_data = df_trans_data.append(df_trans_data_)
        length = len(df_trans_data)
        df_trans_data.index = range(length)
        df_trans_data.to_csv("../" + stockCode + "_" + date_str + ".csv")
        print(f"stock {stockCode} transaction data done!")

    def get_security_bars(self, stockCode: str, start: int, count: int, freq='5分钟:0'):
        params = {
            'stockCode': stock_code,
            'kbarCate': freq,
            'start': start,
            'count': count
        }
        request_url = self.IP_PORT + self.KBARS_PATH
        response = requests.get(request_url, params)
        df = self.parse_security_bars(response.content)
        return df

    def parse_security_bars(self, content: str):

        lines = content.split(b"\n")
        if len(lines) < 2:
            return None
        field_names_str = lines[1]
        field_names = [str(field_name, encoding='utf8') for field_name in field_names_str.split(b"\t")]
        fields_dict = {field_name: field_names.index(field_name) for field_name in field_names}
        kbars_data_list = []

        # 时间,开盘价,收盘价,最高价,最低价,成交量,成交额
        for line in lines[2:]:
            fields = line.split(b"\t")
            if len(fields) > 1:
                bar_time = str(fields[0], encoding='gbk')
                open = round(float(str(fields[1], encoding='gbk')), 3)
                close = round(float(str(fields[2], encoding='gbk')), 3)
                high = round(float(str(fields[3], encoding='gbk')), 3)
                low = round(float(str(fields[4], encoding='gbk')), 3)
                volume = float(str(fields[5], encoding='gbk'))
                amount = float(str(fields[6], encoding='gbk'))
                td = (bar_time, open, close, high, low, volume, amount)
                kbars_data_list.append(td)

        df = pd.DataFrame(kbars_data_list, columns=field_names)
        return df

    def fetch_security_bars(self, stockCode: str, start_date: str, end_date: str, freq='5分钟:0'):

        freq_num = freq.split(":")[1]
        if int(freq_num) == 0:  # 5分钟
            one_day_bars = 48
            one_request_bars = 48
            csv_file = f"../tdx/{stockCode}_5m.csv"
        elif int(freq_num) == 7:
            one_day_bars = 240
            one_request_bars = 240
            csv_file = f"../tdx/{stockCode}_1m.csv"
        elif int(freq_num) == 4:
            one_day_bars = 1
            one_request_bars = 100
            csv_file = f"../tdx/{stockCode}_1d.csv"

        today = datetime.datetime.now()
        today_date = today.strftime('%Y%m%d')
        end_to_today_trade_cal = self.ts_pro.trade_cal(exchange='', start_date=end_date, end_date=today_date)
        end_to_today_trade_cal = end_to_today_trade_cal.loc[end_to_today_trade_cal.is_open == 1, :]
        end_days = len(end_to_today_trade_cal) - 1
        start_bars = end_days * one_day_bars

        trade_cal = self.ts_pro.trade_cal(exchange='', start_date=start_date, end_date=end_date)
        trade_cal = trade_cal.loc[trade_cal.is_open == 1, :]
        trade_days = len(trade_cal)
        trade_cal = trade_cal[::-1]
        total_bars = trade_days * one_day_bars
        counts = total_bars // one_request_bars
        if total_bars % one_request_bars > 0:
            counts = counts + 1

        cols = ['时间', '开盘价', '收盘价', '最高价', '最低价', '成交量', '成交额']
        df_kbars = pd.DataFrame(columns=cols)
        start = start_bars
        for i, _ in enumerate(range(counts)):
            trade_date = trade_cal.iloc[i]['cal_date']
            trade_date = trade_date[0:4] + "-" + trade_date[4:6] + "-" + trade_date[6:]
            df = self.get_security_bars(stockCode, start, one_request_bars, freq)
            if int(freq_num) == 4:  # 日线bar
                pass
            else:
                df['时间'] = df['时间'].apply(lambda x: trade_date + " " + x[12:])
            df = df[::-1]
            df_kbars = df_kbars.append(df)
            start = start + one_request_bars
            time.sleep(0.01)

        df_kbars = df_kbars[::-1]
        df_kbars.index = range(len(df_kbars))

        df_kbars.to_csv(csv_file)


# os.chdir("c:/quant")
# fetcher = hq_transaction_data_fetcher()
# df_stock_list = pd.read_csv("stocklist.csv", encoding='gbk')
# stock_codes = []
# stock_list = df_stock_list['代码'].to_list()
# for stock in stock_list:
#     stock_code = str(stock)
#     length = len(stock_code)
#     stock_code = '0' * (6 - length) + stock_code
#     if stock_codes.count(stock_code) < 1:
#         stock_codes.append(stock_code)

#stock_codes = ['159995.SZ', '512880.SH', '512290.SH']

#stock_codes = ['123072.SZ','113565.SH','123074.SZ','123013.SZ']
stock_codes = ['113565.SH']
fetcher = hq_transaction_data_fetcher()
for stock_code in stock_codes:
    #fetcher.fetch_security_bars(stock_code, start_date='20200210', end_date='20201201', freq="日:4")
    fetcher.fetch_security_bars(stock_code, start_date='20200210', end_date='20201201', freq="分钟:7")
