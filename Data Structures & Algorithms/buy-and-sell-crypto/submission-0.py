class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        l,r=0,1
        for i in range(len(prices)-1):
            profit=prices[r]-prices[l]
            if profit>maxprofit:
                maxprofit=profit
            if prices[l]>=prices[r]:
                l=r
                r+=1
            else:
                r+=1

        return maxprofit
            

        