class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sstr = set()
        max_count = 0
        l = 0

        for r in range(len(s)):
            # Duplicate
            while s[r] in sstr:
                sstr.remove(s[l])
                l += 1
            sstr.add(s[r])
            max_count = max(max_count, r-l+1)
        return max_count