class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dict1 = {}
        dict2 = {}
        for i in range(len(s1)):
            dict1[s1[i]] = dict1.get(s1[i],0) + 1
            dict2[s2[i]] = dict2.get(s2[i],0) + 1
        
        if dict1 == dict2:
            return True

        for j in range(len(s1),len(s2)):
            dict2[s2[j]] = dict2.get(s2[j],0)+1

            out_char = s2[j-len(s1)]
            dict2[out_char] -= 1

            if dict2[out_char]==0:
                del dict2[out_char]

            if dict1 == dict2:
                return True

        return False