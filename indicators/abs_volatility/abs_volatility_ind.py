import backtrader as bt
from backtrader.indicator import  Indicator
import math

class AbsVolatilityIndication(Indicator):
    lines=('abs_volatility_ind',)
    params = dict(
        period=10
    )

    def __init__(self):
        self.addminperiod(self.p.period)

        diff = abs(self.data.close - self.data.close(-1))
        self.lines.abs_volatility_ind = bt.ind.SumN(diff, period=self.p.period)

    def next(self):
        pass