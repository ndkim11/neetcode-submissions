import math

class Solution:
    def timeToEat(self, piles, k):
        time = sum([math.ceil(pile/k) for pile in piles])
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for k in range(min_k, max_k):
        l, r = 1, max(piles)

        while l<=r:
            m = (l+r)//2
            if self.timeToEat(piles,m) > h:
                l = m+1

            else:
                r = m-1

        return l