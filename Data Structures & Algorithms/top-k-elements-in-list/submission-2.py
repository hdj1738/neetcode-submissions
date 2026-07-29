class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        groups={}
        for num in nums:
            if num in groups:
                groups[num]+=1
            else:
                groups[num]=1
        #print(groups)
        topk=heapq.nlargest(k,groups.values())
        print(topk)
        output=[]
        for k,v in groups.items():
            if v in set(topk):
                output.append(k)
        return output
        