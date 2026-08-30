class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[0] < nums[-1]:
                return nums[0]
            else:
                m = (l + r) // 2
                if nums[m] > nums[-1]:
                    l = m + 1
                else:
                    res = nums[m]
                    r = m - 1
        return res