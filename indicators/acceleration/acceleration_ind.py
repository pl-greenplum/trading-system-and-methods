import backtrader as bt
from backtrader.indicator import  Indicator
import math

class AccelerationIndication(Indicator):
    lines=('acceleration_ind',)
    params = dict(
        period=10
    )

    def __init__(self):
        self.addminperiod(self.p.period)

        acc =  (self.data.close - self.data.close(-self.p.period))/self.p.period
        self.lines.acceleration_ind = acc - acc(-1)

    def next(self):
        pass
