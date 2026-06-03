class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for num in nums:
            dict[num]=0
        if len(dict)!=len(nums):
            return True
        else:
            return False        