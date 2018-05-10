#!/usr/bin/env python3

import sys
import argparse
import configparser
import logging
import logging.config
import pprint

import exchanges
import database

# ******************************************************
# config
# ******************************************************

config = configparser.ConfigParser()
config.read('etc/default.toml')

# ******************************************************
# logging
# ******************************************************

import logging
import logging.config

logging.config.fileConfig('etc/logging.toml')
# create logger
logger = logging.getLogger('app')

def fetch_tickers(exchange, db):
    data = exchange.fetch_tickers()
    db.save("tickers", data)

def fetch_ohlcvs(exchange, db, symbols, timeframe):
    for symbol in symbols:
        logger.info("fetching " + symbol)
        data = exchange.fetch_ohlcv(symbol, timeframe)
        db.save("ohlcv_" + symbol, data)


def db_load(db, name):
    data = db.load(name)
    print(data)


banner = """
                       _          ____        _
  ___ _ __ _   _ _ __ | |_ ___   | __ )  ___ | |_
 / __| '__| | | | '_ \| __/ _ \  |  _ \ / _ \| __|
| (__| |  | |_| | |_) | || (_) | | |_) | (_) | |_
 \___|_|   \__, | .__/ \__\___/  |____/ \___/ \__|
           |___/|_|
"""

def main():
    db = database.DB(config["DATABASE"]['path'])
    exchange = exchanges.connect_exchange(config["EXCHANGE"]["exchange"])
    print(banner)
    parser = argparse.ArgumentParser(description='CryptoBot command line utility')
    parser.add_argument('CMD', metavar='CMD',
                help='db_load|fetch_ohlcvs|fetch_tickers')
    parser.add_argument('ARG', nargs='*', help='optional argument')

    args = parser.parse_args()

    if args.CMD == "fetch_tickers":
        fetch_tickers(exchange, db)
    elif args.CMD == "fetch_ohlcvs":
        fetch_ohlcvs(exchange, db, config["EXCHANGE"]["symbols"].split(" "), config["EXCHANGE"]["timeframe"])
    elif args.CMD == "db_load":
        db_load(db, args.ARG[0])

    # logger.info("end")

if __name__ == '__main__':
    main()
