# https://www.interviewcake.com/question/python/stock-price

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

def get_max_profit(stock_prices_yesterday):
    profit = 0
    buy_price = 0
    sell_price = 0
    num_prices = len(stock_prices_yesterday)
    for buy in range(num_prices):
        buy_price = stock_prices_yesterday[buy]
        print("buy %d" % buy_price)
        for sell in range(buy + 1,num_prices):
            sell_price = stock_prices_yesterday[sell]
            print("sell %d" % sell_price)
            profit = max(profit, (sell_price - buy_price))
    return profit
            
print get_max_profit(stock_prices_yesterday)
