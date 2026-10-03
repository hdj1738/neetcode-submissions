class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        l,r=0,1
        for i in range(len(prices)-1):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxprofit=max(maxprofit,profit)
                r+=1
            else:
                l=r
                r+=1

        return maxprofit
            

        