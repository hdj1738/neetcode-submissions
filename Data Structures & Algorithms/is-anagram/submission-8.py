class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        def myhash(string):
            dict={}
            for i in string:
                if i in dict:
                    dict[i]+=1
                else:
                    dict[i]=1
            return dict
        return myhash(s)==myhash(t)
                