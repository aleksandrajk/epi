# Find optimal profit
def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


stock1 = [310.5, 370, 275, 275.25, 250, 260, 260, 230, 230, 230]
stock2 = [1.31, 5, 3, 20, 4, 10, 30.99, 2, 25, 20]
print(buy_and_sell_stock_once(stock1))
print(buy_and_sell_stock_once(stock2))
