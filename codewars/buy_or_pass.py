# In investing, one way of determining where a stock is a worthwhile buy is by
# comparing a stock's current price to a stock's price at its all time high.
#
# If a stock's current price is less than or equal to 80% of its all time high,
# then it's a "buy".
#
# Build a buy calculator takes the current price of a stock, and the stock's all
# time high, and returns "Buy" if the stock is a buy, or "Pass" if it's not
# worthwhile.
def buy_or_pass(stock_price, all_time_high):
    return "Buy" if stock_price <= all_time_high * 0.8 else "Pass"


print(buy_or_pass(800, 1000))  # "Buy"
print(buy_or_pass(12500.8, 15626))  # "Buy"
print(buy_or_pass(46.74, 58.43))  # "Buy"

print(buy_or_pass(56.74, 58.43))  # "Pass"
print(buy_or_pass(1000, 1000))  # "Pass"
