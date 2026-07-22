class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts={}
        countt={}
        for i in s:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        for i in t:
            if i in countt:
                countt[i]+=1
            else:
                countt[i]=1
                  
        return counts==countt
        