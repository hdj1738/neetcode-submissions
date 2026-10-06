class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r=0,len(s1)-1
        hashs1={}
        for i in s1:
            if i in hashs1:
                hashs1[i]+=1
            else:
                hashs1[i]=1

        

        for i in s2:
            hash={}
            for i in s2[l:r+1]:
                if i in hash:
                    hash[i]+=1
                else:
                    hash[i]=1

            l+=1
            r+=1
            if hashs1==hash:
                return True
        return False
        
        
        