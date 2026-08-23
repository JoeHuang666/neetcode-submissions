class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            target = -1 * nums[i]
            l, r = i + 1, len(nums) - 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                if current_sum < target:
                    l += 1
                if current_sum > target:
                    r -= 1
        return res


        