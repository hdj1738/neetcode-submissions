class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for num in nums:
            dict[num]=0
        return len(dict)!=len(nums)     