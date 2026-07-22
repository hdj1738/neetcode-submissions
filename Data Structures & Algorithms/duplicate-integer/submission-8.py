class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #dict={}
        #for i in nums:
         #   dict[i]=""
        if len(set(nums))!= len(nums):
            return True
        else:
            return False        