class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Do one binary search to find min element index
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        minindex = l
        #Using minindex to check the target is in left part or right part
        if minindex == 0: #left part
            l, r = 0, len(nums) - 1
        elif target >= nums[0]:
            l, r = 0, minindex - 1
        else:
            l, r = minindex, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1