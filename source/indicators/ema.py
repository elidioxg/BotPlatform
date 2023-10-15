# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from base.indicator import Indicator
import finta

class EMA(Indicator):

    def __init__(self, symbol, timeframe, period, column='close', adjust=True):

        self.params = {
                'period': period,
                'column': column,
                'adjust': adjust
                }

        super().__init__(symbol, timeframe, finta.TA.EMA, self.params)


    def __repr__(self):
        return 'EMA Indicator. Symbol: %s  Timeframe: %s Function: %s Params: %s' % (self.symbol, self.timeframe, self.function, self.params)

