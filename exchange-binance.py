# -*- coding: utf-8 -*-

import os
import sys
import json

import database

db = database.DB("./db")

from binance.client import Client
client = Client(os.environ["BINANCE_KEY"], os.environ["BINANCE_SECRET"])


# place a test market buy order, to place an actual order use the create_order function
data = client.create_test_order(
    symbol='BNBBTC',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)
db.save("order", data)

# get all symbol prices
data = client.get_all_tickers()
db.save("tickers", data)


# start aggregated trade websocket for BNBBTC
def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

from binance.websockets import BinanceSocketManager
bm = BinanceSocketManager(client)
bm.start_aggtrade_socket('BNBBTC', process_message)
bm.start()
