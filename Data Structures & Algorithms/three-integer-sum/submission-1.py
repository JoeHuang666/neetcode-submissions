class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            target = -1 * nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                if current_sum < target:
                    l += 1
                if current_sum > target:
                    r -= 1
        unique_res = [list(t) for t in dict.fromkeys(tuple(sub) for sub in res)]
        return unique_res


        