class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        newlist = []
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                newlist.append(t)
        one, two, three = False, False, False
        for n in newlist:
            if n[0] == target[0]:
                one = True
            if n[1] == target[1]:
                two = True
            if n[2] == target[2]:
                three = True
        return one and two and three