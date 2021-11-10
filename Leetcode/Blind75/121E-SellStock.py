'''
  You are given an array prices where prices[i] is the price of a given stock on the ith day.
  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. 
  
  Input: prices = [7,1,5,3,6,4]
  Output: 5
  Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
  Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
  
  Input: prices = [7,6,4,3,1]
  Output: 0
  Explanation: In this case, no transactions are done and the max profit = 0.
'''

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    left = 0
    right = 1
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = max(profit,prices[right] - prices[left])
        else:
            left = right
        right += 1
    return profit

#SUMMARY 
#1 We want to create two pointers that will be the indexes for two prices
  #Left will always be the lowest current value    
#2 We want the left price to be lower than the right price so that their can be a profit
  # Left < Right = profit because Right - Left > 0
#3 If their is a profit than we want to compare it to previous profits and see if its greater 
#4 We always move the right pointer but we only move the left pointer when left isnt less than right
  #This indicates that there is a new lower value and we want to start comparing profits with that new lowest value 
#5 return the profit if no profit return 0