# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
sys.path.append('../finta/')

from base.indicator import Indicator
from finta.finta import TA

class CustomIndicator(Indicator):

    def __init__(self, symbol, timeframe, params=params, data=None, function=None):

        super().__init__(symbol, timeframe, function, params,
                data)

        self.params = {
            
            }

    def __repr__(self):
        return 'Indicator. Symbol: %s  Timeframe: %s Function: %s Params: %s' % (self.symbol, self.timeframe, self.function, self.params)

