from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import backtrader.indicators as btind
from volume_weighted_average_price_ind import VwapIndicator

import datetime
from my_csv_data import MyCSVData


class TestStrategy(bt.Strategy):
    params = dict(
        period = 20
    )

    def __init__(self):
        self.test_ind = VwapIndicator(self.data, period = self.p.period)
        self.sma_ind = bt.indicators.MovingAverageSimple(self.data.close, period = self.p.period)

    def next(self):
        print(self.sma_ind[0])
        print(self.test_ind[0])

if __name__ == "__main__":
    cerebro = bt.Cerebro()

    from_date = datetime.datetime(2006, 1, 1)
    to_date = datetime.datetime(2006, 12, 31)
    dataname = "../datas/000868.SZ.csv"
    data_feed = MyCSVData(dataname=dataname,
                          nullvalue=0.0,
                          dtformat=('%Y%m%d'),
                          datetime=0,
                          high=2,
                          low=3,
                          open=1,
                          close=4,
                          volume=5,
                          openinterest=-1)


    cerebro.adddata(data_feed)
    cerebro.addstrategy(TestStrategy,period = 10)
    cerebro.run()
    cerebro.plot()

