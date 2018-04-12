'Parse stock trade information and convert to a convenient form'

import csv

def get_portfolio(filename):
    ''' Parse a CSV file of stock trades into a list of tuples
        in the form: [(symbol: str, shares: int, price: float), ...]
    '''
    trades = []
    with open(filename) as f:
        for symbol, shares, price in csv.reader(f):
            trade = (symbol, int(shares),  float(price))
            trades.append(trade)
    return trades

if __name__ == '__main__':

    port = get_portfolio('notestdd/stocks.txt')
    print(port)
