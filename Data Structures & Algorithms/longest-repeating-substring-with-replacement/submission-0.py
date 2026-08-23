class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sdict = {}
        l = 0
        res = 0
        max_f = 0

        for r in range(len(s)):
            sdict[s[r]] = sdict.get(s[r], 0) + 1
            max_f = max(max_f, sdict[s[r]])

            while (r-l+1) - max_f > k: # 여기가 핵심인듯
                sdict[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res