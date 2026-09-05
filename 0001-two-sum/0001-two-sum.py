class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            keyvalue = target-num
            if keyvalue in d:
                return [d[keyvalue],i]
            else:
                d[num]=i
        
