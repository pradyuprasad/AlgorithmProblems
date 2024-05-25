from typing import List

def maxProfit(prices: List[int]) -> int:
    maxProfitPossible = 0
    LargestPriceInFuture = {} #dict to mark what the largest price in the
    # future for every index is. The key is the index number
    # the value is the largest price
    LENGTH = len(prices)
    LargestPriceInFuture[LENGTH -2] = prices[LENGTH-1] #set 2nd last to last
    index = LENGTH-3 #start from 3rd last
    while index >= 0: #loop through to the start
        if prices[index+1] > LargestPriceInFuture[index+1]: #if the one after me is greater than the one after me's max, then the max needs to get updated
            LargestPriceInFuture[index] = prices[index+1]
        else:
            LargestPriceInFuture[index] = LargestPriceInFuture[index+1]
        index-=1
    for index in range(LENGTH-1):
        currProfitPossible = LargestPriceInFuture[index] - prices[index]
        if maxProfitPossible < currProfitPossible:
            maxProfitPossible = currProfitPossible
    return maxProfitPossible

def main():
    print(maxProfit([7,1,5,3,6,4]))

main()