import backtrader as bt
from backtrader.indicator import Indicator
import math


class BodyMomentumIndicator(Indicator):
    lines = ('body_momentum_ind',)
    params = dict(
        period=5
    )

    def __init__(self):
        self.addminperiod(self.p.period)

    def next(self):
        sumup = sumdown = 0
        for ix in range(self.p.period):
            body = self.data.close[-ix] - self.data.open[-ix]
            if body > 0:
                sumup = sumup + body
            elif body < 0:
                sumdown = sumdown - body

        if sumup + sumdown > 0:
            self.lines.body_momentum_ind[0] = sumup * 100 / (sumup + sumdown)
        else:
            self.lines.body_momentum_ind[0]
