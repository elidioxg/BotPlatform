# -*- coding: utf-8 -*-

class Data:

    def __init__(self, symbol, timeframe, function):

        self.symbol = symbol
        self.timeframe = timeframe

        self.function = function

        self.values = None
        self._update = False

    def _calc(self):

        self.values = self.function(symbol=self.symbol, timeframe=self.timeframe)
 
        self._update = True
        

    def _get(self, astimeseries=False):

        self._update = False
        if astimeseries and self.values is not None:
            return self.values[::-1]

        return self.values

    def __repr__(self):
        return 'Data Symbol: %s Time Frame: %s' % (self.symbol, self.timeframe)
