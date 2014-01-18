# -*- coding: utf-8 -*-
__author__ = 'sjk'


class CexWrapper(object):
    def __init__(self, j, label=''):
        self.label = label
        self.raw = j
        [self.__setattr__(i, j[i]) for i in j.keys()]

    def __unicode__(self):
        return self.__str__()


class Ticker(CexWrapper):
    def __str__(self):
        return '''Ticker:
    Couple:    %(label)s
    Timestamp: %(timestamp)s
    Volume:    %(volume)s
    Last:      %(last)s
    Bid:       %(bid)s
    High:      %(high)s
    Low:       %(low)s
    Ask:       %(ask)s''' % vars(self)

    @property
    def lastn(self):
        return float(self.last)


class Balance(CexWrapper):
    def __str__(self):
        return '''Balance for %s:
    %s''' % (
            self.username,
            '\n    '.join([
                '\n    '.join(str(Coin(self.raw[i], i)).split('\n'))
                for i in self.raw.keys()
                if i != 'username' and i != 'timestamp'
            ])
        )

    @property
    def btc_available(self):
        return float(self.raw['BTC']['available'])

    @property
    def nmc_available(self):
        return float(self.raw['NMC']['available'])

class Coin(CexWrapper):
    def __str__(self):
        if 'orders' in self.raw:
            return '''%(label)s
    Available: %(available)s
    Orders: %(orders)s''' % vars(self)
        else:
            return '''%(label)s
    Available: %(available)s''' % vars(self)
