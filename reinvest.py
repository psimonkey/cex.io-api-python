# -*- coding: utf-8 -*-

from cexapi import Api
from settings import username, api_key, api_secret

a = Api(username, api_key, api_secret)

bt = a.ticker('GHS/BTC')
nt = a.ticker('GHS/NMC')
b = a.balance()

print '-'*20

print 'Current GHS price is %s BTC' % bt.lastn
print 'Have %s GHS' % b.ghs_available
print 'Which is worth %s BTC if sold now' % (b.ghs_available * bt.lastn)

print '-'*20

print 'Have %s BTC' % b.btc_available
print 'Current GHS price is %s BTC' % bt.lastn
btc_price = bt.lastn + 0.0001
buy_btc = (b.btc_available / btc_price) / 1.05
print 'Can therefore buy %s GHS with BTC' % buy_btc
if buy_btc > 0.001:
    print 'Placing order for %s GHS at %s BTC/GHS' % (buy_btc, btc_price)
    #order_id = a.place_order('buy', amount=buy_btc, price=btc_price, couple='GHS/BTC')['id']
    #print 'Order id %s successfully placed' % order_id
else:
    print 'Cannot buy enough - skipping GHS/BTC'

print '-'*20

print 'Have %s NMC' % b.nmc_available
print 'Current GHS price is %s NMC' % nt.lastn
nmc_price = nt.lastn + 0.01
buy_nmc = (b.nmc_available / nmc_price) / 1.05
print 'Can therefore buy %s GHS with NMC' % buy_nmc
if buy_nmc > 0.001:
    print 'Placing order for %s GHS at %s NMC/BTC' % (buy_nmc, nmc_price)
    #order_id = a.place_order('buy', amount=buy_nmc, price=nmc_price, couple='GHS/NMC')['id']
    #print 'Order id %s successfully placed' % order_id
else:
    print 'Cannot buy enough - skipping GHS/NMC'

print '-'*20
