class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minDist = [[point[0]**2 + point[1]**2, point] for point in points] #[dis^2, coordinates]
        heapq.heapify(minDist)

        # print(minDist[0])
        
        ans = []
        for _ in range(k):
            point = heapq.heappop(minDist)[1]
            ans.append(point)

        return ans