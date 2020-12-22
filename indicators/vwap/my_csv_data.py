from backtrader.feeds import GenericCSVData

class  MyCSVData(GenericCSVData):
    lines = ('amount',)
    params = (('amount', 6),)