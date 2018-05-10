import getopt, sys
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

def main():
    db = database.DB(config["DATABASE"]['path'])
    exchange = exchanges.connect_exchange(config["EXCHANGE"]["exchange"])

    logger.info("begin")
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:va:", ["help", "cmd=", "verbose", "args"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        #usage()
        sys.exit(2)
    cmd = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-c", "--cmd"):
            cmd = a
        elif o in ("-a", "--args"):
            args = a
        else:
            assert False, "unhandled option"

    if cmd == "fetch_tickers":
        fetch_tickers(exchange, db)
    elif cmd == "fetch_ohlcvs":
        fetch_ohlcvs(exchange, db, config["EXCHANGE"]["symbols"].split(" "), config["EXCHANGE"]["timeframe"])
    elif cmd == "db_load":
        db_load(db, args)

    logger.info("end")

if __name__ == '__main__':
    main()
