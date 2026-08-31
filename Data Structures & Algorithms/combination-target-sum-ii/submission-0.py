class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(start,cur,remain):
            if remain==0:
                res.append(cur.copy())
                return
            if remain < 0:
                return

            for j in range(start,n):
                # skip duplicate elements at the same recursive
                if j > start and candidates[j] == candidates[j-1]:
                    continue
                
                # early pruning since array is sorted
                if candidates[j] > remain:
                    break
                
                cur.append(candidates[j])
                # move to next index (j+1) because no duplicate elements
                dfs(j+1, cur, remain - candidates[j])
                cur.pop()

        dfs(0,[],target)
        return res