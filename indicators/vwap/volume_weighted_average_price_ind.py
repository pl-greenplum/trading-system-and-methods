import numpy as np
from backtrader.indicator import Indicator
import math

class VwapIndicator(Indicator):
    lines = ('volume_weighted_average_price',)
    params = dict(
        period=20
    )
    plotinfo = dict(
        plot=True,
        subplot=False,
        plotname='vwap',
        plotskip=False,
        plotabove=False,
        plotlinelabels=False,
        plotlinevalues=True,
        plotvaluetags=True,
        plotymargin=0.0,
        plotyhlines=[],
        plotyticks=[],
        plothlines=[],
        plotforce=True,
        plotmaster=None,
        plotylimited=True,
    )

    def __init__(self):
        self.addminperiod(self.p.period)

    def next(self):
        vols = [self.data.volume[-n] for n in range(self.p.period)]
        amounts = [self.data.amount[-n] for n in range(self.p.period)]
        volume_weighted_array = np.array(vols) / np.sum(vols)
        price_array = np.array(amounts) / np.array(vols)*10
        self.lines.volume_weighted_average_price[0] = price_array.dot(volume_weighted_array)

        # vols = [self.data.volume[-n] for n in range(self.p.period)]
        # amounts = [self.data.amount[-n] for n in range(self.p.period)]
        # self.lines.volume_weighted_average_price[0] = np.sum(amounts) / np.sum(vols)*10


