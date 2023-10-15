# -*- coding: utf-8 -*-

import datetime as dt

class TimedEvent:

    def __init__(self, function=None, **kwargs):

        self.function = function
        self.args = kwargs
        self.time = None
        self.increment = 0.

    def OnCycle(self):

        now = dt.datetime.now()
        self.time = dt.datetime.now() if self.time is None else self.time

        if now >= self.time:

            self.time += dt.timedelta(seconds=self.increment)
            if self.function is not None:

                self.function(**self.args)
   
    def EveryDays(self, days=1):

        now = dt.datetime.now()
        
        while (now.day%days) != 0:
            now = now + dt.timedelta(days=1)

        self.time = now - dt.timedelta(hours=now.hour, minutes=now.minute, seconds=now.second, microseconds=now.microsecond)
        self.increment = days * 24 * 60 * 60

    def EveryHours(self, hours=1):

        now = dt.datetime.now()
        
        while (now.hour%hours) != 0:
            now = now + dt.timedelta(hours=1)

        self.time = now - dt.timedelta(minutes=now.minute, seconds=now.second, microseconds=now.microsecond)
        self.increment = hours * 60 * 60

    def EveryMinutes(self, minutes=1):
        
        now = dt.datetime.now()
        while (now.minute%minutes) != 0:

            now = now + dt.timedelta(minutes=1)

        self.time = now - dt.timedelta(seconds=now.second, microseconds=now.microsecond)
        self.increment = minutes * 60

    def EverySeconds(self, seconds=1):

        now = dt.datetime.now()

        self.time = now - dt.timedelta(seconds=now.second, microseconds=now.microsecond)
        self.increment = seconds

    def SetTimeframe(self, timeframe):

        if timeframe == '1m':
            self.EveryMinutes(1)
            return

        elif timeframe == '3m':
            self.EveryMinutes(3)
            return

        elif timeframe == '5m':
            self.EveryMinutes(5)
            return
        
        elif timeframe == '15m':
            self.EveryMinutes(15)
            return
        
        elif timeframe == '30m':
            self.EveryMinutes(30)
            return
        
        elif timeframe == '1h':
            self.EveryHours(1)
            return

        elif timeframe == '2h':
            self.EveryHours(2)
            return

        elif timeframe == '4h':
            self.EveryHours(4)
            return

        elif timeframe == '6h':
            self.EveryHours(6)
            return
        
        elif timeframe == '8h':
            self.EveryHours(8)
            return

        elif timeframe == '12h':
            self.EveryHours(12)
            return
        else:
            raise('Time Frame not recognized: %s' % timeframe)

    

