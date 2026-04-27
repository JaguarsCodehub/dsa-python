# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to 
# buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

 

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# def maxProfit(prices):
#     minPriceSoFar = prices[0]
#     maximumProfit = 0

#     # Scan from left to right:
#     # - treat each day as a potential sell day
#     # - the best buy price before today is minPriceSoFar
#     for price in prices[1:]:
#         profitIfSoldToday = price - minPriceSoFar
#         if profitIfSoldToday > maximumProfit:
#             maximumProfit = profitIfSoldToday

#         if price < minPriceSoFar:
#             minPriceSoFar = price

#     return maximumProfit


# def maxProfit(prices):
#     maxiumProfit = 0
#     minPriceSoFar = prices[0]

#     for price in prices[1:]:
#         profitIfSoldToday = price - minPriceSoFar
#         if profitIfSoldToday > maxiumProfit:
#             maxiumProfit = profitIfSoldToday

#         if price < minPriceSoFar:
#             minPriceSoFar = price
#     return maxiumProfit




def maxProfit(prices):
    maximumProfit = 0

    minPriceSoFar = prices[0]

    for price in prices[1:]:
        profitIfSoldToday = price - minPriceSoFar
        if profitIfSoldToday > maximumProfit:
            maximumProfit = profitIfSoldToday

        
        if price < minPriceSoFar:
            minPriceSoFar = price

    return maximumProfit























def maxProfit(prices):

    minimumPriceSoFar = prices[0]
    maximumProfit = 0

    for price in prices[1:]:
        profitIfSoldToday = prices - minimumPriceSoFar
        if profitIfSoldToday > maximumProfit:
            maximumProfit == profitIfSoldToday
        
        if price < minimumPriceSoFar:
            minimumPriceSoFar == price
    return maximumProfit
