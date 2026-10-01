class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #to return the number of consecutive elements
        #if number repeats also count as one (set)
        base=set(nums) 
        sequence=1
        countbg=0
        for i in base: 
            if i-1 not in base:
                j=i  
                while j+1 in base: 
                    sequence+=1
                    j+=1
                if sequence>countbg:
                    countbg=sequence 
                sequence=1
        return countbg
        
            

        
            
        