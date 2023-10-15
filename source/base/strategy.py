# -*- coding: utf-8 -*-

class Strategy:

    def __init__(self, **kwargs):
        self.bot = None
        self.datas = list()
        self.indicators = list()
        self.parameters = kwargs

    def Initialize(self):

        return True

    def OnCycle(self):

        pass

    def GetData(self, index: int):

        try:

            return self.datas[index]

        except IndexError as error:
            print(error)
        
        return None

    def GetIndicator(self, index: int):

        try:

            return self.indicators[index]

        except IndexError as error:
            print(error)
        
        return None

    def OnStop(self):

        pass

    def _run(self, datas=None, indicators=None):

        if datas is not None:

            for i in range(0, len(datas), 1):

                if datas[i]._update:
                    self.datas[i] = datas[i]._get(True)


        if indicators is not None:

            for i in range(0, len(indicators), 1):

                if indicators[i]._update:
                    self.indicators[i] = indicators[i]._get(True)


        self.OnCycle()
 

    def __repr__(self):
        return 'Strategy \nDatas: %d  Indicators: %d \nParameters: %s' % (
                len(self.datas), len(self.indicators), self.parameters)

