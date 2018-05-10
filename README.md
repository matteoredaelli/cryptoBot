# cryptoBot

## USAGE

```
python3 cryptoBot.py -h

                       _          ____        _
  ___ _ __ _   _ _ __ | |_ ___   | __ )  ___ | |_
 / __| '__| | | | '_ \| __/ _ \  |  _ \ / _ \| __|
| (__| |  | |_| | |_) | || (_) | | |_) | (_) | |_
 \___|_|   \__, | .__/ \__\___/  |____/ \___/ \__|
           |___/|_|

usage: cryptoBot.py [-h] CMD [ARG [ARG ...]]

CryptoBot command line utility

positional arguments:
  CMD         db_load|fetch_ohlcvs|fetch_tickers
  ARG         optional argument

optional arguments:
  -h, --help  show this help message and exit
```

Samples:
- python3 cryptoBot.py fetch_tickers
- python3 cryptoBot.py fetch_ohlcvs
- python3 cryptoBot.py db_load tickers
