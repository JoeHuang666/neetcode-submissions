class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i,num in enumerate(nums):
            dic[num] = i
        for i,num in enumerate(nums):
            diff = target - num
            if diff in dic and dic[diff] != i:
                return [i, dic[diff]]
        return []
        