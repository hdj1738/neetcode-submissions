class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagram(list1,list2):
            if len(list1)!=len(list2):
                return False
            array=[0]*26
            for i in list1:
                array[ord(i)-ord('a')]+=1
            for i in list2:
                array[ord(i)-ord('a')]-=1
            for i in array:
                if i!=0:
                    return False
            return True
        finaloutput=[]
        for i in strs:
            tempoutput=[]
            for j in strs:
                if anagram(i,j):
                    tempoutput.append(j)
            if tempoutput not in finaloutput:
                finaloutput.append(tempoutput)
        return finaloutput

                    

        