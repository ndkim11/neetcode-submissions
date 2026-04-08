class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list, t_list = list(s), list(t)
        s_list.sort()
        t_list.sort()
        return s_list == t_list