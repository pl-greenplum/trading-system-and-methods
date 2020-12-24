import backtrader as bt
from backtrader.indicator import Indicator


class AccSwingIndexIndicator(Indicator):
    lines = ('acc_swing_index_ind',)
    params = dict(
        period=10
    )

    def __init__(self):
        self.addminperiod(self.p.period)



    def next(self):
        pass
