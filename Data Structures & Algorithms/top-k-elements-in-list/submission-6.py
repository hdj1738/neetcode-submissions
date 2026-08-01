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
        topk=heapq.nlargest(k,groups.items(),key=lambda x:x[1])
        print(topk)
        output=[]
        for i in topk:
            output.append(i[0])
        return output
        