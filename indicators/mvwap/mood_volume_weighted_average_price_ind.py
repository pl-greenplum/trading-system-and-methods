import numpy as np
from backtrader.indicator import Indicator
import math

class MvwapIndicator(Indicator):
    lines = ('mood_volume_weighted_average_price',)
    params = dict(
        period=20
    )
    plotinfo = dict(
        plot=True,
        subplot=False,
        plotname='mvwap',
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
        moods = [(self.data.close[-n]-(self.data.high[-n]+self.data.low[-n])/2)**2 for n in range(self.p.period)]
        mood_weighted = np.array(moods)/np.sum(moods)
        result = (volume_weighted_array * mood_weighted)/np.sum(volume_weighted_array * mood_weighted)
        self.lines.mood_volume_weighted_average_price[0] = price_array.dot(result)

