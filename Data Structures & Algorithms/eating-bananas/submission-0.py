class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)
            
            if total_time > h: #need to eat faster
                low = mid + 1

            else: # Can we eat slower?
                high = mid -1
                ans = mid

        return ans