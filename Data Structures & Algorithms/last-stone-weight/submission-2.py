class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHash = []
        for stone in stones:
            heapq.heappush(stoneHash, (-stone,stone))

        while len(stoneHash) > 1:
            stone1 = heapq.heappop(stoneHash)[1]
            stone2 = heapq.heappop(stoneHash)[1]
            
            if stone1 > stone2:
                heapq.heappush(stoneHash, (stone2-stone1, stone1-stone2))

        stoneHash.append((0,0))
        return stoneHash[0][1]