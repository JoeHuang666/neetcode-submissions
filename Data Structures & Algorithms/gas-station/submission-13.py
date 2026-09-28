class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        netcost = []
        for i in range(len(gas)):
            netcost.append(gas[i] - cost[i])
        
        cursum = 0
        res = 0
        for i in range(len(netcost)):
            cursum += netcost[i]
            if cursum < 0:
                cursum = 0
                res = i + 1


        return res