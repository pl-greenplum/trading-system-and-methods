import backtrader as bt
from backtrader.indicator import  Indicator
import math

class SwingIndexIndication(Indicator):
    lines=('swing_index_ind',)
    params = dict(
        period=10
    )

    def __init__(self):
        self.addminperiod(self.p.period)



    def next(self):
        pass