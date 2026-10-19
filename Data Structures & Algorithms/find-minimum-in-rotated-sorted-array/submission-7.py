class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            if nums[-1] >= nums[0]:
                return nums[0]
            else:
                m = (l + r) // 2
                if nums[m] >= nums[0]:
                    l = m + 1
                else:
                    res = nums[m]
                    r = m - 1
        return res