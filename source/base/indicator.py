# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from base.data import Data
from base.exception import InvalidDataException

class Indicator:

    def __init__(self, symbol:str, timeframe:str, function=None, params={}, 
            data=None):


        self.symbol = symbol
        self.timeframe = timeframe
        self.function = function
        self.params = params
        self.data = data

        self.values = None
        self._update = False

    def SetData(self, data):


        if isinstance(data, Data) or issubclass(data, Data):
            self.data = data
        else:
            raise InvalidDataException()

    def _get(self, astimeseries=False):

        self._update = False
        if astimeseries and self.values is not None:
            return self.values[::-1]

        return self.values

    def _calc(self):

        if self.data is None:
            raise InvalidDataException()
            return

        self.values =  self.function(self.data.values, **self.params)
        self._update = True

    def __repr__(self):
        return 'Indicator Symbol: %s  Timeframe: %s Params: %s \n Values: %s ' % (self.symbol, self.timeframe, self.params, self.values)

