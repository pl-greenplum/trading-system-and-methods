import backtrader as bt
from backtrader.indicator import Indicator
import math


class AdaptiveRsiIndicator(Indicator):
    lines = ('adaptive_rsi_ind',)
    params = dict(
        period=10
    )

    def __init__(self):
        self.addminperiod(self.p.period+1)

        self.rsi = bt.indicators.RelativeStrengthIndex(self.p.period)
        self.sc = abs(self.rsi / 100 - 0.5) * 2

    def next(self):
        if len(self)==1:
            self.lines.adaptive_rsi_ind[0] = self.data.close[0]
        else:
            self.lines.adaptive_rsi_ind[0] = self.adaptive_rsi_ind[-1] + self.sc[0] * (
                        self.data.close[0] - self.adaptive_rsi_ind[-1])
