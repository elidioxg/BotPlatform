# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import time
import datetime as dt

from base.event import TimedEvent
from base.strategy import Strategy
from base.data import Data
from base.indicator import Indicator
from base.exception import *

class Bot:

    def __init__(self):
        self.exchanges = []
        self.strategy = None
        self.strategy_args = {}
        self.cycle_period = 1
        self.datas = []
        self.indicators = []
        self.events = []

    def AddData(self, symbol, timeframe, exchange=0):

        if len(self.exchanges) == 0:
            raise NoExchangeException()
            return -1

        data = Data(symbol, timeframe, self.exchanges[exchange].GetData)

        event = TimedEvent(self._processdata, **{'index': len(self.datas)})

        event.SetTimeframe(timeframe)

        self.datas.append(data)
        
        self.AddEvent(event)

        return len(self.datas)-1

    def AddEvent(self, event):
        
        if not isinstance(event, TimedEvent):
            raise InvalidTimedEventException()
            return -1

        self.events.append(event)
        return len(self.events)-1

    def AddIndicator(self, indicator, symbol:str, timeframe:str, params={}, **kwargs):

        if len(self.exchanges) == 0:
            raise NoExchangeException()
            return -1

        if not issubclass(indicator, Indicator):
            raise InvalidIndicatorException()
            return -1

        params.update(kwargs)

        indicator = indicator(
                symbol=symbol, 
                timeframe=timeframe, 
                **params
                )

        found = False
        i = 0

        for data in self.datas:

            if indicator.symbol == data.symbol:

                if indicator.timeframe == data.timeframe:

                    found = True
                    indicator.SetData(self.datas[i])
                    break
            i += 1

        if not found:

            index = self.AddData(indicator.symbol, indicator.timeframe)
            indicator.SetData(self.datas[index])

        event = TimedEvent(self._processindicator, index=len(self.indicators))
        event.SetTimeframe(indicator.timeframe)
        self.AddEvent(event)
        self.indicators.append(indicator)

        return len(self.indicators) -1

    def AddExchange(self, exchange):

        self.exchanges.append(exchange)
        return len(self.exchanges)-1

    def SetStrategy(self, strategy, st_args):

        if not issubclass(strategy, Strategy):

            raise InvalidStrategyException()
            return False

        self.strategy = strategy
        self.strategy_args = st_args

        return True

    def SetPeriod(self, period):

        if period < 0:
            raise InvalidPeriodException()
            return False

        self.cycle_period = period

        return True

    def Initialize(self):

        if self.strategy is None:
            raise NoStrategyException()
            return False

        self.strategy = self.strategy(**self.strategy_args)
        self.strategy.bot = self

        if not self.strategy.Initialize():
            self.Log('Error: Strategy failed to initialize.')
            return False

        for _ in self.datas:
            self.strategy.datas.append(None)

        for _ in self.indicators:
            self.strategy.indicators.append(None)

        return True

    def Run(self):

        while True:

            cycle_init = time.time()

            try:

                for i in range(0, len(self.events), 1):
                    self.events[i].OnCycle()

                self.strategy._run(self.datas, self.indicators)

            except KeyboardInterrupt:

                self.strategy.OnStop()
                self.OnStop()
                sys.exit()

            cycle_period = time.time() - cycle_init

            if cycle_period < self.cycle_period:
                time.sleep(self.cycle_period - cycle_period)

    def OnStop(self):
        pass

    def Log(self, message):
        print('[ %s ] %s' % (dt.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            message))

    def _processindicator(self, index):

        self.indicators[index]._calc()

    def _processdata(self, index):

        self.datas[index]._calc()

    def __repr__(self):
        return 'Bot \nCycle Period: %d seconds Exchanges: %s Strategy: %s ' % (self.cycle_period, len(self.exchanges), self.strategy)



