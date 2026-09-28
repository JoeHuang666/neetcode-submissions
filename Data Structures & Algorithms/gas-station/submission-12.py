class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        netcost = []
        for i in range(len(gas)):
            netcost.append(gas[i] - cost[i])
        
        cursum = 0
        res = -1
        for i in range(len(netcost)):
            if cursum > 0:
                cursum += netcost[i]
                if cursum < 0:
                    cursum = 0
            elif netcost[i] >= 0:
                cursum += netcost[i]
                res = i
            else:
                continue

        return res