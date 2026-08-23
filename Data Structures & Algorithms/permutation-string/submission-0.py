class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicts1 = {}
        for c in s1:
            dicts1[c] = dicts1.get(c,0) + 1

        need = len(dicts1)

        for l in range(len(s2)):
            dicts2, cur = {}, 0
            for r in range(l, len(s2)):
                dicts2[s2[r]] = dicts2.get(s2[r],0) + 1
                if dicts1.get(s2[r],0) < dicts2.get(s2[r],0): # element not in s1
                    break
                if dicts1.get(s2[r],0) == dicts2.get(s2[r],0): # one s1 element satisfied
                    cur += 1
                if cur == need:
                    return True

        return False