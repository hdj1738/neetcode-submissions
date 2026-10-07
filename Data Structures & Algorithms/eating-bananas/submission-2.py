class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            k=l+((r-l)//2)
            output=0
            for i in range(len(piles)):
                output+=math.ceil(piles[i]/k)
            if output<=h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res