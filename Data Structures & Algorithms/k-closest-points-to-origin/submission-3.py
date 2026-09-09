class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = {} #pair: distance: index list
        dis = []
        res = []
        for i in range(len(points)):
            distance = points[i][0]**2 + points[i][1]**2 #dont take the sqrt, since the question only want us to return points
            if distance not in dic:
                dic[distance] = [i]
                dis.append(distance)
            else:
                dic[distance].append(i)
        heapq.heapify(dis)
        while len(res) < k:
            distance = heapq.heappop(dis)
            for ind in dic[distance]:
                res.append(points[ind])
                if len(res) == k:
                    return res        
        return res
