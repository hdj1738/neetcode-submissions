class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #to return the number of consecutive elements
        #if number repeats also count as one (set)
        base = set(nums)
        longest = 0

        for i in base:
            if i - 1 not in base:
                j = i
                current = 1

                while j + 1 in base:
                    j += 1
                    current += 1

                longest = max(longest, current)

        return longest
        
        
            

        
            
        