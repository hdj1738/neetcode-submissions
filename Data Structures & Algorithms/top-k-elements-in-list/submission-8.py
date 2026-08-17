class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        L=[]
        b=0
        a=0
        for i in range(k):
            a=0
            for key,value in dict.items():
                if value>a:
                    a=value
                    b=key
            L.append(b)
            del dict[b]
        return L
            

        '''
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
        '''