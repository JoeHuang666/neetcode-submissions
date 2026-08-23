class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        for i in range(len(numbers)):
            currentSum = numbers[l] + numbers[r]
            if currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                return [l+1, r+1]
 