# -*- coding: utf-8 -*-
import ccxt
import os

def connect_exchange(exchange, enableRateLimit=True, test=False):
    apiKey = exchange.upper() + "_KEY"
    secret = exchange.upper() + "_SECRET"
    options = {
        'apiKey': os.environ[apiKey],
        'secret': os.environ[secret],
        'enableRateLimit': enableRateLimit,
        'test': test,
    }
    return eval("ccxt.%s(options)" % exchange)
