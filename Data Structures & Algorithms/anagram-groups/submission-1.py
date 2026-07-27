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
        groups = []

        for word in strs:
            found = False

            for group in groups:
                if anagram(word, group[0]):
                    group.append(word)                    
                    found = True
                    break

            if not found:
                groups.append([word])
        return groups


                    

        