# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Approach 1: Brute, try every possible
# Time O(n^2) | space O(1)

# Approach 2: Traverse through the list keeping track of minimum value & max profit so far
# Return the max profit
# Time O(n) | space O(1)
def maxProfit(prices):
    max_profit = 0
    min_price = prices[0]

    profit = 0
    for price in prices:
        profit = price - min_price
        max_profit = max(profit, max_profit)
        min_price = min(price, min_price)
    
    return max_profit

prices = [7,6,4,3,1]
print(maxProfit(prices))