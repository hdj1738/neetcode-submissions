class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        count=[0]*26
        result=0
        while r<len(s):
            count[ord(s[r].lower())-97]+=1
            while (r-l+1)-max(count)>k:
                count[ord(s[l].lower())-97]-=1
                l+=1
            result=max(result,r-l+1)
            r+=1
                
        return result