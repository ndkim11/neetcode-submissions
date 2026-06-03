class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        cost=[123]
        2-finished
        costSum[i] = min(costSum[i-1],costSum[i-2])
        '''
        n = len(cost)
        costSum = [0]*n
        
        if n < 2: return cost[n-1]
        else:
            costSum[0] = cost[0]
            costSum[1] = cost[1]

            for i in range(2,n):
                costSum[i] = min(costSum[i-1],costSum[i-2])+cost[i]
            
            return min(costSum[n-1],costSum[n-2])