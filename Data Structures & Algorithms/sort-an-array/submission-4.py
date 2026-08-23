class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if not res:
                res.append(n)
            else:
                for i in range(len(res)):
                    if n >= res[i]:
                        res.insert(i, n)
                        break
                    else:
                        if i == len(res)-1 :
                            res.append(n)
        res.reverse()
        return res
