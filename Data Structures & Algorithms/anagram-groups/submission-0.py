class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        #{'act':['act','cat'],...}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            res[sorted_s].append(s)

        # print(res.values())
        return list(res.values())