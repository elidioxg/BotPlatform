# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from base.indicator import Indicator
import finta

class DCW(Indicator):

    def __init__(self, symbol, timeframe, period, **kwargs):

        super().__init__(symbol, timeframe)

        self.function = finta.TA.DO

        self.params = {
                'upper_period': period,
                'lower_period': period,
                }

        self.params.update(**kwargs)
     
    def __repr__(self):
        return 'DCW Indicator. Symbol: %s Timeframe: %s Function: %s \n' % (self.symbol, self.timeframe, self.function)

